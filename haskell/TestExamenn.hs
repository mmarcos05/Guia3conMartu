import Test.HUnit
import Examen

main = runTestTT ejercicio4

ejercicio1 = test [
    "lista vacía" ~: (hayQueCodificar 'a' []) ~?= False,
    "c no es igual a ninguna primera componente" ~: (hayQueCodificar 'a' [('b', 'c'), ('d', 'e'), ('f', 'g')]) ~?= False,
    "c sí es igual a alguna primera componente" ~: (hayQueCodificar 'd' [('b', 'c'), ('d', 'e'), ('f', 'g')]) ~?= True
 ]

ejercicio2 = test [
    "lista vacía" ~: (cuantasVecesHayQueCodificar 'a' ['h', 'o', 'l', 'a'] []) ~?= 0,
    "c aparece en frase y hayQueCodificar (c, mapeo) = false" ~: (cuantasVecesHayQueCodificar 'l' ['h', 'o', 'l', 'a'] [('b', 'c'), ('d', 'e'), ('f', 'g')]) ~?= 0,
    "c aparece en frase y hayQueCodificar (c, mapeo) = true" ~: (cuantasVecesHayQueCodificar 'l' ['h', 'l', 'o', 'l', 'a'] [('b', 'c'), ('l', 'e'), ('f', 'g')]) ~?= 2
 ]

ejercicio3 = test [
    "lista vacía" ~: (laQueMasHayQueCodificar ['h', 'o', 'l', 'a'] []) ~?= ' ',
    "un caracter aparece más que los otros en frase" ~: (laQueMasHayQueCodificar ['h', 'l', 'a', 'l', 'o', 'l', 'a'] [('b', 'c'), ('l', 'e'), ('a', 'g')]) ~?= 'l',
    "más de un caracter cumplen la condicion anterior" ~: (laQueMasHayQueCodificar ['h', 'a', 'l', 'o', 'l', 'a'] [('b', 'c'), ('l', 'e'), ('a', 'g')]) ~?= 'a'
 ]

ejercicio4 = test [
    "lista vacía" ~: (codificarFrase ['h', 'o', 'l', 'a'] []) ~?= "hola",  
    "ningun caracter cumple con hayQueCodificar = true" ~: (codificarFrase ['h', 'o', 'l', 'a'] [('b', 'c'), ('p', 'e'), ('m', 'g')]) ~?= "hola",
    "todos los caracteres cumplen con hayQueCodificar = true" ~: (codificarFrase ['h', 'o', 'l', 'a'] [('l', 'c'), ('h', 'e'), ('o', 'g'), ('a', 'm')]) ~?= "egcm",
    "algunos caracteres cumplen con hayQueCodificar = true" ~: (codificarFrase ['h', 'o', 'l', 'a'] [('a', 'b'), ('o', 'l'), ('d', 'e')]) ~?= "hllb"
 ]