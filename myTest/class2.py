#!/usr/bin/env python
# coding = utf-8

__metaclass__ = type 

"""class Person:
    def speak(self):
        print "I am speaking."

    def setHeight(self):
        print "The height is:1.60m."

    def breast(self,n):
        print "My breast is:",n

class Girl(Person):
    def setHeight(self):
        print "The height is:1.70m."

if __name__ == "__main__":
    cang = Girl() 
    cang.setHeight() #output The height is:1.70m.
    cang.speak() #output I am speaking.
    cang.breast(90) #output My breast is:90 """

"""class Person:
    def eye(self):
        print "two eyes"

    def breast(self,n):
        print "The breast is:",n

class Girl:
    age = 28
    def color(self):
        print "The girl is white"

class HotGirl(Person,Girl):
    pass

if __name__ == "__main__":
    kong = HotGirl()
    kong.eye() #two eyes
    kong.breast(90) #The breast is:90
    kong.color() #The girl is white
    print kong.age #28"""

"""class Person:
    def __init__(self):
        self.height = 160

    def about(self,name):
        print "{} is about {}".format(name,self.height)

class Girl(Person):
    def __init__(self):
        super(Girl,self).__init__()
        self.breast = 90

    def about(self,name):
        print "{} is a hot girl,she is about {},and her breast is {}".format(name,self.height,self.breast)

if __name__ == "__main__":
    cang = Girl()
    cang.about("canglaoshi") #output canglaoshi is a hot girl,she is about 160,and her breast is 90 """

"""class StaticMethod:
    @staticmethod
    def foo():
        print "This is static method foo()."

class ClassMethod:
    @classmethod
    def bar(cls):
        print "This is class method bar()."
        print "bar() is part of class:",cls.__name__

if __name__ == "__main__":
    static_foo = StaticMethod()
    static_foo.foo() #output This is static method foo().
    StaticMethod.foo() #output This is static method foo().
    print "******"
    class_bar = ClassMethod()
    class_bar.bar() #output This is class method bar(). / bar() is part of class:ClassMethod
    ClassMethod.bar() #output This is class method bar(). / bar() is part of class:ClassMethod """

def get_no_of_instances(cls_obj):
    return cls_obj.no_inst

class Kls(object):
    no_inst = 0
    
    def __init__(self,data):
        #self.data = data
        Kls.no_inst = Kls.no_inst + 1

    def printd(self):
        print(self.data)

ik1 = Kls("arun")
ik2 = Kls("seema")

#ik1.printd() #output arun
#ik2.printd() #output seema

print(get_no_of_instances(Kls))
