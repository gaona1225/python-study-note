#!/usr/bin/env python
#coding=utf-8

"""def sum(l):
    if not l:
        return 0
    else:
        return l[0] + sum(l[1:])

print sum([1,2,3,4,5])"""

"""def sumtree(l):
    tot = 0
    for x in l:
        if not isinstance(x,list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

l = [1,[2,[3,4],5],6,[7,8]]
print(sumtree(l))"""


"""def echo(str):
    print str
    
def indirect(func,arg):
    func(arg)

indirect(echo,"hello world")

schedule = [(echo,"spam!"),(echo,"Ham!")]
for (func,arg) in schedule:
    func(arg)"""

"""def make(label):
    def echo(message):
        print (label + ":" + message)
    return echo

f = make("spam")
f("ham!")
f("eggs!")"""


"""def func(a):
    b = "spam"
    return b*a

print(func(3))"""


"""def func(a,b,c):
    return a + b + c

print func(1,2,3)"""

"""f = lambda x,y,z:x+y+z
print f(2,3,4)"""


"""x = (lambda a ="free",b="fie",c="foe":a+b+c)
print x("wee")"""

"""def fn():
    t = "sir"
    a = (lambda x:t + " " +x)
    return a
act = fn()
print act("gg")"""


"""l = [lambda x:x**2,
     lambda x:x**3,
     lambda x:x**4]

for f in l:
    print (f(2)) #output 4\8\16
    
print (l[0](3)) #output 3**2=9"""

"""import sys
#showall = lambda x:list(map(sys.stdout.write,x))
showall = lambda x:[sys.stdout.write(line) for line in x]
t = showall(["spam\n","toast\n","eggs\n"])"""


"""res = []
for x in "spam":
    res.append(ord(x))

print res"""

"""res = [ord(x) for x in "spam"]
print res"""


def buildsquares(n):
    res = []
    for i in range(n):res.append(i**2)
    return res

for x in buildsquares(5):print x,":"
