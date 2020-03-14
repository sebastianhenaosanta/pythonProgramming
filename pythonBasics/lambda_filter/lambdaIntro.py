#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:26:20 2020

@author: sebastian
"""


"""
Anonymous Functions

One of the more powerful aspects of Python is that it allows for a style of programming called functional programming, which means that you’re allowed to pass functions around just as if they were variables or values. Sometimes we take this for granted, but not all languages allow this!

Check out the code at the right. See the lambda bit? Typing

lambda x: x % 3 == 0

Is the same as

def by_three(x):
  return x % 3 == 0

Only we don’t need to actually give the function a name; it does its work and returns a value without one. That’s why the function the lambda creates is an anonymous function.

When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.

"""

#first exercise
my_list = range(16)
print(list(filter(lambda x: x % 3 == 0, my_list)))
#Second exercise
squares =  [i**2 for i in range(1,11)]

print(list(filter(lambda x: x >= 30 and x <= 70, squares)))



















