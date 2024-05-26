import math
# Así se hace un comentario en python

# Ejercicio 1.1
def imprimir_saludo() -> None:
    saludo: str = "Hola Mundo" 
    print (saludo)
# imprimir_saludo()

def devolver_saludo() -> str:
    saludo: str = "Hola Mundo" 
    return saludo
# print(devolver_saludo())

# Ejercicio 1.2
def imprimir_un_verso() -> None:
    verso: str = "Dale a tu cuerpo alegria Macarena,\nQue tu cuerpo es pa darle alegria y cosa buena,\nDale a tu cuerpo alegria Macarena,\nHey,Macarena!"
    print (verso)

# Ejercicio 1.3
def raizDe2() -> float:
    raiz: float = math.sqrt(2)
    redondeo: float = round(raiz,4)
    return redondeo

# Ejercicio 1.4
def factorial_de_dos() -> int:
    factorial: int = math.factorial (2)
    return factorial 

# Ejercicio 1.5
def perimetro() -> float:
    return 2 * math.pi
# Asi se llama a esta funcion -> print (perimetro())

def perimetro2() -> None:
    print (2 * math.pi) #solo lo imprime, como no me lo devuelve no lo puedo usar con otra cosa
# Asi se llama a esta funcion -> perimetro2()

# Ejercicio 2.1
def imprimir_saludo_nombre(nombre:str) -> str:
    print ("Hola " + nombre)

# Ejercicio 2.2
def raiz_cuadrada_de(numero:int) -> float:
    raiz: float = math.sqrt(numero)
    return raiz

#Ejercicio 2.3
def farenheit_a_celcius(t:float) -> float:
    convertir: float = (((t - 32)*5)/9)
    return convertir

# Ejercicio 2.4
def imprimir_dos_veces(estribillo:str) -> None:
    print (estribillo * 2) 

# Ejercicio 2.5
def es_multiplo_de(n:int,m:int) -> bool:
    elresto: int = n % m
    resultado: bool
    if (elresto == 0):
        resultado = True
    else:
        resultado = False
    return resultado

# Ejercicio 2.6
def es_par(numero:int) -> bool:
    esMultDeDos: bool = (es_multiplo_de(numero,2))
    resultado: bool
    if (esMultDeDos == True):
        resultado = True
    else:
        resultado = False
    return resultado

# Ejercicio 2.7
def cantidad_de_pizzas(gente:int,cantMinPorPer:int) -> int:
    cuenta:int = math.ceil((gente * cantMinPorPer)/8)
    return cuenta

# Ejercicio 3.1
def alguno_es_0(n1:int , n2:int) -> bool:
    condicion: bool
    if (n1 == 0) or (n2 == 0):
        condicion = True
    else:
        condicion = False
    return condicion

# Ejercicio 3.2
def ambos_son_0(n1:int , n2:int) -> bool:
    condicion: bool
    if (n1 == 0) and (n2 == 0):
        condicion = True
    else:
        condicion = False
    return condicion

# Ejercicio 3.3
def es_nombre_largo(nombre:str) -> bool:
    longitud: int = len(nombre)
    condicion: bool = longitud >= 3 and longitud <= 8 
    resultado: bool 
    if (condicion == True):
        resultado = True
    else:
        resultado = False
    return resultado 

# Ejercicio 3.4
def es_bisiesto(año:int) -> bool:
    return es_multiplo_de(año, 400) or ((es_multiplo_de(año, 4)) and not(es_multiplo_de(año, 100)))

# Ejercicio 4.1
def peso_pino(altura_en_cm: int) -> int:
    return min (altura_en_cm,300) * 3 + max (altura_en_cm - 300, 0) * 2

# Ejercicio 4.2
def es_peso_util(peso:int) -> bool:
    resultado: bool
    if (peso <= 1000 and peso >= 400):
        resultado = True
    else:
        resultado = False
    return resultado

# Ejercicio 4.3/4.4
def sirve_pino(altura_en_cm:int) -> bool:
    return (es_peso_util(peso_pino(altura_en_cm)))

# Ejercicio 5.1
def devolver_el_doble_si_es_par(numero:int) -> int:
    doble: int = numero * 2
    condicion: bool = numero % 2 == 0
    resultado: int
    if (condicion == True):
        resultado = doble
    else: 
        resultado = numero
    return resultado

# Ejercicio 5.2
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int:
    siguiente:int = numero + 1
    if (es_par(numero) == True):
        return numero
    else:
        return siguiente

# Ejercicio 5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int:
    if (es_multiplo_de (numero,3) == True):
        return numero*2
    elif (es_multiplo_de (numero,9) == True):
        return numero*3
    else:
        return numero

# Ejercicio 5.4
def lindo_nombre(nombre:str) -> str:
    if len(nombre) >= 5:
        print ("Tu nombre tiene muchas letras!")
    else:
        print ("Tu nombre tiene menos de 5 caracteres")

# Ejercicio 5.5
def elRango(numero:int) -> str:
    if numero < 5:
        print ("Menor a 5")
    else:
        if (numero >= 10) and (numero < 20):
            print ("Entre 10 y 20")
        else: 
            if (numero > 20):
                print ("Mayor a 20")

# Ejercicio 5.6
def vacaciones_o_trabajo(sexo:chr,edad:int) -> str:
    if (edad < 18) or (edad >= 65) or (edad >= 60 and sexo == 'F'):
        print ("Anda de vacaciones")
    else:
        print ("Te toca trabajar")

