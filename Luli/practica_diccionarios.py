from queue import LifoQueue as Pila

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

def copiar_diccionario(diccionario: dict[str,str]) -> dict[str,str]:
    copiar_diccionario: dict[str,str] = {}
    claves: list[str] = diccionario.keys()

    for clave in claves:
        valor: str = diccionario[clave]
        copiar_diccionario[clave] = valor
    return copiar_diccionario

def dia_menor_minima(temps: dict[int, (float, float)]) -> int:
    # temps = {dia: (min,max)}
    dia_actual: int = list(temps.keys())[0]
    minima_actual: float = temps[dia_actual][0]

    for dia, tempes in temps.items():
        min_dia: float = tempes[0]
        if min_dia < minima_actual:
            minima_actual = min_dia
            dia_actual = dia
    return dia_actual

# temps = {1:(18,57), 2:(10,42), 3:(5,34)}
# print(dia_menor_minima(temps))