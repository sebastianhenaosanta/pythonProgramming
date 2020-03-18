#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:04:43 2020

@author: sebastian
"""


"""
On the flip side, sometimes you’ll be working with a derived class 
(or subclass) and realize that you’ve overwritten a method or attribute defined in that class’ 
base class (also called a parent or superclass) that you actually need. Have no fear! You can 
directly access the attributes or methods of a superclass with Python’s built-in super call.

The syntax looks like this:

class Derived(Base):
  def m(self):
    return super(Derived, self).m()

Where m() is a method from the base class.

"""


class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    
    def calculate_wage(self, hours):
        self.hours = hours
        return self.hours * 12.0
    
    def full_time_wage(self, hours):
        return super(PartTimeEmployee,self).calculate_wage(hours)

    
milton = PartTimeEmployee("milton")

print(milton.full_time_wage(10))
    


    