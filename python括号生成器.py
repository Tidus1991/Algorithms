# -*- coding: utf-8 -*-
"""
Created on 2017/10/29 21:11

@author: Tidus
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)

    def generateParenthesis1(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left - 1, right): yield q
                for q in generate(p + ')', left, right - 1): yield q

        return list(generate('', n, n))

    def generateParenthesis(self, n, open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n - 1, open + 1)] + \
                   [')' + p for p in self.generateParenthesis(n, open - 1)]
        return [')' * open] * (not n)