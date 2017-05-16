def divisores_de_un_numero(n,lista):
    '''EL valor de entrada n debe ser un numero entero mayor a cero.
    El valor de lista, tiene que ser una lista conformada por numero enteros.'''
    resolucion = []
    if((n > 0) and (type(n) == int)):
        for elemento in lista:
            if((n % elemento) == 0):
                resolucion.append(elemento)
    '''La devolucion va a ser una lista con todos los numeros que son divisores de n, en caso
    de que n no cumpla con las condiciones pedidas devuelve una lista vacia'''
    return (resolucion)