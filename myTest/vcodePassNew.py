import os
os.chdir('C:\Python27\Lib\site-packages\pytesser')
#��֤��ʶ�𣬴˳���ֻ��ʶ��������֤��
import Image
import ImageEnhance
import ImageFilter
import sys

from pytesser import *

#��ֵ��
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#���ڶ�������
#����ʶ�����ĸ�� ���øñ��������
rep={'0':'0',
     'I':'1','L':'1',
     'Z':'2',
     'S':'8'
     };

def getverify1(name):
    #��ͼƬ
    im = Image.open(name)
    #ת�����Ҷ�ͼ
    imgry = im.convert('L')
    #����ͼ��
    imgry.save('g'+name)
    #��ֵ�������÷�ֵ�ָ��thresholdΪ�ָ��
    #out = imgry.point(table,'1')
    #out.save('b'+name)
    #ʶ��
    text = image_to_string(imgry)
    #text = image_to_string(out)
    #ʶ�����
    text = text.strip()
    text = text.upper();
    for r in rep:
        text = text.replace(r,rep[r])
    #out.save(text+'.jpg')
        print text
        return text
#getverify1('D:\study\python\myTest\genimage.png')
#getverify1('1.jpg') #ע�������ͼƬҪ�ʹ��ļ���ͬһ��Ŀ¼��Ҫ���ʹ�����·��Ҳ��
getverify1('genimage.png')
