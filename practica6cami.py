import math

def imprimir_saludo() -> None:
    saludo: str = "Hola como están?"
    print(saludo)

def devolver_saludo() -> str:
   saludo:str = "Hola como estan?"
   return saludo

print(devolver_saludo())
imprimir_saludo()

#Ejercicio 1
def imprimir_hola_mundo() :
  return ("Hola Mundo")

#Ejercicio 1.5
def perimetro() -> float :
   return 2*math.pi
   
print (perimetro())

def perimetro2() -> None:
   print (2*math.pi) #solo lo imprime, como no me lo devuelve no lo puedo usar con otra cosa

#Ejercicio 2.5
def es_multiplo_de(n:int, m:int) -> bool:
   elresto: int = n % m 
   resultado: bool
   if (elresto == 0): 
      resultado = True
   else: 
      resultado = False
   return resultado

print(es_multiplo_de(2,4))

#Ejercicio 3.3
def es_nombre_largo (nombre: str) -> bool:
    longitud: int = len(nombre)
    condicion: bool = longitud >= 3 and longitud <= 8
    resultado: bool = False
    if (condicion == True):
      resultado = True
    return resultado
 
print(es_nombre_largo("camila"))

#Ejercicio 5.1
def devolver_el_doble_si_es_par (numero: int) -> int:
   doble: int = numero * 2
   condicion: bool = numero % 2 == 0
   resultado: int
   if (condicion == True):
      resultado = doble
   else:
      resultado = numero
   return resultado

print(devolver_el_doble_si_es_par(4))