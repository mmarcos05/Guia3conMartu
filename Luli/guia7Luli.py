import math
import random
import numpy as np

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
def borra_pares2(lista:list[int]) -> None:
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if (es_par(i)):
            lista[i] = 0
        i += 1

# s = [2,4,5,6,3,3]
# print (f"antes: {s}")
# borra_pares2(s)
# print(f"borra_pares2: {s}")

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

# Ejercicio 3
def aprobado(notas:list[int]) -> int:
    if (mayores_o_iguales(notas) and promedio(notas) >= 7):
        return 1
    elif (mayores_o_iguales(notas) and (promedio(notas) >= 4 and promedio(notas) < 7)):
        return 2
    else:
        return 3

def mayores_o_iguales (notas: list[int]) -> bool:
    for nota in notas:
        if nota < 4:
            return False
    return True

def promedio (notas:list[int]) -> float:
    suma_notas: int = 0
    for nota in notas:
        suma_notas += nota
    promedio: float = suma_notas / len(notas)
    return promedio

# Ejercicio 4.1
def registrar_nombres() -> list[str]:
    nombres: list[str] = []
    while True:
        print("Ingrese el nombre o ponga 'Listo' para terminar: ")
        ingresado = input()
        if ingresado != "listo":
            nombres.append(ingresado)
        else:
            return nombres
# Así se usa la funcion
# lista_estudiantes = registrar_nombres()
# print("Lista de estudiantes: ", lista_estudiantes)

# Ejercicio 4.2
def historial_sube() -> list[(str,float)]:
    historial: list[(str,float)] = []
    saldo = 0.0
    while True:
        operacion = input("Seleccione: C para cargar credito, D para descontar credito, X para salir")
        if operacion == 'C':
            monto = float(input("Monto a cargar: "))
            historial.append(('C', monto))
            saldo += monto
            print(f"Se ha cargado {monto}. Su saldo ahora es {saldo}")
        elif operacion == 'D':
            monto = float(input("Monto a descontar: "))
            historial.append(('D', monto))
            saldo -= monto
            print(f"Se ha descontado {monto}. Su saldo ahora es {saldo}")
        elif operacion == 'X':
            print("Ha finalizado")
            break 
    return historial

# Ejercicio 4.3
def valor_carta(carta: int) -> float:
    if carta in [10,11,12]:
        return 0.5
    else:
        return float(carta)

def juego() -> list[int]:
    historial_de_cartas: list[int] = []
    mazo: list[int] = [1,2,3,4,5,6,7,10,11,12]
    puntaje = 0.0
    while True:
        carta = random.choice(mazo)
        historial_de_cartas.append(carta)
        puntaje += valor_carta(carta)
        print(f"Obtuviste una {carta}. Puntaje actual: {puntaje}")

        if puntaje > 7.5:
            print("Te pasaste de 7.5, perdiste!")
            break

        decision = input("Queres sacar otra carta? Si o no: ").lower()
        if decision == 'no':
            print("Ganaste campeón!")
            break

        return historial_de_cartas

# historial = juego
# print("Terminamos. Historial de tus cartas: ", historial)

# Ejercicio 5.1
def pertenece_a_cada_uno_v1(s:list[list[int]], e:int, res:list[bool]) -> None:
    res.clear()
    for sublista in s:
        if pertenece(sublista,e):
            res.append(True)
        else:
            res.append(False)

# resultado: list[bool] = []
# pertenece_a_cada_uno_v1([[1,2,3],[3,4,1],[5,8,3],[2,5,9]], 2, resultado)
# print(f"lista de bool: {resultado}")

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

# Ejercicio 5.3
def es_matriz(s: list[list[int]]) -> bool:
    # Veo si la lista principal está vacía
    if len(s) == 0:
        return False
    # Veo si la primera sublista está vacía
    if len(s[0]) == 0:
        return False
    # Veo que todas las sublistas tengan la misma longitud
    longitud_s1 = len(s[0])
    for sublista in s:
        if len(sublista) != longitud_s1:
            return False
    return True

# s = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
# ]
# print(es_matriz(s)) Deberia devolver True

# s2 = [
#    [1,2,3],
#    [1,5]
# ]
# print(es_matriz(s2)) Deberia devolver False

# Ejercicio 5.4
def filas_ordenadas(matriz: list[list[int]], res: list[bool]) -> None:
    res.clear()
    for fila in matriz:
        if not ordenados(fila):
            res.append(False)
        else:
            res.append(True)
# m = [
#     [1,2,3],
#     [4,5,6],
#     [7,6,9]
# ]
# res:list[bool] = []
# filas_ordenadas(m,res)
# print(res)

# Ejercicio 5.5
def elevar_matriz_azar(d: int, p: int) -> list[list[int]]:
    # Creo la matriz de dimension d
    m = np.random.random((d,d))**2

    # Voy a hacer un print para que me muestre la matriz que creó
    print(f"Se creo la siguiente matriz: \n {m}")

    # Uso una funcion de numpy para que me eleve la matriz a p
    resultado = np.linalg.matrix_power(m, p)

    # Hago un print que me muestre la matriz final
    print(f"El resultado de la matriz elevada a {p}: \n {resultado}")

# elevar_matriz_azar(4,2)