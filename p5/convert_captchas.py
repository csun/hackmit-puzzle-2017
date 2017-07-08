import json
from PIL import ImageOps
from PIL.ImageMorph import MorphOp
from PIL import Image
from io import BytesIO
import cv2
import base64
import numpy as np


raw_dict = {}
######### vvv use your number here
with open('10.json') as f:
    raw_dict = json.loads(f.read())

mask = Image.open('captchas/mask.jpeg')
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
    cv_im = np.array(bw) 
    # Convert RGB to BGR 
    #cv_im = cv_im[:, :, ::-1].copy()
    kernel = np.ones((2,2),np.uint8)
    cv_im = cv2.erode(cv_im,kernel,iterations = 1)
#    cv_im = cv2.dilate(cv_im,kernel, iterations = 1)
    im = ImageOps.invert(Image.fromarray(cv_im))
    im.save('captchas/' + el['name'] + '.png')
