import typing
from typing import List

#EJERCICIO 1
def ind_nesima_aparicion(s:List[int], n:int, elem:int) -> int:
    apariciones:int = 0
    longitud:int = len(s)
    i:int = 0
    while longitud > i:
        if s[i] == elem:
            apariciones += 1
            if apariciones == n:
                return i
            i += 1
        else:
            i += 1
    return -1
    
lista:List[int] = [1,2,3,2,4,6,2,2,9,2]
#print(ind_nesima_aparicion(lista, 8, 2))

#EJERCICIO 2
def es_par(n:int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

#print(es_par(5))

def mezclar(s1:List[int], s2:List[int]) -> List[int]:
    lista_mezclada:List[int] = []
    longitud_listas:int = len(s1)
    i:int = 0

    while longitud_listas > i:
        lista_mezclada.append(s1[i])
        lista_mezclada.append(s2[i])
        i+=1
    return lista_mezclada

s1:List[int] = [1, 3, 0, 1]
s2:List[int] = [4, 0, 2, 3]
#print(mezclar(s1, s2))

#debería devolver res = [1, 4, 3, 0, 0, 2, 1, 3]

#EJERCICIO 3
def frecuencia_posiciones_por_caballo(caballos:List[str], carreras:dict) -> dict:
    #carreras:dict[str,posiciones_caballos]   # posiciones_caballos:List[str]
    #diccionario_final:dict[str,List[int]]    # frecuencia:List[int]

    dicc_frecuencias:dict = dict()
    lista_frecuencia:List[int] = [0]*len(caballos)
    lista_carreras:List[tuple] = list(carreras.items())
    
    for caballo in caballos:
        for tupla in lista_carreras:
            posiciones_caballos:List[str] = tupla[1]
            i:int = 0
            while len(posiciones_caballos) > i:
                if posiciones_caballos[i] == caballo:
                    lista_frecuencia[i] += 1
                    i+=1
                else:
                    i+=1
        dicc_frecuencias[caballo] = lista_frecuencia
        lista_frecuencia = [0]*len(caballos)
    return dicc_frecuencias

caballos = ["linda", "petisa", "mister", "luck" ]
carreras = {"carrera1":["linda", "petisa", "mister", "luck"],"carrera2":["petisa", "mister", "linda", "luck"]}
#se debería devolver res = {"petisa": [1,1,0,0],
                           #"mister": [0,1,1,0],
                           #"linda": [1,0,1,0],
                           #"luck": [0,0,0,2]}
#print(frecuencia_posiciones_por_caballo(caballos, carreras))

#EJERCICIO 4
def reversa(lista:List[int]) -> List[int]:
    reverso:List[int] = []
    i:int = len(lista) - 1
    while i > (-1):
        reverso.append(lista[i])
        i-=1
    return reverso

def es_capicua(lista:List[int]) -> bool:
    if lista == reversa(lista):
        return True
    else:
        return False
    
def matriz_capicua(m:List[List[int]]) -> bool:
    for fila in m:
        if not es_capicua(fila):
            return False
    return True

#m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
#print(matriz_capicua(m))