from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
import typing

#cantidad de elementos Pila

def cantidad_elementos(p:Pila) -> int:
    cantidad = 0
    pila = p
    while not pila.empty():
        pila.get()
        cantidad += 1
    return cantidad

#copiar pila 

def copiar_pila(p:Pila) -> Pila:
    pila1 = Pila()
    pila2 = Pila()

    while not p.empty():
        pila1.put(p.get())
    while not pila1.empty():
        pila2.put(pila1.get())
    return pila2

#invertir pila

def invertir_pila(pila:Pila) -> Pila:
    pAux = Pila()
    while not pila.empty():
        pAux.put(pila.get())
    return pAux

#pertenece en listas

def pertenece(lista,numero):
    i = 0
    while i < len(lista):
        if lista[i] == numero:
            return True
        else:
            i += 1
            
#hay repetidos en lista

def hay_repetidos(lista:list[int]) -> bool:
    i = 0
    contador = 0
    while i < len(lista):
        for elem in lista:
            if elem == lista[i]:
                contador += 1
            if contador > 1:
                return True
        contador = 0
        i +=1
    return False

#lista simetrica (len(lista) par)

def lista_simetrica(lista):
    mitad = int(len(lista) / 2)
    i = 0
    while i < mitad:
        if lista[i] != lista[mitad + i]:
            return False
        i += 1
            
#split de palabras

def mi_split(linea):
    res = []
    palabra = ""
    for char in linea:
        if char == " " or char == "\t" or char == "\n" or char == "\r":
            if len(palabra) > 0:
                res.append(palabra)
                palabra = ""
        else:
            palabra += char
    return res

#pertenece en diccionarios (claves)

def pertenece_dicts(d:dict, k) -> bool:
    lista = list(d.keys())
    for e in lista:
        if e == k:
            return True
    return False

#invertir matriz

def invertir_matriz(m:list[list[int]]) -> list[list[int]]:
    i = 0
    nueva_matriz = []
    nueva_fila = []
    while i < len(m):
        for fila in m:
            nueva_fila.append(fila[i])
        nueva_matriz.append(nueva_fila)
        nueva_fila = []
        i += 1
    return nueva_matriz   