# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:38:38 2017

@author: Tidus
"""
import re

n = input('fuck me :')
n = re.findall(r'.{1}',n)

def func(n):
    x = 1
    count = 0
    for i in range (0,len(n) - 1):
        if n[i] == n[i + 1]:
            x += 1
        elif x>count:
            count = x
            x = 1
        else:
            x = 1
    print(x,count)
    s = max([x,count])
    return s
print(func(n))
