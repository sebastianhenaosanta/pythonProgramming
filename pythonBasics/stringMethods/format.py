#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:47:17 2020

@author: sebastian
"""


def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date= publishing_date, author = author , title= title, original_work= original_work)
  return poem_desc


my_beard_description = poem_description(author = "Shel Silverstein", title = "My Beard", original_work = "Where the Sidewalk Ends", publishing_date = "1974")
