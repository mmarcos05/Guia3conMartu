from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

#Ejercicio 13

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    c = Cola()
    for _ in range(cantidad):
        n = random.randint(desde, hasta)
        c.put(n)
    return c

print(generar_nros_al_azar(3,1,5).queue)

#Ejercicio 16
def pertenece(lista,numero):
    i = 0
    while i < len(lista):
        if lista[i] == numero:
            return True
        else:
            i += 1

def copiar_cola(c:Cola) -> Cola:
    cola1 = Cola()
    cola2 = Cola()

    while not c.empty():
        cola1.put(c.get())
    while not cola1.empty():
        cola2.put(cola1.get())
    return cola2

def armar_secuencia_de_bingo() -> Cola[int]:
    c = Cola()
    lista_numeros = []
    while len(lista_numeros) < 100:
        i = random.randint(0,99)
        if not pertenece(lista_numeros, i):
            lista_numeros.append(i)
            c.put(i)
    return c

def jugar_carton_de_bingo(carton:list[int],bolillero: Cola[int]):
    boli = copiar_cola(bolillero)
    i = 0
    aciertos = 0
    while aciertos < len(carton):
        if pertenece(carton,boli.get()):
            aciertos += 1
            i += 1 
        else:
            i += 1
    return i 

def armar_secuencia_de_carton() -> list:
    c = []
    lista_numeros = []
    while len(c) < 12:
        i = random.randint(0,99)
        if not pertenece(lista_numeros, i):
            lista_numeros.append(i)
            c.append(i)
    return c

carton = armar_secuencia_de_carton()
bolillero = armar_secuencia_de_bingo()
#print(f"el carton es {carton}, el bolillero es {bolillero.queue} y el numero de bolas para sacar es {jugar_carton_de_bingo(carton,bolillero)}")


#Ejercicio 19

#funciones utiles para separar en palabras
def palabras_de_archivo(nombre_de_archivo):
    with open(nombre_de_archivo, 'r') as archivo:
        contenido = archivo.read()

        return mi_split(contenido)

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
    
def pertenece_dicts(d:dict, k) -> bool:
    lista = list(d.keys())
    for e in lista:
        if e == k:
            return True
    return False

def agrupar_por_letras(nombre_de_archivo:str) -> dict:
    archivo = open(nombre_de_archivo, "r")
    contenido : list[str] = archivo.read()
    palabras = mi_split(contenido)
    print(palabras)
    res: dict = {}

    for p in palabras:
        t = len(p)
        if pertenece_dicts(res, t):
            res[t] += 1
        else:
            res[t] = 1
    return res


#print(agrupar_por_letras("pepe.txt"))







