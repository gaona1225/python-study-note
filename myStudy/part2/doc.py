#!/usr/bin/env python
#coding=utf-8

"""
Module documentation
Words Go Here
"""

spam = 40

def square(x):
    """
    function documentation
    can we have your liver then?
    """
    return x**2

class employee:
    "class documentation"
    pass

print square(4)
print square.__doc__


l = [1,2,4,8,16,32,64]
x = 5

found = i = 0
while not found and i < len(l):
    if 2**x == l[i]:
        found = 1
    else:
        i += 1
if found:
    print "at index ",i
else:
    print x,"not found"


def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
