#!/usr/bin/env python
#coding=utf-8


"""class MyList(list):
    def __getitem__(self,offset):
        print "(indexing %s at %s)" % (self,offset)
        return list.__getitem__(self,offset-1)

if __name__ == "__main__":
    print list("abc")
    x = MyList("abc")
    print x

    print x[1]
    print x[3]

    x.append("spam")
    print x
    x.reverse()
    print x"""

class Set(list):
    def __init__(self,value=[]):
        #self.data = []
        list.__init__([])
        self.concat(value)

    def intersect(self,other):
        res = []
        #for x in self.data:
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self,other):
        #res = self.data[:]
        res = Set(self)
        res.concat(other)
        return res

    def concat(self,value):
        for x in value:
            #if not x in self.data:
            if not x in self:
                self.append(x)

    def __and__(self,other):return self.intersect(other)

    def __or__(self,other):return self.union(other)

    def __repr__(self):return "Set:"+ list.__repr__(self)

if __name__ == "__main__":
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])
    print x,y,len(x)
    print x.intersect(y),y.union(x)
    print x & y,x|y
    x.reverse();print x
