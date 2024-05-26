--PROBLEMA 1
relacionesValidas :: [([Char],[Char])] -> Bool
relacionesValidas [] = True
relacionesValidas ((a, b) : xs) = not (pertenece (a, b) xs) &&  tuplaValida (a, b) && relacionesValidas xs

tuplasIguales :: ([Char], [Char]) -> ([Char], [Char]) -> Bool
tuplasIguales (a, b) (c, d) = (a == c) && (b == d) || (b == c) && (a == d)

tuplaValida :: ([Char], [Char]) -> Bool
tuplaValida (a, b) = a /= b

pertenece :: ([Char], [Char]) -> [([Char], [Char])] -> Bool
pertenece _ [] = False
pertenece (a, b) ((c, d) : xs) = tuplasIguales (a, b) (c, d) || pertenece (a, b) xs

--PROBLEMA 2
personas :: [([Char],[Char])] -> [[Char]]
personas [] = []
personas ((a, b) : xs) |perteneceATuplas a xs = b: personas xs
                       |perteneceATuplas b xs = a : personas xs
                       |perteneceATuplas a xs && perteneceATuplas b xs = personas xs
                       |otherwise = a : b : personas xs

perteneceATuplas :: [Char] -> [([Char],[Char])] -> Bool
perteneceATuplas c [] = False
perteneceATuplas c ((a, b) : xs) = c == a || c == b || perteneceATuplas c xs

--PROBLEMA 3
amigosDe :: [Char] -> [([Char],[Char])] -> [[Char]]
amigosDe persona [] = []
amigosDe persona ((a, b) : xs) |persona == a = b : amigosDe persona xs
                               |persona == b = a : amigosDe persona xs
                               |otherwise = amigosDe persona xs

--PROBLEMA 4
personaConMasAmigos :: [([Char],[Char])] -> [Char]
personaConMasAmigos [] = []
personaConMasAmigos ((a, b) : xs) = personaConMasAmigosAux (personas ((a, b) : xs)) ((a, b): xs)

personaConMasAmigosAux :: [[Char]] -> [([Char],[Char])] -> [Char]
personaConMasAmigosAux _ [] = []
personaConMasAmigosAux [c] _ = c
personaConMasAmigosAux (c:d:ds) ((a, b) : xs)|cantidadDeAmigos c ((a, b) : xs) >= cantidadDeAmigos d ((a, b) : xs) = personaConMasAmigosAux (c:ds) ((a, b) : xs)
                                             |otherwise = personaConMasAmigosAux (d:ds) ((a, b) : xs)

cantidadDeAmigos :: [Char] -> [([Char],[Char])] -> Integer
cantidadDeAmigos persona [] = 0
cantidadDeAmigos persona ((a, b) : xs) = longitud (amigosDe persona ((a, b) : xs))

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs