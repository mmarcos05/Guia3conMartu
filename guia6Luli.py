import math

# comentario 

# Ejercicio 1.1
def imprimir_saludo() -> None:
    saludo: str = "Hola Mundo" 
    print (saludo)

imprimir_saludo()

def devolver_saludo() -> str:
    saludo: str = "Hola Mundo" 
    return saludo

print(devolver_saludo())

# Ejercicio 1.5
def perimetro() -> float:
    return 2 * math.pi

print (perimetro())

def perimetro2() -> None:
    print (2 * math.pi) #solo lo imprime, como no me lo devuelve no lo puedo usar con otra cosa

perimetro2()

# Ejercicio 2.5
def es_multiplo_de(n:int,m:int) -> bool:
    elresto: int = n % m
    resultado: bool
    if (elresto == 0):
        resultado = True
    else:
        resultado = False
    return resultado

print (es_multiplo_de(6,2))

#Ejercicio 3.3
def es_nombre_largo(nombre:str) -> bool:
    longitud: int = len(nombre)
    condicion: bool = longitud >= 3 and longitud <= 8 
    resultado: bool 
    if (condicion == True):
        resultado = True
    else:
        resultado = False
    return resultado 

print (es_nombre_largo("francisco"))

