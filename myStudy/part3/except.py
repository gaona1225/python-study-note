#!/usr/bin/env python
#coding=utf-8

"""def fetcher(str,index):
    return str[index]

x = "spam"
print fetcher(x,3) #output m

#print fetcher(x,4) #output error


def catcher():
    try:
        print fetcher(x,4)
    except IndexError:
        print "got except"
    print "continuing"

catcher()"""

"""def gobad(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print "is not a zero division"
    finally:
        print "come finally"
        #gosouth(1) #output die loop

def gosouth(x):
    print gobad(x,0)

gosouth(1)"""

"""def kaboom(x,y):
    print x+y

try:
    kaboom([0,1,2],"spam")
except TypeError:
    print "Hello world!"
print 'resuming here'"""


"""def MyError(Exception):pass

def stuff(file):
    raise MyError()

file = open('data','w')
try:
    stuff(file)
finally:
    file.close()
    print 'finally'"""



"""print '_'*30,'\nexception raised and caught'
try:
    x = 'spam'[99]
except IndexError:
    print 'except run'
finally:
    print 'finally run'
print 'after run'

print '_'*30,'\nno exception raised'
try:
    x = 'spam'[3]
except IndexError:
    print 'except run'
finally:
    print 'finally run'
print 'after run'

print '_'*30,'\nno exception raised,else run'
try:
    x = 'spam'[3]
except IndexError:
    print 'except run'
else:
    print 'else run'
finally:
    print 'finally run'
print 'after run'

print '_'*30,'\nexception raised but not caugth'
try:
    x = 1/0
except IndexError:
    print 'except run'
else:
    print 'else run'
finally:
    print 'finally run'
print 'after run'"""


"""try:
    raise IndexError,'spam'
except IndexError:
    print 'propagating'
    raise"""

"""def f(x):
    print x
    assert x<0,'x must be nagative'
    return x**2
f(1)
#f(-1)"""

"""with open('test.txt') as myfile:
    for line in myfile:
        print line
        lineNew = line.replace('spam','SPAM')
        print lineNew"""

"""class TraceBlock:
    def message(self,arg):
        print 'running',arg
    def __enter__(self):
        print 'starting with block'
        return self
    def __exit__(self,exc_type,exc_value,exc_tb):
        if exc_type is None:
            print 'exited normally\n'
        else:
            print 'raise an exception!',exc_type
            return False

with TraceBlock() as action:
    action.message('test 1') #output starting with block -- running test1 -- reached -- exited normally
    print 'reached'

with TraceBlock() as action:
    action.message('test 2') #output starting with block -- running test1 -- raise an exception!TypeError 
    raise TypeError
    print 'not reached'"""


"""class General(Exception):pass
class Specific1(General):pass
class Specific2(General):pass

def raiser0():
    x = General()
    raise x

def raiser1():
    x = Specific1()
    raise x

def raiser2():
    x = Specific2()
    raise x

for func in (raiser0,raiser1,raiser2):
    try:
        func()
    except General:
        import sys
        print 'caught:',sys.exc_info()[0]"""



"""def action2():
    print 1+[ ]
def action1():
    try:
        action2()
    except TypeError:
        print 'inner try'
try:
    action1()
except TypeError:
    print 'outer try'"""


import sys
def bye():
    sys.exit(40)

try:
    bye()
except:
    print 'got it'
print 'continuing...'
