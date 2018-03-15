#!/usr/bin/env python
#coding=utf-8

"""while True:
	reply = raw_input("Enter text:")
	if reply == "stop" :
		break
	print reply.upper()"""

"""import math
while True:
	reply = raw_input("Enter a number:")
	if not reply.isdigit():
	   print "please input a number"
	else:
	   print math.pow(int(reply),2)"""

import math

while True:
        reply = raw_input("Enter a number:")
        try:
           num = int(reply)
           if num<20:
              print "please input a gt 20"
           else:
              print math.pow(num,2)
        except:
           print "please input a number"
        finally:
           print "haha"
           
           
