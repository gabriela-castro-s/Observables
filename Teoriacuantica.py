from sys import stdin
from classicalToQuantum import *
import numpy as np

def dosdecimales(num, undecimal):
    num = "{:.2f}".format(num)
    num = (num[:-1] if undecimal else num)
    return float(num)


def longitud(vect):
    """Calcula la longitud de un vector dado"""
    acu = 0
    for x in range(len(vect)):
        acu += (modulo(vect[x])) ** 2
    return math.sqrt(acu)


def normalizar(vect):
    """normaliza un vector dado """
    length = longitud(vect)
    for x in range(len(vect)):
        vect[x] = [vect[x][0] / length, vect[x][1] / length]
    return vect


def bra(vect):
    """Devuelve el bra de un vector dado"""
    return adjmatriz(vect)


def transicion(vect1, vect2):
    """Nos dice cuanto es la transicion de un vector a otro"""
    return multivector(vect1, vect2)


def probability(vector, position):
    """Calcula la probabilidad de que un vector este en el estado dado( posicion )"""
    lon = longitud(vector)
    if (0 <= position < len(vector)):
        return dosdecimales(modulo(vector[position]) ** 2 / lon ** 2, False)


def omegaPsi(psi, omega):
    return innervector(accionmatrizvector(omega, psi), psi)[0]


def deltaPsi(omega, expectedValue):
    return subMat(omega, multescalarmatrices(expectedValue, identidadmatriz(len(omega),len(omega[0]))))


def matrixPsi(matrix, psi):
    accionmatrizvector(matrix, adjmatriz(psi))
    vect = accionmatrizvector(matrix, adjmatriz(psi))
    return dosdecimales(multivector(vect, adjmatriz(psi))[0], False)


def variance(psi, omega):
    expectedValue = dosdecimales(omegaPsi(psi, omega), True)
    delta = deltaPsi(omega, [expectedValue, 0.0])
    matrixOfVariance = multimatriz(delta, delta)
    return matrixPsi(matrixOfVariance, psi)


def describeAnObservable(psi, matrix):
    if (isHermitiana(matrix)):
        mean = dosdecimales(omegaPsi(psi, matrix), True)
        return [variance(psi, matrix), mean]
    return None


def translateEightnVector(vector):
    """Traduce todos los valores propios de la libreria numpy a nuestra libreria"""
    answ = []
    for el in vector:
        answ.append([el.real, el.imag])
    return answ


def translateValues(val):
    """Traduce todos los valores propios de la libreria numpy a nuestra libreria"""
    return [val.real, val.imag]


def EigenValues(omega):
    observable = np.array(omega)
    x, v = np.linalg.eig(observable)
    return x, v
