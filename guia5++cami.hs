-- RENOMBRE DE SECUENCIAS
--EJERCICIO 4

type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

--Punto a)
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((a, b):xs) | nombre == a = True
                                  | otherwise = enLosContactos nombre xs

--Punto b)
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto (x, y) [] = (x, y) : []
agregarContacto (x, y) ((a, b):xs) | not (enLosContactos x ((a, b):xs)) = (x, y) : ((a, b):xs)
                                   | otherwise = actualizaTelefono (x, y) ((a, b) : xs)

actualizaTelefono :: Contacto -> ContactosTel -> ContactosTel
actualizaTelefono (x, y) ((a, b) : xs) |x == a = (x, y) : xs
                                       |otherwise = (a, b) : actualizaTelefono (x, y) xs

--Punto c)
eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto nombre ((a, b) : xs) |nombre == a = xs
                                      |otherwise = (a, b) : eliminarContacto nombre xs



