#!/usr/bin/env python
# coding = utf-8

#firstDemo
"""list = [1,2,3,4,5,6,7,8,9,0]
temp = list[0]
list.pop(0)
list.append(temp)"""

#secondDemo
"""from __future__ import division
import random

score = [random.randint(0,100) for i in range(40)]
print score

print sorted(score)

num = len(score)
sum_score = sum(score)
ave_num = sum_score/num
less_ave = []
more_ave = []
other_ave = []
for i in score :
    if i < ave_num :
        less_ave.append(i)
    elif i > ave_num :
        more_ave.append(i)
    else:
        other_ave.append(i)"""

#thirdDemo
"""str = 'I love  code.'
str_lst = str.split(' ')
words = [s for s in str_lst if s!= '']
nStr = ' '.join(words)"""

#fourthDemo
"""a,b = 0,1
for i in range(10):
    a,b = b,a+b"""

#fifthDemo
n = int(raw_input('Enter an interger >= 0:'))

fact = 1
for i in range(2,n+1):
    fact = fact*i
print str(n) + ' factorial is ' + str(fact)
    
