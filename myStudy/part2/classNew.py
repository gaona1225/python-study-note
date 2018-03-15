#!/usr/bin/env python
#coding=utf-8

#from __future__ import generators

"""class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print self.data

x = FirstClass()
y = FirstClass()

x.setdata("is x")
x.display()

y.setdata("is y")
y.display()


class SecondClass(FirstClass):
    def display(self):
        print "Current value = '%s' " % self.data

z = SecondClass()
z.setdata(20)
z.display()


class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data = value
    def __add__(self,other):
        return ThirdClass(self.data+other)
    def __mul__(self,other):
        self.data = self.data*other

a = ThirdClass("abc")
a.display()

b = a + "xyz"
b.display()

a*3
a.display()"""


"""class SharedData:
    spam = 42

x = SharedData()
y = SharedData()
print x.spam,y.spam #output (42,42)


class MixedNames:
    data = "spam"
    def __init__(self,value):
        self.data = value
    def display(self):
        print self.data,MixedNames.data

z = MixedNames(20)
z.display() #output (20,spam)

class NextClass:
    def printer(self,text):
        self.message = text
        print self.message

m = NextClass()
m.printer("hello m")"""

"""class Super:
    def method(self):
        print 'in Super.method'

class Sub(Super):
    def method(self):
        print 'starting Sub.method'
        Super.method(self)
        print 'ending Sub.method'"""

"""class Super:
    def method(self):
        print "in Super.method"
    def delegate(self):
        self.action()
    def action(self):
        assert 0, "action must be defined!"

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print "in Replacer.method"

class Extender(Super):
    def method(self):
        print "starting Extender.method"
        Super.method(self)
        print "ending Extender.method"

class Provider(Super):
    def action(self):
        print "in Provider.action"

if __name__ == "__main__":
    for klass in (Inheritor,Replacer,Extender):
        print "\n" + klass.__name__ + "..."
        klass().method()
        print "\nProvider..."
        x = Provider()
        x.delegate()"""

"""class Number:
    def __init__(self,start):
        self.data = start
    def __sub__(self,other):
        print 'other:',other
        return Number(self.data - other)
x = Number(5)
y = x - 2
print y.data #output other:2--3

class indexer:
    def __getitem__(self,index):
        return index ** 2
m = indexer()
print m[2] #output 2**2 = 4
for i in range(5):
    print m[i] #output 0 1 4 9 16"""

"""class stepper:
    def __getitem__(self,i):
        return self.data[i]
x = stepper()
x.data = "spam"
print(x[1]) #output p
for i in x:
    print i #output s,p,a,m

class Squares:
    def __init__(self,start,stop):
        self.value = start -1
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
for i in Squares(1,5):
    print i #output 0 1 4 9 16 25"""

"""def gsquares(start,stop):
    for i in range(start,stop+1):
        yield i**2
for i in gsquares(1,5):
    print i #output 1,4,9,16,25"""

"""for i in range(1,10):
    for j in range(1,10):
        print str(i)+"*"+str(j)+"="+str(i*j)"""

"""class SkipIterator:
    def __init__(self,wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def next(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class SkipObject:
    def __init__(self,wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print I.next(),I.next(),I.next() #output a,c,e

    for x in skipper: 
        for y in skipper:
            print x + y #output aa/ac/ae/ca/cc/ce/ea/ec/ees"""


"""class empty:
    def __getattr__(self,attrname):
        if attrname == "age":
            return 40
        else:
            raise AttributeError,attrname
x = empty()
print(x.age) #output 40
#print(x.sex) #output error raise AttributeError,attrname

class accesscontrol:
    def __setattr__(self,attr,value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError,attr+' not allowed'
y = accesscontrol()
y.age = 30
print 'y'
print y.age
y.name = 'gn' #output error"""

"""class PrivateExc(Exception):pass

class Privacy:
    def __setattr__(self,attrname,value):
        if attrname in self.privates:
            raise PrivateExc(attrname,self)
        else:
            self.__dict__[attrname] = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name','pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'
x = Test1()
y = Test2()

x.name = 'bob'
print 'x.name'
print x.name
#y.name = 'sue'
#print 'y.name'
#print y.name
x.sex = 20
print 'x.sex'
print x.sex
y.age = 23
print 'y.age'
print y.age"""

"""class adder:
    def __init__(self,value=0):
        self.data = value
    def __add__(self,other):
        self.data += other

class addrepr(adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data

class addstr(adder):
    def __str__(self):
        return '[Value:%s]' % self.data

class addboth(adder):
    def __str__(self):
        return '[Value:%s]' % self.data
    def __repr__(self):
        return 'addboth(%s)' % self.data

class Commuter:
    def __init__(self,val):
        self.val = val
    def __add__(self,other):
        print "add",self.val,other
    def __radd__(self,other):
        print "radd",self.val,other

x = addrepr(2)
x + 1
print x #output addrepr(3)
print str(x),repr(x) #output addrepr(3) addrepr(3)

y = addstr(3)
y + 1
print y #output [Value:4]

z = addboth(5)
z+1
print z #output [Value:6]

m = Commuter(88)
n = Commuter(99)
print(m+1) #output add 88 1
print(n+1) #output add 99 1

class Prod:
    def __init__(self,value):
        self.value = value
    def __call__(self,other):
        return self.value * other
p = Prod(2)
print p(3) #output 2*3 6
print p(4) #output 2*4 8"""

"""x = 11
def f():
    print x

def g():
    x = 22
    print x

class C:
    x = 33
    def m(self):
        x = 44
        self.x = 55

if __name__ == "__main__":
    print x #output 11
    f() #output 11
    g() #output 22
    print x #output 11

    obj = C()
    print obj.x #output 33

    obj.m()
    print obj.x #output 55
    print C.x #output 33"""
    
"""class super:
    def hello(self):
        self.data1 = "spam"

class sub(super):
    def hola(self):
        self.data2 = "eggs"

x = sub()"""


def classtree(cls,indent):
    print "."*indent,cls.__name__
    for supercls in cls.__bases__:
        classtree(supercls,indent+3)

def instancetree(inst):
    print "Tree of ",inst
    classtree(inst.__class__,3)

def selftest():
    class A:pass
    class B(A):pass
    class C(A):pass
    class D(B,C):pass
    class E:pass
    class F(D,E):pass
    instancetree(B())
    instancetree(F())

if __name__ == "__main__":
    selftest()
