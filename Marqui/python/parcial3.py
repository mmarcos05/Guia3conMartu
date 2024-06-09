def ind_nesima_aparicion(s:list[int],n:int,elem:int) -> int:
    i = 0
    contador = 0
    while i < len(s):
        if s[i] == elem:
            contador += 1
            if contador == n:
                return i
        i += 1
    return -1

s = [-1, 1, 1, 5, -7, 1, 3]
n = 2
elem = 1

#print(ind_nesima_aparicion(s,n,elem))

def mezclar(s1:list[int],s2:list[int]) -> list[int]:
    lista1 = s1
    lista2 = s2
    res = []
    i = 0
    while i < len(lista1):
        res.append(lista1[i])
        res.append(lista2[i])
        i += 1
    return res

s1 = [1, 3, 0, 1]
s2 = [4, 0, 2, 3]
#print(mezclar(s1,s2))

def frecuencia_posiciones_por_caballo(caballos:list[str],carreras:dict[str,list[str]]) -> dict[str,dict[int]]:
    icaballo = 0
    i = 0
    apariciones = 0
    res = {}
    lista_posiciones = []
    while icaballo < len(caballos):
        caballo = caballos[icaballo]
        while i < len(caballos):
            for carrera, posiciones in carreras.items():
                if posiciones[i] == caballo:
                    apariciones += 1
            i += 1
            lista_posiciones.append(apariciones)
            apariciones = 0
        res[caballo] = lista_posiciones
        icaballo += 1
        i = 0
        lista_posiciones = []
    return res

caballos= ["linda", "petisa", "mister", "luck" ]
carreras= {"carrera1":["linda", "petisa", "mister", "luck"],
                  "carrera2":["petisa", "mister", "linda", "luck"]}

#print(frecuencia_posiciones_por_caballo(caballos,carreras))

def matriz_capicua(m:list[list[int]]) -> bool:
    matriz = m
    for fila in matriz:
        if lista_capicua(fila) == False:
            return False
    return True

def lista_capicua(lista:list[int]) -> bool:
    i = 0
    while i < len(lista):
        if lista[i] != lista[len(lista) - 1 - i]:
            return False
        i += 1
    return True

m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
print(matriz_capicua(m))

        
            