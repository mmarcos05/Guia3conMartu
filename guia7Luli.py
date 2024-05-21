# Ejercicio 1.1
def pertenece(s:list[int], e:int) -> bool:
    condicion: bool = True
    indice: int = 0
    while indice < len(s): 
        if s[indice] == e:
            return condicion
        else:
            indice += 1
    return False 

# Ejercicio 1.3
def suma_total(lista:list[int]) -> int:
    total: int = 0
    indice: int = 0
    longitud: int = len(lista)
    while indice < longitud:
        total += lista[indice]
        indice += 1
    return total

# Ejercicio 1.7
def fortaleza(contraseña:str) -> str:
   indice: int = 0
   while indice < len(contraseña):
       if (len(contraseña) > 8) and (tiene_minus(contraseña) == True) and (tiene_mayus(contraseña) == True) and (tiene_num(contraseña) == True):
           return "VERDE"
       elif (len(contraseña) < 5):
           return "ROJA"
       else:
           return "AMARILLA"
       
def tiene_minus(contraseña:str) -> bool:
    indice: int = 0
    condicion: bool = True
    while indice < len (contraseña):
        if (contraseña[indice] >= "a") and (contraseña[indice] <= "z"):
            return condicion
        else:
            indice += 1
    return False

def tiene_mayus(contraseña:str) -> bool:
    indice: int = 0
    condicion: bool = True
    while indice < len (contraseña):
        if (contraseña[indice] >= "A") and (contraseña[indice] <= "Z"):
            return condicion
        else:
            indice += 1
    return False

def tiene_num(contraseña:str) -> bool:
    indice: int = 0
    condicion: bool = True
    while indice < len (contraseña):
        if (contraseña[indice] >= "0") and (contraseña[indice] <= "9"):
            return condicion
        else:
            indice += 1
    return False

# Ejercicio 2.1
def es_par(numero:int) -> bool:
    if numero % 2 == 0:
        return True
    else: 
        return False

def borra_pares(lista:list[int]) -> list[int]:
    indice: int = 0
    while indice < len (lista):
        if (es_par (lista[indice]) == True): 
            lista.remove(lista[indice])
            lista.insert(indice, 0)
            indice += 1
        else: 
            indice += 1
    return lista

# Ejercicio 5.2
def pertenece_a_cada_uno(s:list[list[int]], e:int) -> list[bool]:
    indice: int = 0
    while indice < len(s):
        if (pertenece (s[indice],e)):
            s.remove(s[indice])
            s.insert(indice,True)
            indice += 1
        else: 
           s.remove(s[indice])
           s.insert(indice,False) 
           indice += 1
    return s 

print (pertenece_a_cada_uno([[5,2,3],[4,5,6],[7,5,9]],5))
