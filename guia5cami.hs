--concatenación es haskell en vez de :: es ++
--EJERCICIO 1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

--EJERCICIO 1.2
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

--EJERCICIO 1.3
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

--EJERCICIO 1.4
reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = ultimo (x:xs) : (reverso(principio (x:xs)))

--EJERCICIO 2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _[] = False
pertenece x (y:ys) |x == y = True
                   |otherwise = pertenece x ys
                   
--EJERCICIO 2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = False
todosIguales [x] = True
todosIguales (x:y:ys) = x == y && todosIguales (y:ys)

--EJERCICIO 2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = False
todosDistintos [x] = True
todosDistintos (x:y:ys) = x /= y && todosDistintos (y:ys)

--EJERCICIO 2.4
--hayRepetidos :: (Eq t) => [t] -> Bool
--hayRepetidos [] = False
--hayRepetidos (x:xs)| pertenece x xs = True
           --        | otherwise = hayRepetidos xs

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [x] = False
hayRepetidos (x:y:ys) |x == y || hayRepetidos (x:ys) = True
                      |otherwise = hayRepetidos (y:ys)

--EJERCICIO 2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y:ys) | x == y = ys
                | otherwise = y : quitar x ys

--EJERCICIO 2.6
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys) |x == y = quitarTodos x ys
                     |otherwise = y : quitarTodos x ys

--EJERCICIO 2.7
eliminarRepetidos :: (Eq t) => [t] -> [t] 
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos(quitarTodos x xs)

--EJERCICIO 2.8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos (x:xs) (y:ys) = todosPertenecen (x:xs) (y:ys) && todosPertenecen (y:ys) (x:xs)

todosPertenecen :: (Eq t) => [t] -> [t] -> Bool
todosPertenecen [] _ = True
todosPertenecen (x:xs) (y:ys) = pertenece x (y:ys) && todosPertenecen xs (y:ys)

--EJERCICIO 3.3
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:ys) |x > y = maximo (x:ys)
                |y > x = maximo (y:ys)
                |otherwise = maximo (x:ys)

--EJERCICIO 3.9 
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:y:ys) = minimo (x:y:ys) : ordenar (quitar (minimo (x:y:ys)) (x:y:ys))

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:y:ys) |x < y = minimo (x:ys)
                |y < x = minimo (y:ys)
                |otherwise = minimo (x:ys)

--EJERCICIO 3.1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

--EJERCICIO 3.2
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x*productoria xs

--EJERCICIO 3.3
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = n + x : sumarN n xs

--EJERCICIO 3.5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

--EJERCICIO 3.6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

--EJERCICIO 4.1
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [a] = [a]
sacarBlancosRepetidos (a:b:bs) |a == ' ' && b == ' ' = sacarBlancosRepetidos (a:bs)
                               |otherwise = a : sacarBlancosRepetidos (b:bs)

--EJERCICIO 4.2
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras [a] = 1
contarPalabras (a:b:bs)|a /= ' ' && b == ' ' = 1 + contarPalabras((sacarEspacioFinal(sacarBlancosRepetidos (b:bs))))
                       |otherwise = contarPalabras(sacarEspacioFinal(sacarBlancosRepetidos(b:bs)))

sacarEspacioFinal :: [Char] -> [Char]
sacarEspacioFinal [] = []
sacarEspacioFinal [a] |a == ' ' = []
                      |otherwise = [a]
sacarEspacioFinal (a:as) = a : sacarEspacioFinal as

sacarEspacioInicial :: [Char] -> [Char]
sacarEspacioInicial [] = []
sacarEspacioInicial (a:as) |a == ' ' = as
                           |otherwise = a : sacarEspacioInicial as

--EJERCICIO 4.3


primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (a:as) |a == ' ' = []
                      |otherwise = a : primeraPalabra as

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (a:as) |a == ' ' = as
                           |otherwise = sacarPrimeraPalabra as

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (a:as) = primeraPalabra (a:as) : palabras (sacarPrimeraPalabra (sacarBlancosRepetidos(a:as)))

--EJERCICIO 5.1
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x:y:ys) = x : sumaAcumulada ((x+y):ys)

--EJERCICIO 5.2
descomponerEnPrimos :: [Int] -> [[Int]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = factoresPrimos x : descomponerEnPrimos xs

factoresPrimos :: Int -> [Int]
factoresPrimos x | x <= 1 = []
                 | esPrimo (fromIntegral x) = [x]
                 | otherwise = menorDivisor x : factoresPrimos (div x (menorDivisor x)) 

menorDivisor :: Int -> Int
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde n y| n == y = y
                     | mod n y == 0 = y
                     | otherwise = menorDivisorDesde n (y+1)

esPrimo :: Int -> Bool
esPrimo n = menorDivisor n == n 