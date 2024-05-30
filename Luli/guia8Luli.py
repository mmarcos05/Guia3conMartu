from queue import LifoQueue as Pila
import random

# Ejercicio 1.1
def contar_lineas(archivo:str) -> int:
    archivo = open(archivo)
    lineas = archivo.readlines()
    archivo.close()
    return len(lineas)

# print(contar_lineas ("cancion.txt"))

# Ejercicios PILAS clase
def contar_elementos_pila(p:Pila) -> int:
    cantidad:int = 0
    pAux = copiar_pila(p)

    while (not pAux.empty()):
        elem = pAux.get()
        cantidad += 1
    return cantidad

def copiar_pila(p:Pila) -> Pila:
    pAux = Pila()
    res = Pila()
    while (not p.empty()):
        elem = p.get()
        pAux.put(elem)
    # Le saco los elementos a p y los pongo en otra nueva (me quedan al reves)

    while (not pAux.empty()):
        elem = pAux.get()
        p.put(elem)
        res.put(elem)
    # Armo la pila res para que me quede en el mismo orden de p (pAux se invierte)

    return res

# mi_pila: Pila = Pila()
# mi_pila.put(5)
# mi_pila.put(8)
# print(contar_elementos_pila(mi_pila)) 

# Ejercicio 8
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    p = Pila()
    for i in range (cantidad):
        p.put(random.randint(desde,hasta))
    return p

# p = generar_nros_al_azar(4,8,50)
# print(p.queue)
# print(f"pila al azar: {list(generar_nros_al_azar(4,8,50).queue)}")

# Ejercicio 10
def buscar_el_maximo(p:Pila[int]) -> int:
    pAux = Pila()
    pAux = copiar_pila(p)
    maximo_actual: int = pAux.get() # agarro el primer elemento de la pila (como no lo comparo con nada, asumo que es el maximo)

    while (not pAux.empty()):
        comparador:int = pAux.get() # agarro el segundo elemento (que va a ser el primero porque ya saque uno con maximo_actual)
        if comparador > maximo_actual:
            maximo_actual = comparador
    return maximo_actual

# pila: Pila = Pila()
# pila.put(2)
# pila.put(4)
# pila.put(20)
# pila.put(1)
# pila.put(6)
# print(buscar_el_maximo(pila))