# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:40:10 2017

@author: Tidus
"""

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            frist = 1
            second = 2
            for i in range (n-2):
                nowstep = frist + second
                frist = second
                second = nowstep 
            return nowstep