import math as mt
from typing import List

#EJERCICIO 1.3

def suma_total(lista:List[int]) -> int:
    total:int = 0
    ind_actual:int = 0
    longitud:int = len(lista)
    while ind_actual < longitud:
        total += lista[ind_actual]
        ind_actual +=1
    return total

print(suma_total ([1,2,3,4]))

#EJERCICIO 1.1

def pertenece(lista:List[int], numero:int) -> bool:
    condicion:bool = True
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if lista[i] == numero:
            return condicion
        else:
            i += 1
    return False

print(pertenece([1,2,3,4],5))

#EJERCICIO 1.2

def divide_a_todos_2(lista:List[int], e:int) -> bool:
    i:int = 0
    res:bool = False
    longitud = len(lista)
    for i in range (longitud):
        if (lista[i] % e != 0):
            return False
    return True

print(divide_a_todos_2([2,4,6,7,10], 2))


#EJERCICIO 1.7

def tiene_minuscula(contraseña:str) -> bool:
    longitud:int = len(contraseña)
    i:int = 0
    while i < longitud:
        if (contraseña[i] >= "a") and (contraseña[i] <= "z"):
            return True
        else:
            i += 1
    return False

print(tiene_minuscula("HOLA"))

def tiene_mayuscula(contraseña:str) -> bool:
    longitud:int = len(contraseña)
    i:int = 0
    while i < longitud:
        if (contraseña[i] >= "A") and (contraseña[i] <= "Z"):
            return True
        else:
            i += 1
    return False

print(tiene_mayuscula("la"))

def tiene_num(contraseña:str) -> bool:
    longitud:int = len(contraseña)
    i:int = 0
    while i < longitud:
        if (contraseña[i] >= "0") and (contraseña[i] <= "9"):
            return True
        else:
            i += 1
    return False

print(tiene_num("las"))

def fortaleza(contraseña:str) -> str:
    longitud:int = len(contraseña)
    i:int = 0
    while i < longitud:
        if (longitud > 8) and (tiene_minuscula(contraseña) == True) and (tiene_mayuscula(contraseña) == True) and (tiene_num(contraseña) == True):
            return "VERDE"
        elif longitud < 5:
            return "ROJA"
        else:
            return "AMARILLA"
        
print(fortaleza("hola"))

#EJERCICIO 2.1
def es_par(numero:int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

def borra_pares(lista:List[int]) -> List[int]:
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if es_par(lista[i]) == True:
            lista.remove(lista[i])
            lista.insert(i,0)
            i += 1
        else:
            i += 1
    return lista

print(borra_pares([1,2,3,4,5,6,7]))

#EJERCICIO 5.2

def pertenece_a_cada_uno_version_2(lista:List[List[int]], e:int) -> List[bool]:
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if pertenece(lista[i], e) == True:
            lista.remove(lista[i])
            lista.insert(i, True)
            i += 1
        else:
            lista.remove(lista[i])
            lista.insert(i, False)
            i += 1
    return lista

print(pertenece_a_cada_uno_version_2([[1,2], [3,4,5,1], [6,7,8]], 1))