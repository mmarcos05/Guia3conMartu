--EJERCICIO 1
--            
aproboMasDeNmaterias :: String -> Integer -> [(String,[Integer])]->Bool
aproboMasDeNmaterias p n ((p1,ys):xs) | p == p1 = n < notasMayoresa4 ys 
                                      | otherwise = aproboMasDeNmaterias p n xs 

notasMayoresa4 :: [Integer]->Integer
notasMayoresa4 [] = 0
notasMayoresa4 (x:xs) | x >= 4 = 1 + notasMayoresa4 xs
                      | otherwise = notasMayoresa4 xs 

--EJERCICIO 2
buenosAlumnos :: [(String,[Integer])]->[String]
buenosAlumnos [] = []
buenosAlumnos ((al,xs):an) | (promedioNotas xs >= 8) && noHayNotaMenora4 xs = al : buenosAlumnos an
                           | otherwise = buenosAlumnos an

promedioNotas :: [Integer]->Float
promedioNotas [] = 0
promedioNotas (y:ys) = division (sumaDeNotas (y:ys)) (longitud (y:ys))

longitud :: [Integer]->Integer
longitud [] = 0
longitud [x] = 1
longitud (x:xs) = 1 + longitud xs 

sumaDeNotas :: [Integer]->Integer 
sumaDeNotas [] = 0
sumaDeNotas [x] = x
sumaDeNotas (y:ys) = y + sumaDeNotas ys 

division :: Integer->Integer -> Float
division a b = (fromIntegral a / fromIntegral b)

noHayNotaMenora4 :: [Integer] -> Bool
noHayNotaMenora4 [] = True
noHayNotaMenora4 (x:xs) | x < 4 = False 
                        | otherwise = noHayNotaMenora4 xs 

--EJERCICIO 3
mejorPromedio :: [(String,[Integer])] -> String
mejorPromedio [(a,b)] = a 
mejorPromedio ((al,xs):demas) | mejorPromedioAux ((al,xs):demas) == xs = al
                              | otherwise = mejorPromedio demas 

mejorPromedioAux :: [(String,[Integer])]->[Integer]
mejorPromedioAux [] = []
mejorPromedioAux [(al,(x:xs))] = (x:xs)
mejorPromedioAux ((al1,(x:xs)):(al2,(y:ys)):resto) | promedioNotas (x:xs) >= promedioNotas (y:ys) = mejorPromedioAux ((al1,(x:xs)):resto)
                                                   | otherwise = mejorPromedioAux ((al2,(y:ys)):resto)
   
--EJERCICIO 4
seGraduoConHonores :: [(String,[Integer])]->Integer->String->Bool
seGraduoConHonores ((al1,(x:xs)):demas) z al = (aproboMasDeNmaterias al (z-1) ((al1,(x:xs)):demas)) && pertenece al (buenosAlumnos ((al1,(x:xs)):demas)) && (unPuntoMenos ((al1,(x:xs)):demas) al)

unPuntoMenos :: [(String,[Integer])]->String->Bool
unPuntoMenos [] _ = False
unPuntoMenos ((al1,(x:xs)):demas) al = (promedioNotas (mejorPromedioAux ((al1,(x:xs)):demas)) - (promedioNotas (notasDeAlumno ((al1,(x:xs)):demas) al)) < 1)

pertenece :: String -> [String] -> Bool 
pertenece al [] = False 
pertenece al (al1:xs) | al == al1 = True
                      | otherwise = pertenece al xs 

notasDeAlumno :: [(String,[Integer])]->String->[Integer]
notasDeAlumno [] _ = []
notasDeAlumno ((al,(x:xs)):demas) alumno | al == alumno = (x:xs)
                                         | otherwise = notasDeAlumno demas  alumno 