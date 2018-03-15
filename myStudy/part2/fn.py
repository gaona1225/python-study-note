#!/usr/bin/env python
#coding=utf-8


"""x = 99

def func(y):
    x = 88
    z = x+y
    return z

print func(1) #output 89
print x #output 99 """

"""x = 99

def func(y):
    global x
    x = 88
    z = x+y
    return z

print func(1) #output 89
print x #output 88"""

"""import first
print first.x #output 88
first.x = 99
print first.x #output 99"""

"""x = 99
def setX(new):
    global x
    x = new

import first
print first.setX(88)"""

"""x = 88

def fun1():
    x = 99
    def fun2():
        print x #output 99
    fun2()
fun1()"""


"""x = 88

def fun1():
    x = 99
    def fun2():
        print x #output 99
    return fun2
fn = fun1()
fn()"""


"""def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x:i**x)
    return acts

acts = makeActions()
print acts[0](2) #output 2**4 pow(2,4) 16
print acts[1](2) #output 2**4 pow(2,4) 16
print acts[2](2) #output 2**4 pow(2,4) 16"""

"""def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x,i=i:i**x)
    return acts

acts = makeActions()
print acts[0](2) #output 2**0 pow(2,0) 0
print acts[1](2) #output 2**1 pow(2,1) 2
print acts[2](2) #output 2**2 pow(2,2) 4"""

"""def tester(start):
    state = start
    def nested(label):
        print(label,state)
    return nested
f = tester(0)
print f("spam") #output spam,0"""

class tester:
    def __init__(self,start):
        self.state = start
    def __call__(self,label):
        print(label,self.state)
        self.state += 1

m = tester(99)
m("juice") #output juice 99

#practice
"""x = "spam"
def func():
    print x
func() #output spam """

"""x = "spam"
def func():
    x = "ni"
func()
print x #output spam"""

"""x = "spam"
def func():
    x = "ni"
    print x #output ni
func()
print x #output spam"""

"""x = "spam"
def func():
    global x
    x = "ni"
func()
print x #output ni"""

"""x = "spam"
def func():
    x = "ni"
    def nested():
        print x #output ni
    nested()
func()
print x #output spam"""


"""def multiple(x,y):
    x = 2
    y = [3,4]
    return x,y"""

"""def func(spam,eggs,toast=0,ham=0):
    print (spam,eggs,toast,ham)

func(1,2)"""

"""def f(*args):print args
f()

def b(**args):print args"""

"""def func(a,b,c,d):print(a,b,c,d)

def echo(*args,**kwargs):print(args,kwargs)
echo(1,2,a=3,b=4)"""


"""def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first,*rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print min1(3,4,1,2)
print min2("bb","aa")
print min3(3,4,99,10)"""


def intersect(*args):
    res = []
    print args[0]
    print args[1:]
    for x in args[0]:
        for other in args[1:]:
            if x not in other:break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    print args[0]
    print args[1:]
    for seq in args:
        print seq
        for x in seq:
            print x
            if not x in res:
                res.append(x)
        return res


s1,s2,s3 = "spam","scam","slam"
intersect(s1,s2),union(s1,s2)
    



