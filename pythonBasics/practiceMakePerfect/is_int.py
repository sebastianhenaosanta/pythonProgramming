#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:31:27 2020

@author: sebastian
"""


"""
is_int

An integer is just a number without a decimal part (for instance, -17, 0, and 42 are all integers, but 98.6 is not).

For the purpose of this lesson, we’ll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0.

This means that, for this lesson, you can’t just test the input to see if it’s of type int.

If the difference between a number and that same number rounded is greater than zero, what does that say about that particular number?

"""


def is_int(x):
    
    if x - round(x) > 0 or x - round(x) < 0:
        return False
    elif x - round(x) == 0:
        return True
    
print(is_int(7.0))
    
    