import json
from PIL import ImageOps
from PIL import Image
from io import BytesIO
import base64
import numpy as np


raw_dict = {}
with open('captchas.json') as f:
    raw_dict = json.loads(f.read())

mask = Image.open('captchas/mask.png')
mask = np.asarray(mask.convert('L'))

def apply_mask(target):
    for row in range(1,49):
        for col in range(100):
            cur_px = target[row][col]
            mask_px = mask[row][col]
            if cur_px and not mask_px:
                above = target[row - 1][col]
                below = target[row + 1][col]
                if not (above and below):
                    target[row][col] = 0

for el in raw_dict['images']:
    im = Image.open(BytesIO(base64.b64decode(el['jpg_base64'])))
    gray = im.convert('L')
    bw = np.asarray(gray).copy()
    bw[bw < 150] = 0
    bw[bw >= 150] = 255
    apply_mask(bw)
    im = ImageOps.invert(Image.fromarray(bw))
    im.save('captchas/' + el['name'] + '.png')
