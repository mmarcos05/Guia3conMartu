

import re


def acomodar(s):
    lista = s
    lista_nueva = []
    for partido in lista:
        if partido == 'UP':
            lista_nueva.append(partido)
    for partido in lista:
        if partido == 'LLA':
            lista_nueva.append(partido)
    return lista_nueva

#print(acomodar(['LLA','UP','LLA','LLA','UP']))

def pos_umbral(s,u):
    umbral = u
    clientes = s
    i = 0
    total_actual = 0
    while i < len(clientes):
        if clientes[i] > 0:
            total_actual += clientes[i]
            if total_actual > umbral:
                return i
        i += 1

#print(pos_umbral([1,-2,0,5,-7,3], 5))

def columnas_repetidas(mat):
    primera_fila = mat[0]
    mitad = int(len(primera_fila) / 2)
    for fila in mat:
        if lista_simetrica(fila,mitad) == False:
            return False
    return True

def lista_simetrica(lista,mitad):
    i = 0
    while i < mitad:
        if lista[i] != lista[mitad + i]:
            return False
        i += 1


#m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
#print(columnas_repetidas(m))

def cuenta_posiciones_por_nacion(naciones,torneos):
    ipais = 0
    i = 0
    apariciones = 0
    res = {}
    lista_posiciones = []
    while ipais < len(naciones):
        pais = naciones[ipais]
        while i < len(naciones):
            for torneo,posicion in torneos.items():
                if posicion[i] == pais:
                    apariciones += 1
            lista_posiciones.append(apariciones)
            i += 1
            apariciones = 0
        res[pais] = lista_posiciones
        lista_posiciones = []
        ipais += 1
        i = 0
    return res

naciones= ["arg", "aus", "nz", "sud"]
torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}

#print(cuenta_posiciones_por_nacion(naciones,torneos))





    
