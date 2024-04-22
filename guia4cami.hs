--EJERCICIO 1
fibonacci :: Integer -> Integer
fibonacci n |n == 0 = 0
            |n == 1 = 1
            |n>=0 = fibonacci(n-1) + fibonacci(n-2)

--EJERCICIO 2
parteEntera :: Float -> Integer
parteEntera x = truncate x

--EJERCICIO 3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y| x < y = False
               | x == y = True
               |otherwise = esDivisible (x-y) y

--EJERCICIO 4
sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = 1
              | otherwise = (2*n) - 1 + sumaImpares (n-1)

--EJERCICIO 5
medioFact :: Integer -> Integer
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n*medioFact(n-2)

--EJERCICIO 6
sumaDigitos :: Integer -> Integer
sumaDigitos n |n == 0 = 0
              |otherwise = mod n 10 + sumaDigitos(div n 10)

--EJERCICIO 7
digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10

sacarUnidades :: Integer -> Integer
sacarUnidades n = div n 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n |n < 10 = True
                      |otherwise = digitoUnidades(n) == (digitoUnidades(sacarUnidades(n))) 
                                   && todosDigitosIguales(sacarUnidades(n))
--EJERCICIO 7
--digitoUnidades :: Integer -> Integer
--digitoUnidades n = mod n 10

--sacarUnidades :: Integer -> Integer
--sacarUnidades n = div n 10

--todosDigitosIguales :: Integer -> Bool
--todosDigitosIguales n |n < 10 = True
              --        |otherwise = digitoUnidades(n) == (digitoUnidades(sacarUnidades(n))) 
                   --                && todosDigitosIguales(sacarUnidades(n))

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n |n < 10 = True
                      |otherwise = (mod (div n 10) 10 == mod n 10) && todosDigitosIguales(div n 10)

--EJERCICIO 8
cantDigitos :: Integer -> Integer
cantDigitos n |n < 10 = 1
              |otherwise = 1 + cantDigitos(div n 10)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i |cantDigitos n == i = mod n 10
                 |otherwise = iesimoDigito(div n 10) i

--EJERCICIO 10
--Punto c)
potencia :: Float -> Float -> Float
potencia q i |i == 0 = 1
             |otherwise = q * potencia q (i-1)

f3 :: Integer -> Float -> Float
f3 n q |n == 1 = q + potencia q 2
       |otherwise = potencia q (2*q) + potencia q ((2*q)-1) + f3 (n-1) q

--EJERCICIO 11
--Punto a)
eAprox :: Integer -> Float
eAprox n |n == 0 = 1
         |otherwise = 1 / fromIntegral (factorial n) + eAprox (n-1)

factorial :: Integer -> Integer
factorial n |n == 0 = 1
            |otherwise = n * factorial (n-1)

--Punto b)
e :: Float
e = eAprox 10

--EJERCICIO 12
sucesionRaiz :: Integer -> Float
sucesionRaiz n |n == 1 = 2
               |otherwise = 2 + 1 / (sucesionRaiz (n-1))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = sucesionRaiz n - 1

--EJERCICIO 13
--dobleSumaDePotencias :: (Integer, Integer) -> Integer
--dobleSumaDePotencias (n, m) |n == 1 = sumaPotenciasDe (1, m)
                       --     |n>1 = sumaPotenciasDe(n, m) + dobleSumaDePotencias(n-1, m)

--sumaPotenciasDe :: (Integer, Integer) -> Integer
--sumaPotenciasDe (n, m) |m == 1 = n
                     --  |m>1 = n^m + dobleSumaDePotencias(n, m-1)

potencia2 :: Integer -> Integer -> Integer
potencia2 q i |i == 0 = 1
              |otherwise = q * potencia2 q (i-1)

sumaDoblePotencias :: Integer -> Integer -> Integer
sumaDoblePotencias q m |m == 1 = q
                       |m>1 = potencia2 q m + sumaDoblePotencias q (m-1)

sumaPosta :: Integer -> Integer -> Integer
sumaPosta n m |n == 1 = sumaDoblePotencias 1 m
              |n>1 = sumaDoblePotencias n m + sumaPosta (n-1) m

--EJERCICIO 15
sumaRacionalesPrimera :: Integer -> Integer -> Float
sumaRacionalesPrimera n m |m == 1 = fromIntegral n
                          |m>1 = (fromIntegral n / fromIntegral m) + sumaRacionalesPrimera n (m-1)

sumaRacionalesSegunda :: Integer -> Integer -> Float
sumaRacionalesSegunda n m |n == 1 = sumaRacionalesPrimera 1 m
                          |n>1 = sumaRacionalesPrimera n m + sumaRacionalesSegunda (n-1) m

              
--EJERCICIO 16
--Punto a)
menorDivisor :: Int -> Int
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde n y| n == y = y
                     | mod n y == 0 = y
                     | otherwise = menorDivisorDesde n (y+1)

--Punto b)
esPrimo :: Int -> Bool
esPrimo n = menorDivisor n == n 

--Punto c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos x y = divisores x y 2

divisores :: Integer -> Integer -> Integer -> Bool
divisores x y c |x == y = False
                |otherwise = (mod x c == 0) && (mod y c == 0) || divisores x y (c+1)

--Punto d)
nEsimoPrimoDesde :: Int -> Int -> Int
nEsimoPrimoDesde n k |esPrimo k && n == 1 = n
                     |esPrimo k = nEsimoPrimoDesde (n-1) (k+1)
                     |otherwise = nEsimoPrimoDesde n (k+1)

nEsimoPrimo :: Int -> Int
nEsimoPrimo n = nEsimoPrimoDesde n 2

--EJERCICIO 17
esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux n c = n == fibonacci(c) || esFibonacciAux n (c+1)

esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciAux n 0

--EJERCICIO 18
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n |n == 0 = (-1)
                 |esPar n = max (mod n 10) (mayorDigitoPar(div n 10))
                 |otherwise = mayorDigitoPar (div n 10)

esPar :: Integer -> Bool
esPar n = mod n 2 == 0

--EJERCICIO 19
sumaKPrimosDesde :: Int -> Int -> Int
sumaKPrimosDesde i k |k == 0 = 0
                     |esPrimo i = i + sumaKPrimosDesde (i + 1) (k-1)
                     |otherwise = sumaKPrimosDesde (i+1) k

sumaKPrimos :: Int -> Int
sumaKPrimos k = sumaKPrimosDesde 2 k

esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosDesde 1 n

esSumaInicialDePrimosDesde :: Int -> Int -> Bool
esSumaInicialDePrimosDesde k n | (sumaKPrimos k) < n = esSumaInicialDePrimosDesde (k+1) n
                               | (sumaKPrimos k) == n = True
                               | (sumaKPrimos k) > n = False