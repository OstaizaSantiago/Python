# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:14:48 2021

@author: RYZEN
"""

#CLASE 25/01/2021
#VALIDACIÓN MEDIANTE CONDICIONALES
acl=int(input("Ingrese el # de ACL:"))
if acl>=1 and acl<=99:
    print("es una ACL estandar")
elif acl>100 and acl<=199:
    print("es una ACL extendida")
else:
    print("No es un # de ACL válido")
    
#TIPOS DE EXCEPCIONES    
try:
    print("mensaje")
except:
    print("Error")
    
#