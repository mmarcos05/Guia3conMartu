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
    
print(verificar_transacciones("ssrvvrrvvsvvsxrvvv"))
       
            
            
        