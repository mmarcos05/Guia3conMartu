--Ejercicio 1

generarStock :: [[Char]] -> [([Char],Int)]
generarStock (x:xs) = generarStockAyuda (x:xs) []

cuantasVecesAparece :: [[Char]] -> [Char] -> Int
cuantasVecesAparece [] producto = 0
cuantasVecesAparece (x:xs) producto|x == producto = 1 + cuantasVecesAparece xs producto
                                   |otherwise = cuantasVecesAparece xs producto

pertenece :: [Char] -> [([Char],Int)] -> Bool
pertenece producto [] = False
pertenece producto ((a,b):as)|producto == a = True
                             |otherwise = pertenece producto as

generarStockAyuda :: [[Char]] -> [([Char],Int)] -> [([Char],Int)]
generarStockAyuda [] stock = stock
generarStockAyuda (x:xs) stock |not (pertenece x stock) = (generarStockAyuda xs ((x,(cuantasVecesAparece (x:xs) x)):stock))
                               |otherwise = (generarStockAyuda xs stock)

--Ejercicio 2

stockDeProducto :: [([Char],Int)] -> [Char] -> Int
stockDeProducto [] producto = 0
stockDeProducto ((a,b):as) producto|a == producto = b
                                   |otherwise = stockDeProducto as producto 

--Ejercicio 3

dineroEnStock :: [([Char],Int)] -> [([Char],Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((a,b):as) ((x,y):xs) = buscaPrecioMult (a,b) ((x,y):xs) + dineroEnStock as ((x,y):xs)


buscaPrecioMult :: ([Char],Int) -> [([Char],Float)] -> Float
buscaPrecioMult _ [] = 0
buscaPrecioMult (a,b) ((x,y):xs)|a == x = (fromIntegral b)*y
                            |otherwise = buscaPrecioMult (a,b) xs

--Ejercicio 4

aplicarOferta :: [([Char],Int)] -> [([Char],Float)] -> [([Char],Float)]
aplicarOferta [] _ = []
aplicarOferta ((a,b):as) ((x,y):xs)|(stockDeProducto ((a,b):as) a) > 10 = (a,(buscaPrecio (a,b) ((x,y):xs)) * 0.8) : aplicarOferta as ((x,y):xs)
                                   |(stockDeProducto ((a,b):as) a) <= 10 = (a,(buscaPrecio (a,b) ((x,y):xs))) : aplicarOferta as ((x,y):xs)

buscaPrecio :: ([Char],Int) -> [([Char],Float)] -> Float
buscaPrecio _ [] = 0
buscaPrecio (a,b) ((x,y):xs)|a == x = y
                            |otherwise = buscaPrecio (a,b) xs