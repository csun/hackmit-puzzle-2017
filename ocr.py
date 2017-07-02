from tesserocr import PyTessBaseAPI, PSM
from PIL import Image


api = PyTessBaseAPI(psm=PSM.SINGLE_CHAR)

api.SetImageFile('captchas/2c815a8d6cd986429cd868bbdc994949.png')
api.SetRectangle(0, 0, 37, 50)
print api.GetUTF8Text()
api.SetRectangle(30, 0, 37, 50)
print api.GetUTF8Text()
