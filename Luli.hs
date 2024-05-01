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

-- Ejercicio 5
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
data Disponibilidad = Libre | Ocupado deriving (Eq, Show)

existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker _ [] = False
existeElLocker i ((i1,e):resto) | i == i1 = True
                                | otherwise =  existeElLocker i resto

ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker _ [] = []
ubicacionDelLocker i ((i1,(d1,u1)):resto) | i == i1 = u1
                                          | existeElLocker i resto = ubicacionDelLocker i resto
                                          | not (existeElLocker i ((i1,(d1,u1)):resto)) = []

estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker _ [] = False
estaDisponibleElLocker i ((i1,(d1,u1)):resto) | i == i1 && d1 == Libre = True
                                              | i == i1 && d1 == Ocupado = False
                                              | existeElLocker i resto = estaDisponibleElLocker i resto
                                              | not (existeElLocker i ((i1,(d1,u1)):resto)) = False

ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker i ((i1,(d1,u1)):resto) | (i == i1) && (d1 == Libre) = (i1, (Ocupado, u1)):resto
                                    | (i == i1) && (d1 == Ocupado) = ((i1,(d1,u1)):resto)
                                    | otherwise = (i1,(d1,u1)) : ocuparLocker i resto
                                    