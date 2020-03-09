#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:03:55 2020

@author: sebastian
"""


def reverse(text):
  bLetter = ""
  for i in range(len(text)-1,-1,-1):
      bLetter += text[i]       
  return bLetter

reverse("sebastian")        
