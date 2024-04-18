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

-- iesimoDigito :: Int -> Int -> Int

cantDigitos :: Int -> Int
cantDigitos n| n < 10 = 1
             |otherwise = 1 + cantDigitos (sacarUnidades (n))
             where sacarUnidades (n) = div n 10

-- Ejercicio 9



--Ejercicio 10

--Ejercicio 11

--Ejercicio 12

--Ejercicio 13

sumatoriaDoble :: (Int, Int) -> Int
sumatoriaDoble (n,m)|n == 1 = sumaPotenciasDe (1,m)
                    |n > 1 = sumaPotenciasDe (n,m) + sumatoriaDoble ((n-1),m)

sumaPotenciasDe :: (Int, Int) -> Int
sumaPotenciasDe (n,m)| m == 1 = n
                     | otherwise = n^m + sumaPotenciasDe (n, (m-1))

--Ejercicio 14

--Ejercicio 15

--Ejercicio 16.1

menorDivisor :: Int -> Int
menorDivisor n = divisor n 2

divisor:: Int -> Int -> Int
divisor n m| n == m = n
           |mod n m == 0 = m
           |otherwise = divisor n (m+1)

--Ejercicio 16.2

esPrimo :: Int -> Bool
esPrimo n = menorDivisor n == n

--Ejercicio 16.3

--Ejercicio 19

sumaKPrimosDesde :: Int -> Int -> Int
sumaKPrimosDesde i k|k == 0 = 0
                    |menorDivisor i == i = i + sumaKPrimosDesde (i+1) (k-1)
                    |otherwise = sumaKPrimosDesde (i+1) k

sumaKPrimos :: Int -> Int
sumaKPrimos k = sumaKPrimosDesde 2 k

esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n = sumaInicialdePrimosDesde 1 n

sumaInicialdePrimosDesde :: Int -> Int -> Bool
sumaInicialdePrimosDesde k n|sumaKPrimos k < n = sumaInicialdePrimosDesde (k+1) n
                            |sumaKPrimos k == n = True    
                            |sumaKPrimos k > n = False

