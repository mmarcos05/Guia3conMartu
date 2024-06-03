from queue import LifoQueue as Pila
import random
import typing

#Archivos

#Ejercicio 1.1

def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    return len(lineas)

#Ejericicio 1.2

def existe_palabra(palabra:str, nombre_archivo:str) -> bool:
    archivo = open(nombre_archivo, 'r')
    for lineas in archivo:
        if lineas.find(palabra) != -1:
            return True
    archivo.close()
    return False

#Ejercicio 1.3

def cantidad_apariciones(nombre_archivo:str, palabra:str) -> int:
    archivo = open(nombre_archivo, 'r')
    i = 0
    for lineas in archivo:
        if lineas.find(palabra) != -1:
            i += 1
    archivo.close()
    return i

#Ejercicio 2

def clonar_sin_comentarios(nombre_de_archivo:str) -> None:
    archivo: typing.IO = open(nombre_de_archivo, 'r')
    archivo_clonado: typing.IO = open("clonado.txt", 'w')
    lineas = archivo.readlines()
    for linea in lineas:
        if (not es_comentario(linea)):
            archivo_clonado.write(linea)
    archivo.close()
    archivo_clonado.close()
    
def es_comentario(linea:str) -> bool:
    i = 0
    while i < len(linea) and linea[i] == ' ':
        i +=1
    if linea[i] == '#':
        return True

#Ejercicio 3

def invertir_lineas(nombre_archivo:str):
    archivo = open(nombre_archivo, 'r')
    archivo_reverso = open("reverso.txt",'w')
    lineas = archivo.readlines()
    lineas_reverso = reverso(lineas)
    for linea in lineas_reverso:
        archivo_reverso.write(linea)
    archivo.close()

def reverso(lista):
    i = len(lista)
    reversa = []
    while i > 0:
        reversa.append(lista[i-1])
        i -= 1
    return reversa

#Ejercicio 4

def agregar_frase_al_final(nombre_archivo:str, frase:str):
    archivo_leer = open(nombre_archivo, 'r')
    archivo_leer.read()
    archivo_escribir = open(nombre_archivo, 'a')
    lineas = archivo_leer.readlines()
    for linea in lineas:
        archivo_escribir.write(linea)
    archivo_escribir.write(frase)
    archivo_leer.close()
    
#Ejercicio 5

def agregar_frase_al_principio(nombre_archivo:str, frase:str):
    archivo_leer = open(nombre_archivo, 'r')
    lineas = archivo_leer.readlines()
    archivo_escribir = open(nombre_archivo, 'w')
    archivo_escribir.write(frase + '\n')
    for linea in lineas:
        archivo_escribir.write(linea)
    archivo_leer.close()
    archivo_escribir.close()

#Ejercicio 6

#def listar_palabras_de_archivo(nombre_archivo:str) -> list:
        

#Pilas

#Ejercicio 8

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    pila = Pila()
    for _ in range(cantidad):
        pila.put(random.randint(desde, hasta))
    return pila
       
p = generar_nros_al_azar(5,1,10)

#Ejercicio 9

def cantidad_elementos(p:Pila) -> int:
    cantidad = 0
    pila = p
    while not pila.empty():
        pila.get()
        cantidad += 1
    return cantidad

h = Pila()

h.put(1)
h.put(2)
print(cantidad_elementos(h))