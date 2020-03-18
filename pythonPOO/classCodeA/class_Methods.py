#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:50:59 2020

@author: sebastian
"""


"""
A Methodical Approach

When a class has its own functions, those functions are called methods. 
You’ve already seen one such method: __init__(). But you can also define your own methods!
"""

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
      print(self.name)
      print(self.age)
      
      
hippo = Animal("mateo", 29)
hippo.description()