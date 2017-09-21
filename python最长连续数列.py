# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:39:44 2017

@author: Tidus
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 1
        count = 0
        if len(nums) < 1:
            return 0
        for i in range (1,len(nums)):
            if nums[i] > nums[i-1]:
                x += 1
            elif x > count:
                count = x
                x = 1
            else:
                x = 1
        return max([count,x])
        
