import os
os.chdir('C:\Python27\Lib\site-packages\pytesser')
#验证码识别，此程序只能识别数据验证码
import Image
import ImageEnhance
import ImageFilter
import sys

from pytesser import *

#二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#由于都是数字
#对于识别成字母的 采用该表进行修正
rep={'0':'0',
     'I':'1','L':'1',
     'Z':'2',
     'S':'8'
     };

def getverify1(name):
    #打开图片
    im = Image.open(name)
    #转化到灰度图
    imgry = im.convert('L')
    #保存图像
    imgry.save('g'+name)
    #二值化，采用阀值分割法，threshold为分割点
    #out = imgry.point(table,'1')
    #out.save('b'+name)
    #识别
    text = image_to_string(imgry)
    #text = image_to_string(out)
    #识别对码
    text = text.strip()
    text = text.upper();
    for r in rep:
        text = text.replace(r,rep[r])
    #out.save(text+'.jpg')
        print text
        return text
#getverify1('D:\study\python\myTest\genimage.png')
#getverify1('1.jpg') #注意这里的图片要和此文件在同一个目录，要不就穿绝对路径也行
getverify1('genimage.png')
