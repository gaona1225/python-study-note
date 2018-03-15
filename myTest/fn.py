#!/usr/bin/env python
#coding:utf-8


#fun1
"""def add_function(a,b):
    c = a + b
    return c

if __name__ == '__main__':
    result = add_function(2,3)
    print result"""

#fun2
"""def fibs(n):
    result = [0,1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

if __name__ == '__main__':
    lst = fibs(10)
    print lst"""

#fun3
"""def func(x,*arg):
    print x
    result = x
    print arg
    for i in arg:
        result += i
    return result
print func(1,2,3,4,5,6,7,8,9)"""


#fun4
"""def add(x,y):
    return x+y
bars = (2,3)
add(*bars)"""

#fun5
"""def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    f = fib(10)
    print f"""

#fun6
def add(x):
    x += 3
    return x

numbers = range(10)

new_numbers = []
for i in numbers:
    new_numbers.append(add(i))
