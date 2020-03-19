#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:31:32 2020

@author: sebastian
"""


class Point:
  def __init__(self, x=0, y=0):
      self.x = x
      self.y = y     
  def __repr__(self):
      return "(%d, %d)" % (self.x, self.y)
        


point1 = Point(10,20)
print(point1)
