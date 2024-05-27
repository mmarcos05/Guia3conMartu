import math

# Ejercicio 1.1
def pertenece(s:list[int], e:int) -> bool:
    condicion: bool = True
    indice: int = 0
    while indice < len(s): 
        if s[indice] == e:
            return condicion
        else:
            indice += 1
    return False 

# Ejercicio 1.2
def divide_a_todos (s: list[int], divisor: int) -> bool:
    for i in range(len(s)):
        if (not(s[i] % divisor == 0)):
            return False
    return True

# Ejercicio 1.3
def suma_total(lista:list[int]) -> int:
    total: int = 0
    indice: int = 0
    longitud: int = len(lista)
    while indice < longitud:
        total += lista[indice]
        indice += 1
    return total

# Ejercicio 1.4
def ordenados(numeros:list[int]) -> bool:
    for i in range (len(numeros)-1):
        if numeros[i] > numeros[i+1]:
            return False
    return True

# Ejercicio 1.5
def palabras_largas(palabras:list[str]) -> bool:
    for i in range (len(palabras)):
        if len(palabras[i]) > 7:
            return True
    return False

# Ejercicio 1.6
def esPalindromo (texto: str) -> bool:
    longitud: int = len(texto)
    for i in range(longitud):
        if texto[i] != texto[longitud - i - 1]:
            return False
    return True

# Ejercicio 1.7
def fortaleza(contraseña:str) -> str:
   indice: int = 0
   while indice < len(contraseña):
       if (len(contraseña) > 8) and (tiene_minus(contraseña) == True) and (tiene_mayus(contraseña) == True) and (tiene_num(contraseña) == True):
           return "VERDE"
       elif (len(contraseña) < 5):
           return "ROJA"
       else:
           return "AMARILLA"
       
def tiene_minus(contraseña:str) -> bool:
    indice: int = 0
    condicion: bool = True
    while indice < len (contraseña):
        if (contraseña[indice] >= "a") and (contraseña[indice] <= "z"):
            return condicion
        else:
            indice += 1
    return False

def tiene_mayus(contraseña:str) -> bool:
    indice: int = 0
    condicion: bool = True
    while indice < len (contraseña):
        if (contraseña[indice] >= "A") and (contraseña[indice] <= "Z"):
            return condicion
        else:
            indice += 1
    return False

def tiene_num(contraseña:str) -> bool:
    indice: int = 0
    condicion: bool = True
    while indice < len (contraseña):
        if (contraseña[indice] >= "0") and (contraseña[indice] <= "9"):
            return condicion
        else:
            indice += 1
    return False

# Ejercicio 1.8
def saldo_actual(movimientos:list[(str,int)]) -> int:
    saldo: int = 0
    longitud: int = len(movimientos)
    for i in range (0,longitud):
        if (movimientos[i][0] == 'I'):
            saldo += movimientos[i][1]
        elif (movimientos[i][0] == 'R'):
            saldo -= movimientos[i][1]
    return saldo

# otra manera de hacerlo
def saldoActual(operaciones:list[(str,float)]) -> float:
    saldo2: float = 0
    for tipo, monto in operaciones:
        if (tipo == 'I'):
            saldo2 += monto
        elif (tipo == 'R'):
            saldo2 -= monto
    return saldo2

# Ejercicio 1.9
def perteneceVocal(vocal: str, palabra: str) -> bool:
    return (vocal in palabra) or (vocal.upper() in palabra)

def tres_vocales_distintas(palabra:str) -> bool:
    contador:int = 0
    vocales = ['a','e','i','o','u']
    for vocal in vocales:
        if (perteneceVocal(vocal, palabra) or perteneceVocal(vocal.upper(), palabra)):
            contador += 1
    return contador >= 3

# Ejercicio 2.1
def es_par(numero:int) -> bool:
    if numero % 2 == 0:
        return True
    else: 
        return False

def borra_pares(lista:list[int]) -> list[int]:
    indice: int = 0
    while indice < len (lista):
        if (es_par (lista[indice]) == True): 
            lista.remove(lista[indice])
            lista.insert(indice, 0)
            indice += 1
        else: 
            indice += 1
    return lista

# Ejercicio 2.2
def borra_pares_sin_modificar(lista:list[int]) -> list[int]:
    nueva_lista: list[int] = []
    for elemento in lista:
        if es_par(elemento):
            nueva_lista.append(0)
        else:
            nueva_lista.append(elemento)
    return nueva_lista

# Ejercicio 2.3
def borra_vocales(palabra:list[chr]) -> list[chr]:
    nuevo_texto: str = ""
    vocales = ['a','e','i','o','u']
    for i in range (len(palabra)):
        if not pertenece (vocales, palabra[i]):
            nuevo_texto += palabra[i]
    return nuevo_texto

# Ejercicio 2.4
def reemplaza_vocales(palabra:list[chr]) -> list[chr]:
    nuevo_texto: list[chr] = []
    vocales = ['a','e','i','o','u']
    for char in palabra:
        if pertenece (vocales, char):
            nuevo_texto.append('_')
        else: 
            nuevo_texto.append(char)
    return nuevo_texto

# Ejercicio 2.5
def da_vuelta_str(palabra:list[chr]) -> list[chr]:
    nuevo_texto: list[chr] = []
    for i in range (0,len(palabra)):
        nuevo_texto.append(palabra[len(palabra)-i-1])
    return nuevo_texto

# Ejercicio 2.6
def eliminar_repetidos(palabra:list[chr]) -> list[chr]:
    nuevo_texto: list[chr] = []
    for i in range (0, len(palabra)):
        if palabra[i] not in nuevo_texto:
            nuevo_texto.append(palabra[i])
    return nuevo_texto

# Ejercicio 5.2
def pertenece_a_cada_uno(s:list[list[int]], e:int) -> list[bool]:
    indice: int = 0
    while indice < len(s):
        if (pertenece (s[indice],e)):
            s.remove(s[indice])
            s.insert(indice,True)
            indice += 1
        else: 
           s.remove(s[indice])
           s.insert(indice,False) 
           indice += 1
    return s
