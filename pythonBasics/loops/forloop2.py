#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:11:21 2020

@author: sebastian
"""
phrase = "A bird in the hand..."

# Add your for loop
for i in phrase:
  if i == 'a' or i == 'A':
    print("X",  end = ''),
  else:
    print(i, end = ''),


