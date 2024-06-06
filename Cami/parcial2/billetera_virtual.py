import typing
from typing import List, Tuple

#EJERCICIO 1
def verificar_transacciones(s:str) -> int:
    saldo:int = 0
    for caracter in s:
        if caracter != "x":
            if caracter == "r":
                saldo += 350
            elif caracter == "v":
                saldo -= 56
                if 0 > saldo:
                    saldo += 56
                    return saldo
            else:
                saldo = saldo
        else:
            return saldo

s = "ssrvvvvsvvsvvv"
#print(verificar_transacciones(s))
#se debería devolver res = 14

def valor_minimo(temperaturas:List[tuple]) -> float:
    longitud:int = len(temperaturas)
    i:int = 0
    while (longitud - 1) > i:
        if (temperaturas[i])[0] > (temperaturas[i + 1])[0]:
            minimo:float = (temperaturas[i + 1])[0]
            i += 1
        else:
            minimo:float = (temperaturas[i])[0]
            i += 1
    return minimo

s = [(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)]
#se debería devolver res = -3.1
#print(valor_minimo(s))

#EJERCICIO 3
def valores_extremos(valores_diarios:dict) -> dict:   #dict⟨String,seq⟨(Z x R)⟩⟩): dict⟨String,(R x R)⟩
    max_min:dict = dict()
    items_valores_diarios:List[tuple] = list(valores_diarios.items())
    for cotizaciones in items_valores_diarios:
        acciones:List[tuple] = cotizaciones[1]
        maximo = acciones[0]
        for candidato in acciones:
            if candidato[1] > maximo[1]:
                maximo = candidato
        minimo = acciones[0]
        for candidato in acciones:
            if minimo[1] > candidato[1]:
                minimo = candidato
        max_min[cotizaciones[0]] = (minimo[1], maximo[1])
    return max_min
        
cotizaciones_diarias = {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
#resultado_esperado es: {"YPF" : (3,100), "ALUA" : (0,50)}
print(valores_extremos(cotizaciones_diarias))
