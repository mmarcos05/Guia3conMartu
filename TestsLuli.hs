import Test.HUnit
import Luli

main = runTestTT tests

-- "nombre" ~: (funcion parametros) ~?= resultado_esperado

tests = test [
  "lista vacia" ~: (agregarContacto ("ana", "12") []) ~?= [("ana", "12")],
  "no esta el contacto" ~: (agregarContacto  ("Juan", "234") [("ana", "12"), ("sofia", "2312")]) ~?= [("ana", "12"), ("sofia", "2312"), ("Juan", "234")] , 
  "actualizar telefono" ~: (agregarContacto  ("ana", "56") [("ana", "234"), ("pedro", "4123432")]) ~?= [("ana", "56"), ("pedro", "4123432")],
  
  "lista vacia eliminar" ~: (eliminarContacto "ana" []) ~?= [],
  "esta el nombre" ~: (eliminarContacto  "ana" [("ana", "234"), ("pedro", "413")]) ~?= [("pedro", "413")],
  "no esta" ~: (eliminarContacto  "ana" [("caca", "234"), ("pedro", "4123432")]) ~?= [("caca", "234"), ("pedro", "4123432")]
    ]

-- -- EJEMPLOS

-- USUARIO1 = "JUAN"
-- USUARIO2 = "NATALIA"
-- USUARIO3 = "PEDRO"

-- RELACION1_2 = (USUARIO1, USUARIO2)
-- RELACION1_1 = (USUARIO1, USUARIO1)
-- RELACION1_3 = (USUARIO1, USUARIO3)


-- -- FUNCIONES PARA TESTING, NO BORRAR
-- -- EXPECTANY PERMITE SABER SI EL ELEMENOT QUE DEVUELVE LA FUNCIÓN ES ALGUNO DE LOS ESPERADOS
-- EXPECTANY ACTUAL EXPECTED = ELEM ACTUAL EXPECTED ~? ("EXPECTED ANY OF: " ++ SHOW EXPECTED ++ "\N BUT GOT: " ++ SHOW ACTUAL)


-- -- SONIGUALES PERMITE VER QUE DOS LISTAS SEAN IGUALES SI NO IMPORTA EL ORDEN
-- QUITAR :: (EQ T) => T -> [T] -> [T]
-- -- REQUIERE X PERTENECE A Y
-- QUITAR X (Y:YS)
-- | X == Y = YS
-- | OTHERWISE = Y : QUITAR X YS

-- INCLUIDO :: (EQ T) => [T] -> [T] -> BOOL
-- INCLUIDO [] L = TRUE
-- INCLUIDO (X:C) L = ELEM X L && INCLUIDO C (QUITAR X L)

-- SONIGUALES :: (EQ T) => [T] -> [T] -> BOOL
-- SONIGUALES XS YS = INCLUIDO XS YS && INCLUIDO YS XS 

