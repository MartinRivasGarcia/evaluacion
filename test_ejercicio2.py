import unittest
import ejercicio2

class testCasesEjerccio2(unittest.TestCase):
    def test_formato_admitido_envioFormatoQueNoCoincide_deberia_devolver_False(self):
        self.assertFalse(ejercicio2.formato_admitido('/home/user/listado.txt',['mp3','wav','mpeg']))

    def test_formato_admitido_envioFormatoQueCoincide_deberia_devolver_True(self):
        self.assertTrue(ejercicio2.formato_admitido('/home/user/listado.txt',['mp3','wav','mpeg','txt']))
    def test_formato_admitido_envioUnFoormatoQueEstaEnListaPeroEnMayuscula_deberia_devolver_True(self):
        self.assertTrue(ejercicio2.formato_admitido('/home/user/listado.txt',['mp3','wav','mpeg','TXT']))

    def test_formato_admitido_envioUnFormatoConUnaMayusculaQueEstaEnLaListaEnMinuscula__deberia_devolver_True(self):
        self.assertTrue(ejercicio2.formato_admitido('/home/user/listado.tXt',['mp3','wav','mpeg','TXT']))

    def test_formato_admitido_envioFormatoQueCoincide_deberia_devolver_True(self):
        self.assertTrue(ejercicio2.formato_admitido('/home/user/listado.txt',['txt']))

    def test_formato_admitido_envioUnaDireccioonSinFormato_deberia_devolver_False(self):
        self.assertFalse(ejercicio2.formato_admitido('/home/user/listado',['mp3','wav','mpeg','txt']))

    def test_formato_admitido_envioUnaDireccionPeroNoUnaLista_deberia_devolver_False(self):
        self.assertFalse(ejercicio2.formato_admitido('/home/user/listado',[]))

    def test_formato_admitido_envioTantoListaComoDireccionVacia_deberia_devolver_False(self):
        self.assertFalse(ejercicio2.formato_admitido('',[]))