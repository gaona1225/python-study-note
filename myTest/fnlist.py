#! /usr/bin/env python
#  coding = utf-8


"""
    study __getattr__ and __setattr__
"""

"""class Rectangle(object):
    #the width and length of Rectangle
    

    def __init__(self):
        self.width = 0
        self.length = 0

    def setSize(self,size):
        self.width,self.length = size

    def getSize(self):
        return self.width,self.length

    size = property(getSize,setSize)

if __name__ == "__main__":
    r = Rectangle()
    r.width = 3
    r.length = 4
    #print r.getSize() #output (3,4)
    print r.size #output (3,4)
    #r.setSize((30,40))
    r.size = 30,40
    print r.width #output 30
    print r.length #output 40 """

class NewRectangle(object):
    def __init__(self):
        self.width = 0
        self.length = 0

    def __setattr__(self,name,value):
        if name == "size":
            self.width,self.length = value
        else:
            self.__dict__[name] = value

    def __getattr__(self,name):
        if name == "size":
            return self.width,self.length
        else:
            raise AttributeError

if __name__ == "__main__":
    r = NewRectangle()
    r.width = 3
    r.length = 4
    print r.size #output (3,4)
    r.size = 30,40
    print r.width #output 30
    print r.length #output 40


class A(object):
    author = "qiwsir"
    def __getattr__(self,name):
        if name != "author":
            return "from starter to master."

if __name__ == "__main__":
    a = A()
    print a.author #output qiwsir
    print a.lang #output from starter to master.
