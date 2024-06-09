from queue import LifoQueue as Pila
from queue import Queue as Cola

def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str) -> None:
    # historiales = {"nombre": pila}

    if not usuario in historiales.keys():
        historiales[usuario] = Pila() # si no esta, crea la pila vacia
    historiales[usuario].put(sitio) # si esta, agregalo

def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> None:

    ultimo_sitio_visitado = historiales[usuario].get()

    if not historiales[usuario].empty():
        anterior_sitio_visitado = historiales[usuario].get()
        historiales[usuario].put(anterior_sitio_visitado)
        historiales[usuario].put(ultimo_sitio_visitado)
        historiales[usuario].put(anterior_sitio_visitado)
        print(f"Navegaste hacia atras. Ahora tu historial es: {historiales[usuario].queue} y estas actualmente en: {anterior_sitio_visitado}")
    else: print(f"No hay sitios visitados anteriormente, el unico sitio que visitaste es: {ultimo_sitio_visitado}")

# historiales = {}
# visitar_sitio(historiales, "Usuario1", "google.com")
# visitar_sitio(historiales, "Usuario1", "facebook.com")
# visitar_sitio(historiales, "Usuario1", "instagram.com")
# visitar_sitio(historiales, "Usuario1", "whatsapp.com")
# visitar_sitio(historiales, "Usuario2", "youtube.com")

# pila1 = historiales["Usuario1"]
# print(f"Historial de usuario 1: {pila1.queue}")
# pila2 = historiales["Usuario2"]
# print(f"Historial de usuario 2: {pila2.queue}")

# navegar_atras(historiales, "Usuario2")

# --

def agregar_producto(inventario: dict[str,dict[str, str]], nombre: str, precio: float, cantidad:int) -> None:
    # inventario = {"nombre": {info_producto}}
    # info_producto = {"precio: precio, "cantidad":cantidad}

    info_producto: dict[str,str] = dict()
    info_producto["Precio"] = precio
    info_producto["Cantidad"] = cantidad

    inventario[nombre] = info_producto

def actualizar_stock(inventario: dict[str,dict[str, str]], nombre: str, cantidad:int) -> None:
    if nombre in inventario:
        inventario[nombre]["Cantidad"] = cantidad

def actualizar_precio(inventario: dict[str,dict[str, str]], nombre: str, precio: float) -> None:
    if nombre in inventario:
        inventario[nombre]["Precio"] = precio

def calcular_valor_inventario(inventario: dict[str,dict[str, str]]) -> float:
    suma_total: float = 0.00

    for nombre in inventario:
        plata: float = inventario[nombre]["Cantidad"] * inventario[nombre]["Precio"]
        suma_total += plata
    return suma_total

# inventario = {}
# agregar_producto(inventario, "Camisa", 20.0, 50)
# agregar_producto(inventario, "Pantalon", 30.0, 30)
# print(f"Ahora tu inventario es: {inventario}")

# actualizar_stock(inventario, "Camisa", 10)
# print(f"Actualizado el stock: {inventario}")

# actualizar_precio(inventario, "Pantalon", 70.0)
# print(f"Actualizado el precio: {inventario}")

# total = calcular_valor_inventario(inventario)
# print(f"Valor total del inventario: {total}")

# --

def copiar_diccionario(diccionario: dict[str,str]) -> dict[str,str]:
    copiar_diccionario: dict[str,str] = {}
    claves: list[str] = diccionario.keys()

    for clave in claves:
        valor: str = diccionario[clave]
        copiar_diccionario[clave] = valor
    return copiar_diccionario

# --

def dia_menor_minima(temps: dict[int, (float, float)]) -> int:
    # temps = {dia: (min,max)}
    dia_actual: int = list(temps.keys())[0]
    minima_actual: float = temps[dia_actual][0]

    for dia, tupla in temps.items():
        min_dia: float = tupla[0]
        if min_dia < minima_actual:
            minima_actual = min_dia
            dia_actual = dia
    return dia_actual

# temps = {1:(18,57), 2:(10,42), 3:(5,34)}
# print(dia_menor_minima(temps))

# --
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

# --

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

# texto = "hola como estas vos"
# print(separar_en_palabras(texto))
# print(agrupar_por_longitud(texto))

# --

# RESOLVER CON UN DICCIONARIO
def la_palabra_mas_frecuente(texto: str) -> str:
    palabras: list[str] = separar_en_palabras(texto)
    dicc: dict[str, int] = {}

    for palabra in palabras:
        if palabra in dicc.keys():
            dicc[palabra] += 1
        else:
            dicc[palabra] = 1
    print(f"Asi quedo el diccionario: {dicc}")

    palabra_mas_frec: str = ""
    mas_ap: int = 0
    for palabra, apariciones in dicc.items():
        if apariciones > mas_ap:
            mas_ap = apariciones
            palabra_mas_frec = palabra
    return palabra_mas_frec

# texto = "hola como estas hola hola chau como"
# print(la_palabra_mas_frecuente(texto))

# -- 

def contar_caracteres(texto: str) -> dict[chr,int]:
    dicc_final: dict[chr,int] = {}
    palabras: list[int] = separar_en_palabras(texto)

    for palabra in palabras:
        for char in palabra:
            if char in dicc_final.keys():
                dicc_final[char] += 1
            else:
                dicc_final[char] = 1
    return dicc_final

# texto = "hola papa y mama"
# print(contar_caracteres(texto))

# --

# SUPONGO QUE NO HAY NUMEROS REPETIDOS
def invertir_diccionario(diccionario: dict[str,int]) -> dict:
    invertido: dict[int,str] = {}

    for palabra, numero in diccionario.items():
        invertido[numero] = palabra
    return invertido

# dicc = {'hola': 3, 'como': 2,'chau': 1, 'estas': 4}
# print(invertir_diccionario(dicc))

# AHORA SI HAY NUMEROS REPETIDOS, QUE CADA VALOR DE ESA CLAVE SEA UNA LISTA DE TODAS LAS PALABRAS QUE LO TENGAN
def invertir_diccionario_con_rep(diccionario: dict[str,int]) -> dict:
    invertido: dict[int,list[str]] = {}

    for palabra, numero in diccionario.items():
        if numero in invertido:
            invertido[numero].append(palabra)
        else:
            invertido[numero] = [palabra]

    return invertido

# diccionario = {'hola': 3, 'como': 2,'chau': 1, 'estas': 2}
# print(invertir_diccionario_con_rep(diccionario)) # {3: ['hola'], 2: ['como', 'estas'], 1: ['chau']}

# --

# Escribe una función filtrar_diccionario que tome un diccionario y un valor límite, 
# y devuelva un nuevo diccionario con solo las entradas cuyos valores sean mayores que el valor límite.

def filtrar_diccionario(diccionario: dict[str, int], limite: int) -> dict:
    dicc_filtrado: dict[str,int] = {}

    for palabra, numero in diccionario.items():
        if numero > limite:
            dicc_filtrado[palabra] = numero
    return dicc_filtrado

# diccionario = {'a': 1, 'b': 3, 'c': 5, 'd': 2}
# print(filtrar_diccionario(diccionario, 2))  # {'b': 3, 'c': 5}

# -- 

def temperatura_promedio(temps: dict[int, tuple[float, float]]) -> dict:
    dicc_final: dict[int,float] = {}
    
    for dia, (min, max) in temps.items():
        promedio: float = (min + max) / 2
        dicc_final[dia] = promedio
     
    return dicc_final

# temps = {1: (18, 25), 2: (15, 22), 3: (19, 24)}
# print(temperatura_promedio(temps))  # {1: 21.5, 2: 18.5, 3: 21.5}

# --

# Implementa una función rango_temperaturas que, dado un diccionario temperaturas_diarias, devuelva un nuevo diccionario 
# con las mismas claves, pero con tuplas que indiquen la temperatura mínima y máxima alcanzada durante el periodo registrado.

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

def rango_temperaturas(temperaturas_diarias: dict[str, list[tuple[int, float]]]) -> dict[str, tuple[float, float]]:
    dicc_final: dict[str, tuple[float,float]] = {}
    lista: list[tuple[int,float]]

    for lugar, listas in temperaturas_diarias.items():
        min: float = buscar_minimo(listas)
        max: float= buscar_maximo(listas)
        dicc_final[lugar] = (min,max)

    return dicc_final

# temperaturas_diarias = {"Buenos Aires": [(1, 30.5), (15, 25.3), (31, 33.0)], "Cordoba": [(1, 28.0), (20, 29.5), (31, 27.0)]}
# print(rango_temperaturas(temperaturas_diarias)) # {"Buenos Aires": (25.3, 33.0), "Córdoba": (27.0, 29.5)}

# --

# Implementa la función ranking_ventas que, dado un diccionario ventas_diarias y una lista de productos, genere un
# diccionario con los productos como claves y la cantidad de veces que han sido vendidos en cada posición del ranking diario

def ranking_ventas(productos: list[str], ventas_diarias: dict[str, list[str]]) -> dict[str, list[int]]:
    dicc_final: dict[str, list[int]] = {}

    for producto in productos:
        dicc_final[producto] = [0]*len(productos)

    # ventas_diarias = {"dia": [orde_productos]}

    for orden_productos in ventas_diarias.values():
        for posicion in range(len(orden_productos)):
            producto = orden_productos[posicion]
            dicc_final[producto][posicion] += 1

    return dicc_final
                        
# productos = ["camisa", "pantalon", "zapatos", "gorra"]
# ventas_diarias = {
#     "dia1": ["camisa", "pantalon", "zapatos", "gorra"],
#     "dia2": ["pantalon", "zapatos", "camisa", "gorra"]
# }
# print(ranking_ventas(productos, ventas_diarias))
# {"camisa": [1, 0, 1, 0], "pantalon": [1, 1, 0, 0], "zapatos": [0, 1, 1, 0], "gorra": [0, 0, 0, 2]}

# --

# Implementa funciones para registrar una orden de compra y deshacer la última orden usando pilas.

def registrar_orden(historial: dict[str, Pila[str]], usuario: str, orden: str) -> None:
    # historial = {nombre: pila[ordenes]}

    if usuario not in historial.keys():
        historial[usuario] = Pila() # Si no esta, crea la pila vacía
    historial[usuario].put(orden) # Agrega las ordenes


def deshacer_orden(historial: dict[str, Pila[str]], usuario: str) -> str:
    
    orden_des: str = historial[usuario].get()
    return orden_des

# historial = {}
# registrar_orden(historial, "Cliente1", "Orden1")
# registrar_orden(historial, "Cliente1", "Orden2")
# registrar_orden(historial, "Cliente2", "Orden3")

# pila1: Pila = historial["Cliente1"]
# print(f"Historial de cliente 1: {pila1.queue}")

# pila2: Pila = historial["Cliente2"]
# print(f"Historial de cliente 2: {pila2.queue}")

# deshacer1: str = deshacer_orden(historial, "Cliente1")
# print(f"De cliente 1 se deshizo: {deshacer1}")  # Debería imprimir "Orden2"

# deshacer2: str = deshacer_orden(historial, "Cliente2")
# print(f"De cliente 2 se deshizo: {deshacer2}")  # Debería imprimir "Orden3"

# --

# Implementa funciones para agregar tickets de soporte y atenderlos en orden de llegada usando colas.
def agregar_ticket(cola: Cola, ticket: str) -> None:
    cola.put(ticket)

def atender_ticket(cola: Cola) -> str:
    res: str = "No hay mas tickets"

    if not cola.empty():
        return cola.get()
    return res

# cola = Cola()
# agregar_ticket(cola, "Ticket1")
# agregar_ticket(cola, "Ticket2")
# agregar_ticket(cola, "Ticket3")
# print(f"Esta es la cola: {cola.queue}")

# print(atender_ticket(cola))  # Debería imprimir "Ticket1"
# print(atender_ticket(cola))  # Debería imprimir "Ticket2"
# print(atender_ticket(cola))  # Debería imprimir "Ticket3"
# print(atender_ticket(cola))  # Debería imprimir "No hay tickets en la cola"

# --

# Implementa una función para agregar transacciones de clientes en un banco usando colas. 
# Cada cliente puede tener múltiples transacciones pendientes. 
# La función debe permitir agregar transacciones y procesarlas en el orden en que llegaron.

def agregar_transaccion(transacciones: dict[str, Cola], cliente: str, transaccion: str) -> None:
    # transacciones = {cliente, cola[transaccion]}
    if cliente not in transacciones.keys():
        transacciones[cliente] = Cola()
    transacciones[cliente].put(transaccion)

def procesar_transaccion(transacciones: dict[str, Cola], cliente: str) -> str:
    res:str = "No hay transacciones pendientes"

    if cliente not in transacciones.keys():
        return res
    
    cola = transacciones[cliente]
    if not cola.empty():
        res = cola.get()
    return res
    
# cola = Cola()
# transacciones = {}
# agregar_transaccion(transacciones, "Cliente1", "Deposito")
# agregar_transaccion(transacciones, "Cliente1", "Retiro")
# agregar_transaccion(transacciones, "Cliente2", "Consulta de saldo")

# print(procesar_transaccion(transacciones, "Cliente1"))  # Debería imprimir "Deposito"
# print(procesar_transaccion(transacciones, "Cliente1"))  # Debería imprimir "Retiro"
# print(procesar_transaccion(transacciones, "Cliente2"))  # Debería imprimir "Consulta de saldo"
# print(procesar_transaccion(transacciones, "Cliente2"))  # Debería imprimir "No hay transacciones pendientes para este cliente"

# --

# Implementa una función para gestionar la cola de impresión de diferentes usuarios en una oficina.
# Cada usuario puede enviar múltiples documentos a imprimir, que se procesarán en el orden en que llegaron.

def enviar_documento(impresiones: dict[str, Cola], usuario: str, documento: str) -> None:
    if usuario not in impresiones.keys():
        impresiones[usuario] = Cola()
    impresiones[usuario].put(documento)

def imprimir_documento(impresiones: dict[str, Cola], usuario: str) -> str:
    res: str = "No hay documentos pendientes para este usuario"

    if usuario not in impresiones.keys():
        return res
    
    cola: Cola[str] = impresiones[usuario]
    if not cola.empty():
        res = cola.get()
    return res

# impresiones = {}
# enviar_documento(impresiones, "Usuario1", "Documento1.1")
# enviar_documento(impresiones, "Usuario1", "Documento2.1")
# enviar_documento(impresiones, "Usuario2", "Documento1.2")

# print(imprimir_documento(impresiones, "Usuario1"))  # Debería imprimir "Documento1.1"
# print(imprimir_documento(impresiones, "Usuario1"))  # Debería imprimir "Documento2.1"
# print(imprimir_documento(impresiones, "Usuario4"))  # Debería imprimir "No hay documentos pendientes para este usuario"
# print(imprimir_documento(impresiones, "Usuario2"))  # Debería imprimir "Documento1.2"
# print(imprimir_documento(impresiones, "Usuario2"))  # Debería imprimir "No hay documentos pendientes para este usuario"

# -- 

# En una empresa de desarrollo de software, se gestionan varios proyectos. 
    # proyectos = {proyecto: {proyecto}}
# Cada proyecto tiene un nombre y un conjunto de tareas asociadas.    
    # proyecto = {nombre, {tareas}}
# Cada tarea tiene un estado (pendiente, en progreso, completada) y una persona asignada para realizarla.
    # tareas = {estado, persona}
# Vamos a implementar un sistema para gestionar esta información utilizando diccionarios.

def agregar_proyecto(proyectos: dict[str, dict[str, dict[str, str]]], nombre_proyecto: str) -> None:
# Añade un nuevo proyecto con un nombre dado. El valor inicial debe ser un diccionario vacío de tareas.
    if nombre_proyecto not in proyectos.keys():
        proyectos[nombre_proyecto] = {} # Creo el diccionario de proyecto

def agregar_tarea(proyectos: dict[str, dict[str, dict[str, str]]], nombre_proyecto: str, nombre_tarea: str, persona_asignada: str) -> None:
# Añade una nueva tarea a un proyecto existente. La tarea debe tener el estado inicial "pendiente" y la persona asignada.
    if nombre_proyecto in proyectos.keys():
        proyectos[nombre_proyecto][nombre_tarea] = {"Estado": "pendiente", "Persona": persona_asignada}
        
def actualizar_estado(proyectos: dict[str, dict[str, dict[str, str]]], nombre_proyecto: str, nombre_tarea: str, nuevo_estado: str) -> None:
# Actualice el estado de una tarea en un proyecto existente.
    if nombre_proyecto in proyectos.keys():
        proyectos[nombre_proyecto][nombre_tarea]["Estado"] = nuevo_estado

def eliminar_tarea(proyectos: dict[str, dict[str, dict[str, str]]], nombre_proyecto: str, nombre_tarea: str) -> None:
# Elimina una tarea de un proyecto.
    if nombre_proyecto in proyectos:
        proyectos[nombre_proyecto].pop(nombre_tarea)

def obtener_tareas_por_estado(proyectos: dict[str, dict[str, dict[str, str]]], nombre_proyecto: str, estado: str) -> list[str]:
# Devuelva una lista con los nombres de las tareas que están en un estado dado dentro de un proyecto.
    lista_final: list[str] = []
    if nombre_proyecto in proyectos:
        for nombre_tarea in proyectos[nombre_proyecto].keys():
            if proyectos[nombre_proyecto][nombre_tarea]["Estado"] == estado:
                lista_final.append(nombre_tarea)
    return lista_final


# Ejemplo de uso
# proyectos = {}

# Agregar proyectos
# agregar_proyecto(proyectos, "Proyecto A")
# agregar_proyecto(proyectos, "Proyecto B")

# Agregar tareas
# agregar_tarea(proyectos, "Proyecto A", "Tarea 1", "Alice")
# agregar_tarea(proyectos, "Proyecto A", "Tarea 2", "Bob")
# agregar_tarea(proyectos, "Proyecto B", "Tarea 1", "Charlie")
# agregar_tarea(proyectos, "Proyecto B", "Tarea 2", "Marta")

# Actualizar estado
# actualizar_estado(proyectos, "Proyecto A", "Tarea 1", "en progreso")
# actualizar_estado(proyectos, "Proyecto A", "Tarea 2", "completada")
# actualizar_estado(proyectos, "Proyecto B", "Tarea 2", "completada")

# Eliminar tarea
# eliminar_tarea(proyectos, "Proyecto B", "Tarea 1")

# Obtener tareas por estado
# tareas_pendientes = obtener_tareas_por_estado(proyectos, "Proyecto A", "pendiente")
# print("Tareas pendientes en Proyecto A:", tareas_pendientes)  # Debería imprimir: []

# tareas_en_progreso = obtener_tareas_por_estado(proyectos, "Proyecto A", "en progreso")
# print("Tareas en proceso en Proyecto A:", tareas_en_progreso)  # Debería imprimir: ['Tarea 1']

# tareas_completadas = obtener_tareas_por_estado(proyectos, "Proyecto A", "completada")
# print("Tareas completadas en Proyecto A:", tareas_completadas)  # Debería imprimir: ['Tarea 2']

# Mostrar todos los proyectos y tareas
# print("Proyectos:", proyectos)

# --

# En una biblioteca, se lleva un registro de los libros disponibles y los libros prestados. 
# Queremos implementar un sistema de gestión para manejar esta información. 
# Para esto, utilizaremos dos diccionarios: uno para los libros disponibles y otro para los libros prestados. 
# Cada entrada en estos diccionarios tendrá el nombre del libro como clave y una pila (LifoQueue) o una cola (Queue) de personas como valor.

def agregar_libro(disponibles: dict[str, Cola], nombre: str) -> None:
# Agrega un nuevo libro a la lista de libros disponibles. El libro debe ser añadido con una cola vacía.
    if nombre not in disponibles.keys():
        disponibles[nombre] = Cola() #creo la cola vacia para el nombre del libro

def prestar_libro(disponibles: dict[str, Cola], prestados: dict[str, Pila], nombre: str, persona: str) -> None:
# Mueva un libro de la lista de disponibles a la lista de prestados, añadiendo la persona que lo presta a la pila de ese libro en el diccionario de prestados.
    if (nombre in disponibles) and (not disponibles[nombre].empty()):
        disponibles[nombre].get()
        if nombre not in prestados.keys():
            prestados[nombre] = Pila() #creo la pila vacia
        prestados[nombre].put(persona) #pongo el nombre de la persona en la pila correspondiente al nombre del libro

def devolver_libro(prestados: dict[str, Pila], disponibles: dict[str, Cola], nombre: str) -> None:
# Mueva un libro de la lista de prestados a la lista de disponibles. La persona que devuelve el libro debe ser removida de la pila de ese libro en el diccionario de prestados y añadida a la cola del diccionario de disponibles
    if (nombre in prestados) and (not prestados[nombre].empty()):
        persona = prestados[nombre].get()
        if nombre not in disponibles:
            disponibles[nombre] = Cola()
        disponibles[nombre].put(persona)
        

def agregar_a_lista_de_espera(disponibles: dict[str, Cola], nombre: str, persona: str) -> None:
# Añade una persona a la lista de espera para un libro en el diccionario de disponibles.
    if nombre in disponibles.keys():
        disponibles[nombre].put(persona)

# Ejemplo de uso
# libros_disponibles = {}
# libros_prestados = {}

# Agregar libros a la biblioteca
# agregar_libro(libros_disponibles, "1984")
# agregar_libro(libros_disponibles, "El Principito")

# Agregar personas a la lista de espera
# agregar_a_lista_de_espera(libros_disponibles, "1984", "Persona1")
# agregar_a_lista_de_espera(libros_disponibles, "1984", "Persona2")

# print("\nLibros disponibles:")
# for libro, cola in libros_disponibles.items():
#     print(f"{libro}: {list(cola.queue)}")

# Prestar libro a Persona1
# prestar_libro(libros_disponibles, libros_prestados, "1984", "Persona1")

# print("\nLibros prestados:")
# for libro, pila in libros_prestados.items():
#     print(f"{libro}: {list(pila.queue)}")

# Devolver libro
# devolver_libro(libros_prestados, libros_disponibles, "1984")

# Mostrar resultados
# print("\nLista final libros disponibles:")
# for libro, cola in libros_disponibles.items():
#     print(f"{libro}: {list(cola.queue)}")

# print("\nLista final libros prestados:")
# for libro, pila in libros_prestados.items():
#     print(f"{libro}: {list(pila.queue)}")    