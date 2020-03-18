#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:15:47 2020

@author: sebastian
"""

"""
Override!

Sometimes you’ll want one class that inherits from another to not only take on 
the methods and attributes of its parent, but to override one or more of them.

class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print("Hello, %s" % other.name)

class CEO(Employee):
  def greet(self, other):
    print("Get back to work, %s!" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!
"""

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
    
    def calculate_wage(self, hours):
        self.hours = hours
        
        return self.hours * 12.0
        
        






