def formato_admitido(ruta,extensiones):
    '''Ruta tiene que ser un string y extensiones tiene que ser una lista que contenga strings'''
    largo = len(ruta)
    a = 0
    for caracter in ruta:
        if(caracter == '.'):
            b = a+1
        else:
            a = a+1
    '''No se afectaran los valores de entrada, la devolucion va a ser un boolenao igual a True o a False'''
    for valido in extensiones:
        if(valido == ruta[b:largo]):
            return True
    return False