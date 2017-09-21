# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:21:42 2017

@author: Tidus
"""
n=int(input("please enter:"))
def func(n):
    x=[]
    while n != 0:
        if n%2 ==0:
            n=(n-2)/2
            x.append(2)
        else:
            n=(n-1)/2
            x.append(1)
    x=x[::-1]
    return x
print(func(n))
