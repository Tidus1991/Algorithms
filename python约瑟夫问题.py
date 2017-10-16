# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:01:35 2017

@author: Tidus
"""

def JosephusProblem(num):
    h = list(range(1, num+1))
    s = []
    k = 0
    i = 0
    while len(s) != num:
        i += 1
        if h[i-1] not in s:
            k += 1
        if k == 3 :
            s.append(h[i-1])
            k = 0
        if i == len(h) - 1:
            i = -1
    print(s)