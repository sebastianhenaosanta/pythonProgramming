#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:56:30 2020

@author: sebastian
"""


class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
      print(self.name)
      print(self.age)
      
      
hippo = Animal("mateo", 3)
sloth = Animal("carlos", 2)
ocelot = Animal("terry", 4)
hippo.description()
print(hippo.health)
print(sloth.health)
print(ocelot.health)
