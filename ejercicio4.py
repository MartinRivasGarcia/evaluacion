def campeon_torneo(planilla):
    '''La variable de entrada debe ser una lista la cual contenga tuplas
    con el siguiente formato: string,int,string,int '''
    partidos = len(planilla)
    equipos = {}
    ganador = ""
    #Armo un diccionario con todos los equipos participantes
    for encuentros in planilla:
        equipos[encuentros[0]] = 0
        equipos[encuentros[2]] = 0

    #Verifico el resultado de los partidos y sumo el puntaje
    for encuentros in planilla:
        if(encuentros[1] > encuentros[3]):
            equipos [encuentros[0]] = equipos [encuentros[0]] + 2

        elif(encuentros[3] > encuentros[1]):
            equipos[encuentros[2]] = equipos[encuentros[2]] + 2

        else:
            equipos[encuentros[0]] = equipos[encuentros[0]] + 1
            equipos[encuentros[2]] = equipos[encuentros[2]] + 1

    maximo = 0
    for equipo in equipos:
        if(equipos[equipo] > maximo):
            maximo = equipos[equipo]
            ganador = equipo
    '''La devolucion va a ser un string con el nombre del ganador del torneo'''
    return(ganador)