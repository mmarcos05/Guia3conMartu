module ParcialcomiC where

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
seGraduoConHonores ((a,b):as) materias alumno = (aproboMasDeNMaterias ((a,b):as) alumno (materias-1)) && (pertenece (buenosAlumnos ((a,b):as)) alumno) && (((mejorPromedioConNum ((a,b):as)) - (buscarPromedio ((a,b):as) alumno)) < 1) 

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