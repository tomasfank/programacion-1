"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar
su funcionamiento, imprimiendo la matriz luego de invocar cada función

    a) Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.
    b) Ordenar en  fomra ascendente cada una de las filas de la matriz.
    c) Intercambiar dos filas dadas, cuyos números se reciben como parámetro.
    d) Intercambiar dos columnas, cuyos números se reciben como parámetro.
    e) Trasponer la matriz sobre si misma (intercambiar cada elemento Aij por Aji).
    f) Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
    g) Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe
    como parámetro.
    h) Determinar si la matriz es simétrica con respecto a su diagonal principal.
    i) Determinar si la matriz es simétrica con respecto a su diagonar secundaria.
    j) Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con
    los números de las mismas.
    
NOTA = El valor N debe leerso por teclado. Las funciones deben servir cualquiera sea el valor
ingresado
"""

import random

# Básicos
def generarMatriz(fil, col):
    matriz = [[0] * col for i in range(fil)]
    return matriz    

def rellenarMatriz(matriz):
    fil = len(matriz)
    col = len(matriz[0])
    for f in range(fil):
        for c in range(col):
            matriz[f][c] = random.randint(1,9)    

def imprimirMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end="  ")
        print(" ")
    print(" ")

# a)
def cargarEnteros(n):
    matriz = [[0] * n for i in range(n)]
    rellenarMatriz(matriz)
    return matriz

# b) 
def ordenarFilas(n):
    matriz = [[0] * n for i in range(n)]
    rellenarMatriz(matriz)
    for fila in matriz:
        fila.sort()
    return matriz

# c) 
def intercambiarfilas(n,f1,f2):
    matriz = [[0] * n for i in range(n)]
    rellenarMatriz(matriz)
    imprimirMatriz(matriz)
    matriz[f1], matriz[f2] = matriz[f2], matriz[f1]
    return matriz

# d)
def intercambiarColumnas(n,c1,c2):
    matriz = [[0]*n for i in range(n)]
    rellenarMatriz(matriz)
    imprimirMatriz(matriz)
    for fila in matriz:
        fila[c1], fila[c2] = fila[c2], fila[c1]
    return matriz

# e)
def transponer(n):
    matriz = [[0]*n for i in range(n)]
    rellenarMatriz(matriz)
    imprimirMatriz(matriz)
    for i in range(len(matriz)):
        for j in range(i, len(matriz[0])):
            x = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = x
    return matriz

# f) 
def promedioFila(n, f):
    matriz = [[0] * n for i in range(n)]
    rellenarMatriz(matriz)
    imprimirMatriz(matriz)
    promedio = sum(matriz[f]) / len(matriz[f])
    print(f"El promedio de la fila {f+1} es de {promedio}")

# g)
def promedioImpares(n, c):
    matriz = [[0] * n for i in range(n)]
    rellenarMatriz(matriz)
    imprimirMatriz(matriz)
    suma = 0
    for i in range(len(matriz)):
        if matriz[i][c] % 2 == 1:
            suma += matriz[i][c]
    print(f"El promedio de impares de la columna {c+1} es de {suma / len(matriz[0])}")

# Pruebas
print("Punta a)")
a = cargarEnteros(4)
imprimirMatriz(a)

print("Punto b)")
b = ordenarFilas(5)
imprimirMatriz(b)

print("Punto c)")
c = intercambiarfilas(5,1,2)
print("Filas intercambiadas")
imprimirMatriz(c)

print("Punto d)")
d = intercambiarColumnas(4,0,3)
print("Columnas intercambiadas")
imprimirMatriz(d)

print("Punto e)")
e = transponer(4)
print("Matriz transpuesta")
imprimirMatriz(e)

print("Punto f)")
f = promedioFila(5, 2)

print("Punto g)")
g = promedioImpares(4,2)
