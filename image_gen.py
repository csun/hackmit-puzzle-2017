import requests
import jwt

from PIL import Image
import numpy

def gen_image():
    image = Image.fromarray(numpy.uint8(numpy.random.rand(64, 64, 3) * 255), mode='RGB')
    image.save('generated.jpg')

gen_image()
r = requests.post("https://hotsinglebots.delorean.codes/api_predict/csun/predict",
        files={'image': open('generated.jpg', 'r')})
prediction = int(jwt.decode(r.text, verify=False)['prediction'])

while prediction != 1:
    print 'Last prediction: ' + str(prediction)
    gen_image()
    r = requests.post("https://hotsinglebots.delorean.codes/api_predict/csun/predict",
            files={'image': open('generated.jpg', 'r')})
    prediction = int(jwt.decode(r.text, verify=False)['prediction'])
