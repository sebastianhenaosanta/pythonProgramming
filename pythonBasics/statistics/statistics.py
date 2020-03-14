#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 08:27:41 2020

@author: sebastian
"""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

print("Grades",grades);

def print_grades(grades_input):
    for i in grades_input:
        print(i)
        
        
def grades_sum(scores):
    total = 0
    for i in scores:
        total += i    
    return total


def grades_average(grades_input):
    
    return grades_sum(grades_input)/float(len(grades_input))
    

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    
    for score in scores:
        variance += (average - score)**2
    
    variance = variance / len(scores)
    
    return variance

def grades_std_deviation(variance):
    return variance**0.5

variance = grades_variance(grades)

print_grades(grades)
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
variance = grades_variance(grades)
print(grades_std_deviation(variance))


