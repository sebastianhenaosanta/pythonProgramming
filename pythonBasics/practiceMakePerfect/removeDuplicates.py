#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:37:30 2020

@author: sebastian
"""
def remove_duplicates(x):
    auxList = []
    bNumber= 0
    #burbuja algorithm
    for i in range(0, len(x)):
        for j in range(0, len(x)):
           if j == len(x)-1:
               break
           if x[j] > x[j + 1]:
               bNumber = x[j]
               x[j] = x[j+1]
               x[j+1] = bNumber
    #algorithm to filter list
    for i in range(0,len(x)):
        if i == len(x)-1:
            auxList.append(x[i])
            break
        if x[i] != x[i+1]:
            auxList.append(x[i])
    
    return auxList
                
print(remove_duplicates([4, 5, 5, 4]))        
    
        
    
