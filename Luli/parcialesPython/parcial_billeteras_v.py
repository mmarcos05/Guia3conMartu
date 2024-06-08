def ap_antes_corte(c: chr, s: str) -> int:
    contador: int = 0
    saldo: int = 0

    for char in s:
        if char == 'r':
            saldo += 350
        if char == 'v':
            saldo -= 56
        if char == 'x':
            return contador # como en x se deberia cortar, no va a haber aparecido ninguna antes
        
        if char == c:
            if saldo >= 0: # me aseguro que el saldo no sea negativo
                contador += 1
    
    return contador

def verificar_transacciones(s: str) -> int:
    res: int = (350 * ap_antes_corte('r',s)) - (56 * ap_antes_corte('v',s))
    return res

# --

def valor_minimo(s: list[float,float]) -> float:
    minimo_actual: float = s[0][0]

    for temperaturas in s:
        if temperaturas[0] < minimo_actual:
            minimo_actual = temperaturas[0]
    return minimo_actual

# --
def buscar_minimo(s: list[(int,float)]) -> float:
    minimo_actual = s[0][1]
    for tupla in s:
        if tupla[1] < minimo_actual:
            minimo_actual = tupla[1]
    return minimo_actual

def buscar_maximo(s: list[(int,float)]) -> float:
    maximo_actual = s[0][1]
    for tupla in s:
        if tupla[1] > maximo_actual:
            maximo_actual = tupla[1]
    return maximo_actual

def valores_extremos(cotizaciones_diarias: dict[str,list[(int,float)]]) -> dict[str,(float,float)]:
    # cotizaciones diarias {"nombre": [(dia, valor de accion)]}
    diccionario_final: dict[str,(float,float)] = {}

    for nombre, lista in cotizaciones_diarias.items():
        minimo = buscar_minimo(lista) 
        maximo = buscar_maximo(lista)
        diccionario_final[nombre] = minimo, maximo 
    return diccionario_final

# cotizaciones_diarias = {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
# print(valores_extremos(cotizaciones_diarias))

# --

# def es_sudoku_valido(m: list[list[int]]) -> bool:

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
    res: bool

    for fila in m:
        if (hay_repetidos(fila)):
            return False
    for i in range(len(m)):
        columna: list[int] = columna_matriz(m,i)
        for columna in m:
            if hay_repetidos(columna):
                return False

    return True