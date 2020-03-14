#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:18:30 2020

@author: sebastian
"""
"""
List Comprehension Syntax

Here’s a simple example of list comprehension syntax:

new_list = [x for x in range(1, 6)]
# => [1, 2, 3, 4, 5]

This will create a new_list populated by the numbers one to five. If you want those numbers doubled, you could use:

doubles = [x * 2 for x in range(1, 6)]
# => [2, 4, 6, 8, 10]

And if you only wanted the doubled numbers that are evenly divisible by three:

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# => [6]
"""

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares =  [x**2 for x in range(1,11,2)]

print(even_squares)


