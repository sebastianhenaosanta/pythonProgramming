#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:40:49 2020

@author: sebastian
"""


with open("text.txt", 'w') as my_file:
    my_file.write("sebastian Henao")

print(my_file.closed)