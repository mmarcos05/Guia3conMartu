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

--EJERCICIO 13
dobleSumaDePotencias :: (Integer, Integer) -> Integer
dobleSumaDePotencias (n, m) |n == 1 = sumaPotenciasDe (1, m)
                            |n>1 = sumaPotenciasDe(n, m) + dobleSumaDePotencias(n-1, m)

sumaPotenciasDe :: (Integer, Integer) -> Integer
sumaPotenciasDe (n, m) |m == 1 = n
                       |m>1 = n^m + dobleSumaDePotencias(n, m-1)

--EJERCICIO 16
--Punto a)
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n y| n == y = y
                     | mod n y == 0 = y
                     | otherwise = menorDivisorDesde n (y+1)

--Punto b)
esPrimo :: Integer -> Bool
esPrimo n |menorDivisor n == n = True
          |otherwise = False

--Punto c)
--sonCoprimos :: Integer -> Integer -> Bool
--sonCoprimos x y |

--EJERCICIO 19
sumaKPrimosDesde :: Integer -> Integer -> Integer
sumaKPrimosDesde i k |k == 0 = 0
                     |esPrimo i = sumaKPrimosDesde (i + 1) (k-1)
                     |otherwise = sumaKPrimosDesde (i+1) k

sumaKPrimos :: Integer -> Integer
sumaKPrimos k = sumaKPrimosDesde 2 k

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosDesde 1 n

esSumaInicialDePrimosDesde :: Integer -> Integer -> Bool
esSumaInicialDePrimosDesde k n | (sumaKPrimos k) < n = esSumaInicialDePrimosDesde (k+1) n
                               | (sumaKPrimos k) == n = True
                               | (sumaKPrimos k) > n = False