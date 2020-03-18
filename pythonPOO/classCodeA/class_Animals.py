#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:38:42 2020

@author: sebastian
"""


class Animal(object):
    def __init__(self, name):
        self.name = name


zebra = Animal("Jeffrey")

print(zebra.name)