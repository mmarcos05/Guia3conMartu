-- Ejercicio 1
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((a,b):xs) = not (pertenece (a,b) xs) && tuplaValida (a,b) && relacionesValidas xs

tuplasSonIguales :: (String, String) -> (String, String) -> Bool
tuplasSonIguales (a,b) (c,d) | (a == c && b == d) = True
                             | (a == d && b == c) = True
                             | otherwise = False

tuplaValida :: (String, String) -> Bool
tuplaValida (a,b) = a /= b 

pertenece :: (String, String) -> [(String, String)] -> Bool
pertenece _ [] = False
pertenece (a,b) ((c,d):xs) | tuplasSonIguales (a,b) (c,d) = True
                           | pertenece (a,b) xs = True
                           | otherwise = False

-- Ejercicio 2
personas :: [([Char], [Char])] -> [[Char]]
personas [] = []
personas ((a,b):xs) | perteneceATuplas a xs = b : personas xs
                      | perteneceATuplas b xs = a : personas xs 
                      | perteneceATuplas a xs && perteneceATuplas b xs = personas xs 
                      | otherwise = a : b : personas xs 

perteneceATuplas :: [Char] -> [([Char], [Char])] -> Bool
perteneceATuplas c [] = False
perteneceATuplas c ((a,b):xs) = c == a || c == b || perteneceATuplas c xs

-- Ejercicio 3
amigosDe :: [Char] -> [([Char], [Char])] -> [[Char]]
amigosDe persona [] = []
amigosDe persona ((a,b):xs) | persona == a = b : amigosDe persona xs
                            | persona == b = a : amigosDe persona xs
                            | otherwise = amigosDe persona xs

-- Ejercicio 4
personaConMasAmigos :: [([Char], [Char])] -> [Char]
personaConMasAmigos [] = []
personaConMasAmigos ((a,b):xs) = personaConMasAmigosAux (personas ((a,b):xs)) ((a,b):xs)

personaConMasAmigosAux :: [[Char]] -> [([Char], [Char])] -> [Char]
personaConMasAmigosAux _ [] = []
personaConMasAmigosAux [c] _ = c
personaConMasAmigosAux (c:d:ds) ((a,b):xs) | cantDeAmigos c ((a,b):xs) >= cantDeAmigos d ((a,b):xs) = personaConMasAmigosAux (c:ds) ((a,b):xs)
                                           | otherwise = personaConMasAmigosAux (d:ds) ((a,b):xs)

longitud :: [t] -> Integer
longitud [] = 0 
longitud (x:xs) = 1 + longitud xs

cantDeAmigos :: [Char] -> [([Char], [Char])] -> Integer
cantDeAmigos persona [] = 0
cantDeAmigos persona ((a,b):xs) = longitud (amigosDe persona ((a,b):xs))

