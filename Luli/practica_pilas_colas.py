from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

def separar_en_palabras(linea: str) -> list:
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

# PRACTICA 8 - PILAS

def copiar_pila(p: Pila) -> Pila:
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

# -- 

def generar_nros_al_azar_pilas(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    pila_azar: Pila = Pila()

    for _ in range(cantidad):
        numero: int = random.randint(desde, hasta)
        pila_azar.put(numero)
    return pila_azar

# --

def cantidad_elementos_pila(p: Pila) -> int:
    contador: int = 0
    copia: Pila = copiar_pila(p)
    
    while not copia.empty():
        copia.get()
        contador += 1
    return contador

# --

def buscar_el_maximo_pila(p: Pila[int]) -> int:
    copia: Pila[int] = copiar_pila(p)
    maximo_actual = 0

    while not copia.empty():
        elemento: int = copia.get()
        if elemento > maximo_actual:
            maximo_actual = elemento
    return maximo_actual

# --

def esta_bien_balanceada(s: str) -> bool:
    p: Pila = Pila()
    
    for char in s:
        if char == '(':
            p.put(char)
        elif char == ')':
            if p.empty(): # si no hay un '(' antes ya es false
                return False
            else: 
                p.get() # si hay, saca el que pusiste
    return p.empty() # tiene que dar True si la pila queda vacia al final

# --

def es_operando(char: chr) -> bool:
    numeros: str = "0123456789"
    if char in numeros:
        return True
    return False
    
def es_operador(char: chr) -> bool:
    operadores: str = "+-*/"
    if char in operadores:
        return True
    return False

def evaluar_expresion(s: str) -> float:
    pila: Pila = Pila()
    for char in s:
        if es_operando(char):
            pila.put(float(char))
        elif es_operador(char):
            elemento2: int = pila.get()
            elemento1: int = pila.get()

            if char == '+':
                res = elemento1 + elemento2
            if char == '-':
                res = elemento1 - elemento2
            if char == '*':
                res = elemento1 * elemento2
            if char == '/':
                res = elemento1 / elemento2
            pila.put(res)
    return float(pila.get())

# -- 

def revertir_lista(lista: list[int]) -> list[int]:
    p: Pila[int] = Pila()
    lista_final: list[int] = []

    for numero in lista:
        p.put(numero)
    
    while not(p.empty()):
        lista_final.append(p.get())  
    
    return lista_final

# --

def es_palindromo_pilas(texto: str) -> bool:
    res: bool = False
    pila: Pila[str] = Pila()
    texto_final: str = ""

    for letra in texto:
        pila.put(letra)
    
    while not pila.empty():
        texto_final += pila.get()
    
    if texto_final == texto:
        res = True
    return res

# --

def revertir_cola_con_pila(cola: Cola[int]) -> None:
    pila: Pila[int] = Pila()

    while not cola.empty(): 
        pila.put(cola.get())

    while not pila.empty():
        cola.put(pila.get())

# -- 

def validar_html(html: str) -> bool:
# verifica si las etiquetas HTML están correctamente balanceadas utilizando una pila. 
# Las etiquetas serán del tipo <tag> y </tag>
    p: Pila[str] = Pila()

    for chr in html:
        if chr == '<' or chr == '</':
            p.put(chr)
        elif chr == '>':
            if p.empty():
                return False
            else: 
                p.get()
    return p.empty()

# html = "<html><body><h1></h1></body></html>"
# valido = validar_html(html)
# print(valido)  # Debería imprimir: True

# PRACTICA 8 - COLAS 

def copiar_cola(c: Cola) -> Cola:
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

# --

def es_correo_spam(correo: str) -> bool:
# Es considerado spam si contiene la palabra "OFERTA", "PUBLICIDAD", "ATENCION" o "DESCUENTO"
    palabras_correo: list[str] = separar_en_palabras(correo)

    for palabra in palabras_correo:
        if palabra == "OFERTA" or palabra == "PUBLICIDAD" or palabra == "ATENCION" or palabra == "DESCUENTO":
            return True
    return False

def procesar_correos(correos: Cola[str]) -> tuple[list[str], list[str]]:
# Procesa una cola de correos electrónicos, clasificando entre correos legítimos y correos no deseados (spam).
# Para los correos legítimos, agregarlos a una lista de correos aceptados.
# Para los correos spam, agregarlos a una lista de correos no deseados

    correo_spam: list[str] = []
    correo_aceptado: list[str] = []

    while not correos.empty():
        correo: str = correos.get()
        if es_correo_spam(correo):
            correo_spam.append(correo)
        else: 
            correo_aceptado.append(correo)

    return correo_spam, correo_aceptado

# correos: Cola[str] = Cola()
# correos.put("ATENCION OFERTA!!")
# correos.put("Buen dia, como estas?")
# correos.put("Hoy hay DESCUENTO")
# print(procesar_correos(correos)) # deberia imprmir (['ATENCION OFERTA!!', 'Hoy hay DESCUENTO'], ['Buen dia, como estas?'])

# --

# Simulacion de supermercado
def llegada_clientes(cola: Cola[str], nombre_cliente: str) -> None:
    cola.put(nombre_cliente)

def atender_cliente(cola: Cola[str]) -> str:
    proximo: str = cola.get()
    return proximo

def obtener_estadisticas(cola: Cola[str]) -> dict[str, str]:
    # dict = {cantidad de clientes: contador, proximo: nombre}
    copia = copiar_cola(cola)
    proximo = ""
    contador: int = 0

    while not copia.empty():
        cliente = copia.get()
        contador += 1
        if proximo == "":
            proximo = cliente

    dicc = dict()
    dicc["Cantidad de clientes"] = contador 
    dicc["Proximo cliente"] = proximo
    return dicc

# c = Cola()
# c.put("Julio")
# c.put("Maria")
# print(c.queue)
# print(obtener_estadisticas(c))

# --

def encolar_llamada(llamadas_entrantes: Cola, llamada: tuple[str, int]) -> None:
    llamadas_entrantes.put(llamada)

def asignar_llamada(llamadas_entrantes: Cola, agentes_disponibles: Cola) -> tuple[str, str]:
    llamada: str = llamadas_entrantes.get()
    agente: str = agentes_disponibles.get()

    return llamada, agente

def registrar_tiempo_espera(tiempo_espera: dict[str, int], cliente: str, tiempo: int) -> None:
    if not cliente in tiempo_espera.keys():
        tiempo_espera[cliente] = tiempo
    else: 
        tiempo_espera[cliente] += tiempo

# --

def generar_nros_al_azar_colas(cantidad: int, desde: int, hasta: int) -> Cola:
    cola: Cola = Cola()
    
    for _ in range(cantidad):
        numero: int = random.randint(desde, hasta)
        cola.put(numero)
    return cola

# --

def cantidad_elementos_cola(c: Cola) -> int:
    copia: Cola = copiar_cola(c)
    contador: int = 0

    while not copia.empty():
        copia.get()
        contador += 1
    return contador

# --

def buscar_el_maximo_cola(c: Cola) -> int:
    copia: Cola = copiar_cola(c)
    maximo_actual: int = 0

    while not copia.empty():
        elem: int = copia.get()
        if elem > maximo_actual:
            maximo_actual = elem
    return maximo_actual

# --

def armar_secuencia_bingo() -> Cola[int]:
    secuencia: Cola[int] = Cola()
    numeros: list[int] = []

    while len(numeros) < 100:
        numero: int = random.randint(0,99)
        if numero not in numeros:
            secuencia.put(numero)
            numeros.append(numero)
    return secuencia

def armar_carton_bingo() -> list[int]:
    carton: list[int] = []
    numeros: list[int] = []

    while len(numeros) < 12:
        numero: int = random.randint(0,99)
        if numero not in numeros:
            carton.append(numero)
            numeros.append(numero)
    return carton

def jugar_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
    copia_bolillero: Cola[int] = copiar_cola(bolillero)
    aciertos: int = 0

    while aciertos < 12:
        bolilla: int = copia_bolillero.get()
        if bolilla in carton:
            aciertos += 1
            jugadas += 1
        else:
            jugadas += 1
    return jugadas

# --

def n_pacientes_urgentes(c: Cola[(int,str,str)]) -> int:
    contador: int = 0
    copia: Cola[(int,str,str)] = copiar_cola(c)

    while not copia.empty():
        datos_paciente: tuple[int,str,str] = copia.get()
        prioridad: int = datos_paciente[0]

        if prioridad >= 1 and prioridad <= 3:
            contador += 1

    return contador

# --

def atencion_a_clientes(c: Cola[(str,int,bool,bool)]) -> Cola[(str,int,bool,bool)]:
    copia: Cola[(str,int,bool,bool)] = copiar_cola(c)
    orden_de_atencion: Cola[(str,int,bool,bool)] = Cola()

    con_prioridad: Cola[(str,int,bool,bool)] = Cola()
    cuenta_preferencial: Cola[(str,int,bool,bool)] = Cola()
    resto: Cola[(str,int,bool,bool)] = Cola()

    while not copia.empty():
        datos_cliente: tuple[(str,int,bool,bool)] = copia.get()
        prioridad: bool = datos_cliente[3]
        preferencial: bool = datos_cliente[2]

        if prioridad:
            con_prioridad.put(datos_cliente)
        elif preferencial:
            cuenta_preferencial.put(datos_cliente)
        else: 
            resto.put(datos_cliente)
    
    while not con_prioridad.empty():
        orden_de_atencion.put(con_prioridad.get())
    while not cuenta_preferencial.empty():
        orden_de_atencion.put(cuenta_preferencial.get())
    while not resto.empty():
        orden_de_atencion.put(resto.get())

    return orden_de_atencion