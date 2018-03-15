#!/usr/bin/env python
# coding = utf-8

__metaclass__ = type 

class Person:
    def __init__(self,name,lang="golang",website="www.baidu.com"):
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "gaona02@baidu.com"
        print self
        print type(self)

    def getName(self):
        return self.name

    def color(self,color):
        print "%s is %s" %(self.name, color)

    def breast(self,n):
        self.breast = n

    def how(self):
        print "%s breast is %s" % (self.name,self.breast)

girl = Person("zhangsan")
info = Person("lisi",lang="python",website="passport.baidu.com")

print "girl.name = ",girl.name
print "info.name = ",info.name
print "-------"
print "girl.lang = ",girl.lang
print "info.lang = ",info.lang
print "------"
print "girl.website = ",girl.website
print "info.website = ",info.website

print girl.getName()
girl.color("yellow")
girl.breast(90)
girl.how()


def outer_foo():
    a = 10
    def inner_foo():
        a = 20
        print "inner_foo,a=",a

    inner_foo()
    print "outer_foo,a=",a

a = 30
outer_foo()
print "a=",a
