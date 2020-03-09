#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:24:34 2020

@author: sebastian
"""


fruits = ['banana', 'apple', 'orange', 'tomat', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!') # (It actually is.)
    break
  print('A', f)
else:
  print('A fine selection of fruits!')
  
  
