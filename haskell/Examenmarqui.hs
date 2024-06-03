

--PARCIAL ELECCIONES

--Ejercicio 1

porcentajeDeVotosAfirmativos :: [(String, String)] -> [Int] -> [Int] -> Float
porcentajeDeVotosAfirmativos _ _ [] = 0
porcentajeDeVotosAfirmativos (z:zs) (x:xs) (y:ys) = (division (sumaVotos (x:xs)) (sumaVotos (y:ys))) * 100


division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

sumaVotos :: [Int] -> Int
sumaVotos [] = 0
sumaVotos (x:xs) = x + sumaVotos xs

--Ejercicio 2

formulasInvalidas :: [(String, String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas ((a,b):xs)|mismoPresiyVice ((a,b):xs) || presi2Veces (a,b) xs == True = True  
                            |otherwise = formulasInvalidas xs


mismoPresiyVice :: [(String, String)] -> Bool
mismoPresiyVice [] = False
mismoPresiyVice ((a,b):xs)| a == b = True   
                          | otherwise = mismoPresiyVice xs

presi2Veces ::(String,String) -> [(String, String)] -> Bool
presi2Veces _ [] = False
presi2Veces (a,b) ((x,y):xs)|a == x || a == y || b == x || b == y = True
                            |otherwise = presi2Veces (a,b) xs

--Ejercicio 3

porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos _ [] [] = 0
porcentajeDeVotos vice ((x,y):xs) votos = (division (nEsimoVoto (iFormula 1 vice ((x,y):xs)) votos) (sumaVotos votos)) * 100

iFormula :: Int -> String -> [(String,String)] -> Int
iFormula _ _ [] = 0
iFormula i vice ((a,b):xs)|vice == b = i
                          |otherwise = iFormula (i+1) vice xs

nEsimoVoto :: Int -> [Int] -> Int
nEsimoVoto _ [] = 0
nEsimoVoto 1 (x:xs) = x
nEsimoVoto n (x:xs) = nEsimoVoto (n-1) xs

--Ejercicio 4

menosVotado :: [(String, String)] -> [Int] -> String
menosVotado [] [] = "Nadie"
menosVotado ((presi,vice):resto) votos = nEsimoPresi (iNumero 1 (menorNumero votos) votos) ((presi,vice):resto)

menorNumero :: [Int] -> Int
menorNumero [] = 0
menorNumero (x:[]) = x
menorNumero (x:y:xs)| x < y = menorNumero (x:xs)
                    | x > y = menorNumero (y:xs)
                    | x == y = menorNumero (x:xs)

iNumero :: Int -> Int -> [Int] -> Int
iNumero _ _ [] = 0
iNumero i menor (x:xs)|menor == x = i
                      |otherwise = iNumero (i+1) menor xs

nEsimoPresi :: Int -> [(String,String)] -> String
nEsimoPresi _ [] = "Nadie"
nEsimoPresi 1 ((a,b):as) = a
nEsimoPresi n ((a,b):as) = nEsimoPresi (n-1) as

--PARCIAL FUTBOL

--Ejercicio 1

atajaronSuplentes :: [(String, String)] -> [Int] -> Int -> Int
atajaronSuplentes [] [] 0 = 0
atajaronSuplentes _ goles golestotal = golestotal - (sumaGoles goles)

sumaGoles :: [Int] -> Int
sumaGoles [] = 0
sumaGoles (x:xs) = x + sumaGoles xs

--Ejercicio 2

equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos (x:xs)|repetido (x:xs) == True = False   
                     |otherwise = equiposValidos xs

repetido :: [(String, String)] -> Bool
repetido [] = False
repetido ((a,b):[])| a == b = True
                   |otherwise = False
repetido ((a,b):(x,y):xs)|a == b || a == x || a == y || b == x || b == y = True
                         |otherwise = repetido ((a,b):xs)

--Ejercicio 3

porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles _ [] [] = 0
porcentajeDeGoles arquero ((a,b):as) goles = (division (nGoles (iArquero 1 arquero ((a,b):as)) goles) (sumaGoles goles)) * 100

iArquero :: Int -> String -> [(String, String)] -> Int
iArquero _ _ [] = 0
iArquero i arquero ((x,y):xs)|arquero == y = i
                             |otherwise = iArquero (i+1) arquero xs

nGoles :: Int -> [Int] -> Int
nGoles _ [] = 0
nGoles 1 (x:xs) = x
nGoles n (x:xs) = nGoles (n-1) xs

--Parcial Goleadores

{-Goles de no goleadores [1 punto]
problema golesDeNoGoleadores (goleadoresPorEquipo: seq⟨String x String⟩,goles:seq< Z >, totalGolesTorneo: Z) : Z {
  requiere: {equiposValidos(goleadoresPorEquipo)}
  requiere: {|goleadoresPorEquipo| = |goles|}
  requiere: {Todos los elementos de goles son mayores o iguales a 0}
  requiere: {La suma de todos los elementos de goles es menor o igual a totalGolesTorneo}
  asegura: {res es la cantidad de goles convertidos en el torneo por jugadores que no son los goleadores de sus equipos}
}
2) Equipos Válidos [3 puntos]
problema equiposValidos (goleadoresPorEquipo: seq⟨String x String⟩) : Bool {
  requiere: {True}
  asegura: {(res = true) <=> goleadoresPorEquipo no contiene nombres de clubes repetidos, ni goleadores repetidos, ni jugadores con nombre de club}
}
3) Porcentaje de Goles [3 puntos]
problema porcentajeDeGoles (goleador: String, goleadoresPorEquipo: seq⟨String x String⟩,goles:seq< Z >) : R {
  requiere: {La segunda componente de algún elemento de goleadoresPorEquipo es goleador}
  requiere: {equiposValidos(goleadoresPorEquipo)}
  requiere: {|goleadoresPorEquipo| = |goles|}
  requiere: {Todos los elementos de goles son mayores o iguales a 0}
  requiere: {Hay al menos un elemento de goles mayores estricto a 0}
  asegura: {res es el porcentaje de goles que marcó goleador sobre el total de goles convertidos por goleadores}
}

Para resolver este ejercicio pueden utilizar la siguiente función que devuelve como Float la división entre dos números de tipo Int:

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)
4) Botín de Oro [3 puntos]
problema botinDeOro (goleadoresPorEquipo: seq⟨String x String⟩, goles:seq< Z >) : String {
  requiere: {equiposValidos(goleadoresPorEquipo)}
  requiere: {|goleadoresPorEquipo| = |goles|}
  requiere: {Todos los elementos de goles son mayores o iguales a 0}
  requiere: {|goles| > 0}
  asegura: {res es alguno de los goleadores de goleadoresPorEquipo que más tantos convirtió de acuerdo a goles}
}-}

--Ejercicio 1

hayQueCodificar :: Char -> [(Char, Char)] -> Bool
hayQueCodificar c [] = False
hayQueCodificar c ((a,b):as)|c == a = True
                            |otherwise = hayQueCodificar c as

--Ejercicio 2

cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char,Char)] -> Int
cuantasVecesHayQueCodificar c [] codificador = 0
cuantasVecesHayQueCodificar c (x:xs) codificador |hayQueCodificar c codificador == False = 0
                                                 |c == x = 1 + cuantasVecesHayQueCodificar c xs codificador
                                                 |otherwise = cuantasVecesHayQueCodificar c xs codificador

--Ejercicio 3

laQueMasHayQueCodificar :: [Char] -> [(Char,Char)] -> Char
laQueMasHayQueCodificar (x:xs) ((a,b):[]) = a
laQueMasHayQueCodificar (x:xs) ((a,b):(c,d):as)|(cuantasVecesHayQueCodificar a (x:xs) ((a,b):(c,d):as)) >= (cuantasVecesHayQueCodificar c (x:xs) ((a,b):(c,d):as)) = laQueMasHayQueCodificar (x:xs) ((a,b):as)
                                               |otherwise = laQueMasHayQueCodificar (x:xs) ((c,d):as)

--Ejercicio 4

codificarFrase :: [Char] -> [(Char, Char)] -> [Char]
codificarFrase [] _ = []
codificarFrase (y:ys) ((a,b):as) = cambioLetras (y:ys) ((a,b):as) : codificarFrase ys ((a,b):as)


cambioLetras :: [Char] -> [(Char,Char)] -> Char
cambioLetras (y:ys) [] = y
cambioLetras (y:ys) ((a,b):as)| y == a = b 
                              |otherwise = cambioLetras (y:ys) as


mayus :: [Char] -> Bool
mayus [] = False
mayus (x:xs) = x <= 'a' 


--Parcial Tarde

--Ejercicio 1

aproboMasDeNMaterias :: [([Char],[Int])] -> [Char] -> Int -> Bool
aproboMasDeNMaterias [] alumno n = False
aproboMasDeNMaterias ((x,y):xs) alumno n|(alumno == x) && ((calcularNotas y) > n) = True
                                        |(alumno == x) && ((calcularNotas y) <= n) = False
                                        |otherwise = aproboMasDeNMaterias xs alumno n

calcularNotas :: [Int] -> Int 
calcularNotas [] = 0
calcularNotas (x:xs)|x >= 4 = 1 + calcularNotas xs 
                    |otherwise = calcularNotas xs 

--Ejercicio 2

buenosAlumnos :: [([Char], [Int])] -> [[Char]]
buenosAlumnos [] = []
buenosAlumnos ((a,b):as)|((promedio (sumaNotas b) (cantidadNotas b)) >= 8) && ((aplazos b) == False) = a : buenosAlumnos as
                        |otherwise = buenosAlumnos as

cantidadNotas :: [Int] -> Int
cantidadNotas [] = 0
cantidadNotas (x:xs) = 1 + cantidadNotas xs

sumaNotas :: [Int] -> Int
sumaNotas [] = 0
sumaNotas (x:xs) = x + sumaNotas xs

aplazos :: [Int] -> Bool
aplazos [] = False
aplazos (x:xs)| x < 4 = True
              |otherwise = aplazos xs

promedio :: Int -> Int -> Float
promedio x y = (fromIntegral x) / (fromIntegral y)

--Ejercicio 3

mejorPromedio :: [([Char], [Int])] -> [Char]
mejorPromedio ((a,b):[]) = a
mejorPromedio ((a,b):(c,d):as)|(promedio (sumaNotas b) (cantidadNotas b)) >= (promedio (sumaNotas d) (cantidadNotas d)) = mejorPromedio ((a,b):as)
                              |otherwise = mejorPromedio ((c,d):as)

--Ejercicio 4

seGraduoConHonores :: [([Char], [Int])] -> Int -> [Char] -> Bool
seGraduoConHonores ((a,b):as) materias alumno = (aproboMasDeNMaterias ((a,b):as) alumno materias) && (pertenece (buenosAlumnos ((a,b):as)) alumno) && (((mejorPromedioConNum ((a,b):as)) - (buscarPromedio ((a,b):as) alumno)) < 1) 

pertenece :: [[Char]] -> [Char] -> Bool
pertenece [] alumno = False
pertenece (a:as) alumno|a == alumno = True
                       |otherwise = pertenece as alumno

mejorPromedioConNum :: [([Char], [Int])] -> Float
mejorPromedioConNum ((a,b):[]) = (promedio (sumaNotas b) (cantidadNotas b))
mejorPromedioConNum ((a,b):(c,d):as)|(promedio (sumaNotas b) (cantidadNotas b)) >= (promedio (sumaNotas d) (cantidadNotas d)) = mejorPromedioConNum ((a,b):as)
                                    |otherwise = mejorPromedioConNum ((c,d):as)

buscarPromedio :: [([Char], [Int])] -> [Char] -> Float
buscarPromedio [] alumno = 0
buscarPromedio ((a,b):as) alumno|a == alumno = (promedio (sumaNotas b) (cantidadNotas b))
                                |otherwise = buscarPromedio as alumno