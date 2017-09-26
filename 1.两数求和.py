# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:05:54 2017

@author: Tidus
"""
n = [0,1,2,3,4,5,6,7,8,9]
t = 9
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
f=Solution()
print(tuple(f.twoSum(n,t)))
 #so fucking smart!
 '''
 建立字典dic与列表s
 用目标数减去原列表中的数求得实现目标数所需要的另一个数，这里我们称为助力数
 检查字典中是否有这个数，没有的话将这个助力数和index存入dic
 循环直到字典中有助力数，就说明列表中有满足求和后获得目标数的两个数
 然后返回这两个数的index（一个是enumerate获取的i，另一个是在dic中存储的value值即index值,注意key值即为助力数）
 '''