digitoUnidades :: Integer -> Integer
digitoUnidades x | x > 0 = x `mod` 10
                 | otherwise = (x * (-1)) `mod` 10

sacarUnidades :: Integer -> Integer
sacarUnidades x = div x 10


fibonacci :: Int -> Int
fibonacci n| n == 0 = 0
           | n == 1 = 1
           | n >= 0 = fibonacci (n-1) + fibonacci (n-2)

parteEntera :: Float -> Int
parteEntera x = truncate x

esDivisible :: Int -> Int -> Bool
esDivisible x y| x < y = False
               | x == y = True
               | otherwise = esDivisible (x-y)y

sumaImpares :: Int -> Int
sumaImpares n| n == 1 = 1
             | otherwise = (2*n) - 1 + sumaImpares (n-1)

medioFact :: Int -> Int
medioFact n|n == 0 = 1
           |n == 1 = 1
           |otherwise = n*medioFact(n-2)

sumaDigitos :: Int -> Int
sumaDigitos n |n == 0 = 0
              |otherwise = mod n 10 + sumaDigitos(div n 10)

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n |n < 10 = True
                      |otherwise = digitoUnidades (n) == (digitoUnidades(sacarUnidades(n))) 
                                   && todosDigitosIguales(sacarUnidades(n))

iesimoDigito :: Int -> Int -> Int

cantDigitos :: Int -> Int
cantDigitos n| n < 10 = 1
             |otherwise = 1 + cantDigitos (sacarUnidades (n))
             where sacarUnidades (n) = div n 10