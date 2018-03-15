#!/usr/bin/env python
#coding=utf-8

class Worker:
    def __init__(self,name,pay):
        self.name = name
        self.pay  = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRasie(self,per):
        self.pay *= (1.0+per)

me = Worker("Gao na",24800)
print me.lastName() #output na

me.giveRasie(0.3)
print me.pay #output 32240
