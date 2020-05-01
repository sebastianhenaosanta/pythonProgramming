#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 02:49:15 2020

@author: sebastian
"""

from datetime import datetime
parsed_date = datetime.strptime("May 1, 2020", "%b %w, %Y")

dateString = datetime.strftime(datetime.now(), '%b %d, %Y')