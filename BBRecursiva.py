
def BB_recursiva(Lista, busqueda, izquierda, derecha):
    if izquierda > derecha:
        return -1
    indiceDelElementoDelMedio = (izquierda + derecha) // 2
    elementoDelMedio = Lista[indiceDelElementoDelMedio]
    if elementoDelMedio == busqueda:
        return indiceDelElementoDelMedio
    if busqueda < elementoDelMedio:
        return BB_recursiva(Lista, busqueda, izquierda, indiceDelElementoDelMedio - 1)
    else:
        return BB_recursiva(Lista, busqueda, indiceDelElementoDelMedio + 1, derecha)

Lista= [1, 2, 3, 10, 50, 80, 120, 150, 500, 1000]
print("Vamos a buscar en la siguiente lista:", Lista)
busqueda = 500
indice = BB_recursiva(Lista, busqueda, 0, len(Lista) - 1)
print("El elemento {} está en el índice {}".format(busqueda, indice))