#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:35:20 2020

@author: sebastian
"""


lloyd = {"name":"Lloyd",
         "homework": [90.0, 97.0, 75.0, 92.0],
         "quizzes": [88.0, 40.0, 94.0],
         "tests": [75.0, 90.0]
        }

alice = {"name":"Alice",
         "homework": [100.0, 92.0, 98.0, 100.0],
         "quizzes": [82.0, 83.0, 91.0],
         "tests": [89.0, 97.0]
        }

tyler = {"name":"Tyler",
         "homework": [100.0, 92.0, 98.0, 100.0],
         "quizzes": [82.0, 83.0, 91.0],
         "tests": [89.0, 97.0]
        }

students = [lloyd, alice, tyler]


for i in students:
    print(i["name"])
    print(i["homework"])
    print(i["quizzes"])
    print(i["tests"])
    
def average(numbers):
    total = 0
    total = sum(numbers)/len(numbers)
    return total
    
def get_average(student):
    
    homework = average(student["homework"])*0.1
    quizzes  = average(student["quizzes"])*0.3
    tests = average(student["tests"])*0.6    
    return sum([homework,quizzes,tests])   


def get_letter_grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return  "C"
	elif score >= 60:
		return "D"
	else:
		return "F"
    

def get_class_average(class_list):
    
    results = []
    for i in class_list:
        results.append(get_average(i))
    return average(results)

	
print(get_letter_grade(get_class_average(students)))
	
	







