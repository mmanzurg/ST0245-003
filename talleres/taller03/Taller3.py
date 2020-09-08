def hanoi(n, origen, intermedio, destino):
    if n>=1:
        hanoi(n-1,origen,intermedio,destino)
        mover(origen,destino)
        hanoi(n-1,intermedio,origen,destino)


def mover(inicio, fin):
     print("mover un disco de la "+inicio + " a "+fin)

hanoi(5,"torre 1","torre 2","torre 3")

def permutations(base, stri):
    if (stri==""):
        print (base)
    else:
        for i in range(len(stri)):
            permutations(base+stri[i], stri[:i]+stri[i+1:])

permutations("","abcd")
