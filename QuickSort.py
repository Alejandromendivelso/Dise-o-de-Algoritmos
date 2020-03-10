from random import randint
from time import time 

lista_QuickSort = []

for i in range(0,100000000):# aqui hacemos la introduccion de datos que queremos ingresar 
    lista_QuickSort.append(randint(0,10000000000))# aqui podremos ver el rando de los numeros quee se van a coloar alateorios

Tiempo_inicial = time()
def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return sort(izquierda)+centro+sort(derecha)
    else:
        return lista


print("La lista es:")
print(lista_QuickSort)
print("La nueva lista es:")
print(sort(lista_QuickSort))
Tiempo_Final = time()
print("Tiempo de ejecucion es: "+ str(Tiempo_Final-Tiempo_inicial))
