# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:27:33 2017

@author: Tidus
"""

class LinkedListNode:
    def __init_(self, value = None):
        self.next = None
        self.value = value
        
    def prepend(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self
        return new_node
    
    def append(self, value):
        curr_node = self
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = LinkedListNode(value)
        return self
    
    def find(self, value):
        curr_node = self
        while curr_node is not None:
            if curr_node.value == value:
                return curr_node
        return None
    
    def insert(self, index, value):
        curr_index = 0
        curr_node = self
        while curr_index != index:
            curr_node = curr_node.next
            curr_index += 1
        new_node = LinkedListNode(value)
        new_node.next = curr_node.next
        curr_node.next = new_node
        return self
    
    def traverse(self):
        curr_node = self
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next

def create(value):
    return LinkedListNode(value)

def merge(a, b):
    curr_a = a
    while curr_a.next is not None:
        curr_a = curr_a.next
    curr_a.next = b
    
def length(ll):
    curr_node = ll
    curr_length = 1
    while curr_node is not None:
        curr_length += 1
    return curr_length