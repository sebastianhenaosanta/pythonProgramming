#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:33:22 2020

@author: sebastian
"""
"""
median

Great work! You’ve covered a lot in these exercises. Last but not least, let’s write a function to find the median of a list.

The median is the middle number in a sorted sequence of numbers.

Finding the median of [7, 12, 3, 1, 6] would first consist of sorting the sequence into [1, 3, 6, 7, 12] and then locating the middle value, which would be 6.

If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.

For example, the median of the sequence [7, 3, 1, 4] is 3.5, since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.

You can sort the sequence using the sorted() function, like so:

sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]

"""

def median(x):
    x = sorted(x)
    if len(x) % 2 != 0:
        return int(x[(len(x)-1)/2])
    else:
        return float((x[int(len(x)/2.0)-1] + x[int(len(x)/2.0)])/2.0)
    
print(median([4, 5, 5, 4]))    
    
    
    
    
    

