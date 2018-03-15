import os
os.chdir('C:\Python27\Lib\site-packages\pytesser')
from pytesser import *
image = Image.open('D:\study\python\myTest\genimage.png')  # 需要被识别的验证码路径
print image_to_string(image)
