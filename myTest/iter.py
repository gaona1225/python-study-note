#!/usr/bin/env python
# coding=utf-8

# the interator as range()

"""class MyRange(object):
    def __init__(self,n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i <self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

if __name__ == "__main__":
    x = MyRange(7)
    print "x.next()==>",x.next() #output 0
    print "x.next()==>",x.next() #output 1
    print "---for loop---"
    for i in x:
        print i #output 2,3,4,5,6
    #print list(x) #output  StopIteration() -- 报错 将对象返回值都装进了列表中并打印出来，这个正常运行了。此时指针已经移动到了迭代对象的最后一个
    #print "x.next()==>",x.next() #output 0"""

__metaclass__ = type

class Fibs:
    def __init__(self,max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a,self.b = self.b,self.a+self.b
        return fib

if __name__ == "__main__":
    fibs = Fibs(5)
    print list(fibs) #output 0,1,1,2,3,5 
