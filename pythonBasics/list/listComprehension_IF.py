#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:15:25 2020

@author: sebastian
"""


"""
c = ['C' for x in range(5) if x < 3]
print c
"""


cube_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0]
print(cube_by_four)