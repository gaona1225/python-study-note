#!/usr/bin/env python
#coding=utf-8

class c1():
    def setname(self,who):
        self.name = who

i1 = c1()
i2 = c1()
i1.setname("bob")
print i1.name
i2.setname("mel")
print i1.name
print i2.name
