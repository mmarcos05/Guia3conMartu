#Ejercicio 1.1

def pertenece(s:list[int], e:int) -> bool:
    i:int = 0
    while i < len(s):
        if s[i] == e:
            return True
        else:
            i += 1
    return False



#Ejercicio 1.3

def suma_total(lista:list[int]) -> int:
    y = 0
    total = 0
    while y < len(lista):
        total += lista[y]
        y += 1
    return total 



#Ejercicio 1.7

def fortaleza_contraseña(contra:str) -> str:
    if ((len(contra) > 8) and (tiene_mayuscula(contra) == True) and (tiene_minuscula(contra) == True) and (tiene_numero(contra) == True)):
        return "VERDE"
    elif len(contra) < 5:
        return "ROJO"
    else:
        return "AMARILLO"
        


def tiene_minuscula(contra):
    i = 0
    while i < len(contra):
        if (contra[i] <= "z") and (contra[i] >= "a"):
            return True
        else:
            i += 1
        
def tiene_mayuscula(contra):
    i = 0
    while i < len(contra):
        if (contra[i] <= "Z") and (contra[i] >= "A"):
            return True
        else:
            i += 1

def tiene_numero(contra):
    i = 0
    while i < len(contra):
        if ((contra[i] <= "9") and (contra[i] >= "0")):
            return True
        else:
            i += 1
#Ejercicio 2.1

def quitar_pares(lista:list[int]) -> list[int]:
    i = 0
    while i < len(lista):
        if es_par(lista[i]):
            lista.remove(lista[i])
            lista.insert(i,0)
            i += 1
        else:
            i += 1
    return lista


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

#Ejercicio 3

def aprobado(notas:list[int]) -> int:
    if notas_mayores_a_4(notas) and promedio(notas) >= 7:
        return 1
    elif notas_mayores_a_4(notas) and promedio(notas) >=4 and promedio(notas) < 7:
        return 2
    else:
        return 3

def notas_mayores_a_4(notas:list[int]) -> bool:
    i = 0
    while i < len(notas):
        if notas[i] >= 4:
            i +=1
        else:
            return False
    return True


def promedio(notas:list[int]) -> float:
    return (suma_lista(notas) / len(notas)) 

def suma_lista(numeros:list[int]) -> int:
    i = 0
    suma = 0
    while i < len(numeros):
        suma += numeros[i]
        i += 1
    return suma

print(aprobado([8,6,7,10,6]))

#Ejercicio 4.1

def nombres_estudiantes() -> list[str]:
    lista = []
    while True:
        nombre = input("ingrese el nombre del estudiante o ""LISTO"" para finalizar:")
        if nombre == "LISTO":
            return lista
        else:
            lista.append(nombre)


#Ejercicio 4.2

def sube() -> list[tuple]:
    saldo = 0
    historial = []
    while True:
        operacion = input(f"Su saldo es de {saldo} \nIngrese C para cagar creditos \nIngrese D para descontar creditos \nIngrese X para finalizar la operacion \n")
        if operacion == "C":
            carga = int(input("ingrese el monto a cargar:"))
            historial.append(("C",carga))
            saldo += carga
        elif operacion == "D":
            descontar = int(input(f"ingrese el monto a retirar, su saldo es de {saldo}\n"))
            if saldo - descontar < 0:
                print("saldo insuficiente, debe ingresar un monto mas chico")
            else:
                historial.append(("D", descontar))
                saldo -= descontar
        elif operacion == "X":
            return f"Ha finalizado su operacion, su saldo es de {saldo} \nEl historial es: {historial}"

#Ejercicio 4.3

#explicacion "in", "inout", "in and out"

# modificar (in edad:N) : N

def modificar(edad:int) -> int:
    return edad + 5

# modificar (inout edad:N)

def modificar(edad: int) -> None:
    edad += 5

# modificar (in edad:N, out: otra_edad)

def modificar(edad, otra_edad) -> None:
    otra_edad = edad + 5

#Ejercicio 5.2

def pertenece_a_cada_uno(s:list[list[int]], e:int) -> list[bool]:
    i = 0
    lista = [] 
    while i < len(s):
        if pertenece(s[i], e):
            lista.append(True)
            i += 1
        else:
            lista.append(False)
            i += 1
    return lista
        

print(pertenece_a_cada_uno([[1,34,45,65,5,3,45,2],[2,5,6],[0,16]], 5))
