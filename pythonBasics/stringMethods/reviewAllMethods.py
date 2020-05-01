#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 02:04:54 2020

@author: sebastian
"""


highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
#print(highlighted_poems_list)

highlighted_poems_stripped = [highlighted_poems_list[i].strip() for i in range(len(highlighted_poems_list))]

#print(highlighted_poems_stripped)

highlighted_poems_details =[highlighted_poems_stripped[i].split(":") for i in range(len(highlighted_poems_stripped))]
print(highlighted_poems_details)

titles = []
poets = []
dates = []

for i in range(len(highlighted_poems_details)):
  titles.append(highlighted_poems_details[i][0])
  poets.append(highlighted_poems_details[i][1])
  dates.append(highlighted_poems_details[i][2])


for i in range(len(titles)):
  print("The poem {titles} was published by {poets} in {dates}.".format(titles=titles[i],poets = poets[i], dates = dates[i]))  