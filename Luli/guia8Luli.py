from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
import typing
import csv

def readLines(archivo:str) -> list[str]:
    archivo = open(archivo, "r")
    lineas = archivo.readlines()
#    print(lineas)
    
# readLines("cancion.txt")

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

# Ejercicio 7
def promedio_estudiante(nombre_archivo:str, lu:str) -> float:
    archivo = open(nombre_archivo,"r")
    lector = csv.reader(archivo)
    total_notas = 0
    cantidad_notas = 0

    for fila in lector:
        nro_lu, materia, fecha, nota = fila
        if nro_lu == lu:
            total_notas += float(nota)
            cantidad_notas += 1 
    
    if cantidad_notas == 0:
        return 0.0
    else: return total_notas / cantidad_notas

def calcular_prom_por_estudiante(nombre_archivo_notas: str, nombre_archivo_promedios: str) -> None:
    estudiantes_cargados: list[str] = []

    archivo_promedios = open(nombre_archivo_promedios,"w")
    escritor_csv = csv.writer(archivo_promedios)
    escritor_csv.writerow(['nro de LU', 'promedio'])
   
    archivo_notas = open(nombre_archivo_notas, "r")
    lector_csv_notas = csv.reader(archivo_notas)

    for fila in lector_csv_notas:
        nro_lu = fila[0]
        if nro_lu not in estudiantes_cargados:
            promedio = promedio_estudiante(nombre_archivo_notas, nro_lu)
            escritor_csv.writerow([nro_lu, promedio])
            estudiantes_cargados.append(nro_lu)

# Crear el archivo 'notas.csv'
# with open('notas.csv', 'w', newline='') as archivo_notas:
#     escritor_csv = csv.writer(archivo_notas)
#     escritor_csv.writerow(['12345', 'Matemáticas', '2023-03-01', 8.5])
#     escritor_csv.writerow(['12345', 'Historia', '2023-03-15', 7.0])
#     escritor_csv.writerow(['67890', 'Literatura', '2023-03-01', 9.0])
#     escritor_csv.writerow(['67890', 'Física', '2023-03-15', 8.0])
#     escritor_csv.writerow(['67890', 'Química', '2023-04-01', 7.5])
#     escritor_csv.writerow(['11223', 'Matemáticas', '2023-03-01', 6.0])
#     escritor_csv.writerow(['11223', 'Historia', '2023-03-15', 5.5])
#     escritor_csv.writerow(['12345', 'Física', '2023-04-01', 9.0])

# Crear un archivo 'promedios.csv' vacío
# with open('promedios.csv', 'w', newline='') as archivo_promedios:
#     escritor_csv = csv.writer(archivo_promedios)
#     escritor_csv.writerow(['nro de LU', 'promedio'])

# nombre_archivo_notas = 'notas.csv'
# nombre_archivo_promedios = 'promedios.csv'
# calcular_prom_por_estudiante(nombre_archivo_notas, nombre_archivo_promedios)

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

# Ejercicio 9
def cantidad_elementos(p:Pila) -> int:
    pAux = Pila()
    contador = 0

    # voy sacando cada elemento y los cuento
    while not p.empty():
        elemento = p.get()
        pAux.put(elemento)
        contador += 1
    
    # restauro la pila original
    while not pAux.empty():
        p.put(pAux.get())
    
    return contador

# mi_pila = Pila()
# mi_pila.put(2)
# mi_pila.put(9)
# mi_pila.put(7)

# print(cantidad_elementos(mi_pila))

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

# Ejercicio 11
def esta_bien_balanceada(s:str) -> bool:
    pila = Pila()

    for char in s:
        if char == '(':
            pila.put(char) #Si hay un '(' lo agrega a una pila
        elif char == ')':
            if pila.empty(): #Si no hay un ')' entonces ya es False
                return False
            pila.get() #Si hay un ')' entonces saca el '(' que pusimos antes (los voy cancelando)
    
    return pila.empty() #Si al final me queda vacia, quiere decir que estan bien balanceados (por cada '(' hay un ')')

# print(esta_bien_balanceada("1 + ( 2 x 3 − ( 20 / 5 ) )"))  # True
# print(esta_bien_balanceada("10 * ( 1 + ( 2 * ( -1)))"))    # True
# print(esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))           # False
# print(esta_bien_balanceada("((()))"))                      # True
# print(esta_bien_balanceada("(()"))                         # False

# Ejercicio 12
def es_numero_operando(caracter:chr) -> bool:
    numeros: str = "0123456789"
    if caracter in numeros:
        return True
    else:
        return False
    
def es_operador(caracter:str) -> bool:
    operadores: list[str] = ["+","-","*","/"]
    if pertenece (caracter,operadores):
        return True
    else: 
        return False
    
def evaluar_expresion(s:str) -> float:
    pila = Pila()
    separador: list[str] = separar_en_palabras(s)
    
    for char in separador:
        if es_numero_operando(char):
            pila.put(float(char))
        elif es_operador(char):
            operando2 = pila.get()
            operando1 = pila.get()
        
            if char == '+':
                res = operando1 + operando2
            elif char == '-':
                res = operando1 - operando2
            elif char == '*':
                res = operando1 * operando2
            elif char == '/':
                res = operando1 / operando2

            pila.put(res)

    return pila.get()
        
# print(evaluar_expresion("3 4 + 5 * 2 -"))

# COLAS
def copiar_cola(c:Cola) -> Cola:
    cAux = Cola()
    res = Cola()
    while (not c.empty()):
        elem = c.get()
        res.put(elem)
        cAux.put(elem)
    
    while not cAux.empty():
        c.put(cAux.get())

    return res

# Ejercicio 13
def cola_de_enteros(cantidad, desde, hasta) -> None:
    c = Cola()
    p = generar_nros_al_azar(cantidad, desde, hasta)
    while not p.empty():
        c.put(p.get())  
    return c

# cola = generar_nros_al_azar(6,3,58)
# print(cola.queue)

# Ejercicio 14
def cantidad_elementos_cola(c:Cola) -> int:
    copia: Cola = copiar_cola(c)
    cAux = Cola()
    contador = 0

    while not (copia.empty()):
        elemento = copia.get()
        cAux.put(elemento)
        contador += 1

    while not (cAux.empty()):
        c.put(cAux.get())

    return contador

# cola = Cola()
# cola.put(341)
# cola.put(8)
# cola.put(23)
# print(cantidad_elementos_cola(cola))

# Ejercicio 15
def buscar_el_max_cola(c:Cola[int]) -> int:
    copia: Cola = copiar_cola(c)
    maximo: int = c.get() #Agarro el primero que tengo q sacar y ese va a ser mi maximo por ahora

    while not copia.empty():
        elemento = copia.get() #Agarro el proximo elemento a sacar y me fijo con el que habia agarrado antes
        if elemento > maximo: 
            maximo = elemento
    return maximo

# cola = Cola()
# cola.put(3)
# cola.put(56)
# cola.put(233)  
# print(buscar_el_max_cola(cola))

# Ejercicio 16 
# Bingo: un carton de bingo contiene 12 numeros al azar en el rango [0, 99]
def armar_secuencia_de_bingo() -> Cola[int]:
    return cola_de_enteros(100,0,99)

# cola = armar_secuencia_de_bingo()
# print(cola.queue)

def pertenece_num(numero:int, lista:list[int]) -> bool:
    for i in lista:
        if numero == i:
            return True
    return False

def jugar_carton_de_bingo(carton:list[int], bolillero:Cola) -> int:
    bolilla = bolillero.get()
    jugadas:int = 0
    bingo:int = 0

    while 12 > bingo:
        if pertenece_num(bolilla, carton):
            bingo += 1
            jugadas += 1
        else:
            jugadas += 1
    return jugadas

# Armo el bolillero
b = armar_secuencia_de_bingo()

# Armo el carton
c = random.sample(range(0,100),12)
# print(f"Carton de bingo: {carton}")

print(jugar_carton_de_bingo(c,b))


# Ejercicio 17
def n_pacientes_urgentes(c:Cola[(int,str,str)]) -> int:
    copia: Cola = copiar_cola(c)
    cAux = Cola()
    contador = 0

    while not copia.empty():
        paciente: tuple = copia.get()
        if isinstance(paciente,tuple) and len(paciente) == 3:
            prioridad, nombre, especialidad = paciente 
            if (1 <= prioridad <= 3):
                contador += 1
            cAux.put(paciente)

    while not cAux.empty():
        copia.put(cAux.get())

    return contador


def n_pacientes_urgentes2(c:Cola[(int,str,str)]) -> int:
    copia: Cola = copiar_cola(c)
    contador = 0

    while not copia.empty():
        prioridad, _, _ = copia.get()
        if 1 <= prioridad <= 3:
            contador += 1
    return contador

def n_pacientes_urgentes3(c:Cola[(int,str,str)]) -> int:
    copia_cola: Cola = copiar_cola(c)
    contador = 0

    while not copia_cola.empty():
        datos_paciente: tuple[int,str,str] = copia_cola.get()
        prioridad:int = datos_paciente[0]

        if 1 <= prioridad <= 3:
            contador += 1
    return contador
    
# cola_pacientes = Cola()
# cola_pacientes.put((10, "juan", "cardio"))
# cola_pacientes.put((9, "sofia", "pediatria"))
# cola_pacientes.put((3, "pedro", "neuro"))
# cola_pacientes.put((1, "marta", "cardio"))
# cola_pacientes.put((2, "luis", "trauma"))
# cola_pacientes.put((7, "ana", "cardio"))
# print(n_pacientes_urgentes2(cola_pacientes))

# Ejercicio 18
def atencion_a_clientes(c:Cola[(str,int,bool,bool)]) ->  Cola[(str, int, bool, bool)]:
    copia_cola: Cola = copiar_cola(c)
    res: Cola = Cola()

    cola_prioridad = Cola()
    cola_preferencial = Cola()
    cola_resto = Cola()

    while not copia_cola.empty():
        datos_cliente: tuple[str,int,bool,bool] = copia_cola.get()
        preferencial: bool = datos_cliente[2]
        prioridad: bool = datos_cliente[3]
        if prioridad == True:
            cola_prioridad.put(datos_cliente)
        elif preferencial == True:
            cola_preferencial.put(datos_cliente)
        else: 
            cola_resto.put(datos_cliente)

    # Si hay, ongo primero a los que tienen prioridad
    while not cola_prioridad.empty():
        res.put(cola_prioridad.get())

    # Si hay, pongo despues a los que tienen cuenta preferencial
    while not cola_preferencial.empty():
        res.put(cola_preferencial.get())

    # Pongo al resto
    while not cola_resto.empty():
        res.put(cola_resto.get()) 
    
    return res

#cola_clientes = Cola()
#cola_clientes.put(("Juan", 12345678, False, True))  # Prioridad
#cola_clientes.put(("Ana", 23456789, True, False))   # Preferencial
#cola_clientes.put(("Luis", 34567890, False, False))
#cola_clientes.put(("Maria", 45678901, True, False))  # Preferencial
#cola_clientes.put(("Carlos", 56789012, False, False))
#cola_clientes.put(("Sofia", 67890123, False, True))  # Prioridad

# cola_atencion = atencion_a_clientes(cola_clientes)

# print("Cola de atencion resultante:")
# while not cola_atencion.empty():
#     print(cola_atencion.get())

# EJERCICIOS DICCIONARIOS
# Ejercicio 19
def separar_en_palabras_sin_enter(linea: str) -> list:
    palabras = []
    palabra = ""
    for caracter in linea:
        if caracter == ' ' or caracter == '"' or caracter == '\n':
            if palabra:  # Añade solo si palabra no está vacía
                palabras.append(palabra)
                palabra = ''
        else: 
            palabra += caracter
    if palabra:  # Añadir la última palabra si no está vacía
        palabras.append(palabra)
    return palabras

def agrupar_por_longitud(nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo, "r")
    linea:str 
    diccionario: dict = dict()

    for linea in archivo:
        palabras = separar_en_palabras_sin_enter(linea)
        for palabra in palabras:
            if pertenece(len(palabra), list(diccionario.keys())):
                diccionario[len(palabra)] += 1
            else:
                diccionario[len(palabra)] = 1
    archivo.close()
    return diccionario

# print(agrupar_por_longitud("prueba.txt"))

# Ejercicio 20
def calcular_promedio_por_estudiante(nombre_archivo_notas:str) -> dict[str,float]:
    diccionario_promedios: dict[str,float] = dict()
    archivo_notas: typing.IO = open(nombre_archivo_notas,"r")
    lector_csv_notas = csv.reader(archivo_notas)
    estudiantes_cargados: list[str] = []

    for fila in lector_csv_notas:
        nro_lu = fila[0]
        if not pertenece(nro_lu,estudiantes_cargados):
            promedio:float = promedio_estudiante(nombre_archivo_notas, nro_lu)
            diccionario_promedios[nro_lu] = promedio
            estudiantes_cargados.append(nro_lu)

    archivo_notas.close()
    return diccionario_promedios

# archivo = open("notas.csv","r")
# print(calcular_promedio_por_estudiante("notas.csv"))

# Ejercicio 21
# Armo un diccionario que me diga cuantas veces aparece cada palabra y me fijo que valor es mas alto
def cantidad_de_apariciones(nombre_archivo:str) -> dict:
    diccionario_palabras: dict = dict()
    archivo: typing.IO = open(nombre_archivo,"r")
    
    for linea in archivo:
        palabras: list[str] = separar_en_palabras_sin_enter(linea)
        for palabra in palabras:
            if pertenece(palabra, list(diccionario_palabras.keys())):
                diccionario_palabras[palabra] += 1
            else:
                diccionario_palabras[palabra] = 1  

    archivo.close()
    return diccionario_palabras

# archivo = open("prueba.txt","r")
# print(cantidad_de_apariciones("prueba.txt"))

def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    diccionario_palabras:dict = cantidad_de_apariciones(nombre_archivo)
    maximo_actual:int = 0
    palabra_frecuente: str = ""

    for palabra, cantidad in diccionario_palabras.items():
        if cantidad > maximo_actual:
            maximo_actual = cantidad
            palabra_frecuente = palabra

    return palabra_frecuente

# print(la_palabra_mas_frecuente("prueba.txt"))

# Ejercicio 22
def visitar_sitio(historiales:dict[str, Pila[str]], usuario:str, sitio:str) -> None:
    if not pertenece(usuario, list(historiales.keys())):
        historiales[usuario] = Pila()
    historiales[usuario].put(sitio)


def navegar_atras(historiales:dict[str, Pila[str]], usuario:str) -> None:
    if not pertenece(usuario, list(historiales.keys())):
        print(f"El usuario {usuario} no tiene historial")

    if historiales[usuario].empty():
        print(f"No hay sitios anteriores en el historial de {usuario}")
    
    historiales[usuario].get() # Descarto el ultimo
    if not historiales[usuario].empty():
        anterior_sitio_visitado = historiales[usuario].get() # Ahora si agarro el que era el anteúltimo
        historiales[usuario].put(anterior_sitio_visitado) # Lo convierto en el ultimo para que me lo imprima
        print(f"Navegaste hacia atras a {anterior_sitio_visitado} en el historial de {usuario}")
    else:
        print(f"Es el principio del historial de navegacion de {usuario}")
        
# historiales = {}
# visitar_sitio(historiales, "user1", "instagram.com")
# visitar_sitio(historiales, "user2", "facebook.com")
# visitar_sitio(historiales, "user1", "whatsapp.com")
# pila1 = historiales["user1"]
# pila2 = historiales["user2"]
 
# print(f'Historial de user1: {pila1.queue}')
# print(f'Historial de user2: {pila2.queue}')
 
# navegar_atras(historiales, "user1")
# navegar_atras(historiales, "user2")

