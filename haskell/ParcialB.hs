module ParcialB where

-- Ejercicio 1
aproboMasDeNMaterias :: [([Char],[Integer])] -> [Char] -> Integer -> Bool
aproboMasDeNMaterias ((a1,[]):restor) alumno n = False
aproboMasDeNMaterias ((a1,(n1:reston)):restor) alumno n 
            | (alumno == a1) && ((cuantasMateriasAprobo (a1,(n1:reston))) == 0) = False
            | (alumno == a1) && ((cuantasMateriasAprobo (a1,(n1:reston))) <= n) = False
            | (alumno == a1) && ((cuantasMateriasAprobo (a1,(n1:reston))) > n) = True
            | otherwise = aproboMasDeNMaterias restor alumno n 

cuantasMateriasAprobo :: ([Char],[Integer]) -> Integer
cuantasMateriasAprobo (_,[]) = 0
cuantasMateriasAprobo (a1,(n1:reston))
            | (notaAprobada n1 == True) = 1 + cuantasMateriasAprobo (a1,reston)
            | (notaAprobada n1 == False) = cuantasMateriasAprobo (a1,reston)

notaAprobada :: Integer -> Bool
notaAprobada n | n >= 4 = True
               | otherwise = False

-- Ejercicio 2 
buenosAlumnos :: [([Char],[Integer])] -> [[Char]]
buenosAlumnos [] = []
buenosAlumnos ((a1,(n1:reston)):restor)
        | ((promedioNotasAlumno (n1:reston)) >= 8) && ((tieneAplazos (n1:reston)) == False) = a1 : buenosAlumnos restor
        | otherwise = buenosAlumnos restor

promedioNotasAlumno :: [Integer] -> Float
promedioNotasAlumno [] = 0
promedioNotasAlumno (n1:reston) = division (sumaDeNotas (n1:reston)) (cantDeNotas (n1:reston))

division :: Integer -> Integer -> Float
division a b = (fromIntegral a) / (fromIntegral b)

cantDeNotas :: [Integer] -> Integer
cantDeNotas [] = 0
cantDeNotas (n1:reston) = 1 + cantDeNotas reston

sumaDeNotas :: [Integer] -> Integer
sumaDeNotas [] = 0
sumaDeNotas (n1:reston) = n1 + sumaDeNotas reston

tieneAplazos :: [Integer] -> Bool
tieneAplazos [] = False
tieneAplazos (n1:reston) | n1 < 4 = True
                         | otherwise = tieneAplazos reston

-- Ejercicio 3
mejorPromedio :: [([Char],[Integer])] -> [Char]
mejorPromedio [] = " "
mejorPromedio [(alumno,_)] = alumno
mejorPromedio ((a1,(n1:reston)):restor)
            | promedioMasAlto ((a1,(n1:reston)):restor) == promedioNotasAlumno (n1:reston) = a1
            | otherwise = mejorPromedio restor 

promedioMasAlto :: [([Char],[Integer])] -> Float
promedioMasAlto [] = 0
promedioMasAlto ((a1,(n1:reston)):restor) 
            | promedioNotasAlumno (n1:reston) >= promedioMasAlto restor = promedioNotasAlumno (n1:reston)
            | otherwise = promedioMasAlto restor

-- Ejercicio 4
seGraduoConHonores :: [([Char],[Integer])] -> Integer -> [Char] -> Bool
seGraduoConHonores _ _ [] = False
seGraduoConHonores ((a1,(n1:reston)):restor) m alumno = ((aproboMasDeNMaterias ((a1,(n1:reston)):restor) alumno (m-1)) == True) && ((pertenece alumno (buenosAlumnos ((a1,(n1:reston)):restor))) == True) && ((promedioHonores ((a1,(n1:reston)):restor)) == True)

                {-  promAlu  mejorProm  -}
promedioHonores :: [([Char],[Integer])] -> Bool
promedioHonores [] = False 
promedioHonores ((a1,(n1:reston)):restor) = ((promedioNotasAlumno (n1:reston)) > ((promedioMasAlto ((a1,(n1:reston)):restor)) - 1))

pertenece :: [Char] -> [[Char]] -> Bool
pertenece _ [] = False
pertenece alumno (a1:restoa) | alumno == a1 = True
                             | otherwise = pertenece alumno restoa

{- estaEnElRegistro :: [Char] -> [([Char],[Integer])] -> Bool
estaEnElRegistro _ [] = False
estaEnElRegistro alumno ((a1,n1):restor) | (alumno == a1) = True
                                         | (alumno /= a1) = estaEnElRegistro alumno restor
                                         | otherwise = False -}