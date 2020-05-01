#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:00:49 2020

@author: sebastian
"""


love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = [love_maybe_lines[i].strip() for i in range(len(love_maybe_lines))]

love_maybe_full = "\n".join(love_maybe_lines_stripped)