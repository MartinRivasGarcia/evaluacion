import random
def matriz_triangular(n):
    '''La variable de entrada tiene que ser un numero entero positivo'''
    matriz = []
    if(type(n) == int):
        if(n > 1 or n < -1):
            if(n < 0):
                n = -n
            for a in range(1, n + 1):
                matriz.append([])
            for a in range(0,n):
                retengo = a
                while(retengo > 0):
                    matriz[a].insert(a, 0)
                    retengo = retengo - 1
                for b in range(a, n):
                    numero = random.randint(0,9)
                    matriz[a].insert(b,numero)
    '''La devolucion es una lista con listas dentro'''
    return (matriz)