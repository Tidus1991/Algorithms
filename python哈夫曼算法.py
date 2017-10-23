# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:15:13 2017

@author: Tidus
"""
class PrioQueueError(ValueError):
    pass

class PrioQueue:
    def __init__(self, elist=[]):
        self.elems = list(elist)
        if elist:
            self.buildheap
        
    def is_empty(self):
        return not self.elems
    
    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self.elems[-1]
    
    def enqueue(self, e):
        self.elems.append(None)
        self.siftup(e, len(self.elems)-1)
        
    def siftup(self, e, last):
        elems, i, j = self.elems, last, (last-1)/2
        while i > 0 and e < elems[j]:
            i, j = j, (j-1)//2
        elems[i] = e
        
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self.elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0
    
    def siftdown(self, e, begin, end):
        elems, i, j = self.elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e
        
    def buildheap(self):
        end = len(self.elems)
        for i in range(end//2, 1, -1):
            self.siftdown(self.elems[i], i, end)

class BinTNode:
    def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
    
def count_BinTnodes(t):
    return 1 + count_BinTnodes(t.left) + count_BinTnodes(t.right)

def sum_BinTnodes(t):
    if t is None:
        return 0
    return t.data + sum_BinTnodes(t.left) + sum_BinTnodes(t.right)

def print_BinTnodes(t): #先根遍历
    if t is None:
        print('^', end='')
        return
    print('('+str(t.data), end='')
    print_BinTnodes(t.left)
    print_BinTnodes(t.right)
    print(')', end='')
    
def print_BinTnodes1(t): #中根遍历 
    if t is None:
        print('^', end='')
        return
    print_BinTnodes1(t.left)
    print('('+str(t.data), end='')
    print_BinTnodes1(t.right)
    print(')', end='')

def print_BinTnodes2(t): #后根遍历
    if t is None:
        print('^', end='')
        return
    print_BinTnodes2(t.left)
    print_BinTnodes2(t.right)
    print('('+str(t.data), end='')
    print(')', end='')
    
class HTNode(BinTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data
    
class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self.elems)
    
def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()