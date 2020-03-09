#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:36:50 2020

@author: sebastian
"""


"""

Write a function called digit_sum that takes a positive integer n as 
input and returns the sum of all that number’s digits. For example: digit_sum(1234) 
should return 10 which is 1 + 2 + 3 + 4. 
(Assume that the number you are given will always be positive.)

"""

def digit_sum(n):
    newNum = str(n)
    total = 0
    for i in newNum:
        total += int(i)
        
    return total

print(digit_sum(1234))