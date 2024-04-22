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