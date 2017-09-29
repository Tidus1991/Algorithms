# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:02:27 2017

@author: Tidus
"""


def reverse(a):
    if a <= 10:
        return a
    else:
        f = a % 10
        z = a / 10
        return int(f * 10 + z)
    
def isPrime(n):  
    if n <= 1:  
        return False 
    i = 2 
    while i * i <= n:  
        if n % i == 0:  
            return False 
        i += 1 
    return True

def found(K):
    count = 0
    i = 2
    while count != K:
        if isPrime(i) and isPrime(int(reverse(i))):
            count += 1
            i += 1
        else:
            i += 1
    return i-1
