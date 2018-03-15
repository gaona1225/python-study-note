#!/usr/bin/env python
# coding=utf-8

"""import urllib
def go(a,b,c):
    per = 100.0*a*b/c
    if per>100:
        per = 100
        print "11==%.2f%%" % per

url = "https://passport.baidu.com/static/passpc-account/img/login/smsSwitchPhone.png"
local = "D:/study/python/myTest/me2.jpg"
urllib.urlretrieve(url,local,go)


import xml.etree.cElementTree as ET

tree = ET.ElementTree(file="D:/study/python/myTest/test.xml")

root = tree.getroot()

print root.tag #output bookstore
print root.attrib #output {}

for i in root:
    print i.tag #output bookstore,book,category...
    print i.attrib #output
#output for
#bookstore
#{}
#book
#{'category': 'COOKING'}
#book
#{'category': 'CHILDREN'}
#book
#{'category': 'WEB'}"""


import json
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Person Object name: %s,age: %d" % (self.name,self.age)

def object2dict(obj):
    d = {}
    d["__class__"] = obj.__class__.__name__
    d["__module__"] = obj.__module__
    d.update(obj.__dict__)
    return d

def dict2object(d):
    if "__class__" in d:
        class_name = d.pop("__class__")
        module_name = d.pop("__module__")
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode("ascii"),value) for key, value in d.items())
        inst = class_(**args)
    else:
        inst = d
    return inst

if __name__ == "__main__":
    p = Person("Peter",40)
    print p #output Person Object name:Peter,age:40
    d = object2dict(p)
    print d #output {'age': 40, '__module__': '__main__', '__class__': 'Person', 'name': 'Peter'}
    o = dict2object(d)
    print type(o),o #output <class '__main__.Person'> Person Object name: Peter,age: 40

    dump = json.dumps(p,default=object2dict)
    print dump #output {"age": 40, "__module__": "__main__", "__class__": "Person", "name": "Peter"}
    load = json.loads(dump,object_hook=dict2object)
    print load #output Person Object name: Peter,age: 40
