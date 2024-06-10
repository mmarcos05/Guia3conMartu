from queue import Queue as Cola

def copiar_cola(c: Cola) -> Cola: # sirve para COLAS tambien
    cAux: Cola = Cola()
    res: Cola = Cola()

    while not c.empty():
        elemento = c.get()
        cAux.put(elemento)
    while not cAux.empty():
        elem = cAux.get()
        c.put(elem)
        res.put(elem)
    return res

def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str,str]]) -> Cola[str]:
    copia: Cola[tuple[str,str]] = copiar_cola(filaClientes)
    cola_vips: Cola[str] = Cola()
    cola_comunes: Cola[str] = Cola()
    cola_final: Cola[str] = Cola()

    while not copia.empty():
        tupla = copia.get()
        cliente: str = tupla[0]
        tipo: str = tupla[1]
        if tipo == "vip":
            cola_vips.put(cliente)
        if tipo == "comun":
            cola_comunes.put(cliente)

    while not cola_vips.empty():
        cola_final.put(cola_vips.get())

    while not cola_comunes.empty():
        cola_final.put(cola_comunes.get())

    return cola_final

filaC = Cola()
filaC.put(("Martin", "vip"))
filaC.put(("Julio", "comun"))
filaC.put(("Martina", "comun"))
filaC.put(("Pedro", "comun"))
filaC.put(("Maria", "vip"))

# final = reordenar_cola_priorizando_vips(filaC)
# print(final.queue)

# --

# chocan entre si: -5 c/u
# ambos se desvian: -10 c/u
# uno solo se desvia: el que se desvia -15 y ganador +10

def torneo_de_gallinas(estrategias:dict[str,str]) -> dict[str,int]:
    dicc_final: dict[str,int] = {}
    puntos_jug: int = 0

    for jugador, estrategia in estrategias.items():
        for rival, estrategia_rival in estrategias.items():
            if jugador != rival:
                if (estrategia == "me desvio siempre") and (estrategia_rival == "me desvio simepre"):
                    puntos_jug -= 10
                elif (estrategia == "me la banco y no me desvio") and (estrategia_rival == "me la banco y no me desvio"):
                    puntos_jug -= 5
                elif (estrategia == "me desvio siempre") and (estrategia_rival == "me la banco y no me desvio"):
                    puntos_jug -= 15
                elif (estrategia == "me la banco y no me desvio") and (estrategia_rival == "me desvio simepre"):
                    puntos_jug += 10
        dicc_final[jugador] = puntos_jug
        puntos_jug = 0
    return dicc_final

# --

def columnas(matriz:list[list[int]]) -> list[list[int]]: #[[1,2,3], [4,5,6], [7,8,9]]
    i:int = 0                                            #[[1,4,7], [2,5,8], [3,6,9]]
    longitud_fila:int = len(matriz[0])
    columnas:list[list[int]] = []
    lista:list[int] = []
    while longitud_fila > i:
        for fila in matriz:
            lista.append(fila[i])
        columnas.append(lista)
        lista = []
        i += 1
    return columnas

def quien_gano_el_tateti_facilito(tablero: list[list[chr]]) -> int:
    hay_tres_x: bool = False
    hay_tres_o: bool = False
    columnas_tateti: list[list[chr]] = columnas(tablero)
    i: int = 0

    for columna in columnas_tateti:
        while(len(columnas_tateti[0]) - 2) > i:
            if columna[i] == 'X' and columna[i + 1] == 'X' and columna[i + 2] == 'X':
                hay_tres_x = True
            if columna[i] == 'O' and columna[i + 1] == 'O' and columna[i + 2] == 'O':
                hay_tres_o = True
            i += 1
        i = 0
    
    if hay_tres_x and not hay_tres_o:
        return 1
    elif hay_tres_o and not hay_tres_x:
        return 2
    elif hay_tres_x and hay_tres_o:
        return 3
    else: 
        return 0

# tab = [["","X","X","X","O"],
#        ["O","O","","X","O"],
#        ["O","O","X","X",""],
#        ["X","","O","O","X"],
#        ["X","O","O","X",""]]
# print(quien_gano_el_tateti_facilito(tab))

# --

def capicua_str(texto: str) -> bool: # es lo mismo para lista de int
    for i in range(len(texto)):
        if texto[i] != texto[len(texto) - i - 1]:
            return False
    return True

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    contador: int = 0
    palabra: str = ""

    for i in range(len(texto) - 1, -1, -1):
        palabra += texto[i]
        print(palabra)
        if capicua_str(palabra):
            contador += 1
    return contador

# OTRA OPCION COMO YO LO HABIA PENSADO
def convertir_a_lista(texto:str) -> list[str]:
    lista: list[str] = []
    for char in texto:
        lista.append(char)
    return lista

def convertir_a_texto(lista: list[str]) -> str:
    palabra: str = ""
    for i in range(len(lista)):
        palabra += lista[i]
    return palabra

def cuantos_sufijos_son_pal(texto:str) -> int:
    contador: int = 0
    texto_lista = convertir_a_lista(texto)
    
    while len(texto_lista) > 0:
        nuevo_texto: str = convertir_a_texto(texto_lista)
        print(nuevo_texto)
        if capicua_str(nuevo_texto):
            contador += 1
        texto_lista.pop(0)
    return contador    

print(cuantos_sufijos_son_pal("oso lolo"))