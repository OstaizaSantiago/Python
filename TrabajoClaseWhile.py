# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:35:23 2021

@author: RYZEN
"""

#CLASE 25/01/2021
#TRABAJO EN CLASE
#BUCLE WHILE
while True:
    x=input("Enter a number to count to:")
    if x == "q" or x =="quit":
        break
    
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
   