import os
os.chdir('C:\Python27\Lib\site-packages\pytesser')
from pytesser import *
image = Image.open('D:\study\python\myTest\genimage.png')  # ��Ҫ��ʶ�����֤��·��
print image_to_string(image)
