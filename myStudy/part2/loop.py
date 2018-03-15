#!/usr/bin/env python
#coding=utf-8

x = "spam"
y = "scam"
z = []

for m in x:
    if m in y:
        z.append(m)

print z


l = [1,2,3,4,5]
for i in range(len(l)):
    print l[i] + 1


s = "span"
for (offset,item) in enumerate(s):
    print item," is at ",offset


e = enumerate(s)
print e.next()


l = [1,2,3,4,5]
l = [x+10 for x in l]




