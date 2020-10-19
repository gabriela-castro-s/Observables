# Gabriela Castro Santamaria
# Librería numeros imaginarios
# CNYT

import math

def suma (num1, num2):
    """Funcion que suma dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans1 = num1[0] + num2[0]
    ans2 = num1[1] + num2[1]
    return (ans1, ans2)

def resta (num1, num2):
    """Funcion que resta dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans1 = num1[0] - num2[0]
    ans2 = num1[1] - num2[1]
    return (ans1, ans2)

def mult (num1, num2):
    """Funcion que multiplica dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans1 = num1[0]*num2[0] - num1[1]*num2[1]
    ans2 = num1[0]*num2[1] + num1[1]*num2[0]
    return (ans1, ans2)

def div (num1, num2):
    """Funcion que divide dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans1 = (num1[0]*num2[0] + num1[1]*num2[1])/(num2[0]**2 + num2[1]**2)
    ans2 = (num1[1]*num2[0] - num1[0]*num2[1])/(num2[0]**2 + num2[1]**2)
    return (ans1, ans2)

def modulo (num):
    """Funcion que regresa el modulo de un numero imaginario
    (list 1D) -> float"""
    ans = (num[0] ** 2 + num[1] ** 2) ** (1/2)
    return ans

def polar(num):
    """Funcion que convierte un numero imaginario a su forma polar
    (list 1D) -> list 1D"""
    ans1 = modulo(num)
    ans2 = math.atan2(num[1], num[0])
    return (ans1, ans2)

def polarc (num):
    """Funcion que convierte un numero imaginario en su forma polar a su forma cartesiana
    (list 1D) -> list 1D"""
    ans1 = num[0] * math.cos(num[1])
    ans2 = num[0] * math.sin(num[1])
    return (ans1, ans2)

def conjugado (num):
    """Funcion que retorna el conjugado de un numero imaginario
    (list 1D) -> list 1D"""
    num1 = num[1] * -1
    return (num[0], num1)


def sub(num1, num2):
    answ = [num1[0] - num2[0], num1[1] - num2[1]]
    return answ

#----------------------------------Calculadora de matrices y vectores imaginarios--------------------------------------

def sumav (v1, v2):
    """Funcion que suma dos vectores
    (list 1D, list 1D) -> list 1D"""
    ans = []
    for i in range(len(v1)):
        a = suma(v1[i], v2[i])
        ans.append(a)
    return ans

def inversoaditivo (v1):
    """Funcion que halla el inverso aditivo de un vector
    (list 1D) -> list 1D"""
    ans = []
    for i in range(len(v1)):
        ans.append((v1[i][0] * (-1), v1[i][1]*(-1)))
    return ans


def subVect(v1, v2):
    length = len(v1)
    if (length == len(v2)):
        for x in range(length):
            v1[x] = sub(v1[x], v2[x])
        return v1

def subMat(mat1, mat2):
    row, colum = len(mat1), len(mat1[0])
    for i in range(row):
        mat1[i] = subVect(mat1[i], mat2[i])
    return mat1

def multescalarvector (num1, v1):
    """Funcion que realiza la multiplicacion escalar entre un numero imaginario y un vector
    (list 1D, list 1D) -> list 1D"""
    ans = []
    for i in range(len(v1)):
        ans.append(mult(num1, v1[i]))
    return ans

def multescalarmatrices(num1,m1):
    """Funcion que realiza la multiplicacion escalar entre un numero imaginario y una matriz
    (list 1D, list 2D) -> list 2D"""
    ans = []
    for i in range(len(m1)):
        ans.append(multescalarvector(num1, m1[i]))
    return ans

def matriztranspuesta(m1):
    """Funcion que convierte una matriz en su forma transpuesta
    (list 2D) -> list 2D"""
    ans = []
    for j in range(len(m1[0])):
        ans.append([])
        for i in range(len(m1)):
            num1 = m1[i][j]
            ans[j].append(num1)
    return(ans)

def matrizconjugada(m1):
    """Funcion que convierte una matriz en su forma conjugada
    (list 2D) -> list 2D"""
    ans = []
    for i in range(len(m1)):
        bandera = []
        ans.append(bandera)
        for j in range(len(m1[i])):
            bandera.append([])
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            ans[i][j] = conjugado(m1[i][j])
    return ans

def adjmatriz(m1):
    """Funcion que convierte una matriz a su forma adjunta o daga
    (list 2D) -> list 2D"""
    return matrizconjugada(matriztranspuesta(m1))

def multivector(v1, v2):
    """Funcion que multiplica dos vectores, el proposito de esta funcion es facilitar la funcion multimatriz
    (list 1D) -> list 1D"""
    ans = []
    for i in range(len(v1)):
        ans.append(mult(v1[i], v2[i]))
    while len(ans) > 1:
        ans[0] = suma(ans[0], ans[-1])
        ans.pop()
    return ans[0]

def multimatriz(mat1, mat2):
    """Funcion que multiplica dos matrices
    (list 2D) -> list 2D"""
    row1, col1 = len(mat1), len(mat1[0])
    row2, col2 = len(mat2), len(mat2[0])

    if (col1 == row2):

        answ = [[(0, 0) for t in range(col2)] for x in range(row1)]

        for i in range(row1):
            for j in range(col2):

                current = (0, 0)

                for k in range(row2):
                    multi = mult(mat1[i][k], mat2[k][j])

                    current = suma(current, multi)

                answ[i][j] = current

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")

def sumacompvector(v1):
    """Funcion que suma los componentes de un vector, el proposito de esta funcion es facilitar la funcion accionmatrizvector
        (list 1D) -> list 1D"""
    if len(v1) < 2:
        return v1[0]
    elif len(v1) == 2:
        ans = suma(v1[0], v1[1])
        return ans
    else:
        ans = suma(v1[0], v1[1])
        for i in range(2, len(v1)):
            ans = suma(ans, v1[i])
        return ans

def accionmatrizvector(matrix, vector):
    """Funcion que realiza la accion de un vector sobre una matriz
    (list 2D, list 1D) -> list 1D"""
    row, col = len(matrix), len(matrix[0])
    length = len(vector)

    if (col == length):
        answ = [[0, 0] for x in range(row)]

        for i in range(row):
            for j in range(col):
                multi = mult(matrix[i][j], vector[j])
                answ[i] = suma(answ[i], multi)

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")

def innervector(v1,v2):
    """Funcion que calcula el producto interno entre dos vectores
    (list 1D, list 1D) -> list 1D"""
    ans = mult(v1[0], v2[0])
    for i in range(1, len(v1)):
        ans = suma(ans, mult(v1[i], v2[i]))
    return ans

def norma(v1):
    """Funcion que calcula la norma de un vector
    (list 1D) -> int"""
    suma = 0
    for i in range(len(v1)):
        suma += (v1[i][0]**2)+(v1[i][1]**2)
    ans = math.sqrt(suma)
    return ans

def distancia (v1,v2):
    """Funcion que calcula la distancia entre dos vectores
    (list 1D, list 1D) -> int"""
    ans = 0
    for i in range (len(v1)):
        v = resta(v1[i],v2[i])
        ans += v[0] **2 + v[1]**2
    c = ans ** 0.5
    return c


def identidadmatriz(filas, columnas):
    """Funcion que realiza la matriz identidad para determinado numero de filas y columnas, el proposito de esta funcion es ayudar all desarrollo de isUnitaria
    (int, int) -> list 2D"""
    c = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            val = 1 if i == j else 0
            fila.append(val)
        c.append(fila)
    return (c)

def isUnitaria(m1):
    """Funcion que define si una matriz es unitaria o no
    (list 2D) -> Boolean"""
    row, col = len(m1), len(m1[0])
    if row == col:
        adj = adjmatriz(m1)
        return (multimatriz(m1, adj) == identidadmatriz(row, col)) or (multimatriz(m1, adj) == multimatriz(adj, m1))
    
def isHermitiana(m1):
    """Funcion que define si una matriz es hermitiana o no
    (list 2D) -> Boolean"""
    if m1 == adjmatriz(m1):
        return True
    else:
        return False

def productotensor(m1, m2):
    """Funcion que realiza el producto tensor entre dos matrices
    (list 2D, list 2D) -> list 2D"""
    ans = []
    pj = 0
    for pi in range((len(m1) - 1) * 2):
        f1 = m1[pi]
        f2 = m2[pj]
        f = []
        for i in f1:
            for j in f2:
                f.append(mult(i, j))
        pj += 1
        f2 = m2[pj]
        ans.append(f)
        f = []
        for i in f1:
            for j in f2:
                f.append(mult(i, j))
        pj -= 1
        ans.append(f)
    return ans


def accionvectormatrizboolean(matrix, vector):
    row, col = len(matrix), len(matrix[0])
    length = len(vector)

    if (col == length):
        answ = [False for c in range(row)]

        for i in range(row):
            And = True

            for j in range(col):
                And = matrix[i][j] and vector[j]
                answ[i] = answ[i] or And

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")
