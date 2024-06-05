--Ejercicio 1.1

longitud :: [t] -> Int
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

--Ejercicio 1.2

ultimo :: [t] -> t
ultimo [z] = z
ultimo (_:zs) = ultimo zs

--Ejercicio 2.1

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys)|y == x = True
                  |otherwise = pertenece x ys

--Ejercicio 2.4

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs)|pertenece x xs = True
                   |otherwise = hayRepetidos xs

--Ejercicio 2.5

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x (y:ys) |x == y = ys
                |otherwise = y : quitar x ys

--Ejercicio 3.1

sumatoria :: [Int] -> Int
sumatoria (x:xs) = iDelTresPuntoUno (longitud(x:xs)) (x:xs)

iDelTresPuntoUno :: Int -> [Int] -> Int
iDelTresPuntoUno 1 [x] = x
iDelTresPuntoUno i (x:xs) = (head (x:xs)) + iDelTresPuntoUno (i-1) xs

--Ejercicio 3.2

productoria :: [Int] -> Int
productoria [] = 1
productoria (x:xs) = x * productoria xs

--Ejercicio 3.3

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:ys)|x > y = maximo (x:ys)
               |y > x = maximo (y:ys)
               |otherwise = maximo (x:ys)

--Ejercicio 3.4

sumarN :: Int -> [Int] -> [Int]
sumarN _ [] = []
sumarN n (x:xs) = n + x : sumarN n xs

--Ejercicio 3.5

sumarElPrimero :: [Int] -> [Int]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

--Ejercicio 3.6

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

--Ejercicio 3.9 

ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) = minimo (x:xs) : ordenar (quitar (minimo (x:xs)) (x:xs))

minimo :: [Int] -> Int
minimo [x] = x
minimo (x:y:ys)|x > y = minimo (y:ys)
               |y > x = minimo (x:ys)
               |otherwise = maximo (x:ys)