module Luli where

-- Ejercicio 4
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos n ((n1, t1):xs) | n ==  n1 = True
                               | otherwise = enLosContactos n xs

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto (n,t) [] = [(n,t)]
agregarContacto (n,t) ((n1, t1):xs) | n == n1 = (n,t) : xs
                                    | otherwise = (n1,t1) : agregarContacto (n,t) xs

eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto n ((n1, t1):xs) | n == n1 = eliminarContacto n xs 
                                 | otherwise = (n1, t1) : eliminarContacto n xs
