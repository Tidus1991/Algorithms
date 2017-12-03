# -*- coding: utf-8 -*-
"""
Created on 2017/10/29 21:11

@author: Tidus
"""
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return zip(*Counter(nums).most_common(k))[0]
