import unittest
import ejercicio1

class testCasesEjerccio1(unittest.TestCase):
    def test_divisores_de_vacio_deberia_devolver_vacio(self):
        self.assertEqual([],ejercicio1.divisores_de_un_numero("",[1,2,3]))

    def test_divisores_de_menosUno_deberia_devolver_vacio(self):
        self.assertEqual([],ejercicio1.divisores_de_un_numero(-1,[1,2,3]))

    def test_divisores_de_cero_deberia_devolver_vacio(self):
        self.assertEqual([], ejercicio1.divisores_de_un_numero(0,[1,2,3]))

    def test_divisores_vacio_de_cero_deberia_devolver_vacio(self):
        self.assertEqual([],ejercicio1.divisores_de_un_numero(0,[]))

    def test_divisores_de_uno_deberia_devolver_uno(self):
        self.assertEqual([1], ejercicio1.divisores_de_un_numero(1, [1,2]))

    def test_divisores_de_dos_deberia_devolver_unoYmenosDos(self):
        self.assertEqual([1,-2], ejercicio1.divisores_de_un_numero(2, [1,-2]))

    def test_divisores_de_ocho_deberia_devolver_uno_dosYmenosCuatro(self):
        self.assertEqual([1,2,-4], ejercicio1.divisores_de_un_numero(8, [1,7,2,-4,6,9]))

    def test_divisores_de_un_numero_primo_deberia_devolver_elNumero_Uno(self):
        self.assertEqual([1,331], ejercicio1.divisores_de_un_numero(331, [1,2,3,7,147,331,518]))