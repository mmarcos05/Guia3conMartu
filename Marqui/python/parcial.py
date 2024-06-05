from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
import typing
import csv

def verificar_transacciones(s:str) -> int:
    transacciones = s
    saldo = 0
    for transaccion in transacciones:
            if transaccion == 'x':
                return saldo
            if transaccion == 'r':
                saldo += 350
            if transaccion == 'v':
                saldo -= 56
                if saldo < 0:
                    saldo += 56
                    return saldo
    return saldo
    
def ap_antes_corte(c:str, s:str) -> int:
    apariciones = 0
    for char in s:
        if char == 'x':
            return apariciones
        if char == c:
            apariciones += 1
    return apariciones
    
#print(verificar_transacciones("ssrvvrrvvsvvsxrvvv"))

def valor_minimo(s:list[tuple[float,float]]) -> float:
    lista_temp = s
    dia1 = lista_temp[0]
    menor_actual = dia1[0]
    for dia in lista_temp:
        if dia[0] < menor_actual:
            menor_actual = dia[0]
    return menor_actual

#print(valor_minimo([(1.0,5.2),(10.4,15.1),(20.7,28.9),(-3.1,1.3),(1.2,3.7)]))

def valores_extremos(cotizaciones_diarias:dict[str,list[tuple[int,float]]]) -> dict[str,tuple[float,float]]:
    copia = cotizaciones_diarias
    res = {}
    for nombre, lista in copia.items():
        minimo = buscar_minimo(cotizaciones_diarias[nombre])
        maximo = buscar_maximo(cotizaciones_diarias[nombre])
        res[nombre] = (minimo,maximo)
    return res
        
def buscar_minimo(lista:list[tuple[int,float]]) -> float:
    primero = lista[0]
    minimo_actual = primero[1]
    for tupla in lista:
        if tupla[1] < minimo_actual:
            minimo_actual = tupla[1]
    return minimo_actual

def buscar_maximo(lista:list[tuple[int,float]]) -> float:
    primero = lista[0]
    maximo_actual = primero[1]
    for tupla in lista:
        if tupla[1] > maximo_actual:
            maximo_actual = tupla[1]
    return maximo_actual
        
#print(valores_extremos({"YPF":[(1,10),(15,3),(31,100)],"ALUA":[(1,0),(20,50),(31,30)]}))            
        
def es_sudoku_valido(m:list[list[int]]) -> bool:
    sudoku = m
    sudoku_invertido = invertir_matriz(m)
    for fila in sudoku:
        if hay_repetidos_sin0(fila):
            return False
    for fila in sudoku_invertido:
        if hay_repetidos_sin0(fila):
            return False
    return True
  
def hay_repetidos_sin0(lista:list[int]) -> bool:
    i = 0
    contador = 0
    while i < len(lista):
        for elem in lista:
            if elem != 0:
                if elem == lista[i]:
                    contador += 1
                if contador > 1:
                    return True
        contador = 0
        i +=1
    return False      
            
#print(hay_repetidos_sin0([1,2,3,4,5,6,7,8,9]))           
        
def invertir_matriz(m:list[list[int]]) -> list[list[int]]:
    i = 0
    nueva_matriz = []
    nueva_fila = []
    while i < len(m):
        for fila in m:
            nueva_fila.append(fila[i])
        nueva_matriz.append(nueva_fila)
        nueva_fila = []
        i += 1
    return nueva_matriz   
        
m = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(es_sudoku_valido(m))