#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:12:25 2020

@author: sebastian
"""


import mmap


header= [170, 68, 18]
count = 0
flag = 0
lenghHead = []
idMessage = []
with open("./data/GPS_HELIPUERTO_Dronearth_Colombia.rgi", mode = 'rb') as data:
    with mmap.mmap(data.fileno(), 0, access=mmap.ACCESS_READ) as m:
        for i in range(0, len(m)):
            if(i == len(m)-1):
                break
            if m[i] == 170 and m[i+1] == 68 and m[i+2] == 18:
                idMessage.append(int(hex(m[i+5]).rstrip("L").lstrip("0x")+hex(m[i+4]).rstrip("L").lstrip("0x"),16))
                for j in range(i+3, len(m)):
                    if m[j] == 170 and m[j+1] == 68 and m[j+2] == 18:
                        break
                
                
                    
                
                
                                      
                    
                
                

        
    
    
    


