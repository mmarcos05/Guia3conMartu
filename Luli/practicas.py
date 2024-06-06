import random

# PRACTICA 7

def pertenece(s: list[int], e: int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False

# ---

def suma_total(s: list[int]) -> int:
    suma: int = 0

    for i in range(len(s)):
        suma += s[i]
    return suma

# ---

def ordenados(s: list[int]) -> bool:
    for i in range(len(s)-1):
        if s[i] > s[(i+1)]:
            return False
    return True

# ---

def alguna_mayor_a_7_char(palabras: list[str]) -> bool:
    for i in range(len(palabras)):
        if len(palabras[i]) > 7:
            return True
    return False

# ---

def capicua(texto: str) -> bool:
    for i in range(len(texto)):
        if texto[i] != texto[len(texto) - i - 1]:
            return False
    return True

# ---

def fortaleza_contrasena(contrasena: str) -> str:
    if len(contrasena) < 5:
        return "ROJA"
        
    elif (len(contrasena) > 8) and tiene_minus(contrasena) and tiene_mayus(contrasena) and tiene_numero(contrasena):
        return "VERDE"
    
    else:
        return "AMARILLA"
    
def tiene_minus(palabra:str) -> bool:
    for i in range(len(palabra)):
        if palabra[i] >= 'a' and palabra[i] <= 'z':
            return True
    return False

def tiene_mayus(palabra:str) -> bool:
    for i in range(len(palabra)):
        if palabra[i] >= 'A' and palabra[i] <= 'Z':
            return True
    return False

def tiene_numero(palabra:str) -> bool:
    for i in range(len(palabra)):
        if palabra[i] >= '0' and palabra[i] <= '9':
            return True
    return False

# ---

def saldo_actual(movimientos: list[(str,int)]) -> int:
    saldo: int = 0

    for i in range(len(movimientos)):
        if movimientos[i][0] == 'I':
            saldo += movimientos[i][1]
        elif movimientos[i][0] == 'R':
            saldo -= movimientos[i][1]
    return saldo

# ---

def tres_vocales_dif(palabra: str) -> bool:
    vocales: str = "aeiou"
    contador: int = 0

    for vocal in vocales:
        if vocal in palabra:
            contador += 1
    return contador >= 3

# ---

def cero_en_pos_pares(numeros: list[int]) -> None: # numeros es inout
    for i in range(len(numeros)):
        if i % 2 == 0:
            numeros[i] = 0
    
# lista = [1,2,3,4,6,7]
# cero_en_pos_pares(lista)
# print(lista)

# ---

def borrar_vocales(palabra: str) -> str:
    vocales: str = "aeiou"
    palabra_final: str = ""

    for char in palabra:
        if char in vocales:
            palabra_final += ""
        else:
            palabra_final += char
    return palabra_final

# ---

def reemplazar_vocales(s: list[chr]) -> list[chr]:
    vocales: str = "aeiou"
    palabra_final: list[chr] = []

    for char in s:
        if char in vocales:
            palabra_final.append('-')
        else:
            palabra_final.append(char)
    return palabra_final

# ---

def dar_vuelta_str(s: list[chr]) -> list[chr]:
    nuevo_str: list[chr] = []

    for i in range(len(s)):
        nuevo_str.append(s[len(s) - 1 - i])
    return nuevo_str

# ---

def eliminar_repetidos(s: list[chr]) -> list[chr]:
    nuevo_str: list[chr] = []
    
    for char in s:
        if char not in nuevo_str:
            nuevo_str.append(char)
    return nuevo_str

# ---

def cantidad_de_nums(numeros: list[int]) -> int:
    cantidad: int = 0
    for i in range(0, len(numeros)):
        cantidad += 1
    return cantidad
    
def promedio(numeros: list[int]) -> float:
    return suma_total(numeros) / cantidad_de_nums(numeros)

def aprobado(notas: list[int]) -> int:
    res: int 
    for i in range(len(notas)):
        if notas[i] >= 4 and promedio(notas) >= 7:
            res = 1
        elif notas[i] >= 4 and 4 <= promedio(notas) < 7:
            res = 2
        else:
            res = 3
    return res

# ---

def armar_lista_estudiantes() -> list[str]:
    nombres: list[str] = []

    while True:
        print("Ingrese el nombre o ponga 'listo' para terminar: ")
        ingresado: str = input()
        if ingresado != 'listo':
            nombres.append(ingresado)
        else: 
            return nombres
        
# lista_es = armar_lista_estudiantes()
# print(f"Lista de estudiantes: {lista_es}")

def historial_tarjeta() -> list[tuple[str,float]]:
    lista_final: list[tuple[str,float]] = []

    while True:
        print("Ingrese 'C' si quiere cargar, 'D'  si quiere descontar, o 'X' si quiere finalizar: ")
        eleccion: str = input()
        if eleccion == 'C':
            print("Ingrese cuanto quiere cargar: ")
            carga: float = float(input())
            lista_final.append(('C', carga))
        elif eleccion == 'D':
            print("Ingrese cuanto quiere descontar: ")
            descarga: float = float(input())
            lista_final.append(('D', descarga))
        elif eleccion == 'X':
            print("Ok, finalizo el progrma")
            break
    return lista_final

# ---

def valores_de_cartas(carta: int) -> float:
    if carta == 10 or carta == 11 or carta == 12:
        return 0.5
    else:
        return carta
    
def juego() -> list[int]:
    historial_de_cartas: list[int] = []
    mazo: list[int] = [1,2,3,4,5,6,7,10,11,12]
    puntaje: float = 0.0

    while True:
        carta: int = random.choice(mazo)
        historial_de_cartas.append(carta)
        puntaje += valores_de_cartas(carta)
        print(f"Te salio un {carta}. Puntaje actual: {puntaje}")

        if puntaje > 7.5:
            print("Te pasaste de 7.5, perdiste!")
            break
        else:
            print("Queres sacar otra carta? Escribi SI o NO: ")
            decision = input()
            if decision == 'NO':
                print("Ganaste")
                break

    return historial_de_cartas

# ---

def pertenece_a_cada_uno(s: list[list[int]], e: int, res:list[bool]) -> None:
    for lista in s:
        if e in lista:
            res.append(True)
        else: res.append(False)

# res: list[bool] = []
# listas = [[1,2,3,5],[3,4,5],[5,6,7]]
# pertenece_a_cada_uno(listas, 5, res)
# print(res)

def es_matriz(matriz: list[list[int]]) -> bool:
    fila: list[int]

    if len(matriz[0]) == 0:
        return False
    
    for fila in matriz:
        if len(fila) != len(matriz[0]):
            return False
    return True
        
# ---

def filas_ordenadas(matriz: list[list[int]], res: list[bool]) -> None:
    fila: list[int]
    for fila in matriz:
        if ordenados(fila):
            res.append(True)
        else:
            res.append(False)

# res = []
# matriz = [[1,4,3],[4,5,3],[19,8,9]]
# filas_ordenadas(matriz, res)
# print(res)