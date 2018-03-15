#!/usr/bin/env python
# coding=utf-8


"""def r_return(n):
    print "You taked me."
    while n>0:
        print "before return"
        #return n
        yield n
        n -= 1
        print "after return"

rr = r_return(3)
# return n执行输出
#output You taked me. -- return 再执行到return n的时候就停止了，后面的代码就不再执行
#output before return

# yield n执行输出

#rr.next()
#output You taked me. -- yield 再执行到yield n的时候不停止每次.next就继续执行
#output before return
#output 3

#rr.next()
#output You taked me. -- yield 再执行到yield n的时候不停止每次.next就继续执行
#output before return
#output 2

#rr.next()
#output You taked me. -- yield 再执行到yield n的时候不停止每次.next就继续执行
#output before return
#output 1"""

"""def fibs(max):
    #斐波那契数列的生成器

    n,a,b=0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1

if __name__ == "__main__":
    f = fibs(10)
    for i in f:
        print i  #output 1,1,2,3,5,8,13,21,34,55 """


"""read_file = open("D:/study/python/myTest/23501.txt")
write_file = open("D:/study/python/myTest/23502.txt","w")

try:
    r = read_file.readlines()
    for line in r:
        write_file.write(line)
finally:
    read_file.close()
    write_file.close()"""

"""with open("D:/study/python/myTest/23501.txt") as read_file,open("D:/study/python/myTest/23502.txt","w") as write_file:
    for line in read_file.readlines():
        write_file.write(line)"""


"""class ContextManagerOpenDemo(object):
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        print "Starting the Manager."
        self.open_file = open(self.filename,self.mode)
        return self.open_file

    def __exit__(self,*others):
        self.open_file.close()
        print "Exiting the Manager."

with ContextManagerOpenDemo("D:/study/python/myTest/23501.txt","r") as reader:
    print "In the Manager."
    for line in reader:
        print line

#output
#Starting the Manager.
#In the Manager.
#hello laoqi
#www.itdiffer.com
#Exiting the Manager. """

from contextlib import contextmanager

@contextmanager
def demo():
    print "before yield."
    yield "contextmanager demo."
    print "after yield."

with demo() as dd:
    print "the word is:%s"% dd

#output
#before yield.
#the word is:contextmanager demo.
#after yield.







