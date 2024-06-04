from queue import LifoQueue as Pila
import random
import typing
from typing import List, Tuple, Dict
from queue import Queue as Cola

#EJERCICIO 1.1
def contar_lineas(nombre_archivo:str) -> int:
    archivo = open(nombre_archivo, 'r')
    archivo_lineas = archivo.readlines()
    archivo.close()
    return len(archivo_lineas)

#print(contar_lineas("archivo.txt"))

#EJERCICIO 1.2
def pertenece(a:str, b: List[str]) -> bool:
    indice: int = 0
    while indice < len(b):
        if b[indice] == a:
            return True
        else: indice += 1
    return False

#EJERCICIO 2
def es_comentario(linea:str) -> bool:
    i:int = 0
    while(i < len(linea) and linea[i] == ' '):
        i += 1
    return i < len(linea) and linea[i] == '#'

"""def es_comentario(linea:str) -> bool:     está mal no sé por qué
    longitud:int = len(linea)
    i:int = 0
    res:bool = False
    while (longitud > i):
        if (linea[i] == ' '):
            i+=1        
        else:
            if (linea[i] == '#'):
                res = True
            else:
                res = False
    return res"""


def clonar_sin_comentarios(nombre_archivo:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    nuevo_archivo:typing.IO = open("clonado.txt", 'w')
    lineas:List[str] = archivo.readlines()

    for linea in lineas:
        if (not es_comentario(linea)):
            nuevo_archivo.write(linea)
    nuevo_archivo.close()
    archivo.close()

    nuevo_archivo = open("clonado.txt", 'r')
    contenido = nuevo_archivo.read()
    print(contenido)
    nuevo_archivo.close()

#clonar_sin_comentarios("ejemplo_clonado.py")
        
        
#EJERCICIO 3
def reversa(lista:List[str]) -> List[str]:    #otra forma de hacer la función de reversa
    nueva_lista:List[str] = []
    longitud:int = len(lista)
    i:int = longitud - 1

    for i in range (longitud-1, (-1), (-1)):
        nueva_lista.append(lista[i])
    return nueva_lista

#print(reversa(["cami", "niki", "wendy", "kelly"]))

"""def invertir_lineas(nombre_archivo:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    nuevo_archivo:typing.IO = open("reverso.txt", 'w')

    lineas:List[str] = archivo.readlines()
    lineas_reversa:List[str] = reversa(lineas)

    nuevo_archivo.writelines(lineas_reversa)

    archivo.close()
    nuevo_archivo.close()

    nuevo_archivo = open("reverso.txt", 'r')
    contenido = nuevo_archivo.read()
    print(contenido)
    nuevo_archivo.close()

invertir_lineas("ejemplo_clonado.py")"""

def invertir_lineas(nombre_archivo:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    nuevo_archivo:typing.IO = open("reverso.txt", 'w')
    lineas:List[str] = archivo.readlines()
    cantidad_lineas:int = len(lineas)

    while cantidad_lineas > 0:
        if pertenece('\n', lineas[cantidad_lineas - 1]):
            nuevo_archivo.write(lineas[cantidad_lineas - 1])
        else:
            nuevo_archivo.write(lineas[cantidad_lineas - 1] + '\n')
        cantidad_lineas -=1
    archivo.close()
    nuevo_archivo.close()

    nuevo_archivo = open("reverso.txt", 'r')
    contenido = nuevo_archivo.readlines()
    print(contenido)
    nuevo_archivo.close()

#invertir_lineas("ejemplo_clonado.py")

#EJERCICIO 4
def agregar_frase_al_final(nombre_archivo:str, frase:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    lineas:List[str] = archivo.readlines()
    cantidad_lineas:int = len(lineas)
    archivo.close()

    archivo:typing.IO = open(nombre_archivo, 'a')
    
    if pertenece ('\n', lineas[cantidad_lineas - 1]):
        archivo.write(frase)
    else:
        archivo.write('\n' + frase)
    archivo.close()

    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    print(contenido)
    archivo.close()

#agregar_frase_al_final("archivo.txt", "esta es una prueba")

#EJERCICIO 5
def agregar_frase_al_principio(nombre_archivo:str, frase:str) -> None:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    
    archivo = open(nombre_archivo, 'w')
    archivo.write(frase + '\n' + contenido)
    archivo.close()

    archivo = open(nombre_archivo, 'r')
    contenidofinal = archivo.read()
    print(contenidofinal)
    archivo.close()

#agregar_frase_al_principio("feliz_cumple.txt", "esta es una prueba")

#EJERCICIO 6
def listar_palabras_de_archivo(nombre_archivo:str) -> List:
    lista:List = []
    i:int = 0
    archivo_binario = open(nombre_archivo, 'rb')
    contenido_binario = archivo_binario.read()
    contenido = chr(contenido_binario)
    archivo_binario.close()

    archivo = open("nuevo.txt", 'w')
    archivo.write(contenido)
    lineas:List = archivo.readlines()
    cantidad_lineas:int = len(lineas)

    while cantidad_lineas - 1 > i:
        if len(lineas[i]) > 5:
            if (pertenece("_", lineas[i]) and pertenece(" ", lineas[i])):
                lista.append(lineas[i])
                i+=1
        i+=1
    return lista

#EJERCICIO 7
"""def promedio_estudiante(nombre_archivo, lu:str) -> float:
    archivo = open(nombre_archivo, 'r')
    lineas:List = archivo.readlines()
    i:int = 0
    total:int = 0
    cantidad_materias:int = 0
    cantidad_lineas:int = len(lineas)

    while (cantidad_lineas - 1) > i:
        if (lineas[i])[0] == lu:
            total += (lineas[i])[3]
            cantidad_materias += 1
            i += 1
        else:
            i += 1
    archivo.close()
    if cantidad_materias == 0:
        return 0.0
    else:
        return (total/cantidad_materias)

print(promedio_estudiante("notas.csv", "67890"))"""



#EJERCICIO 8
def copiar_pila(p:Pila) -> Pila:
    pila_aux:Pila = Pila()
    res:Pila = Pila()

    while not p.empty():
        pila_aux.put(p.get())
    
    while not pila_aux.empty():
        val = pila_aux.get()
        p.put(val)
        res.put(val)
    return res

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    p = Pila()
    for i in range (cantidad):
        p.put(random.randint(desde,hasta))
    return p

"""def generar_nros_al_azar(cantidad: int, desde:int, hasta:int) -> Pila[int]:
    pila = Pila()
    while longitud_pila(pila) < 100:
        i = random.randint(desde, hasta)
        if i not in pila:
            pila.put(i)
    return pila

p = generar_nros_al_azar(5, 20, 40)"""

#print(p.get())

#EJERCICIO 9
def cantidad_elementos(p:Pila) -> int:
    pila:Pila = p
    cantidad:int = 0
    while not pila.empty():
        pila.get()
        cantidad += 1
    return cantidad

h = Pila()

h.put(3)
h.put(10)
h.put(2)
h.put(7)
h.put(1)
h.put(4)

#print(cantidad_elementos(h))

#EJERCICIO 10
def buscar_el_maximo(p:Pila[int]) -> int:
    pila:Pila[int] = p
    maximo = pila.get()
    while not pila.empty():
        candidato = pila.get()
        if candidato > maximo:
            maximo = candidato
    return maximo
    
p = Pila()

p.put(3)
p.put(10)
p.put(2)
p.put(7)
p.put(1)
p.put(4)

#print(buscar_el_maximo(p))

#EJERCICIO 11

def esta_bien_balanceada(s:str) -> bool:
    pila:Pila[chr] = Pila()
    for caracter in s:
        if caracter == '(':
            pila.put(caracter)
        elif caracter == ')':
            if pila.empty():
                return False
            else:
                pila.get()
    return pila.empty()

#print(esta_bien_balanceada("1 + (2 x 3 - (20 / 5))"))
#print(esta_bien_balanceada("10 ∗ ( 1 + ( 2 ∗ ( −1)))"))
#print(esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))

#EJERCICIO 12
"""def pertenece2(a:chr, b: str) -> bool:
    indice: int = 0
    while indice < len(b):
        if b[indice] == a:
            return True
        else: indice += 1
    return False"""

def evaluar_expresion(s:str) -> float:
    operadores:List = ['+', '-', '*', '/']
    pila:Pila[int] = Pila()
    for caracter in s:
        if (not pertenece(caracter, operadores)) and (caracter != ' '):
            pila.put(caracter)
        elif pertenece(caracter, operadores):
            if caracter == '+':
                total = (int(pila.get()) + int(pila.get()))
                pila.put(total)
            elif  caracter == '-':
                total = - (int(pila.get()) - int(pila.get()))
                pila.put(total)
            elif  caracter == '*':
                total = (int(pila.get()) * int(pila.get()))
                pila.put(total)
            else:
                total = (int(pila.get()) / int(pila.get()))
                pila.put(total)
    return int(pila.get())

#print(evaluar_expresion("3 4 + 5 * 2 -"))

#EJERCICIO 13
def copiar_cola(c:Cola) -> Cola:
    cola_aux:Cola = Cola()
    res:Cola = Cola()

    while not c.empty():
        cola_aux.put(c.get())
    
    while not cola_aux.empty():
        val = cola_aux.get()
        c.put(val)
        res.put(val)
    return res

def armar_cola(cantidad, desde, hasta) -> None:
    c = Cola()
    pila:Pila[int] = generar_nros_al_azar(cantidad, desde, hasta)
    while not pila.empty():
        c.put(pila.get())
    return c

cola = armar_cola(5, 1, 20)
#print(cola.queue)


def cantidad_elementos(c:Cola) -> int:
    cantidad:int = 0
    cola:Cola = copiar_cola(c)
    while not cola.empty():
        cola.get()
        cantidad += 1
    return cantidad

c = Cola()
c.put(1)
c.put(2)
c.put(3)
c.put(7)

#print(cantidad_elementos(c))

def buscar_el_maximo_cola(c:Cola) -> int:
    cola:Cola = copiar_cola(c)
    maximo:int = cola.get()
    while not cola.empty():
        candidato:int = cola.get()
        if candidato > maximo:
            maximo = candidato
    return maximo

c = Cola()
c.put(1)
c.put(0)
c.put(8)
c.put(7)

#print(buscar_el_maximo_cola(c))

#EJERCICIO 16
#nros:List = list(range(100)) #hace lista de nùmeros del 0 al 99
#Punto 1)
def armar_secuencia_de_bingo() -> Cola:
    pila:Pila[int] = generar_nros_al_azar(100,0,99)
    cola = Cola()
    while not pila.empty():
        cola.put(pila.get())
    return cola

c = armar_secuencia_de_bingo()
#print(c.queue)

#Punto 2)
def pertenece_num(numero:int, lista:List[int]) -> bool:
    for i in lista:
        if numero == i:
            return True
    return False

#print(pertenece_num(5, [1,2,3,4,6,7]))

def jugar_carton_de_bingo(carton:List[int], bolillero:Cola) -> int:
    tarjeta:List[int] = carton.copy()
    bolilla:Cola = copiar_cola(bolillero)
    jugadas:int = 0
    bingo:int = 0

    while 12 > bingo:
        elemento:int = bolilla.get()
        if pertenece_num(elemento, tarjeta):
            bingo += 1
            jugadas += 1
        else:
            jugadas += 1
    return jugadas

c:List[int] = random.sample(range(0,99),12)
b:Cola = armar_secuencia_de_bingo()

#print(b.queue)
#print(f"el carton es {c} y {jugar_carton_de_bingo(c, b)}")

#EJERCICIO 17
def n_pacientes_urgentes(c:Cola) -> int:
    cola:Cola = copiar_cola(c)
    rango:List[int] = [1, 2, 3]
    urgentes:int = 0
    while not cola.empty():
        elemento = cola.get()
        if pertenece_num(elemento[0], rango):
            urgentes += 1
    return urgentes

c = Cola()
c.put((1, "camila", "cardio"))
c.put((5, "marcela", "cirugia"))
c.put((1, "nicole", "plastico"))
c.put((2, "gabriel", "clinica"))
c.put((3, "wendy", "trauma"))

#print(n_pacientes_urgentes(c))

#EJERCICIO 18
def clientes() -> Cola:
    c:Cola = Cola()
    nuevo_cliente:str = input(f"¿Quiere registrarse?: ")
    datos:Tuple[str, int, bool, bool] = ("hola", 0, True, False)
    datos_lista = list(datos)

    while nuevo_cliente == "si":
        nombre:str = input(f"Por favor, ingrese su nombre y apellido: ")
        datos_lista[0] = nombre
        dni:int = input(f"Por favor, ingrese su DNI sin espacios: ")
        datos_lista[1] = dni
        cuenta:str = input("¿Tiene cuenta preferencial, sí o no?:  ")
        if cuenta == "si":
            datos_lista[2] = True
        else:
            datos_lista[2] = False
        prioridad:str = input(f"Si cumple alguna de las siguientes condiciones responda 'si', en caso contrario responda 'no':\nAdulto +65\nEmbarazada\nMovilidad Reducida\n")
        if prioridad == "si":
            datos_lista[3] = True
        else:
            datos_lista[3] = False
        datos_modificado = tuple(datos_lista)
        c.put(datos_modificado)
        nuevo_cliente:str = input(f"¿Quiere registrarse?: ")
    return c

#cola = clientes()
#print(cola.queue)


def atencion_a_clientes(c:Cola) -> Cola:
    cola:Cola = copiar_cola(c)
    cola_prioridad_y_cuenta:Cola = Cola()
    cola_prioridad:Cola = Cola()
    cola_cuenta:Cola = Cola()
    cola_resto:Cola = Cola()
    cola_final:Cola = Cola()

    # Clasificar clientes en las colas correspondientes
    while not cola.empty():
        elemento = cola.get()
        if (elemento[2] == True) and (elemento[3] == True):  # Prioridad y cuenta
            cola_prioridad_y_cuenta.put(elemento)
        elif (elemento[2] == False) and (elemento[3] == True):  # Prioridad
            cola_prioridad.put(elemento)
        elif (elemento[2] == True) and (elemento[3] == False):  # Cuenta
            cola_cuenta.put(elemento)
        else:  # Resto
            cola_resto.put(elemento)

    # Unir todas las colas en el orden especificado
    while not cola_prioridad_y_cuenta.empty():
        elemento = cola_prioridad_y_cuenta.get()
        cola_final.put(elemento)
    while not cola_prioridad.empty():
        elemento = cola_prioridad.get()
        cola_final.put(elemento)
    while not cola_cuenta.empty():
        elemento = cola_cuenta.get()
        cola_final.put(elemento)
    while not cola_resto.empty():
        elemento = cola_resto.get()
        cola_final.put(elemento)
    return cola_final

c = clientes()
cola_atencion = atencion_a_clientes(c)
#print(cola_atencion.queue)


#EJERCICIO 19
def separar_palabras(linea:str) -> List[str]:
    palabra:str = ''
    lista:List[str] = []
    for caracter in linea:
        if caracter != ' ':
            palabra += caracter
        else:
            lista.append(palabra)
            palabra = ''
    lista.append(palabra)
    return lista

#print(separar_palabras("hola todo bien soy cami"))

def contar_letras(palabra:str) -> int:
    total_letras:int = 0
    for caracter in palabra:
        total_letras += 1
    return total_letras

#print(contar_letras("hola"))

"""def misma_longitud(lista:List[str]) -> int:
    total:int = 0
    for i in lista:
        if contar_letras(lista[i]) == 
 
def agrupar_por_longitud(nombre_archivo:str) -> dict:
    diccionario:dict = {}
    archivo:typing.IO = open(nombre_archivo, 'r')
    lineas:List = archivo.readlines()
    lista:List = separar_palabras(linea)
    for linea in lineas:
        for i in lista:
            diccionario[contar_letras(lista[i])] = """

#EJ 19 PROFE
def pertenece_dic (d:dict, k) -> bool:
    lista = list(d.keys())
    for e in lista:
        if e == k:
            return True
    return False

#def palabras_de_archivo(nombre_Archivo:str) -> list[str]:


def agrupar(nombre_archivo:str) -> dict:
    palabras:List[str] = listar_palabras_de_archivo(nombre_archivo)
    res:dict = {}
    for p in palabras:
        t = len(p)
        if pertenece_dic(res, t):
            res[t] = res[t] + 1
        else:
            res[t] = 1
    return res

#EJERCICIO 21

    for linea in lineas:
        for i in lista:
            diccionario[contar_letras(lista[i])] = """
