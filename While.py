# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:18:52 2021

@author: RYZEN
"""

#CLASE 25/01/2021
#BUCLE WHILE
x=input("Ingrese el # que contaré:")
x=int(x)
y=1
while y<=x:
    print(y)
    y+=1

#EVALUACIÓN DEL WHILE TRUE
x=input("Ingrese el # que contaré:")
x=int(x)
y=1
while True:
    print(y)
    y+=1
    if y>x:
        break

