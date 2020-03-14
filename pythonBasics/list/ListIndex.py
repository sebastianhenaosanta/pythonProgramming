#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:22:38 2020

@author: sebastian
"""


"""
If you don’t pass a particular index to the list slice, Python will pick a default.

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

    The default starting index is 0.
    The default ending index is the end of the list.
    The default stride is 1.
"""

my_list = list(range(1, 11)) # List of numbers 1 - 10

print(my_list[1::2])


