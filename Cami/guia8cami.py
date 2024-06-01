from queue import LifoQueue as Pila
import random
import typing
from typing import List
from queue import Queue as Cola

#EJERCICIO 1.1
def contar_lineas(nombre_archivo:str) -> int:
    archivo = open(nombre_archivo, 'r')
    archivo_lineas = archivo.readlines()
    archivo.close()
    return len(archivo_lineas)

#print(contar_lineas("archivo.txt"))

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

#clonar_sin_comentarios("ejemplo_clonado.py")
        
        
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

#invertir_lineas("ejemplo_clonado.py")

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
def agregar_frase_al_principio(nombre_archivo:str, frase:str) -> None:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    
    archivo = open(nombre_archivo, 'w')
    archivo.write(frase + '\n' + contenido)
    archivo.close()

    archivo = open(nombre_archivo, 'r')
    contenidofinal = archivo.read()
    print(contenidofinal)
    archivo.close()

#agregar_frase_al_principio("feliz_cumple.txt", "esta es una prueba")

#EJERCICIO 6
"""def listar_palabras_de_archivo(nombre_archivo:str) -> List:
    lista:List = []
    i:int = 0
    archivo_binario = open(nombre_archivo, 'r')
    contenido_binario = archivo_binario.read()
    contenido = chr(contenido_binario)
    archivo_binario.close()

    archivo = open("nuevo.txt", 'w')
    archivo.write(contenido)
    lineas:List = archivo.readlines()
    cantidad_lineas:int = len(lineas)

    while cantidad_lineas - 1 > i:
        if len(lineas[i]) > 5:
            if (pertenece("_", lineas[i]) and pertenece(" ", lineas[i])):
                lista.append(lineas[i])
                i+=1
        i+=1
    return lista"""

#EJERCICIO 7
"""def promedio_estudiante(nombre_archivo, lu:str) -> float:
    archivo = open(nombre_archivo, 'r')
    lineas:List = archivo.readlines()
    i:int = 0
    total:int = 0
    cantidad_materias:int = 0
    cantidad_lineas:int = len(lineas)

    while (cantidad_lineas - 1) > i:
        if (lineas[i])[0] == lu:
            total += (lineas[i])[3]
            cantidad_materias += 1
            i += 1
        else:
            i += 1
    archivo.close()
    if cantidad_materias == 0:
        return 0.0
    else:
        return (total/cantidad_materias)

print(promedio_estudiante("notas.csv", "67890"))"""



#EJERCICIO 8
def generar_nros_al_azar(cantidad: int, desde:int, hasta:int) -> Pila[int]:
    pila = Pila()
    for _ in range (cantidad):
        pila.put(random.randint(desde, hasta))
    return pila

p = generar_nros_al_azar(5, 20, 40)

#print(p.get())

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

#print(cantidad_elementos(h))

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

#print(buscar_el_maximo(p))

#EJERCICIO 11

def esta_bien_balanceada(s:str) -> bool:
    pila:Pila[chr] = Pila()
    for caracter in s:
        if caracter == '(':
            pila.put(caracter)
        elif caracter == ')':
            if pila.empty():
                return False
            else:
                pila.get()
    return pila.empty()

#print(esta_bien_balanceada("1 + (2 x 3 - (20 / 5))"))
#print(esta_bien_balanceada("10 ∗ ( 1 + ( 2 ∗ ( −1)))"))
#print(esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))

#EJERCICIO 12
"""def pertenece2(a:chr, b: str) -> bool:
    indice: int = 0
    while indice < len(b):
        if b[indice] == a:
            return True
        else: indice += 1
    return False"""

def evaluar_expresion(s:str) -> float:
    operadores:List = ['+', '-', '*', '/']
    pila:Pila[int] = Pila()
    total:int = 0
    for caracter in s:
        if (not pertenece(caracter, operadores)) and (caracter != ' '):
            pila.put(caracter)
        elif pertenece(caracter, operadores):
            if caracter == '+':
                total = (int(pila.get()) + int(pila.get()))
                pila.put(total)
            elif  caracter == '-':
                total = - (int(pila.get()) - int(pila.get()))
                pila.put(total)
            elif  caracter == '*':
                total = (int(pila.get()) * int(pila.get()))
                pila.put(total)
            else:
                total = (int(pila.get()) / int(pila.get()))
                pila.put(total)
    return int(pila.get())

#print(evaluar_expresion("3 4 + 5 * 2 -"))

#EJERCICIO 13
def armar_cola(lista:List[int]) -> Cola:
    c = Cola()
    i:int = 0
    longitud:int = len(lista)
    for i in range (longitud):
        c.put(lista[i])
    return c

print(armar_cola([1,2,3,4,5]))
