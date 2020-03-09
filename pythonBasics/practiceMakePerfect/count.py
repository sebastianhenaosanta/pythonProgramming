#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:31:20 2020

@author: sebastian
"""

def count(sequence, item):
    counter = 0
    for i in sequence:
        if i == item:
            counter += 1
    return counter
