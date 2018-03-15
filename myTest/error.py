#!/usr/bin/env python
# coding=utf-8

"""while 1:
    print "this is a division program."
    c = raw_input("input 'c' continue,otherwise logout:")
    if c == 'c':
        a = raw_input("first number:")
        b = raw_input("second number:")
        try:
            print float(a)/float(b)
            print "******"
        #except ZeroDivisionError:
        #    print "The second number can't be zero!"
        #    print "******"
        #except ValueError:
        #    print "please input number."
        #    print "******"
        #except(ZeroDivisionError,ValueError):
        except(ZeroDivisionError,ValueError),e:
            #print "please input rightly."
            print e
            print "******"
        else:
            print "else"
    else:
        break """

"""class Calculator(object):
    is_raise = False
    def calc(self,express):
        try:
            return eval(express)
        except ZeroDivisionError:
            if self.is_raise:
                print "zero can not be division."
            else:
                raise

if __name__ == "__main__":
    c = Calculator()
    c.is_raise = True
    print c.calc("8/0")"""

"""while 1:
    try:
        x = raw_input("the first number:")
        y = raw_input("the second number:")

        r = float(x)/float(y)
        print r
    except Exception,e:
        print e
        print "try again."
    else:
        break"""

"""x = 10
try:
    x = 1/0
except Exception,e:
    print e
finally:
    print "del x"
    del x"""

class Account(object):
    def __init__(self,number):
        self.number = number
        self.balance = 0

    def deposit(self,amount):
        assert amount>0
        self.balance += balance

    def withdraw(self,amount):
        assert amount>0
        if amount <= self.balance:
            self.balance -= amount
        else:
            print "balance is not enough."
if __name__ == "__main__":
    a = Account(1000)
    a.deposit(-10)
