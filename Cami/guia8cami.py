from queue import LifoQueue as Pila
import random

#EJERCICIO 1.1
def contar_lineas(nombre_archivo:str) -> int:
    archivo = open(nombre_archivo, 'r')
    archivo_lineas = archivo.readlines()
    archivo.close()
    return len(archivo_lineas)

#print(contar_lineas("archivo.txt"))

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
#def esta_bien_balanceada(s:str) -> bool:
    