from random import randint
from time import time

lista_Insercion=[]

for i in range(0,1000000): # aqui hacemos la introduccion de datos que queremos ingresar 
    Tiempo_inicial = time()
    lista_Insercion.append(randint(0,1000))# aqui podremos ver el rando de los numeros quee se van a coloar alateorios 
def insercion(lista_Insercion):  
    for i in range(len(lista_Insercion)):
        for j in range(i,0,-1):
            if(lista_Insercion[j-1] > lista_Insercion[j]):
                aux=lista_Insercion[j]
                lista_Insercion[j]=lista_Insercion[j-1]
                lista_Insercion[j-1]=aux
                
    print("la nuesva lista es:")
    print (lista_Insercion)

print("la lista es: ")
print (lista_Insercion)
insercion(lista_Insercion)
tiempo_final = time()

print("Tiempo de ejecucion: " +str(tiempo_final-Tiempo_inicial))