from random import randint
from time import time

lista=[]

for i in range(0,100): # aqui hacemos la introduccion de datos que queremos ingresar 
    lista.append(randint(0,1000)) # aqui podremos ver el rando de los numeros quee se van a coloar alateorios 

Tiempo_inicial = time()
temporal = 0 

for j in range(1,len(lista)):
    for i in range (0,len(lista)-j):
        if lista[i]>lista[i+1]: 
            temporal = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temporal


print(lista) 
tiem_final = time()
print("TIempo de ejecucion: "+ str(tiem_final-Tiempo_inicial))