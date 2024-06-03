digitoUnidades :: Integer -> Integer
digitoUnidades x | x > 0 = x `mod` 10
                 | otherwise = (x * (-1)) `mod` 10

sacarUnidades :: Integer -> Integer
sacarUnidades x = div x 10

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)

-- Ejercicio 1
fibonacci :: Int -> Int
fibonacci n| n == 0 = 0
           | n == 1 = 1
           | n >= 0 = fibonacci (n-1) + fibonacci (n-2)

--Ejercicio 2
parteEntera :: Float -> Int
parteEntera x = truncate x


--Ejercicio 3
esDivisible :: Int -> Int -> Bool
esDivisible x y| x < y = False
               | x == y = True
               | otherwise = esDivisible (x-y)y

--Ejercicio 4
sumaImpares :: Int -> Int
sumaImpares n| n == 1 = 1
             | otherwise = (2*n) - 1 + sumaImpares (n-1)


--Ejercicio 5
medioFact :: Int -> Int
medioFact n|n == 0 = 1
           |n == 1 = 1
           |otherwise = n*medioFact(n-2)

--Ejercicio 6
sumaDigitos :: Int -> Int
sumaDigitos n |n == 0 = 0
              |otherwise = mod n 10 + sumaDigitos(div n 10)


--Ejercicio 7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n |n < 10 = True
                      |otherwise = digitoUnidades (n) == (digitoUnidades(sacarUnidades(n))) 
                                   && todosDigitosIguales(sacarUnidades(n))


--Ejercicio 8

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito x n = div (mod x (elevar 10 n) - mod x (elevar 10 (n-1))) (elevar 10 (n-1))

cantDigitos :: Integer -> Integer
cantDigitos x = contarDigitosDesde x 1

contarDigitosDesde :: Integer -> Integer -> Integer
contarDigitosDesde x i
    | x < elevar 10 i = i
    | otherwise = contarDigitosDesde x (i+1)

elevar :: Integer -> Integer -> Integer
elevar _ 0 = 1
elevar x 1 = x
elevar x y
    | y < 0 = 0
    | otherwise = x * elevar x (y-1)

-- Ejercicio 9

esCapicua :: Integer -> Bool
esCapicua x = inicioCapicua x 1

inicioCapicua :: Integer -> Integer -> Bool
inicioCapicua x i
    | i > div (cantDigitos x) 2 = True
    | otherwise = parEsCapicua x i && inicioCapicua x (i+1)

parEsCapicua x i = iesimoDigito x i == iesimoDigito x (cantDigitos x - i + 1)

--Ejercicio 10.1

sumatoriaUno :: Int -> Int
sumatoriaUno 0 = 1
sumatoriaUno n = 2^n + sumatoriaUno (n-1)

--Ejercicio 10.2

sumatoriaDos :: Integer -> Float -> Float
sumatoriaDos n x|n == 1 = x
                |otherwise = (x^n) + sumatoriaDos (n-1) x

--Ejercicio 10.3

sumatoriaTres :: Integer -> Float -> Float
sumatoriaTres n x = sumatoriaDos (2*n) x
--Ejercicio 10.4

sumatoriaCuatro :: Integer -> Float -> Float
sumatoriaCuatro n x = sumatoriaTres n x - sumatoriaDos (n-1) x

--Ejercicio 11

eAprox :: Int -> Float
eAprox 0 = 1
eAprox n = 1 / fromIntegral (factorial n) + eAprox n-1

--Ejercicio 12

fAux :: Integer -> Float
fAux 1 = 2
fAux n = 2 + 1 / (fAux (n-1))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = fAux n - 1

--Ejercicio 13

sumatoriaDoble :: (Int, Int) -> Int
sumatoriaDoble (n,m)|n == 1 = sumaPotenciasDe (1,m)
                    |n > 1 = sumaPotenciasDe (n,m) + sumatoriaDoble ((n-1),m)

sumaPotenciasDe :: (Int, Int) -> Int
sumaPotenciasDe (n,m)| m == 1 = n
                     | otherwise = n^m + sumaPotenciasDe (n, (m-1))

--Ejercicio 14

sumaPotencias ::  Int -> Int -> Int -> Int
sumaPotencias q n m| n == 1 = sumaPotenciasM q 1 m
                   | otherwise = sumaPotenciasM q n m + sumaPotencias 1 (n-1) m

sumaPotenciasM :: Int -> Int -> Int -> Int
sumaPotenciasM q n m| m == 1 = q^(n+1)
                    | otherwise = q^(n+m) + sumaPotencias q n (m-1)

--Ejercicio 15

sumaRacionales :: Int -> Int -> Float
sumaRacionales n m| n == 1 = sumaRacionalesM 1 m
                  | otherwise = sumaRacionalesM n m + sumaRacionales (n-1) m

sumaRacionalesM :: Int -> Int -> Float
sumaRacionalesM n m|m == 1 = fromIntegral n
                   |otherwise = fromIntegral n / fromIntegral m + sumaRacionalesM n (m-1)
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

--Ejercicio 17

esFibonacci :: Int -> Bool
esFibonacci n = inicioFibonacci n 0

inicioFibonacci :: Int -> Int -> Bool
inicioFibonacci n i|fibonacci i == n = True
                   |n < fibonacci i = False
                   |otherwise = inicioFibonacci n (i + 1)

--Ejercicio 18

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar x = analizarPar x (cantDigitos x) 8

analizarPar :: Integer -> Integer -> Integer -> Integer
analizarPar x i y|y == (-2) = (-1)
                 |i == 0 = analizarPar x (cantDigitos x) (y-2)
                 |iesimoDigito x i == y = y
                 |otherwise = analizarPar x (i-1) y
 --amase

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

--Ejercicio 20

