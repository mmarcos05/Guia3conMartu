-- Ejercicio 1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- 1.2
ultimo :: [t] -> t
ultimo [x] = x -- Cuando la lista tiene 1 solo elemento, ese es el único
ultimo (_:xs) = ultimo xs -- Cuando tiene mas de uno, descarto el primero y busco el último en el resto de la lista

-- 1.3
principio :: [t] -> [t]
principio [x] = [] -- Cuando hay 1 solo elemento
principio (x:xs) = x : principio xs -- Cuando hay mas de uno, añadimos el primero al principio hasta que me quedan solo dos

-- 1.4
reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso xs ++ [x]

-- Ejercicio 2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) | x == y = True  -- Veo si es igual al primer elemento de la lista
                   | otherwise = pertenece x ys  -- Si no me fijo en todo el resto

-- 2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:xs) | x == y = todosIguales (y:xs)  -- Si el primero es igual al segundo sigo viendo con el resto
                      | otherwise = False

-- 2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:y:xs) | x /= y = todosDistintos (y:xs) && todosDistintos (x:xs)
                        | otherwise = False
                     
-- 2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | hayRepetidos xs = True
                    | otherwise = False

-- 2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y:ys) | x == y = ys
                | otherwise = y : quitar x ys

-- 2.6
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys) | x == y = quitarTodos x ys
                     | otherwise = y : quitarTodos x ys 

-- 2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)

-- 2.8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos s r = todosPertenecen s r && todosPertenecen r s 

todosPertenecen :: (Eq t) => [t] -> [t] -> Bool
todosPertenecen [] _ = True
todosPertenecen (x:xs) ys = pertenece x ys && todosPertenecen xs ys

-- 2.9
capicua :: (Eq t) => [t] -> Bool
capicua [x] = True
capicua (x:xs) = (x:xs) == reverso (x:xs)

-- Ejercicio 3.1  
sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- 3.2
productoria :: [Int] -> Int
productoria [] = 1
productoria (x:xs) = x * productoria xs

-- 3.3
maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:ys) | x > y = maximo (x:ys)
                | x < y = maximo (y:ys)
                | otherwise = maximo (x:ys)
                
-- 3.4
sumarN :: Int -> [Int] -> [Int]
sumarN _ [] = []
sumarN x (y:ys) = y + x : sumarN x ys

-- 3.5
sumarElPrimero :: [Int] -> [Int]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- 3.6
sumarElUltimo :: [Int] -> [Int]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

-- 3.7
pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | esPar x = x : pares xs
             | otherwise = pares xs
             
esPar :: Int -> Bool
esPar x = mod x 2 == 0 

-- 3.8
multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs
-- 3.9
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) = minimo (x:xs) : ordenar (quitar (minimo (x:xs))(x:xs))
               
minimo :: [Int] -> Int
minimo [x] = x
minimo (x:y:ys) | x < y = minimo (x:ys)
                | x > y = minimo (y:ys)
                | otherwise = minimo (x:ys)

-- Ejercicio 4.a.a
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [a] = [a]
sacarBlancosRepetidos (a:b:bs) | a == ' ' && b == ' ' = sacarBlancosRepetidos (a:bs)
                               | otherwise = a : sacarBlancosRepetidos (b:bs)

-- 4.a.b
contarPalabras :: [Char] -> Int
contarPalabras [] = 0
contarPalabras (a:as) = 1 + contarPalabrasAux (sacarBlancoInicio (sacarBlancoFinal (sacarBlancosRepetidos (a:as))))


contarPalabrasAux :: [Char] -> Int -- cuento las palabras despues del primer espacio
contarPalabrasAux [] = 0 
contarPalabrasAux (a:as) | a == ' ' = 1 + contarPalabrasAux as
                         | otherwise = contarPalabrasAux as

sacarBlancoInicio :: [Char] -> [Char]
sacarBlancoInicio [] = []
sacarBlancoInicio (a:as) | a == ' ' = as
                         | otherwise = a:as

sacarBlancoFinal :: [Char] -> [Char]
sacarBlancoFinal [] = []
sacarBlancoFinal [a] | a == ' ' = []
                     | otherwise = [a]
sacarBlancoFinal (a:as) = a : sacarBlancoFinal as

-- 4.a.c
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (a:as) = primeraPalabra (a:as) : palabras (sacarPrimeraPalabra (a:as))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (a:as) = primeraPalabraAux (sacarBlancoInicio (sacarBlancoFinal (sacarBlancosRepetidos (a:as))))

primeraPalabraAux :: [Char] -> [Char]
primeraPalabraAux [] = []
primeraPalabraAux (a:as) | a == ' ' = []
                         | otherwise = a : primeraPalabraAux as

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (a:as) = sacarPrimeraPalabraAux (sacarBlancoInicio (sacarBlancoFinal (sacarBlancosRepetidos (a:as))))

sacarPrimeraPalabraAux :: [Char] -> [Char]
sacarPrimeraPalabraAux [] = []
sacarPrimeraPalabraAux (a:as) | a == ' ' = as
                              | otherwise = sacarPrimeraPalabraAux as

-- 4.a.d
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga (a:as) | sacarPrimeraPalabra (a:as) == "" = primeraPalabra (a:as)
                       | longitud (primeraPalabra (a:as)) < longitud (primeraPalabra (sacarPrimeraPalabra (a:as))) = palabraMasLarga (sacarPrimeraPalabra (a:as))
                       | otherwise = palabraMasLarga ((primeraPalabra (a:as)) ++ [' '] ++ sacarPrimeraPalabra (sacarPrimeraPalabra (a:as)))

-- 4.a.e
aplanar :: [[Char]] -> [Char] -- a partir de una lista de palabras arma una lista de caracteres
aplanar [] = []
aplanar (a:as) = a ++ aplanar as

-- 4.a.f
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos [a] = a
aplanarConBlancos (a:as) = a ++ " " ++ (aplanarConBlancos as)

-- 4.a.g
aplanarConNBlancos :: [[Char]] -> Int -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos [a] _ = a
aplanarConNBlancos (a:as) n = a ++ (nBlancos n) ++ (aplanarConNBlancos (as) n)

nBlancos :: Int -> [Char]
nBlancos n | n == 0 = []
           | otherwise = ' ' : nBlancos (n-1)

-- 4.b
-- ¿Como cambian los ejercicios si agregamos el renombre de tipos: type Texto = [Char]?
type Texto = [Char]
aplanar2 :: [Texto] -> Texto -- a partir de una lista de palabras arma una lista de caracteres
aplanar2 [] = []
aplanar2 (a:as) = a ++ aplanar2 as

-- Ejercicio 5.1 
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x:y:ys) = x : sumaAcumulada ((x+y):ys)

-- 5.2
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = factoresPrimos x : descomponerEnPrimos xs

factoresPrimos :: Integer -> [Integer]
factoresPrimos x | x <= 1 = []
                 | esPrimo (fromIntegral x) = [x]
                 | otherwise = menorDivisor x : factoresPrimos (div x (menorDivisor x))

menorDivisor :: Integer -> Integer
menorDivisor x = menorDivisorDesde x 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde x y | x == y = y
                      | mod x y == 0 = y
                      | otherwise = menorDivisorDesde x (y+1)

esPrimo :: Integer -> Bool
esPrimo x = menorDivisor x == x
