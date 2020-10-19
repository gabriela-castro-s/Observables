import unittest
from Teoriacuantica import *

sx = [[0, 1],
      [1, 0]]
sy = [[0, -1j],
      [1j, 0]]
sz = [[1, 0],
      [0, -1]]

def ans4_3_1(observable):
    """PRE: ingresa uno de los  tres spin operators
       POST: retorna los posibles estados que el spin puede transitar despues de ser observado"""
    x, v = EigenValues(observable)
    answ = []
    for el in v:
        current = translateEightnVector(el)
        answ.append(current)
    return answ

def ans4_3_2(observable):
    """PRE: ingresa uno de los  tres spin operators
       POST: retorna la media de la distribucion del spin ingresado"""
    shi = [[1, 0], [0, 0]]
    x, v = EigenValues(observable)

    meanValueDistribution = [0, 0]
    for i in range(len(x)):
        eigenValue = translateValues(x[i])
        eigenVector = translateEightnVector(v[:, i])

        prob = mult(eigenValue, [longitud([transicion(eigenVector, shi)]) ** 2, 0])

        meanValueDistribution = suma(meanValueDistribution, prob)
    return meanValueDistribution

class observableTest(unittest.TestCase):

    def testExercice4_3_1(self):
        self.assertEqual(ans4_3_1(sx), [[[0.7071067811865475, 0.0], [-0.7071067811865475, 0.0]],
                                                     [[0.7071067811865475, 0.0], [0.7071067811865475, 0.0]]])
        self.assertEqual(ans4_3_1(sy), [[[-0.0, -0.7071067811865474], [0.7071067811865475, 0.0]],
                                                     [[0.7071067811865476, 0.0], [0.0, -0.7071067811865475]]])
        self.assertEqual(ans4_3_1(sz), [[[1.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [1.0, 0.0]]])

    def testExercice4_3_2(self):
        self.assertEqual(ans4_3_2(sx), (0.0, 0.0))
        self.assertEqual(ans4_3_2(sy), (-2.7755575615628914e-16, 0.0))
        self.assertEqual(ans4_3_2(sz), (1.0, 0.0))

    def testExercice4_4_1(self):
        raiz = math.sqrt(2) / 2
        u1 = [[[0, 0], [1, 0]], [[1, 0], [0, 0]]]
        u2 = [[[raiz, 0], [raiz, 0]], [[raiz, 0], [-raiz, 0]]]
        self.assertEqual(isUnitaria(u1), True)
        self.assertEqual(isUnitaria(u2), True)
        self.assertEqual(isUnitaria(multimatriz(u1, u2)), True)
        self.assertEqual(isUnitaria(multimatriz(u1, u2)), True)

    def testExercice4_4_2(self):
        raiz = 1 / math.sqrt(2)
        vectIni = [[1, 0], [0, 0], [0, 0], [0, 0]]
        matrix = [[[0, 0], [raiz, 0], [raiz, 0], [0, 0]],
                  [[0, raiz], [0, 0], [0, 0], [raiz, 0]],
                  [[raiz, 0], [0, 0], [0, 0], [0, raiz]],
                  [[0, 0], [raiz, 0], [-raiz, 0], [0, 0]]]
        self.assertEqual(sistemaprobabilisticoquantico(matrix, vectIni, 3),
                         [[[0.4999999999999996, 0], [0.0, 0], [0.0, 0], [0.4999999999999996, 0]],
                          [[0.0, 0], [0.4999999999999996, 0], [0.4999999999999996, 0], [0.0, 0]],
                          [[0.0, 0], [0.4999999999999996, 0], [0.4999999999999996, 0], [0.0, 0]],
                          [[0.4999999999999996, 0], [0.0, 0], [0.0, 0], [0.4999999999999996, 0]]])


if __name__ == '__main__':
    unittest.main()
