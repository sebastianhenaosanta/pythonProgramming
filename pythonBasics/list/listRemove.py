#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:54:48 2020

@author: sebastian
"""


"""
Removing elements from lists

This exercise will expand on ways to remove items from a list. You actually have a few options. For a list called n:

    n.pop(index) will remove the item at index from the list and return it to you:

    n = [1, 3, 5]
    n.pop(1)
    # Returns 3 (the item at index 1)
    print n
    # prints [1, 5]

    n.remove(item) will remove the actual item if it finds it:

    n.remove(1)
    # Removes 1 from the list,
    # NOT the item at index 1
    print n
    # prints [3, 5]

    del(n[1]) is like .pop in that it will remove the item at the given index, but it won’t return it:

    del(n[1])
    # Doesn't return anything
    print n
    # prints [1, 5]
    
    .
#exercise
    
    
Remove the first item from the list n using either .pop(), .remove(), or del.


"""

n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0)
print(n)



























