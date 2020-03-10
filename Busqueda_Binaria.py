import random
import time 

Archivo = open('Numeros.txt','w')
newText=''
for numero in range(10):
    newText += str(random.randrange(199)) + ','
Archivo.write(newText.strip(','))

Archivo.close()

contenido=open('Numeros.txt','r')
listas= [lista.split() for lista in contenido]
for lista in listas:
    print  (listas)

def busqueda_binaria(lista,valor):
    primero = 0
    ultimo = len(lista)-1
    encontro = False

    while primero <= ultimo and not encontro:
        mitad =(primero + ultimo)// 2

        if lista[mitad] == valor:
            encontro = True
        else:
            if valor < lista[mitad]:
                ultimo = mitad -1
            else:
                primero = mitad +1
    return encontro

    listas = []

    




