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
            del li[last]  
            del li[0]      
            count = dealhw(li,count)  
        else:  
            if li[0]>li[last]:  
                li.reverse()       
            li[0]=li[0]+li[1]  
            del li[1]  
            count+=1  
            count=dealhw(li,count)   
    return count  
  
num = input()  
li  = input().split()  
li = [int(li[i]) for i in range(int(num))]  
print(dealhw(li)) 
