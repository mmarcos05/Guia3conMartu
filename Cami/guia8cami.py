from queue import LifoQueue as Pila
import random
import typing
from typing import List

#EJERCICIO 1.1
def contar_lineas(nombre_archivo:str) -> int:
    archivo = open(nombre_archivo, 'r')
    archivo_lineas = archivo.readlines()
    archivo.close()
    return len(archivo_lineas)

print(contar_lineas("archivo.txt"))

#EJERCICIO 1.2
def pertenece(a:str, b: List[str]) -> bool:
    indice: int = 0
    while indice < len(b):
        if b[indice] == a:
            return True
        else: indice += 1
    return False

#EJERCICIO 2
def es_comentario(linea:str) -> bool:
    i:int = 0
    while(i < len(linea) and linea[i] == ' '):
        i += 1
    return i < len(linea) and linea[i] == '#'

"""def es_comentario(linea:str) -> bool:     está mal no sé por qué
    longitud:int = len(linea)
    i:int = 0
    res:bool = False
    while (longitud > i):
        if (linea[i] == ' '):
            i+=1        
        else:
            if (linea[i] == '#'):
                res = True
            else:
                res = False
    return res"""


def clonar_sin_comentarios(nombre_archivo:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    nuevo_archivo:typing.IO = open("clonado.txt", 'w')
    lineas:List[str] = archivo.readlines()

    for linea in lineas:
        if (not es_comentario(linea)):
            nuevo_archivo.write(linea)
    nuevo_archivo.close()
    archivo.close()

    nuevo_archivo = open("clonado.txt", 'r')
    contenido = nuevo_archivo.read()
    print(contenido)
    nuevo_archivo.close()

clonar_sin_comentarios("ejemplo_clonado.py")
        
        
#EJERCICIO 3
def reversa(lista:List[str]) -> List[str]:    #otra forma de hacer la función de reversa
    nueva_lista:List[str] = []
    longitud:int = len(lista)
    i:int = longitud - 1

    for i in range (longitud-1, (-1), (-1)):
        nueva_lista.append(lista[i])
    return nueva_lista

#print(reversa(["cami", "niki", "wendy", "kelly"]))

"""def invertir_lineas(nombre_archivo:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    nuevo_archivo:typing.IO = open("reverso.txt", 'w')

    lineas:List[str] = archivo.readlines()
    lineas_reversa:List[str] = reversa(lineas)

    nuevo_archivo.writelines(lineas_reversa)

    archivo.close()
    nuevo_archivo.close()

    nuevo_archivo = open("reverso.txt", 'r')
    contenido = nuevo_archivo.read()
    print(contenido)
    nuevo_archivo.close()

invertir_lineas("ejemplo_clonado.py")"""

def invertir_lineas(nombre_archivo:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    nuevo_archivo:typing.IO = open("reverso.txt", 'w')
    lineas:List[str] = archivo.readlines()
    cantidad_lineas:int = len(lineas)

    while cantidad_lineas > 0:
        if pertenece('\n', lineas[cantidad_lineas - 1]):
            nuevo_archivo.write(lineas[cantidad_lineas - 1])
        else:
            nuevo_archivo.write(lineas[cantidad_lineas - 1] + '\n')
        cantidad_lineas -=1
    archivo.close()
    nuevo_archivo.close()

    nuevo_archivo = open("reverso.txt", 'r')
    contenido = nuevo_archivo.readlines()
    print(contenido)
    nuevo_archivo.close()

invertir_lineas("ejemplo_clonado.py")

#EJERCICIO 4
def agregar_frase_al_final(nombre_archivo:str, frase:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    lineas:List[str] = archivo.readlines()
    cantidad_lineas:int = len(lineas)
    archivo.close()

    archivo:typing.IO = open(nombre_archivo, 'a')
    
    if pertenece ('\n', lineas[cantidad_lineas - 1]):
        archivo.write(frase)
    else:
        archivo.write('\n' + frase)
    archivo.close()

    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    print(contenido)
    archivo.close()

#agregar_frase_al_final("archivo.txt", "esta es una prueba")

#EJERCICIO 5
"""def agregar_frase_al_principio(nombre_archivo:str, frase:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    lineas:List[str] = archivo.readlines()
    cantidad_lineas:int = len(lineas)
    archivo.close()
    
    archivo:typing.IO = open(nombre_archivo, 'w')
    archivo.write(lineas[cantidad_lineas - 1])
    archivo.close()

    archivo:typing.IO = open(nombre_archivo, 'r')
    lineas:List[str] = archivo.readlines()
    cantidad_lineas:int = len(lineas)
    archivo.close()

    archivo:typing.IO = open(nombre_archivo, 'a')

    while cantidad_lineas >= 0:
        lineas[cantidad_lineas - 2] = lineas[cantidad_lineas - 3]
        cantidad_lineas -= 1
    lineas[0] = frase
    archivo.close()

    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    print(contenido)
    archivo.close()

agregar_frase_al_principio("archivo.txt", "esta es una prueba")"""


#EJERCICIO 8
def generar_nros_al_azar(cantidad: int, desde:int, hasta:int) -> Pila[int]:
    pila = Pila()
    for _ in range (cantidad):
        pila.put(random.randint(desde, hasta))
    return pila

p = generar_nros_al_azar(5, 20, 40)

print(p.get())

#EJERCICIO 9
def cantidad_elementos(p:Pila) -> int:
    pila:Pila = p
    cantidad:int = 0
    while not pila.empty():
        pila.get()
        cantidad += 1
    return cantidad

h = Pila()

h.put(3)
h.put(10)
h.put(2)
h.put(7)
h.put(1)
h.put(4)

print(cantidad_elementos(h))

#EJERCICIO 10
def buscar_el_maximo(p:Pila[int]) -> int:
    pila:Pila[int] = p
    maximo = pila.get()
    while not pila.empty():
        candidato = pila.get()
        if candidato > maximo:
            maximo = candidato
    return maximo
    
p = Pila()

p.put(3)
p.put(10)
p.put(2)
p.put(7)
p.put(1)
p.put(4)

print(buscar_el_maximo(p))

#EJERCICIO 11
#def esta_bien_balanceada(s:str) -> bool:
    