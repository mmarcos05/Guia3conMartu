from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# PRACTICA 8 - PILAS

def copiar_pila(p: Pila) -> Pila:
    pAux: Pila = Pila()
    res: Pila = Pila()

    while not p.empty():
        elemento = p.get()
        pAux.put(elemento)
    
    while not pAux.empty():
        elem = pAux.get()
        p.put(elem)
        res.put(elem)

    return res

# -- 

def generar_nros_al_azar_pilas(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    pila_azar: Pila = Pila()

    for _ in range(cantidad):
        numero: int = random.randint(desde, hasta)
        pila_azar.put(numero)
    return pila_azar

# --

def cantidad_elementos_pila(p: Pila) -> int:
    contador: int = 0
    copia: Pila = copiar_pila(p)
    
    while not copia.empty():
        copia.get()
        contador += 1
    return contador

# --

def buscar_el_maximo_pila(p: Pila[int]) -> int:
    copia: Pila[int] = copiar_pila(p)
    maximo_actual = 0

    while not copia.empty():
        elemento: int = copia.get()
        if elemento > maximo_actual:
            maximo_actual = elemento
    return maximo_actual

# --

def esta_bien_balanceada(s: str) -> bool:
    p: Pila = Pila()
    
    for char in s:
        if char == '(':
            p.put(char)
        elif char == ')':
            if p.empty(): # si no hay un '(' antes ya es false
                return False
            else: 
                p.get() # si hay, saca el que pusiste
    return p.empty() # tiene que dar True si la pila queda vacia al final

# --

def es_operando(char: chr) -> bool:
    numeros: str = "0123456789"
    if char in numeros:
        return True
    return False
    
def es_operador(char: chr) -> bool:
    operadores: str = "+-*/"
    if char in operadores:
        return True
    return False

def evaluar_expresion(s: str) -> float:
    pila: Pila = Pila()
    for char in s:
        if es_operando(char):
            pila.put(float(char))
        elif es_operador(char):
            elemento2: int = pila.get()
            elemento1: int = pila.get()

            if char == '+':
                res = elemento1 + elemento2
            if char == '-':
                res = elemento1 - elemento2
            if char == '*':
                res = elemento1 * elemento2
            if char == '/':
                res = elemento1 / elemento2
            pila.put(res)
    return float(pila.get())

# PRACTICA 8 - COLAS 

def copiar_cola(c: Cola) -> Cola:
    cAux: Cola = Cola()
    res: Cola = Cola()

    while not c.empty():
        elemento = c.get()
        cAux.put(elemento)
    
    while not cAux.empty():
        elem = cAux.get()
        c.put(elem)
        res.put(elem)
    return res

# --

def generar_nros_al_azar_colas(cantidad: int, desde: int, hasta: int) -> Cola:
    cola: Cola = Cola()
    
    for _ in range(cantidad):
        numero: int = random.randint(desde, hasta)
        cola.put(numero)
    return cola

# --

def cantidad_elementos_cola(c: Cola) -> int:
    copia: Cola = copiar_cola(c)
    contador: int = 0

    while not copia.empty():
        copia.get()
        contador += 1
    return contador

# --

def buscar_el_maximo_cola(c: Cola) -> int:
    copia: Cola = copiar_cola(c)
    maximo_actual: int = 0

    while not copia.empty():
        elem: int = copia.get()
        if elem > maximo_actual:
            maximo_actual = elem
    return maximo_actual

# --

def armar_secuencia_bingo() -> Cola[int]:
    secuencia: Cola[int] = Cola()
    numeros: list[int] = []

    while len(numeros) < 100:
        numero: int = random.randint(0,99)
        if numero not in numeros:
            secuencia.put(numero)
            numeros.append(numero)
    return secuencia

def armar_carton_bingo() -> list[int]:
    carton: list[int] = []
    numeros: list[int] = []

    while len(numeros) < 12:
        numero: int = random.randint(0,99)
        if numero not in numeros:
            carton.append(numero)
            numeros.append(numero)
    return carton

def jugar_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
    copia_bolillero: Cola[int] = copiar_cola(bolillero)
    aciertos: int = 0

    while aciertos < 12:
        bolilla: int = copia_bolillero.get()
        if bolilla in carton:
            aciertos += 1
            jugadas += 1
        else:
            jugadas += 1
    return jugadas

 