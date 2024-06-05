import Test.HUnit
import ParcialcomiC

main = runTestTT tests

tests = test [
    "no aprobo ninguna" ~: (aproboMasDeNMaterias [("juan",[1,2,3]),("maria",[2,2,1])] "maria" 2) ~?= False,
    "aprobo < n" ~: (aproboMasDeNMaterias [("juan",[1,2,3]),("luis",[4,2,1]),("maria",[2,2,1])] "luis" 2) ~?= False,
    "aprobo = n" ~: (aproboMasDeNMaterias [("juan",[1,2,3]),("maria",[6,4,1])] "maria" 2) ~?= False,
    "aprobo > n" ~: (aproboMasDeNMaterias [("juan",[8,7,10]),("maria",[2,2,1])] "juan" 2) ~?= True,
    "aprobo todas" ~: (aproboMasDeNMaterias [("juan",[10,10,10]),("luis",[4,2,1]),("maria",[2,2,1])] "juan" 2) ~?= True,

    "todos buenos alumnos" ~: (buenosAlumnos [("juan",[9,9,8]),("luis",[10,10,10]),("maria",[8,8,9])]) ~?= ["juan","luis","maria"],
    "todos malos alumnos" ~: (buenosAlumnos [("juan",[2,3,1]),("luis",[1,1,6]),("maria",[3,2,5])]) ~?= [],
    "uno es bueno y otro todo mal" ~: (buenosAlumnos [("juan",[2,3,1]),("luis",[9,9,9]),("maria",[3,2,5])]) ~?= ["luis"],
    "uno es bueno y otro tiene un aplazo" ~: (buenosAlumnos [("juan",[6,6,6]),("luis",[1,5,6]),("maria",[8,9,10]),("julieta",[1,1,1])]) ~?= ["maria"],
    "dos son buenos" ~: (buenosAlumnos [("juan",[9,9,10]),("luis",[1,1,6]),("maria",[8,8,8])]) ~?= ["juan","maria"],

    "uno tiene mejor promedio" ~: (mejorPromedio [("juan",[8,6,3]),("luis",[10,9,8]),("maria",[10,10,10])]) ~?= "maria",
    "dos tienen el mejor" ~: (mejorPromedio [("juan",[5,6,7]),("luis",[9,10,10]),("maria",[10,10,9])]) ~?= "luis",
    "todos son iguales" ~: (mejorPromedio [("juan",[7,5,6]),("luis",[5,6,7]),("maria",[6,5,7])]) ~?= "juan",

    "no cumple nada" ~: (seGraduoConHonores [("juan",[8,6,4]),("luis",[6,7,2]),("maria",[10,9,10])] 3 "luis") ~?= False,
    "cumple todo" ~: (seGraduoConHonores [("juan",[8,6,4]),("luis",[10,10,8]),("maria",[10,9,10])] 3 "luis") ~?= True,
    "solo cumple re1 1" ~: (seGraduoConHonores [("juan",[8,6,4]),("luis",[6,7,2]),("maria",[10,9,10])] 3 "luis") ~?= False,
    "solo cumple req 2" ~: (seGraduoConHonores [("juan",[8,6,4]),("luis",[8,8,8]),("maria",[10,9,10])] 3 "luis") ~?= False,
    "seGraduoConHonores koko" ~: seGraduoConHonores [("toto", [10, 10, 10, 3]), ("pedro", [4, 5, 6, 2, 2]), ("fer", [10, 5, 9, 4, 8]), ("pipo", [10, 10, 10, 3]), ("mati", [7,8,9]), ("koko", [9])] 1 "koko" ~?= True
    ]