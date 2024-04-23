--concatenación es haskell en vez de :: es ++
--EJERCICIO 1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

--EJERCICIO 1.2
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

--EJERCICIO 2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _[] = False
pertenece x (y:ys) |x == y = True
                   |otherwise = pertenece x ys

--EJERCICIO 2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs)| pertenece x xs = True
                   | otherwise = hayRepetidos xs

--EJERCICIO 2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y:ys) | x == y = ys
                | otherwise = y : quitar x ys

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

--Punto 1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

--Punto 2
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x*productoria xs

--Punto 3
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = n + x : sumarN n xs

--Punto 5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)