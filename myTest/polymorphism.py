#!/usr/bin/env python
# coding=utf-8

def length(x):
    print "The length of",repr(x),"is",len(x)

length("how are you") #output The length of 'how are you' is 11
length([1,2,3]) #output The length of [1, 2, 3] is 3
length({"lang":"python","book":"itdiffer.com"}) #outpt The length of {'lang': 'python', 'book': 'itdiffer.com'} is 2

"the code is from:http:zetcode.com/lang/python/oop"


"""__metaclass__ = type

class Animal:
    def __init__(self,name=""):
        self.name = name


    def talk(self):
        print "the sound of",self.name,"is default!"

class Cat(Animal):
    def talk(self):
        print "the sound of",self.name,"is Meow!"

class Dog(Animal):
    def talk(self):
        print "the sound of",self.name,"is Woof!"

a = Animal()
a.talk() #output the sound of  is default!

c = Cat("Missy")
c.talk() #output the sound of Missy is Meow!

d = Dog("Rocky")
d.talk() #output the sound of Rocky is Woof! """

__metaclass__ = type

class ProtectMe:
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "kivi"

    @property
    def name(self):
        return self.__name

    def __python(self):
        print "I love Python"

    def code(self):
        print "Which language do you like?"
        self.__python()

if __name__ == "__main__":
    p = ProtectMe()
    print p.me
    #print p.__name
    p.name
    p.code()
    #p.__python()
