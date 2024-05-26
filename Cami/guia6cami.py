import math

def imprimir_saludo() -> None:
    saludo: str = "Hola como están?"
    print(saludo)

def devolver_saludo() -> str:
   saludo:str = "Hola como estan?"
   return saludo

print(devolver_saludo())
imprimir_saludo()

#EJERCICIO 1
def imprimir_hola_mundo() :
  return ("Hola Mundo")

#EJERCICIO 1.4
def factorial_de_dos() -> int:
   factorial:int = 1*2
   return factorial

print(factorial_de_dos())


#EJERCICIO 1.5
def perimetro() -> float :
   return 2*math.pi
   
print (perimetro())

def perimetro2() -> None:
   print (2*math.pi) #solo lo imprime, como no me lo devuelve no lo puedo usar con otra cosa

#EJERCICIO 2.2
def raiz_cuadrada_de(numero:float) -> float:
   return math.sqrt(numero)

print(raiz_cuadrada_de(49))

#EJERCICIO 2.5
def es_multiplo_de(n:int, m:int) -> bool:
   elresto: int = n % m 
   resultado: bool
   if (elresto == 0): 
      resultado = True
   else: 
      resultado = False
   return resultado

print(es_multiplo_de(2,4))

#EJERCICIO 3.3
def es_nombre_largo (nombre: str) -> bool:
    longitud: int = len(nombre)
    condicion: bool = longitud >= 3 and longitud <= 8
    resultado: bool = False
    if (condicion == True):
      resultado = True
    return resultado
 
print(es_nombre_largo("camila"))

#EJERCICIO 5.1
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

#EJERCICIO 6.2
def es_par(numero:int) -> bool:
   condicion:bool = numero % 2 == 0
   res:bool = False
   if (condicion == True):
      res = True
   return res

def numeros_pares() -> int:
   i:int = 10
   while (i>=10 and 40>i):
      if (es_par(i) == True):
         print(i)
         i+=1
      else:
         i+=1
   return print(i)

print(numeros_pares())

def numeros_pares_2() -> int:
   i:int = 10
   for i in range (10, 40, 1):
      if (es_par(i) == True):
         print(i)
         i+=1
      else:
         i+=1
         
   return print(i)

print(numeros_pares_2())

#EJERCICIO 6.4
def despegue(numero:int) -> None:
   i = numero
   while(i>=1):
      print(i)
      i-=1
   return print("Despegue")

print(despegue(10))

#EJERCICIO 7
def despegue_2(numero:int) -> None:
   for numero in range (numero, 0, (-1)):
      print(numero)
   return print("Despegue")

print(despegue_2(10))