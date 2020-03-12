import random
import time 

Archivo = open('Numeros.txt','w')
newText=''
for numero in range(10):
    newText += str(random.randrange(20)) + ','
Archivo.write(newText.strip(','))

Archivo.close()

def busqueda_binaria(n_lista, valores):
    primero =0
    ultimo = len(n_lista) -1
    encon = False

    while primero <= ultimo and not encon:
         mitad = (primero + ultimo)//2

         if n_lista[mitad] ==valores:
             encon= True
         else:
            if valores <  n_lista[mitad]:
                ultimo =mitad -1
            else:
                primero = mitad+1
    return encon

contenido=open('Numeros.txt','r')
listas= [lista.split() for lista in contenido]
for lista in listas:
    print  (listas)
n_lista = sorted(listas)
llave = 3
print(busqueda_binaria(n_lista,llave))

