from queue import LifoQueue as Pila
from queue import Queue as Cola

def copiar_pila(p: Pila) -> Pila: # sirve para COLAS tambien
    pAux: Pila = Pila()
    res: Pila = Pila()

    while not p.empty():
        elemento = p.get()
        pAux.put(elemento)
    while not pAux.empty():
        elem = pAux.get()
        p.put(elem)
        res.put(elem)
    return res

def n_pacientes_urgentes(c: Cola[(int,str,str)]) -> int:
    contador: int = 0
    copia: Cola[(int,str,str)] = copiar_cola(c)
    while not copia.empty():
        datos_paciente: tuple[int,str,str] = copia.get()
        prioridad: int = datos_paciente[0]

        if prioridad >= 1 and prioridad <= 3:
            contador += 1
    return contador

def separar_en_palabras(linea: str) -> list: # no cuenta nos enter como palabra!!!
    palabras = []
    palabra = ""
    for caracter in linea:
        if caracter == ' ' or caracter == '"' or caracter == '\n' or caracter == '\r' or caracter == '\t':
            if palabra:  # Añade solo si palabra no está vacía (es lo mismo que decir if len(palabra) > 0)
                palabras.append(palabra)
                palabra = ''
        else: 
            palabra += caracter
    if palabra:  # Añadir la última palabra si no está vacía
        palabras.append(palabra)
    return palabras

def buscar_minimo(temps: list[tuple[int,float]]) -> float:
    minimo_actual: float = temps[0][1]

    for temperatura in temps:
        minimo = temperatura[1]
        if minimo < minimo_actual:
            minimo_actual = minimo
    return minimo_actual

def buscar_maximo(temps: list[tuple[int,float]]) -> float:
    maximo_actual: float = temps[0][1]

    for i in range (len(temps)):
        maximo = temps[i][1]
        if maximo > maximo_actual:
            maximo_actual = maximo
    return maximo_actual

def suma_total(lista:list[int]) -> int:
    total: int = 0
    for i in range(len(lista)):
        total += lista[i]
    return total

def ordenados(numeros:list[int]) -> bool:
    for i in range (len(numeros)-1):
        if numeros[i] > numeros[i+1]:
            return False
    return True

def capicua_str(texto: str) -> bool: # es lo mismo para lista de int
    for i in range(len(texto)):
        if texto[i] != texto[len(texto) - i - 1]:
            return False
    return True

def invertir_lista(lista:list[int]) -> bool:
    res: list[int] = []
    for i in range(len(lista) -1, -1, -1):
        res.append(lista[i])
    return res

def eliminar_repetidos(s: str) -> str:
    nuevo_str: str = ""
    vistos: list = []
    
    for char in s:
        if char == ' ' or char not in vistos:
            nuevo_str += char
            if char != ' ':
                vistos.append(char)    
    return nuevo_str

def hay_repetidos(lista: list[int]) -> bool:
    contador: int = 0
    for i in range(len(lista)):
        for elemento in lista:
            if elemento == lista[i]:
                contador += 1
            if contador > 1:
                return True
        contador = 0
    return False

def pertenece_a_cada_uno(s: list[list[int]], e: int, res:list[bool]) -> None:
    for lista in s:
        if e in lista:
            res.append(True)
        else: res.append(False)
# res: list[bool] = []
# listas = [[1,2,3,5],[3,4,5],[5,6,7]]
# pertenece_a_cada_uno(listas, 5, res)
# print(res)

def lista_simetrica(lista):
    mitad = int(len(lista) / 2)
    i = 0
    while i < mitad:
        if lista[i] != lista[mitad + i]:
            return False
        i += 1

def es_matriz(matriz: list[list[int]]) -> bool:
    fila: list[int]

    if len(matriz[0]) == 0:
        return False
    
    for fila in matriz:
        if len(fila) != len(matriz[0]):
            return False
    return True

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

def columna_matriz(m: list[list[int]], num_col: int) -> list[int]:
    columna: list[int] = []
    for fila in m:
        columna.append(fila[num_col]) # de cada fila agarro el elemento que esta en la posicion igual que el numero de columna
    return columna

def copiar_diccionario(diccionario: dict[str,str]) -> dict[str,str]:
    copiar_diccionario: dict[str,str] = {}
    claves: list[str] = diccionario.keys()
    for clave in claves:
        valor: str = diccionario[clave]
        copiar_diccionario[clave] = valor
    return copiar_diccionario

def frecuencia_posiciones_por_caballo(caballos: list[str], carreras: dict[str,list[str]]) -> dict[str,list[int]]:
    diccionario_final: dict[str,list[int]] = {}
    for caballo in caballos:
        diccionario_final[caballo] = [0]*len(caballos)
    # carreras = dict['carrera': [posiciones caballos]]
    # diccionario_final = dict['caballo': [posiciones]]
    for posiciones_caballos in carreras.values():
        for posicion in range(len(posiciones_caballos)):
            caballo = posiciones_caballos[posicion]
            diccionario_final[caballo][posicion] += 1
    return diccionario_final

# para hacer un print de historiales con pilas:
""" historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario2", "youtube.com")
pila1 = historiales["Usuario1"]
print(f"Historial de usuario 1: {pila1.queue}")
pila2 = historiales["Usuario2"]
print(f"Historial de usuario 2: {pila2.queue}") """

def agregar_producto(inventario: dict[str,dict[str, str]], nombre: str, precio: float, cantidad:int) -> None:
    # inventario = {"nombre": {info_producto}}
    # info_producto = {"precio: precio, "cantidad":cantidad}
    info_producto: dict[str,str] = dict()
    info_producto["Precio"] = precio
    info_producto["Cantidad"] = cantidad
    inventario[nombre] = info_producto

def agrupar_por_longitud(texto: str) -> dict:
    diccionario_final: dict[int,int] = {}
    palabras: list[str] = separar_en_palabras(texto)
    for palabra in palabras:
        longitud: int = len(palabra)
        if longitud in diccionario_final.keys():
            diccionario_final[longitud] += 1
        else: 
            diccionario_final[longitud] = 1
    return diccionario_final

def invertir_diccionario_con_rep(diccionario: dict[str,int]) -> dict:
    invertido: dict[int,list[str]] = {}
    for palabra, numero in diccionario.items():
        if numero in invertido:
            invertido[numero].append(palabra)
        else:
            invertido[numero] = [palabra]
    return invertido

def registrar_orden(historial: dict[str, Pila[str]], usuario: str, orden: str) -> None:
    # historial = {nombre: pila[ordenes]}
    if usuario not in historial.keys():
        historial[usuario] = Pila() # Si no esta, crea la pila vacía
    historial[usuario].put(orden) # Agrega las ordenes