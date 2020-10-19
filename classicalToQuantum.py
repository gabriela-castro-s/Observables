import matplotlib.pyplot as plot
import numpy as np
from calculadora_imaginarios import *

def finalMatrix(matrix):
    """Función que halla la magnitud de una matriz de imaginarios
    (list 2D) -> list 2D"""
    row, column = len(matrix), len(matrix[0])
    for i in range(row):
        nRow = []
        for j in range(column):
            nRow.append([(modulo(matrix[i][j]) ** 2), 0])

        matrix[i] = nRow
    return matrix


def sistemaprobabilisticoquantico(matrix, vectIni, clicks):
    """Función que simula un sistema probabilistico cuantico
    (list 2D, list 1D, int) -> list 2D"""
    if (clicks >= 0) and (type(clicks) is int):
        length = len(vectIni)
        copyMatrix = matrix[:]

        for x in range(clicks):
            matrix = multimatriz(matrix, copyMatrix)

        return finalMatrix(matrix)
    return -1


def sistemaprobabilistico(matrix, vectIni, clicks):
    """Función que simula un sistema probabilistico clasico
        (list 2D, list 1D, int) -> list 1D"""
    if (clicks >= 0) and (type(clicks) is int):
        length = len(vectIni)
        for x in range(clicks):
            vectIni = accionmatrizvector(matrix, vectIni)
        return vectIni
    return -1


def canicasbooleanas(clicks, booleanMatrix, vectIni):
    """Funcion que simula experimento de canicas con coeficientes booleanos
    (int, list 2D boolean, list 1D) -> list 1D"""
    if (clicks >= 0 and type(clicks) is int):
        for c in range(clicks):
            vectIni = accionvectormatrizboolean(booleanMatrix, vectIni)

        return vectIni


def multiplerendijaclasico(matrix, vectIni, clicks):
    """Función que simula el experimento de multiples rendijas clasico
    (list 2D, list 1D, int) -> list 2D"""
    return sistemaprobabilistico(matrix, vectIni, clicks)


def multiplerendijacuantico(matrix, vectIni, clicks):
    """Función que simula el experimento de multiples rendijas cuantico
        (list 2D, list 1D, int) -> list 2D"""
    return sistemaprobabilisticoquantico(matrix, vectIni, clicks)


def grafico(vector):
    """Funcion que grafica un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen puede
    guardarse en el computador.
    (list 1D) -> None"""
    data = len(vector)
    x = np.array([x for x in range(data)])
    y = np.array([round(vector[x][0] * 100, 2) for x in range(data)])

    plot.bar(x, y, color='b', align='center')
    plot.title('Probabilidades vector')
    plot.show()
