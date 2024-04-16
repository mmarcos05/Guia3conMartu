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

--EJERCICIO 8
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i |

cantDigitos :: Integer -> Integer
cantDigitos n |n < 10 = 1
              |otherwise = 1 + cantDigitos (sacarUnidades (n))
              |where sacarUnidades n = div n 10

