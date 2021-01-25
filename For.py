# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:31:12 2021

@author: RYZEN
"""
#CLASE 25/01/2021
#BUCLE FOR
#LISTAS BLANCAS
listadf=[]
listar=[]
listasw=[]
lista=["R1","R2","R3","S1","S2","S3","R4","R5","PC"]
for i in lista:
    if "S" in i:
        listasw.append(i)
    elif "R" in i:
        listar.append(i) 
    else:
        listadf.append(i)
print("SWITCHES:",listasw, "\nROUTERS:",listar, "\nDISPOSITIVOS:",listadf)

#MODIFICACIÓN
print("Comienzo")
for i in range(18,0,-1):
    print(1,end=" ")
print()
print("Final")