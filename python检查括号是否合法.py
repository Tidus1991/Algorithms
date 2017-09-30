# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 13:55:58 2017

@author: Tidus
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        f = []
        dict = {']':'[',')':'(','}':'{'}
        for char in s:
            if char in dict.values():
                f.append(char)
            elif char in dict.keys():
                if f == [] or dict[char] != f.pop():
                    return False
            else:
                return False
        return f == []
