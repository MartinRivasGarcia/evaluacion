import random
def matriz_triangular(n):
    '''La variable de entrada tiene que ser un numero entero positivo'''
    matriz = []
    for a in range(1, n + 1):
        matriz.append([])
    for a in range(0,n):
        for b in range(0, n):
            numero = random.randint(0,9)
            matriz[a].insert(b,numero)
    '''La devolucion es una lista con listas dentro'''
    return (matriz)