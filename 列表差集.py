# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        x=[i for i in range (1,len(nums)+1)]
        diff = list(set(x).difference(set(nums)))
        return diff