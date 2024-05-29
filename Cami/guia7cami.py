import math as mt
from typing import List, Tuple

#EJERCICIO 1.1

def pertenece(lista:List[int], numero:int) -> bool:
    condicion:bool = True
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if lista[i] == numero:
            return condicion
        else:
            i += 1
    return False

print(pertenece([1,2,3,4],5))

#EJERCICIO 1.2

def divide_a_todos_(lista:List[int], e:int) -> bool:
    i:int = 0
    res:bool = False
    longitud = len(lista)
    for i in range (longitud):
        if (lista[i] % e != 0):
            return False
    return True

print(divide_a_todos_([2,4,6,7,10], 2))

#EJERCICIO 1.3

def suma_total(lista:List[int]) -> int:
    longitud:int = len(lista)
    i:int = 0
    total:int = 0
    while(longitud>i):
        total += lista[i]
        i+=1
    return total

print(suma_total([1,2,3,4]))

#EJERCICIO 1.4

"""def ordenados(lista:List[int]) -> bool:
    longitud:int = len(lista)
    i:int = 0
    while((longitud-1)>i):
        if (lista[i] > lista[i+1]):
            return False
        else:
            i+=1
    return True"""

def ordenados(lista:List[int]) -> bool:
    longitud:int = len(lista)
    i:int = 0
    for i in range (longitud-1):
        if (lista[i] > lista[i+1]):
            return False
    return True

print(ordenados([1,2,5,4]))

#EJERCICIO 1.6

def reversa(texto:str) -> str:
    longitud:int = len(texto)
    i:int = longitud-1
    reverso:str = ""
    while (i>=0):
        reverso += texto[i]
        i -= 1
    return reverso

def es_palindromo(texto:str) -> bool:
    if (texto == reversa(texto)):
        return True
    else:
        return False

print(es_palindromo("neuquen"))


#EJERCICIO 1.7

def tiene_minuscula(contraseña:str) -> bool:
    longitud:int = len(contraseña)
    i:int = 0
    while i < longitud:
        if (contraseña[i] >= "a") and (contraseña[i] <= "z"):
            return True
        else:
            i += 1
    return False

print(tiene_minuscula("HOLA"))

def tiene_mayuscula(contraseña:str) -> bool:
    longitud:int = len(contraseña)
    i:int = 0
    while i < longitud:
        if (contraseña[i] >= "A") and (contraseña[i] <= "Z"):
            return True
        else:
            i += 1
    return False

print(tiene_mayuscula("la"))

def tiene_num(contraseña:str) -> bool:
    longitud:int = len(contraseña)
    i:int = 0
    while i < longitud:
        if (contraseña[i] >= "0") and (contraseña[i] <= "9"):
            return True
        else:
            i += 1
    return False

print(tiene_num("las"))

def fortaleza(contraseña:str) -> str:
    longitud:int = len(contraseña)
    i:int = 0
    while i < longitud:
        if (longitud > 8) and (tiene_minuscula(contraseña) == True) and (tiene_mayuscula(contraseña) == True) and (tiene_num(contraseña) == True):
            return "VERDE"
        elif longitud < 5:
            return "ROJA"
        else:
            return "AMARILLA"
        
print(fortaleza("hola"))

#EJERCICIO 1.8

def cuenta_bancaria(lista:List[Tuple[chr, float]]) -> float:
    i:int = 0
    longitud:int = len(lista)
    saldo_actual = 0
    while i< longitud:
        if lista[i][0] == "I":
            saldo_actual += lista[i][1]
            i+=1
        else:
            saldo_actual -= lista[i][1]
            i+=1
    return saldo_actual

print(cuenta_bancaria([('I', 2000), ('R', 20), ('R', 1000), ('I', 300)]))


#EJERCICIO 2.1
#si el NÚMERO es par
def es_par(numero:int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

def borra_pares(lista:List[int]) -> List[int]:
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if es_par(lista[i]) == True:
            lista.remove(lista[i])
            lista.insert(i,0)
            i += 1
        else:
            i += 1
    return lista

print(borra_pares([1,2,3,4,5,6,7]))

#si la POSICIÓN es par
def reemplaza_pares(lista:List[int]) -> None:
    i:int = 0
    longitud:int = len(lista)
    while i<longitud:
        if (es_par(i)):
            lista[i] = 0
        i += 1

s = [2,4,5,6,3,3]
print (f"antes: {s}")
reemplaza_pares(s)
print(f"remplaza_pares: {s}")


#EJERCICIO 2.2
def borra_pares_2(lista:List[int]) -> List[int]:
    i:int = 0
    longitud:int = len(lista)
    nueva_lista:List[int] = []
    while i < longitud:
        if es_par(lista[i]) == True:
            nueva_lista.insert(i,0)
            i += 1
        else:
            nueva_lista.insert(i,lista[i])
            i += 1
    return nueva_lista

print(borra_pares_2([1,2,3,4,5,6,7]))

#EJERCICIO 2.3

def pertenece_chr(lista:List[chr], letra:chr) -> bool:
    condicion:bool = True
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if lista[i] == letra:
            return condicion
        else:
            i += 1
    return False

def borra_vocales(lista:List[chr]) -> List[chr]:
    i:int = 0
    longitud:int = len(lista)
    vocales:List[chr] = ['a','e','i','o','u','A','E','I','O','U']
    while i < longitud:
        if pertenece_chr(vocales, lista[i]):
            lista.remove(lista[i])
            longitud -=1
            i+=1
        else:
            i+=1
    return lista

print(borra_vocales(['h','O','l','a','m','U','n','d','o']))

#EJERCICIO 2.4
def reemplaza_vocales(palabra:List[chr]) -> List[chr]:
    i:int = 0
    longitud:int = len(palabra)
    vocales:List[chr] = ['a','e','i','o','u']
    while i < longitud:
        if pertenece_chr(vocales, palabra[i]):
            palabra.remove(palabra[i])
            palabra.insert(i,'_')
            i+=1
        else:
            i+=1
    return palabra

print(reemplaza_vocales(['h','o','l','a','m','u','n','d','o']))

#EJERCICIO 2.5 --> igual a la función reversa

#EJERCICIO 2.6

def eliminar_repetidos(palabra:List[chr]) -> List[chr]:
    i:int = 0
    longitud:int = len(palabra)
    palabra_nueva:str = ""
    while i < longitud:
        if not pertenece(palabra_nueva, palabra[i]):
            palabra_nueva += palabra[i]
            i+=1
        else:
            i+=1
    return palabra_nueva

print(eliminar_repetidos(['h','h','h','a','m','u','n','d','a']))

#EJERCICIO 3

def promedio(notas:List[int]) -> int:
    i:int = 0
    total = 0
    longitud:int = len(notas)
    for i in range (longitud):
        total += notas[i]
    return (total / longitud)

def mayor_igual(notas:List[int], numero:int) -> bool:
    i:int = 0
    longitud:int = len(notas)
    for i in range (longitud):
        if 4>notas[i]:
            return False
    return True

def aprobado(notas:List[int]) -> int:
    i:int = 0
    res:int = 0
    longitud:int = len(notas)
    while i < longitud:
        if (promedio(notas)>=7) and (mayor_igual((notas), 4) == True):
            return res + 1
        elif (7>promedio(notas)>=4) and (mayor_igual((notas), 4) == True):
            return res + 2
        else:
            return res + 3
        
print(aprobado([1,2,3]))

#EJERCICIO 4.1
def nombres_estudiantes() -> List[str]:
    lista_alumnos:List[str] = []
    nombre:str = str(input('Ingrese el nombre de alumno: '))
    while nombre != "listo":
        lista_alumnos.append(nombre)
        nombre:str = str(input('Ingrese el nombre de alumno: '))
    return lista_alumnos

print(nombres_estudiantes())

#EJERCICIO 4.2
"""def sube() -> List[tuple]:
    monedero:int = 0
    opciones:str = input(f"Por favor, seleccione una de las siguientes opciones: \nC = Cargar créditos \nD = Descontar créditos \n X = Finalizar")
    while opciones != "X":
        cargar_monto:int = int(input(f"Por favor, establezca el monto deseado para realizar la operación: "))
        if opciones == "C":"""

#EJERCICIO 5.2

def pertenece_a_cada_uno_version_2(lista:List[List[int]], e:int) -> List[bool]:
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if pertenece(lista[i], e) == True:
            lista.remove(lista[i])
            lista.insert(i, True)
            i += 1
        else:
            lista.remove(lista[i])
            lista.insert(i, False)
            i += 1
    return lista

print(pertenece_a_cada_uno_version_2([[1,2], [3,4,5,1], [6,7,8]], 1))

def pertenece_a_cada_uno_profe(s:List[List[int]], e:int, res:List[bool]) -> None:
    res.clear()
    for v in s:
        if pertenece(v,e):
            res.append(True)
        else:
            res.append(False)



resultados: List[bool] = []
pertenece_a_cada_uno_profe([[1,2], [3,4,5,1], [6,7,8]], 1, resultados)
print(resultados)
