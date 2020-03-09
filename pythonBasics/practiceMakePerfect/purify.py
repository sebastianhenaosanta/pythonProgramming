#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:37:20 2020

@author: sebastian
"""

"""this programm recieaves a list and remove all odd numbers"""

def purify(x):
    newList = []
    
    for i in x:
        if i % 2 == 0:
            newList.append(i)
    return newList

print(purify([1,2,3]))
            
    