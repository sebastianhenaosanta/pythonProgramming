#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 02:09:00 2020

@author: sebastian
"""


# Import random below:
import random 

# Create random_list below:
random_list = []

# Create randomer_number below:
random_list =[random.randint(1,100) for i in range(101)]
print(random_list)
# Print randomer_number below:
randomer_number = random.choice(random_list)
print(randomer_number)