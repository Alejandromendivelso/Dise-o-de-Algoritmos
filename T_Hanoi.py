def Hanoi(altura,origen, destino, intermedio):
    if altura >= 1:
        Hanoi(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        Hanoi(altura-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("Mover desde:  ",desde,"hasta la",hacia)

Hanoi(3,"Posicion 0","Posicion 1","Posicion 2")
