def formato_admitido(ruta,extensiones):
    '''Ruta tiene que ser un string y extensiones tiene que ser una lista que contenga strings'''
    largo = len(ruta)
    a = 0
    existencia = 0
    for caracter in ruta:
        if(caracter == '.'):
            b = a+1
            existencia = 1
        else:
            a = a+1
    '''No se afectaran los valores de entrada, la devolucion va a ser un boolenao igual a True o a False'''
    if(existencia == 1):
        prueba = ruta[b:largo].lower()
        for valido in extensiones:
            valido = valido.lower()
            if(valido == prueba):
                return True
    return False

print(formato_admitido('/home/user/listado.txt',['mp3','wav','mpeg']))