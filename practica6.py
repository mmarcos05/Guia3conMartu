import math

#Ejercicio 1.1

def imprimir_hola_mundo():
    return ("Hola mundo!")

#Ejercicio 1.2

#Ejercicio 1.3

def raizDe2() -> float:
    return round(math.sqrt(2),4)

#Ejercicio 1.4

def factorial_de_dos () -> int:
    return 1*2

#Ejercicio 1.5

def perimetro():
    return 2*math.pi

#Ejercicio 2.1

def imprimir_saludo(nombre:str):
    return f"Hola {nombre}"

#Ejercicio 2.2

def raiz_cuadrada_de(x:int):
    return math.sqrt(x)

#Ejercicio 2.3

def fahrenheit_a_celsius(x:float):
    return ((x-32)*5)/9

#Ejercicio 2.4

def imprimir_dos_veces(estribillo:str):
    return f"{estribillo} \n {estribillo}"

#Ejercicio 2.5

def es_multiplo_de(n:int,m:int):
    if m%n == 0:
        return True
    else:
        return False
    
#Ejercicio 2.6

def es_par(n):
    if es_multiplo_de(2,n) == True:
        return True
    else:
        return False
    
#Ejercicio 2.7

def cantidad_de_pizzas(comensales:int,min_porciones:int):
    return math.ceil(comensales*min_porciones/8)

#Ejercicio 3.1

def alguno_es_0(n1:int,n2:int):
    return (n1 == 0) or (n2 == 0)

#Ejercicio 3.2

def ambos_son_0(n1:int,n2:int):
    return (n1 == 0) and (n2 == 0)

#Ejercicio 3.3

def es_nombre_largo(nombre:str):
    return (len(nombre) >= 3) and (len(nombre) <= 8)

#Ejercicio 3.4

def es_bisiesto(año:str):
    return (año%400 == 0) or ((año%4 == 0) and (año%100 != 0))

#Ejercicio 4

def peso_pino(metros:int):
    if metros <= 3:
        return metros*100*3
    else:
        return 3*100*3 + (metros-3)*100*2
    
def es_peso_util(peso:int) -> bool:
    return (400 <= peso) and (1000 >= peso)
    
def sirve_pino(metros:int) -> bool:
    return (400 <= peso_pino(metros)) and (1000 >= peso_pino(metros))

#Ejercicio 5.1

def devolver_el_doble_si_es_par(numero:int) -> int:
    if es_par:
        return numero*2
    else:
        return numero
#Ejercicio 5.2

def devolver__valor_si_es_par_sino_el_que_sigue(numero:int) -> int:
    if es_par:
        return numero
    else:
        return (numero+1)
    
#Ejercicio 5.3

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int):
    if (numero%9) == 0:
        return numero*3 
    
#Ejercicio 5.4

def lindo_nombre(nombre:str) -> str:
    if len(nombre) >= 5:
        return"Tu nombre tiene muchas letras"
    else:
        return"Tu nombre tiene menos de 5 caracteres"

#Ejercicio 5.5

def elRango(numero:int) -> str:
    if numero <= 5:
        return "Menor a 5"
    elif numero >= 20:
        return "Mayor a 20"
    else: 
        return "Entre 10 y 20"

#Ejercicio 5.6

def vacaciones(sexo:str, edad:int) -> str:
    if ((sexo == "F") and (18 >= edad) and (edad <= 60)) or ((sexo == "M") and (18 >= edad) and (edad <= 65)):
        return "Te toca trabajar"
    else:
        "Anda de vacaciones"
        
#Ejercicio 6







print(lindo_nombre("marcos"))

