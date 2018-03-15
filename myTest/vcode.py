import os
os.chdir('C:\Python27\Lib\site-packages\pytesser')
from pytesser import *
image = Image.open('fnord.tif')
print image_to_string(image)

imageJpg = Image.open('1.jpg')
print image_to_string(imageJpg)
