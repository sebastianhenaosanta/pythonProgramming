#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:15:41 2020

@author: sebastian
"""

def anti_vowel(text):
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    newText = ''
    for i in range(0, len(text)):
        for j in vowels:
            if text[i] == j:
                break
        else:
            newText += text[i]
    return newText
print(anti_vowel("Hey You!"))
                
                
    


