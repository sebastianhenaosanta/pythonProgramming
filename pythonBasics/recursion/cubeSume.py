#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:27:57 2020

@author: sebastian
"""

import time
number = int(input("enter the number of n: "))


"""
this part of the code execute the fallowing recursion and also is measuring 
how long time the code takes to execute 

sc(n) = sc(n-1) + n 3

"""
start = time.time()
def sumCubes(x):
    total = 0
    if x == 1:
        total = 1
    else:
        total = sumCubes(x-1) + x**3        
    return total

endTime = time.time()
final = endTime -start


total = 0 

"""
This is the same code but using a for loop

"""

start2 = time.time()
for i in range(0, number+1):
    
    total += i**3

end2 = time.time()

final2 = end2 -start2
    

print(final)
print(final2)
print(sumCubes(number))
print(total)    
    