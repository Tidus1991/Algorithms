# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:39:05 2017

@author: Tidus
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        

'''
the other method
return len([x for x in nums if x<target])

'''
