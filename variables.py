# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# CLASE 11/01/2021
# TIPOS DE VARIABLES
print(type(5))
print(type(8.5))
print(type('Python'))
print(type(False))

# VARIABLES BOOLEANOS
print(8>5)
print(8>=5)
print(8<=5)

# OPERACIONES
X=5
print(X**5)
print(X/5)
print(X-5)
print(X+5)

# SEPARADORES
print(X, '\n'*2)
print(X/5, '\n'*2)
print(X-5, '\n'*2)
print(X+5, '\n'*2)
    
# STRING
str1= 'Cisco'
str2= 'Networking'
str3= "Academy"
space=" "
print(str1+space+str2+space+str3)
print('\n')
print(str1+str2+str3)
print(str1,str2,str3, '\n'*2)
print(str1,str2,str3, '\n'*2)
print(type(X), '\n')
print('El valor de X es: ' +str(X), '\n')

# IMPRIMIR VARIABLES
print(type(X))
X=str(X)
print(type(X))
X=int(X)
print(type(X))
X=float(X)
print(type(X))
X=bool(X)
print(type(X))

# DECIMALES
pi=22/7
print(pi)
print('{:.5f}'.format(pi))

# LISTAS Y DICCIONARIOS - VECTORES
lista=['R1',5,5.8,True,'R2']
print(lista)
print(type(lista))
print(len(lista))
print(lista[0], '\n')
print(lista[4], '\n')
print(lista[-1], '\n') 
lista[3]-False
print(lista)
del lista[4]
print(len(lista))
print(lista)
lista.append('R2')
print(lista)
lista.append('R3')
print(lista)