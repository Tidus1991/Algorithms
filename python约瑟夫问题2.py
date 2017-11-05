# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:01:35 2017

@author: Tidus
"""

#每个人随机获得一个10以内的死亡数字，按照自杀的人所获得的死亡数字循环杀人(第一个死亡数字随机决定)
#直接取模就可以
import random as r

def JosephusProblem(num):
    h = list(range(1, num+1))
    key = [r.randint(1,10) for i in range(1, num+1)]
    s = []
    k = 0
    i = 0
    t = r.randint(1,10)
    while len(s) != num:
        i += 1
        if h[i-1] not in s:
            k += 1
        if k == t :
            s.append(h[i-1])
            t = key[i-1]
            k = 0
        if i == len(h) - 1:
            i = -1
    print(s)
