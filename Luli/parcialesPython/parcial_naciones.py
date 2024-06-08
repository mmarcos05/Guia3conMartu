def acomodar(s: list[str]) -> list[str]:
    lista_up: list[str] = []
    lista_lla: list[str] = []
    lista_final: list[str] = []

    for palabra in s:
        if palabra == "UP":
            lista_up.append("UP")
        if palabra == "LLA":
            lista_lla.append("LLA")

    lista_final = lista_up + lista_lla
    return lista_final

# s = ["LLA", "UP", "LLA", "LLA", "UP"]
# print(acomodar(s))

# --

def pos_umbral(s: list[int], u: int) -> int:
    suma_positivos: int = 0
    pos: int = 0

    for numero in s:
        if numero > 0:
            suma_positivos += numero
            if suma_positivos > u:
                return pos
        pos += 1
    return -1


# s = [1,5,6,5,-7,3]
# u = 222
# print(pos_umbral(s,u))

# --

def columnas_repetidas(mat: list[list[int]]) -> bool:
    res: bool = True

    cant_col: int = len(mat[0]) # cant en primera fila = cantidad de columnas
    mitad_long: int = cant_col // 2

    for fila in mat: 
        for i in range(mitad_long):
            if fila[i] != fila[mitad_long + i]:
                res = False 

    return res

# --

def cuenta_posiciones_por_nacion(naciones: list[str], torneos: dict[int, list[str]]) -> dict[str, list[int]]:
    diccionario_final: dict[int, list[int]] = {}
    
    for nacion in naciones:
        diccionario_final[nacion] = [0]*len(naciones)

    # torneos = ["año",[orden_naciones]]

    for orden_naciones in torneos.values():
        for orden in range(len(orden_naciones)):
            nacion = orden_naciones[orden]
            diccionario_final[nacion][orden] += 1
    return diccionario_final

# naciones= ["arg", "aus", "nz", "sud"]
# torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
# print(cuenta_posiciones_por_nacion(naciones,torneos))