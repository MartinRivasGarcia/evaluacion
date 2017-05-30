import unittest
import ejercicio4

class testCasesEjercicio4(unittest.TestCase):
    def test_campeon_torneo_envioUnaPlanillaVacia_deberia_devolver_UnCampeonVacio(self):
        self.assertEqual("", ejercicio4.campeon_torneo([]))

    def test_envioUnPartidoCuyoGanadorEsa_deberia_devolver_a(self):
        self.assertEqual("a", ejercicio4.campeon_torneo([("a",1,"b",0)]))

    def test_envioTresPartidosDondeElmasGanadorEsc_deberia_devolver_c(self):
        self.assertEqual("c", ejercicio4.campeon_torneo([("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]))

    def test_envioUnTorneoDondeHayTodosEmpates_deberia_devolver_UnCampeonAleatoriamente(self):
        for a in range(0,10):
            self.assertIn(ejercicio4.campeon_torneo([("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]),["a","b","c"])

    def test_envioUnTorneoDondeElMasGanadorEsa_deberia_devolver_a(self):
        self.assertEqual("a", ejercicio4.campeon_torneo([("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]))