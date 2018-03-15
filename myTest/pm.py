#!/usr/bin/env python
# coding = utf-8

def lang():
    return "python"

#如果仅仅是作为模块引用，下面部分无需添加
if __name__ == "__main__":
    print lang()

#作为模块引用方法,在需要引入的文件中加入下面内容
"""
    import sys
    sys.path.append("D:/study/python/myTest/pm.py")
    import pm
    pm.lang()
"""
