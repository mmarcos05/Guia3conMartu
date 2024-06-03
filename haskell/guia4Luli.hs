-- Ejercicio 1 con pattern matching
fibonacci :: Int -> Int 
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

-- Ejercicio 2
parteEntera :: Float -> Int
parteEntera x = truncate x

-- Ejercicio 2.1
parteEntera2 :: Float -> Int
parteEntera2 x | x >= 0 = parteEnteraPositiva x
               | otherwise = parteEnteraNegativa x

parteEnteraPositiva :: Float -> Int
parteEnteraPositiva x | x < 1 = 0
                      | otherwise = 1 + parteEnteraPositiva (x-1)
parteEnteraNegativa :: Float -> Int
parteEnteraNegativa x | x > (-1) = 0
                      | otherwise = (-1) + parteEnteraNegativa (x+1)

-- Ejercicio 3 
esDivisible :: Int -> Int -> Bool
esDivisible x y | x < y = False
                | x == y = True
                | otherwise = esDivisible (x-y) y

-- Ejercicio 4
sumaImpares :: Int -> Int
sumaImpares x | x == 1 = 1
              | otherwise = (2*x) - 1 + sumaImpares (x-1)

-- Ejercicio 5 
medioFac :: Int -> Int
medioFac x | x == 0 = 1
           | x == 1 = 1
           |otherwise = x * medioFac (x-2)

-- Ejercicio 6
sumaDigitos :: Int -> Int
sumaDigitos x | x == 0 = 0
              | otherwise = mod x 10 + sumaDigitos (div x 10)

-- Ejercicio 7
todosDigitosIguales :: Int -> Bool
todosDigitosIguales x | x < 10 = True
                      |(digitoUnidades x == digitoUnidades (sacarUnidades x)) && todosDigitosIguales (sacarUnidades x) = True
                      |otherwise = False

digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

sacarUnidades :: Int -> Int
sacarUnidades x = div x 10

-- Ejercicio 8
iesimoDigito :: Int -> Int -> Int
iesimoDigito x i | i == cantDigitos x = mod x 10
                 | otherwise = iesimoDigito (sacarUnidades x) i
                 where sacarUnidades x = div x 10

cantDigitos :: Int -> Int
cantDigitos x | x == 0 = 1
              | x < 10 = 1
              | otherwise = 1 + cantDigitos (sacarUnidades x)
              where sacarUnidades x = div x 10

-- Ejercicio 9
esCapicua :: Int -> Bool
esCapicua x | x < 10 = True
            | x == reversa x = True
            | otherwise = False

reversa :: Int -> Int
reversa x | x < 10 = x
          | otherwise = digitoUnidades * 10^((cantDigitos x)-1) + reversa (sacarUnidades x)


-- Ejercicio 10.a
sumatoria1 :: Int -> Int 
sumatoria1 n | n == 0 = 1
             | otherwise = 2^n + sumatoria1 (n-1)

-- Ejercicio 10.b
sumatoria2 :: (Int, Float) -> Float
sumatoria2 (n,q) | n == 1 = q
                 | otherwise = q^n + sumatoria2 (n-1,q)

-- Ejercicio 10.c
sumatoria3 :: (Int, Float) -> Float
sumatoria3 (n,q) | n == 1 = (q + q^2)
                 | otherwise = q^(2*n) + q^(2*n-1) + sumatoria3 (n-1,q)

-- Ejercicio 10.d
sumatoria4 :: (Int, Float) -> Float
sumatoria4 (n,q) | n == 1 = (q + q^2)
                 | otherwise = sumatoria3 (n,q) - sumatoria2 (n-1,q)

--Ejercicio 11.a
eAprox :: Int -> Float
eAprox n | n == 0 = 1
         | otherwise = 1 / fromIntegral (factorial n) + eAprox (n-1)

factorial :: Int -> Int
factorial x | x == 0 = 1
            | otherwise = x * factorial (x-1)

-- 11.b
e :: Float
e = eAprox 10

-- Ejercicio 12
raizDe2Aprox :: Int -> Float
raizDe2Aprox x | x == 1 = 1
               | otherwise = sucesion x - 1

sucesion :: Int -> Float
sucesion x | x == 1 = 2
           | otherwise = 2 + 1 / sucesion (x-1)

-- Ejercicio 13
sumatoriaDoble :: (Int, Int) -> Int
sumatoriaDoble (n,m) | n == 1 = sumaPotenciasDe (1,m)
                     | n > 1 = sumaPotenciasDe (n,m) + sumatoriaDoble(n-1,m)
                     
sumaPotenciasDe :: (Int,Int) -> Int
sumaPotenciasDe (n,m) | m == 1 = n
                      | m > 1 = n^m + sumaPotenciasDe (n,m-1)

-- Ejercicio 14
sumaPotencias :: Int -> Int -> Int -> Int
sumaPotencias q n m | n == 1 = sumaPotenciasAux q 1 m
                    | otherwise = sumaPotenciasAux q n m + sumaPotencias q (n-1) m

sumaPotenciasAux :: Int -> Int -> Int -> Int
sumaPotenciasAux q n m | m == 1 = q^(n+1)
                       | otherwise = q^(n+m) + sumaPotenciasAux q n (m-1)
                     
-- Ejercicio 15
sumaRacionales :: Int -> Int -> Float 
sumaRacionales n m | n == 1 = sumaRacionalesM 1 m
                   | otherwise = sumaRacionalesM n m + sumaRacionales (n-1) m

sumaRacionalesM :: Int -> Int -> Float
sumaRacionalesM n m | m == 1 = fromIntegral n -- Lo mismo q decir 1/n
                    | otherwise = (fromIntegral n / fromIntegral m) + sumaRacionalesM n (m-1)

-- Ejercicio 16.a
menorDivisor :: Int -> Int
menorDivisor x = menorDivisorDesde x 2

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde x y | x == y = y
                      | mod x y == 0 = y
                      | otherwise = menorDivisorDesde x (y+1)

-- Ejercicio 16.b
esPrimo :: Int -> Bool
esPrimo x = menorDivisor x == x

-- Ejercicio 16.c
sonCoprimos :: Int -> Int -> Bool
sonCoprimos x y = gcd x y == 1

-- Ejercicio 16.d
nEsimoPrimo :: Int -> Int
nEsimoPrimo n = nEsimoPrimoDesde n 2

nEsimoPrimoDesde :: Int -> Int -> Int
nEsimoPrimoDesde n x | esPrimo x && n == 1 = x 
                     | esPrimo x = nEsimoPrimoDesde (n-1) (x+1)
                     | otherwise = nEsimoPrimoDesde n (x+1)

-- Ejerciciio 17
esFibonacci :: Int -> Bool
esFibonacci n = esFibonacciDesde n 0

esFibonacciDesde :: Int -> Int -> Bool
esFibonacciDesde n i | n == fibonacci i = True
                     | n < fibonacci i = False
                     | otherwise = esFibonacciDesde n (i+1)

-- Ejercicio 18
mayorDigitoPar :: Int -> Int
mayorDigitoPar x = buscarMayorDigitoPar x

buscarMayorDigitoPar :: Int -> Int
buscarMayorDigitoPar x | x == 0 = (-1)
                       | esPar (digitoUnidades x) = max (digitoUnidades x) (buscarMayorDigitoPar (sacarUnidades x))
                       | otherwise = buscarMayorDigitoPar (sacarUnidades x)

esPar :: Int -> Bool
esPar x = mod x 2 == 0

-- Ejercicio 19 
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosDesde 1 n 

esSumaInicialDePrimosDesde :: Int -> Int -> Bool
esSumaInicialDePrimosDesde m n | sumaMprimerosPrimos m == n = True
                               | sumaMprimerosPrimos m > n = False
                               | sumaMprimerosPrimos m < n = esSumaInicialDePrimosDesde (m+1) n

sumaMprimerosPrimos :: Int -> Int
sumaMprimerosPrimos m = sumaMprimerosPrimosDesde 2 m 

sumaMprimerosPrimosDesde :: Int -> Int -> Int
sumaMprimerosPrimosDesde i m | m == 0 = 0
                             | esPrimo i = i + sumaMprimerosPrimosDesde (i+1) (m-1)
                             | otherwise = sumaMprimerosPrimosDesde (i+1) m 

-- Ejercicio 20

-- Ejercicio 21
