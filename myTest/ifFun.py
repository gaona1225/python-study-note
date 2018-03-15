#! /usr/bin/env python
#coding:utf-8

"""testList = ['a','b','c','d','e'];

if 'g' in testList:
    testList.remove('a');
    print testList;
else:
    print 'no has'"""

"""citys = ["suzhou","tangshan","beijing","shanghai"];
city_codes = ["0512","0315","011","012"];
print "{}:{}".format(citys[0], city_codes[0]);

person = {"name":"qiwsir","site":"qiwsir.github.io","language":"python"} ;

ad = dict(name="qiwsir", age=23)

website = {}.fromkeys(("third","forth"),"facebook")


newCity = {'suzhou':'0512','beijing':'011','shanghai':'012','tangshan':'0315'}


g = 6
n = 8
if g == n :
    print '等于'
elif g < n :
    print '小于'
else:
    print '大于'


print '请输入任意一个整数数字：'
number = int(raw_input())
if number == 10:
    print '您输入的数字是:%d'%number
    print 'You are SMAET.'
elif number > 10:
    print '您输入的数字是:%d'%number
    print 'You are is more than 10.'
elif number < 10:
    print '您输入的数字是:%d'%number
    print 'You are is less than 10.'
else:
    print '您输入的数字是:%d'%number
    print 'hahha' """

"""test = []
for n in range(1,100):
    #print n
    if n%3 == 0:
        #print n
        test.append(n)
print test"""

"""a = 7
while a:
    if a%2 == 0:
        break
    else:
        print '%d is odd number'%a
        a = 0
print '%d is even number'%a"""

from math import sqrt
for n in range(99,1,-1):
    print n
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print 'Nothing'


