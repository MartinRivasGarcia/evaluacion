import unittest
import ejercicio3

def probarMatrizRandom(n):
    matriz = ejercicio3.matriz_triangular(n)

    for a in range(0, n):
        for c in range(0,a):
            if(matriz[a][c] != 0):
                return False
        for b in range(a, n):
            numero = random.randint(0, 9)
            matriz[a].insert(b, numero)

class testCasesEjercicio3(unittest.TestCase):
    def test_matrices_triangular_inexistentePorEnviarUnNumeroNegativo_deberia_devolver_vacio(self):
        self.assertEqual([], ejercicio3.matriz_triangular(-1))

    def test_EnvioUnCero_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular(0))

    def test_EnvioUnUno_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular(1))

    #No se puede realizar pruebas random
    #def test_EnvioUnDos_deberia_devolver_UnaMatrizDe2x2ConUnCeroDebajoDeLaDiagonal(self):
        #self.assertEqual([[type(int),type(int)],[0,type(int)]], ejercicio3.matriz_triangular(2))   No se como probar lo de numero aleatorio
        #self.assertIn(ejercicio3.matriz_triangular(2),[[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],[[0],[1,2,3,4,5,6,7,8,9]]])

    #def test_EnvioUnCuatro_deberia_devolver_UnaMatrizDe4x4ConCerosDebajoDeLaDiagonal(self):
        #self.assertEqual([[x,x,x,x],[0,x,x,x],[0,0,x,x],[0,0,0,x]], ejercicio3.matriz_triangular(4))

    def test_EnvioUnNumeroMetidoEnUnString_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular("4"))

    def test_EnvioUnStringConTexto_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular("PEPE"))

    def test_EnvioUnNumeroDecimal_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular(2.5))