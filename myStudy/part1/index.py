#!/usr/bin/env python
#coding=utf-8

#通过import引入myfile.py文件（模块），并通过myfile.title引用myfile.py模块中的title -- import **载入模块作为一个整体
"""import myfile
print myfile.title"""

#通过from ** import **方式引用myfile.py模块中的title -- 实际上from ** import ** 有拷贝的含义
"""from myfile import title 
print title"""

from myfile import a,b,c
#print c,b
inputValue = raw_input("please input a or b or c or d")
if(inputValue == "a"):
	print "you change ",a
elif(inputValue == "b"):
	print "you change ",b
elif(inputValue == "c"):
	print "you change ",c
else:
	print "you input others"
