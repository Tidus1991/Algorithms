# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:39:05 2017

@author: Tidus
"""
nums = [4,7,9,12]
target = 8

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
        
f = Solution()
print(f.searchInsert(nums,target))

'''
return len([x for x in nums if x<target])

返回小于target的值的长度，长知识了。
'''