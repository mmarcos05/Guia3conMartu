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