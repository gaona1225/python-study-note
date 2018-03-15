#!/usr/bin/env python
#coding=utf-8

import time,sys
reps = 1000
size = 10000

def teseter(func,*args):
    startTime = time.time()
    for i in range(reps):
        func(*args)
    elapsed = time.time()-startTime
    return elapsed

def forStatement():
    res = []
    for x in range(size):
        res.append(abs(x))

def listComprehension():
    res = [abs(x) for x in range(size)]

def mapFunction():
    res = map(abs,range(size))

def generatorExpression():
    res = list(abs(x) for x in range(size))

print sys.version
tests = (forStatement, listComprehension, mapFunction, generatorExpression)

for testfunc in tests:
    print testfunc.__name__.ljust(20),"=>",teseter(testfunc)
