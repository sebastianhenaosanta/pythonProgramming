#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:08:51 2020

@author: sebastian
"""


"""
Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks. For example:

censor("this hack is wack hack", "hack") ```

should return: 

```py
"this **** is wack ****"

    Assume your input strings won’t contain punctuation or upper case letters.
    The number of asterisks you put should correspond to the number of letters in the censored word.

"""

def censor(text, word):
    text = text.split()
    for i in range(0, len(text)):
        if text[i] == word:
            text[i] = len(word)*"*"
    
    return " ".join(text)
    
print(censor("sebastian henao santa", "henao"))
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    