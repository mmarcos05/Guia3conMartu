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