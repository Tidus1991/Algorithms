# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:45:32 2017

@author: Tidus
"""

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
    

class Solution2:
    def reverseList(self, head):
        return self._reverse(head)
    
    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
