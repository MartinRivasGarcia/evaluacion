import unittest
import ejercicio3

def probarMatrizRandom(n):
    anterior = []
    iguales = 0
    distintos = 0
    for d in range(0,10):
        matriz = ejercicio3.matriz_triangular(n)

        for a in range(0, n):
            for c in range(0,a):
                if(matriz[a][c] != 0):
                    return False
            for b in range(a, n):
                if((matriz[a][b]<0) or (matriz[a][b]>9)):
                    return False

        if(anterior != []):
            for a in range(0, n):
                for b in range(a, n):
                    if ((matriz[a][b] == anterior[a][b]) or (matriz[a][b] == anterior[a][b])):
                        iguales = iguales + 1
                    else:
                        distintos = distintos + 1
            if(iguales > distintos):
                return False
            else:
                iguales = 0
                distintos = 0

        anterior = matriz
    return True

class testCasesEjercicio3(unittest.TestCase):
    def test_matrices_triangular_inexistentePorEnviarUnNumeroNegativo_deberia_devolver_vacio(self):
        self.assertEqual([], ejercicio3.matriz_triangular(-1))

    def test_EnvioUnCero_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular(0))

    def test_EnvioUnUno_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular(1))

    def test_EnvioUnDos_deberia_devolver_UnaMatrizDe2x2ConUnCeroDebajoDeLaDiagonal(self):
        self.assertTrue(probarMatrizRandom(2))

    def test_EnvioUnCuatro_deberia_devolver_UnaMatrizDe4x4ConCerosDebajoDeLaDiagonal(self):
        self.assertTrue(probarMatrizRandom(4))

    def test_EnvioUnNumeroMetidoEnUnString_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular("4"))

    def test_EnvioUnStringConTexto_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular("PEPE"))

    def test_EnvioUnNumeroDecimal_deberia_devolver_UnaMatrizVacia(self):
        self.assertEqual([], ejercicio3.matriz_triangular(2.5))