from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
import typing

#Archivos

#Ejercicio 1.1

def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    return len(lineas)

#Ejericicio 1.2

def existe_palabra(palabra:str, nombre_archivo:str) -> bool:
    archivo = open(nombre_archivo, 'r')
    for lineas in archivo:
        if lineas.find(palabra) != -1:
            return True
    archivo.close()
    return False

#Ejercicio 1.3

def cantidad_apariciones(nombre_archivo:str, palabra:str) -> int:
    archivo = open(nombre_archivo, 'r')
    i = 0
    for lineas in archivo:
        if lineas.find(palabra) != -1:
            i += 1
    archivo.close()
    return i

#Ejercicio 2

def clonar_sin_comentarios(nombre_de_archivo:str) -> None:
    archivo: typing.IO = open(nombre_de_archivo, 'r')
    archivo_clonado: typing.IO = open("clonado.txt", 'w')
    lineas = archivo.readlines()
    for linea in lineas:
        if (not es_comentario(linea)):
            archivo_clonado.write(linea)
    archivo.close()
    archivo_clonado.close()
    
def es_comentario(linea:str) -> bool:
    i = 0
    while i < len(linea) and linea[i] == ' ':
        i +=1
    if linea[i] == '#':
        return True

#Ejercicio 3

def invertir_lineas(nombre_archivo:str):
    archivo = open(nombre_archivo, 'r')
    archivo_reverso = open("reverso.txt",'w')
    lineas = archivo.readlines()
    lineas_reverso = reverso(lineas)
    for linea in lineas_reverso:
        archivo_reverso.write(linea)
    archivo.close()

def reverso(lista):
    i = len(lista)
    reversa = []
    while i > 0:
        reversa.append(lista[i-1])
        i -= 1
    return reversa

#Ejercicio 4

def agregar_frase_al_final(nombre_archivo:str, frase:str):
    archivo_leer = open(nombre_archivo, 'r')
    archivo_leer.read()
    archivo_escribir = open(nombre_archivo, 'a')
    lineas = archivo_leer.readlines()
    for linea in lineas:
        archivo_escribir.write(linea)
    archivo_escribir.write(frase)
    archivo_leer.close()
    
#Ejercicio 5

def agregar_frase_al_principio(nombre_archivo:str, frase:str):
    archivo_leer = open(nombre_archivo, 'r')
    lineas = archivo_leer.readlines()
    archivo_escribir = open(nombre_archivo, 'w')
    archivo_escribir.write(frase + '\n')
    for linea in lineas:
        archivo_escribir.write(linea)
    archivo_leer.close()
    archivo_escribir.close()

#Ejercicio 6

#def listar_palabras_de_archivo(nombre_archivo:str) -> list:
        

#Pilas

#Ejercicio 8

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    pila = Pila()
    for _ in range(cantidad):
        pila.put(random.randint(desde, hasta))
    return pila
       
#p = generar_nros_al_azar(5,1,10)

#Ejercicio 9

def cantidad_elementos(p:Pila) -> int:
    cantidad = 0
    pila = p
    while not pila.empty():
        pila.get()
        cantidad += 1
    return cantidad

#h = Pila()

#h.put(1)
#h.put(2)
#print(cantidad_elementos(h))

#Ejercicio 10

def buscar_el_maximo(p:Pila[int]) -> int:
    pila = p
    maximo = pila.get()
    while not pila.empty():
        numero = pila.get()
        if numero > maximo:
            maximo = numero
    return maximo

#m = Pila()

#m.put(2)
#m.put(7)
#m.put(0)
#m.put(10)
#m.put(8)
#print(buscar_el_maximo(m))

#Ejercicio 11

def esta_bien_balanceada(s:str) -> bool:
    formula = s
    pila = Pila()
    
    for char in formula:
        if char == '(':
            pila.put(char)
        elif char == ')':
            if pila.empty():
                return False
            else:
                pila.get()
    return pila.empty()

#Ejercicio 12

def evaluar_expresion(s:str) -> float:
    numeros = "123456789"
    pila = Pila()
    
    for char in s:
        if char in numeros:
            pila.put(float(char))
        elif char == '+':
            numero1 = pila.get()
            numero2 = pila.get()
            nuevo_num = numero2 + numero1
            pila.put(nuevo_num)
        elif char == '-':
            numero1 = pila.get()
            numero2 = pila.get()
            nuevo_num = numero2 - numero1
            pila.put(nuevo_num)
        elif char == '*':
            numero1 = pila.get()
            numero2 = pila.get()
            nuevo_num = numero2 * numero1
            pila.put(nuevo_num)
        elif char == '/':
            numero1 = pila.get()
            numero2 = pila.get()
            nuevo_num = numero2 / numero1
            pila.put(nuevo_num)
    return pila.get()

expresion = "3 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
#print(resultado) # Deber´ıa devolver 33
    

#Ejercicio 13

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    c = Cola()
    for _ in range(cantidad):
        n = random.randint(desde, hasta)
        c.put(n)
    return c

#print(generar_nros_al_azar(3,1,5).queue)

#Ejercicio 14
def copiar_cola(c:Cola) -> Cola:
    cola1 = Cola()
    cola2 = Cola()

    while not c.empty():
        cola1.put(c.get())
    while not cola1.empty():
        cola2.put(cola1.get())
    return cola2

def cantidad_elementos_cola(c:Cola) -> int:
    cola = copiar_cola(c)
    elementos = 0
    while not cola.empty():
        cola.get()
        elementos += 1
    return elementos

c = Cola()

c.put(1)
c.put(2)
#print(cantidad_elementos_cola(c))

#Ejercicio 15

def buscar_el_maximo_cola(c:Cola) -> int:
    cola = copiar_cola(c)
    maximo = cola.get()
    while not cola.empty():
        numero = cola.get()
        if numero > maximo:
            maximo = numero
    return maximo
j = Cola()
j.put(5)
j.put(6)
j.put(3)
j.put(8)
j.put(1)
#print(buscar_el_maximo_cola(j))

#Ejercicio 16
def pertenece(lista,numero):
    i = 0
    while i < len(lista):
        if lista[i] == numero:
            return True
        else:
            i += 1

def copiar_cola(c:Cola) -> Cola:
    cola1 = Cola()
    cola2 = Cola()

    while not c.empty():
        cola1.put(c.get())
    while not cola1.empty():
        cola2.put(cola1.get())
    return cola2

def armar_secuencia_de_bingo() -> Cola[int]:
    c = Cola()
    lista_numeros = []
    while len(lista_numeros) < 100:
        i = random.randint(0,99)
        if not pertenece(lista_numeros, i):
            lista_numeros.append(i)
            c.put(i)
    return c

def jugar_carton_de_bingo(carton:list[int],bolillero: Cola[int]):
    boli = copiar_cola(bolillero)
    i = 0
    aciertos = 0
    while aciertos < len(carton):
        if pertenece(carton,boli.get()):
            aciertos += 1
            i += 1 
        else:
            i += 1
    return i 

def armar_secuencia_de_carton() -> list:
    c = []
    lista_numeros = []
    while len(c) < 12:
        i = random.randint(0,99)
        if not pertenece(lista_numeros, i):
            lista_numeros.append(i)
            c.append(i)
    return c

carton = armar_secuencia_de_carton()
bolillero = armar_secuencia_de_bingo()
#print(f"el carton es {carton}, el bolillero es {bolillero.queue} y el numero de bolas para sacar es {jugar_carton_de_bingo(carton,bolillero)}")

#Ejercicio 17

def n_pacientes_urgentes(c : Cola[(int, str, str)]) -> int:
    cola = copiar_cola(c)
    urgencias = 0
    while not cola.empty():
        paciente = cola.get()
        if paciente[0] <= 3:
            urgencias += 1
    return urgencias

p = Cola()
p.put((2,"a","a"))
p.put((1,"a","a"))
p.put((4,"a","a"))
p.put((7,"a","a"))
p.put((3,"a","a"))

#print(n_pacientes_urgentes(p))

#Ejercicio 18

def atencion_a_clientes(c : Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    fila = copiar_cola(c)
    fila_repuesto = Cola()
    fila_final = Cola()
    while not fila.empty():
        paciente = fila.get()
        if paciente[3]:
            fila_final.put(paciente)
        else:
            fila_repuesto.put(paciente)
    while not fila_repuesto.empty():
        paciente = fila_repuesto.get()
        if paciente[2]:
            fila_final.put(paciente)
        else:
            fila.put(paciente)
    while not fila.empty():
        fila_final.put(fila.get())
    return fila_final

cola_clientes = Cola()
cola_clientes.put(("Juan", 12345678, False, True))  # Prioridad
cola_clientes.put(("Ana", 23456789, True, False))   # Preferencial
cola_clientes.put(("Luis", 34567890, False, False))
cola_clientes.put(("Maria", 45678901, True, False))  # Preferencial
cola_clientes.put(("Carlos", 56789012, False, False))
cola_clientes.put(("Sofia", 67890123, False, True))  # Prioridad

res = (atencion_a_clientes(cola_clientes))
#print(res.queue)

#Ejercicio 19

#funciones utiles para separar en palabras
def palabras_de_archivo(nombre_de_archivo):
    with open(nombre_de_archivo, 'r') as archivo:
        contenido = archivo.read()

        return mi_split(contenido)

def mi_split(linea):
    res = []
    palabra = ""
    for char in linea:
        if char == " " or char == "\t" or char == "\n" or char == "\r":
            if len(palabra) > 0:
                res.append(palabra)
                palabra = ""
        else:
            palabra += char
    return res
    
def pertenece_dicts(d:dict, k) -> bool:
    lista = list(d.keys())
    for e in lista:
        if e == k:
            return True
    return False

def agrupar_por_letras(nombre_de_archivo:str) -> dict:
    archivo = open(nombre_de_archivo, "r")
    contenido : list[str] = archivo.read()
    palabras = mi_split(contenido)
    print(palabras)
    res: dict = {}

    for p in palabras:
        t = len(p)
        if pertenece_dicts(res, t):
            res[t] += 1
        else:
            res[t] = 1
    return res


#print(agrupar_por_letras("pepe.txt")) 

#Ejercicio 21

def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    archivo = open(nombre_archivo,'r')
    contenido = archivo.read()
    palabras = mi_split(contenido)
    palabras_dict = {}
    for palabra in palabras:
        if palabra in palabras_dict:
            palabras_dict[palabra] += 1
        else:
            palabras_dict[palabra] = 1
    maximo = 0
    palabra = ""
    for palabra_mayor,cantidad in palabras_dict.items():
        if cantidad > maximo:
            palabra = palabra_mayor
    return palabra

#print(la_palabra_mas_frecuente("marcos.txt"))

#Ejercicio 22

historiales: dict[str,Pila[str]] = {}

def visitar_sitio(historiales:dict[str,Pila[str]],usuario:str,sitio:str) -> None:
    user = usuario
    web = sitio
    if not user in historiales:
        historiales[user] = Pila()
    historiales[user].put(web)
    
def invertir_pila(pila:Pila) -> Pila:
    pAux = Pila()
    while not pila.empty():
        pAux.put(pila.get())
    return pAux

m = Pila()
m.put(1)
m.put(2)
m.put(3)
m.put(4)

u = (invertir_pila(m))
#print(u.queue)

def navegar_atras(historiales:dict[str,Pila[str]], usuario:str) -> None:
    user = usuario
    ultimo_sitio = historiales[user].get()
    #print(f"Sitio actual de {usuario}: {ultimo_sitio}")
    nueva_pila = invertir_pila(historiales[user])
    #print(f"Pila invertida después de extraer el sitio actual de {usuario}: {list(nueva_pila.queue)}")
    nueva_pila.put(ultimo_sitio)
    #print(f"Pila invertida después de agregar el sitio actual al final de {usuario}: {list(nueva_pila.queue)}")
    historiales[user] = invertir_pila(nueva_pila)
    #print(f"Pila final del historial del usuario {usuario}: {list(historiales[usuario].queue)}")
    
    


#visitar_sitio(historiales, "user1", "instagram.com")
#visitar_sitio(historiales, "user2", "facebook.com")
#visitar_sitio(historiales, "user1", "whatsapp.com")
#pila1 = historiales["user1"]
#pila2 = historiales["user2"]
 
#print(f'Historial de user1: {pila1.queue}')
#print(f'Historial de user2: {pila2.queue}')
 
#navegar_atras(historiales, "user1")
#navegar_atras(historiales, "user2")
#pila1 = historiales["user1"]
#pila2 = historiales["user2"]
#print(f'Historial de user1: {pila1.queue}')
#print(f'Historial de user2: {pila2.queue}')

#Ejercicio 23

inventario = {}

def agregar_producto(inventario:dict[str,dict[str,str]],nombre:str,precio:str,cantidad:str):
    inventario[nombre] = {"precio":precio,"cantidad":cantidad}

def actualizar_stock(inventario:dict[str,dict[str,str]],nombre:str,cantidad:str):
    info = inventario[nombre]
    info["cantidad"] = cantidad
    inventario[nombre] = info

def actualizar_precios(inventario:dict[str,dict[str,str]],nombre:str,precio:str):
    info = inventario[nombre]
    info["precio"] = precio
    inventario[nombre] = info
    
def calcular_valor_inventario(inventario:dict[str,dict[str,str]]) -> float:
    copia = inventario
    valor_inventario = 0
    for nombre,productos in copia.items():
        valor_prod = productos["precio"] * productos["cantidad"]
        valor_inventario += valor_prod
    return valor_inventario
            
    
agregar_producto(inventario,"remera",1000,4)
agregar_producto(inventario,"gorra",500,4)

#print(inventario)

actualizar_stock(inventario,"remera",2)

#print(inventario)

print(calcular_valor_inventario(inventario))