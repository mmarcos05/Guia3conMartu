# Ejercicio 1
def cantidad_de_apariciones(s: list[int], elem: int) -> int:
    res: int = 0
    for elemento in s:
        if elem == elemento:
            res += 1
    return res

def ind_nesima_aparicion(s: list[int], n: int, elem: int) -> int:
    res: int

    if cantidad_de_apariciones(s, elem) < n:
        res = -1
    else:
        contador: int = 0
        for i in range(len(s)):
            if s[i] == elem:
                contador += 1
                if contador == n:
                    res = i
    return res

# lista = [1,2,4,5,2,5,5]
# print(ind_nesima_aparicion(lista, 3, 4))

# Ejercicio 2
def mezclar(s1: list[int], s2:list[int]) -> list[int]:
    lista_mezclada: list[int] = []
    for i in range(0, len(s1)):
        elemento_s1 = s1[i]
        lista_mezclada.append(elemento_s1) #En el primer lugar, agrego el elem en la pos 0 de s1
        elemento_s2 = s2[i]
        lista_mezclada.append(elemento_s2) #Despues agrego el elem de la pos 0 de s2 (en la pos 1 de lista final)
    return lista_mezclada

# lista1 = [1,3,0,1] 
# lista2 = [4,0,2,3]
# print(mezclar(lista1,lista2))

# Ejercicio 3
def frecuencia_posiciones_por_caballo(caballos: list[str], carreras: dict[str,list[str]]) -> dict[str,list[int]]:
    diccionario_final: dict[str,list[int]] = {}

    for caballo in caballos:
        diccionario_final[caballo] = [0]*len(caballos)

    # print(diccionario_final)

    # carreras = dict['carrera': [posiciones caballos]]
    # diccionario_final = dict['caballo': [posiciones]]

    for posiciones_caballos in carreras.values():
        for posicion in range(len(posiciones_caballos)):
            caballo = posiciones_caballos[posicion]
            diccionario_final[caballo][posicion] += 1
    return diccionario_final

# caballos= ["linda", "petisa", "mister", "luck" ]
# carreras= {"carrera1":["linda", "petisa", "mister", "luck"],"carrera2":["petisa", "mister", "linda", "luck"]}
# print(frecuencia_posiciones_por_caballo(caballos, carreras))

# Ejercicio 4
def matriz_capicua(m:list[list[int]]) -> bool:
    fila: list[int]
    i: int
    for fila in m:
        for i in range(0, len(fila)):
            if fila[i] != fila[len(fila)-1-i]:
                return False
    return True

# matriz = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
# print(matriz_capicua(matriz))