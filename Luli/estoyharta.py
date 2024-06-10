def ap_antes_corte(c: chr, s: str) -> int:
    contador: int = 0
    saldo: int = 0

    for char in s:
        if char == 'r':
            saldo += 350
        if char == 'v':
            saldo -= 56
        if char == 'x':
            return contador
        
        if char == c:
            if saldo >= 0:
                contador += 1

    return contador

def verificar_transacciones(s:str) -> int:
    res: int = (350 * ap_antes_corte('r', s)) - (56 * ap_antes_corte('v', s))
    return res

# --

def valor_minimo(s: list[tuple[float, float]]) -> float:
    minimo_actual: float = s[0][0]

    for tupla in s:
        minimo_tupla: float = tupla[0]
        if minimo_tupla < minimo_actual:
            minimo_actual = minimo_tupla
    return minimo_actual

# --

def min_max(lista: list[tuple[int,float]]) -> tuple[float,float]:
    minimo_actual: float = lista[0][1]
    for tupla in lista:
        minimo_tupla: float = tupla[1]
        if minimo_tupla < minimo_actual:
            minimo_actual = minimo_tupla
        
    
    maximo_actual: float = lista[0][1]
    for tupla in lista: 
        maximo_tupla: float = tupla[1]
        if maximo_tupla > maximo_actual:
            maximo_actual = maximo_tupla

    return (minimo_actual,maximo_actual)

def valores_extremos(cotizaciones_diarias: dict[str, list[tuple[int,float]]]) -> dict[str, tuple[float,float]]:
    # cot_diarias = {nombre_empresa: [dia, valor]}
    dic_final: dict[str, tuple[float,float]] = {}

    for nombre, tuplas in cotizaciones_diarias.items():
        dic_final[nombre] = min_max(tuplas)
    return dic_final

# -- 

def hay_repetidos(lista: list[int]) -> bool:
    i: int = 0
    contador: int = 0
    
    for i in range(len(lista)):
        for elemento in lista:
            if elemento != 0:
                if elemento == lista[i]:
                    contador += 1
                if contador > 1:
                    return True
        contador = 0
    return False 

def columna_matriz(m: list[list[int]], num_col: int) -> list[int]:
    columna: list[int] = []
    for fila in m:
        columna.append(fila[num_col])
    return columna 

def es_sudoku_valido(m: list[list[int]]) -> bool:
    fila: list[int]

    for fila in m:
        if hay_repetidos(fila):
            return False
    for i in range(len(m)):
        columna:list[int] = columna_matriz(m,i)
        if hay_repetidos(columna):
            return False
    return True

# -- 
def copiar_lista(lista: list[int]) -> list[int]:
    copia: list[int] = []
    for i in range(len(lista)):
        copia.append(lista[i])
    return copia

def rotar_lista(lista: list[int], n: int) -> list[int]:
    rotada: list[int] = []
    n = n % len(lista)

    if n == 0:
        rotada = lista

    for i in range(len(lista) - n, len(lista)):
        rotada.append(lista[i])
    
    for i in range(len(lista) - n):
        rotada.append(lista[i])

    return rotada

# --

def intercalar_listas(lista1: list[int], lista2: list[int]) -> list[int]:
    intercalada: list[int] = []
    copia1 = copiar_lista(lista1)
    copia2 = copiar_lista(lista2)
    
    while (len(copia1) != 0) or (len(copia2) != 0):
        if len(copia1) != 0:
            intercalada.append(copia1[0])
            copia1.pop(0)
        if len (copia2) != 0:
            intercalada.append(copia2[0])
            copia2.pop(0)

    return intercalada

# --

def eliminar_repetidos(lista: list[int]) -> list[int]:
    sin_repe: list[int] = []
    vistos: list[int] = []

    for numero in lista:
        if numero not in vistos:
            vistos.append(numero)
            sin_repe.append(numero)
    return sin_repe

