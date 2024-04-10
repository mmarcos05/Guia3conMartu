doubleMe x = x + x

f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

h :: Integer -> Integer
h = f . g

k :: Integer -> Integer
k = g . f

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z| (x >= y && x >= z) = x
             | (y >= x && y >= z) = y
             | otherwise = z

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z| (x /= y && y /= z && x /= z) = x + y + z
                   | (x == y && x /= z) = z
                   | (x == z && x /= y) = y
                   | (y == z && y /= x) = x
                   | (x == y && y == z) = 0

digitoUnidades :: Integer -> Integer
digitoUnidades x | x > 0 = x `mod` 10
                 | otherwise = (x * (-1)) `mod` 10

digitoDecenas :: Integer -> Integer
digitoDecenas x | x > 0 = div ((x `mod` 100) - digitoUnidades x) 10
                |otherwise = div (((x * (-1)) `mod` 100) - digitoUnidades x)10

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor t1 t2 | fst t1 < fst t2 && snd t1 < snd t2 = True
                |otherwise = False

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z)  | even x = 1
                        | even y = 2
                        | even z = 3
                        |otherwise = 4

bisiesto :: Int -> Bool
bisiesto año| (año `mod` 4 /= 0) ||(año `mod` 100 == 0) && (año `mod` 400 /= 0) = False
            | otherwise = True

distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a, b, c) (d, e, f) = (abs (a-d)) + (abs (b-e)) + (abs (c-f)) 


sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = digitoUnidades x + digitoDecenas x

comparar :: Int -> Int -> Int
