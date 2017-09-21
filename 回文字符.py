# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:24:52 2017

@author: Tidus
"""

def dealhw(li,count=0):  
    leng = len(li)  
    if leng > 1:  
        last = leng-1  
        if li[0] == li[last]:  
            del li[last]   #先删除最后一个，再删除第一个  
            del li[0]      #否则就应为del li[0],del li[last-1]  
            count = dealhw(li,count)  
        else:  
            if li[0]>li[last]:  
                li.reverse()         #将最小的放在最前  
            li[0]=li[0]+li[1]  
            del li[1]  
            count+=1  
            count=dealhw(li,count)   #递归处理  
    return count  
  
num = input()  
li  = input().split()  
li = [int(li[i]) for i in range(int(num))]  
print(dealhw(li)) 