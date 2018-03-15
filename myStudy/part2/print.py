#!/usr/bin/env python
#coding=utf-8

"""import sys
temp = sys.stdout
sys.stdout = open("myfile.txt","a")
print 20161020
print "span"
print 1,2,3
sys.stdout.close()
sys.stdout = temp"""

x = 1
if x:
    y = 2
    if y:
        print "block 222"
    print "block 111"
print "block 000"
           
           

x = "span"
while x:
    print x
    x = x[1:]

a = 0;b =10
while a<b:
    print a,
    a += 1


print "\n"
m = 10
while m:
    m -= 1
    if m%2 !=0:continue
    print m

while 1:
    name = raw_input("input name:")
    if name == "stop":break
    age = raw_input("input age:")
    if float(age)>160 or float(age)<=0:break
    print "hello ",name,"age is ",age


z= raw_input("input num:")
y = int(z)/2
while y >1:
    if int(z)%y == 0:
        print z, "has factor",y
        break
    y -= 1
else:
    print z,"is prime"


items = ["aaa",111,(4,5),2.01]
tests = [(4,5),3,14]
for key in tests:
    for item in items:
        if (item == key):
            print key,"was found"
            break
    else:
        print key,"not found"
