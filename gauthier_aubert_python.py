#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:44:18 2020 

@author: gauthieraubert
"""

def affichage():
    i = 0
    while i <= 999:
         if i < 10:
            print("00",i)
         if i < 100 and i >= 10:
            print("0",i)
         elif i>= 100:
            print(i)
         i=i+1
         
print(affichage())
      
     
     
    
    
            
    