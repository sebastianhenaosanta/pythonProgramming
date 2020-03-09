#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:40:36 2020

@author: sebastian
"""


"""
factorial

All right! Now we’re cooking. Let’s try a factorial problem.

To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example:

    factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
    factorial(1) would equal 1.
    factorial(3) would equal 3 * 2 * 1, which is 6.


"""

def factorial(x):
    total = 1
    for i in range(1,x+1):
        total *=i
    return total
    
print(factorial(5))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    