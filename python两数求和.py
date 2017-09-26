# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:05:54 2017

@author: Tidus
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        s=[]
        for i, num in enumerate(nums):
            if num in dic:
                s.append([dic[num], i])
            else:
                dic[target - num] = i
        return s
