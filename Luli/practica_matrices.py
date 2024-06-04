def es_matriz(m:list[list[int]]) -> bool:
    if len(m) == 0 or len(m[0]) == 0:
        return False

    for fila in m:
        if len(fila) != len(m[0]):
            return False
    return True
    
def sumar_matriz(m:list[list[int]]) -> int:
    res: int = 0
    for fila in m:
        for elemento in fila:
            res += elemento
    return res

def sumar_cada_fila(m:list[list[int]]) -> list[int]:
    lista_sumas: list[int] = []

    for fila in m:
        contador: int = 0
        for elemento in fila:
            contador += elemento
        lista_sumas.append(contador)
    return lista_sumas

def sumar_cada_columna(m:list[list[int]]) -> list[int]:
    resultado: list[int] = []
    fila0: list[int] = m[0]

    for columna in range (len(fila0)):
        contador_col:int = 0
        for fila in range (len(m)):
            contador_col += m[fila][columna]
        resultado.append(contador_col)
    return resultado

def columna_matriz(m: list[list[int]], num_col: int) -> list[int]:
    columna: list[int] = []
    for fila in m:
        columna.append(fila[num_col]) # de cada fila agarro el elemento que esta en la posicion igual que el numero de columna
    return columna

def minimo_columna(col: list[int]) -> int:
    minimo_actual: int = col[0]
    for i in range(1,len(col)):
        if col[i] < minimo_actual:
            minimo_actual = col[i]
    return minimo_actual

def maximo_columna(col: list[int]) -> int:
    maximo_actual: int = 0
    for i in range (len(col)):
        if col[i] > maximo_actual:
            maximo_actual = col[i]
    return maximo_actual

# hago esta funcion para que me ponga los valores en una tupla directamente
def min_max(col: list[int]) -> tuple[int,int]:
    min = minimo_columna(col)
    max = maximo_columna(col)
    return min, max

# columna = [12,10,8,2]
# print(minimo_columna(columna))

def min_max_de_cada_columna_matriz (m:list[list[int]]) -> list[(int, int)]:
    res: list[(int, int)] = []
    for num_col in range(len(m[0])):
        col: list[int] = columna_matriz(m,num_col)
        res.append(min_max(col))
    return res

# matriz = [[1,2,3],[4,5,6],[7,8,9],[9,8,1]]
# print(min_max_de_cada_columna_matriz(matriz))