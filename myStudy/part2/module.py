#!/usr/bin/env python
#coding=utf-8

"""def spam(text):
    print text,"spam"

def spamSum(a,b):
    print a+b

print "ffff"

X = 88
def f():
    global x
    x = 99


message = "First version 22"

def printer():
    print "reloaded:", message



def tester():
    print "It's Christmas in Heaven.."

if __name__ == "__main__":
    tester()"""

print "I'm:",__name__

def tester():
    print "It's Christmas in Heaven.."

def minmax(test,*args):
    res = args[0]
    for arg in args[1:]:
        if test(arg,res):
            res = arg
    return res

def lessthan(x,y):return x<y
def grtrthan(x,y):return x>y

if __name__ == "__main__":
    print minmax(lessthan,4,2,1,5,6,3)
    print minmax(grtrthan,4,2,1,5,6,3)

