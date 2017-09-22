# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:52:37 2017

@author: Tidus
"""
class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        else:
            nums.sort()
            return nums[-3]
