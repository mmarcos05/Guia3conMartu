from queue import LifoQueue as Pila
import random
import typing

def readLines(archivo:str) -> list[str]:
    archivo = open(archivo, "r")
    lineas = archivo.readlines()
#    print(lineas)
    
readLines("cancion.txt")

# Ejercicio 1.1
def contar_lineas(nombre_archivo:str) -> int:
    archivo: typing.IO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    return len(lineas)

# print(contar_lineas ("cancion.txt"))

# Ejercicio 1.2
def pertenece(a:str, b: list[str]) -> bool:
    indice: int = 0
    while indice < len(b):
        if b[indice] == a:
            return True
        else: indice += 1
    return False

def separar_en_palabras(linea: str) -> list[str]:
    palabras: list[str] = []
    palabra: str = ""
    for caracter in linea:
        if caracter == ' ' or caracter == '"' or caracter == '\n':
            palabras.append(palabra) # Va recorriendo la linea y cuando encuetra un espacio suma la palabra acumulada a la lista de palabras 
            palabra = '' # La reinicia para seguir con la otra palabra
        else: 
            palabra += caracter # Vuelve al if
    palabras.append(palabra) # Agrega la ultima palabra que encuentra
    return palabras

# print(separar_en_palabras("hola como estas"))

def existe_palabra_en_archivo(palabra: str, nombre_archivo:str) -> bool:
    archivo: typing.IO = open(nombre_archivo, "r")
    linea: str
    for linea in archivo:
        palabras: list[str] = separar_en_palabras(linea)
        if pertenece(palabra,palabras):
            archivo.close()
            return True
    archivo.close()
    return False

# print(existe_palabra_en_archivo("la", "cancion.txt"))

# hago el ejercicio pero que tambien me diga en que linea esta la palabra
def existe_palabra_en_archivo_en_donde(palabra: str, nombre_archivo:str) -> tuple:
    archivo: typing.IO = open(nombre_archivo, "r")
    linea: str
    lineas_con_palabra: list[int] = []
    contador_linea = 1
    for linea in archivo:
        palabras: list[str] = separar_en_palabras(linea)
        if pertenece(palabra,palabras):
            lineas_con_palabra.append(contador_linea)
        contador_linea += 1 
    archivo.close()
    return len(lineas_con_palabra) > 0, lineas_con_palabra # si len(lineas_con_palabra es mayor a 0 es porque la palabra esta en alguna)

# existe, lineas_con_palabra = existe_palabra_en_archivo_en_donde("la","cancion.txt")
# if existe:
#     print(f"Existe 'la' en las lineas {lineas_con_palabra} del archivo 'cancion.txt'")
# else: 
#     print("No existe la palabra en el archivo")     

# Ejercicio 1.3
def cantidad_apariciones(nombre_archivo:str, palabra:str) -> int:
    contador: int = 0
    linea: str
    archivo: typing.IO = open(nombre_archivo, "r")
    for linea in archivo:
        palabras: list[str] = separar_en_palabras(linea)
        if pertenece(palabra,palabras):
            contador += 1
    archivo.close()
    return contador

# print(cantidad_apariciones("cancion.txt","feliz"))

# Ejercicio 2
def es_comentario(linea:str) -> bool:
    i:int = 0
    while(i < len(linea) and linea[i] == ' '):
        i += 1
    return i < len(linea) and linea[i] == '#' # Encontre un char que no es blanco y es el numeral

def clonar_sin_comentarios(nombre_archivo:str) -> None:
    archivo: typing.IO = open(nombre_archivo,"r")
    archivo2: typing.IO = open("clonado.txt","w")
    lineas: list[str] = archivo.readlines()

    for linea in lineas:
        if (not es_comentario(linea)):
            archivo2.write(linea)
    
    archivo.close()
    archivo2.close()

    # Quiero que me imprima en la consola el archivo clonado entonces lo abro como read
    archivo2 = open("clonado.txt","r")
    contenido = archivo2.read()
    print(contenido)

    archivo2.close()

# clonar_sin_comentarios("ejemplo_comentado.py")

# Ejercicio 3
def invertir_lineas(nombre_archivo:str) -> None:
    archivo: typing.IO = open(nombre_archivo,"r")
    lineas: list[str] = archivo.readlines()
    archivo2: typing.IO = open("reverso.txt", "w")
    cant_lineas: int = len(lineas)
    # print(len(lineas))
    while cant_lineas > 0:
        if pertenece('\n', lineas[cant_lineas - 1]):
            archivo2.write(lineas[cant_lineas - 1])
        else:
            archivo2.write(lineas[cant_lineas - 1] + '\n')    
        cant_lineas -= 1

    archivo.close()
    archivo2.close()

#    archivo2 = open("reverso.txt","r")
#    contenido = archivo2.read()
#    print(contenido)
#
#    archivo2.close()
    
# invertir_lineas("cancion.txt")

# Ejercicio 4
def agregar_frase_al_final(nombre_archivo:str, frase:str) -> None:
    archivo = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    cant_lineas: int = len(lineas)
    archivo.close()
    archivo: typing.IO = open(nombre_archivo,"a")
    if pertenece('\n', lineas[cant_lineas - 1]):
        archivo.write(frase)
    else:
        archivo.write('\n' + frase)
    archivo.close()

    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()

# agregar_frase_al_final("cancion.txt","Y tengas buenos regalos") 
# no pongo print porque si no me aparece None en la terminal

# Ejercicio 5
def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
    archivo = open(nombre_archivo,"r")
    contenido = archivo.read()
    archivo.close()

    archivo = open(nombre_archivo,"w")
    archivo.write(frase + '\n' + contenido)
    archivo.close()

    archivo = open(nombre_archivo, "r")
    contenidofinal = archivo.read()
    print(contenidofinal)
    archivo.close()

# agregar_frase_al_principio("cancion.txt", "Felicidades")

# Ejercicios PILAS clase
def contar_elementos_pila(p:Pila) -> int:
    cantidad:int = 0
    pAux = copiar_pila(p)

    while (not pAux.empty()):
        elem = pAux.get()
        cantidad += 1
    return cantidad

def copiar_pila(p:Pila) -> Pila:
    pAux = Pila()
    res = Pila()
    while (not p.empty()):
        elem = p.get()
        pAux.put(elem)
    # Le saco los elementos a p y los pongo en otra nueva (me quedan al reves)

    while (not pAux.empty()):
        elem = pAux.get()
        p.put(elem)
        res.put(elem)
    # Armo la pila res para que me quede en el mismo orden de p (pAux se invierte)

    return res

# mi_pila: Pila = Pila()
# mi_pila.put(5)
# mi_pila.put(8)
# print(contar_elementos_pila(mi_pila)) 

# Ejercicio 8
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    p = Pila()
    for i in range (cantidad):
        p.put(random.randint(desde,hasta))
    return p

# p = generar_nros_al_azar(4,8,50)
# print(p.queue)
# print(f"pila al azar: {list(generar_nros_al_azar(4,8,50).queue)}")

# Ejercicio 10
def buscar_el_maximo(p:Pila[int]) -> int:
    pAux = Pila()
    pAux = copiar_pila(p)
    maximo_actual: int = pAux.get() # agarro el primer elemento de la pila (como no lo comparo con nada, asumo que es el maximo)

    while (not pAux.empty()):
        comparador:int = pAux.get() # agarro el segundo elemento (que va a ser el primero porque ya saque uno con maximo_actual)
        if comparador > maximo_actual:
            maximo_actual = comparador
    return maximo_actual

# pila: Pila = Pila()
# pila.put(2)
# pila.put(4)
# pila.put(20)
# pila.put(1)
# pila.put(6)
# print(buscar_el_maximo(pila))
