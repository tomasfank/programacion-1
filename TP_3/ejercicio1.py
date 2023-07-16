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

def crearMatriz(filas, columnas):
    """ crea una matriz rellenar de 0 """
    matriz = list([0] * columnas for i in range(filas))
    return matriz

def rellenarMatriz(matriz):
    """ rellena la matriz con números aleatorios de 1 al 9 """
    #detectamos el tamaño de la matriz 
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            n = random.randint(1,9)
            matriz[i][j] = n
            
def imprimirMatriz(matriz):
    """ imprime la matriz de una fomra que facilite su lectura """
    #detectamos el tamaño de la matriz 
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end="  ")
        print()
        
def ordenarAscendente(matriz):
    """ ordena de fomra ascendente las filas de la matriz """
    for fila in matriz:
        fila.sort()
        
def intercambiarFilas(matriz, fila1, fila2):
    """ la función permite intercambiar dos filas de la matriz """ 
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def intercambiarColumnas(matriz, col1, col2):
    """ la función permite intercambiar dos columnas de la matriz """
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]
        
def transponerMatriz(matriz):
    """ la función transpone la matriz sobre si misma """
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            x = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = x
            
def calcularPromedio(matriz, prom):
    """ la función calcula el promedio de los valores de una fila """
    suma = sum(matriz[prom])
    cant = len(matriz[prom])
    promedio = suma / cant
    return promedio

def elementos_de_columna(matriz, columna):
    """ devuelve todos los elementos de una columna seleccionada """
    elementos = []
    cant = len(matriz[columna])
    for i in range(cant):
        elementos.append(matriz[i][columna])
    return elementos
    
    


#programa 
a = crearMatriz(4,4)
rellenarMatriz(a)
print("matriz desordenada")
imprimirMatriz(a)
print()

#ordenamos las filas de forma ascendente
print("filas ordenadas en forma ascendente")
ordenarAscendente(a)
imprimirMatriz(a)
print()

#intercambio de filas
print("intercambiamos filas")
intercambiarFilas(a, 1, 3)
imprimirMatriz(a)
print()

#intercambio de columnas
print("intercambiamos columnas")
intercambiarColumnas(a, 0, 3)
imprimirMatriz(a)
print()

#transponer matriz
print("Transponer matriz")
transponerMatriz(a)
imprimirMatriz(a)
print()

#calcular promedio de una fila
promedio = int(input("De que fila desea calcular el promedio? "))
print("el promedio de la fila seleccionada es", calcularPromedio(a, promedio))
print()

#calcular el porcentaje de números impares en una columna 
elegir_columna = int(input("De que columna desea calcular el porcentaje de impares?"))
elems = elementos_de_columna(a, elegir_columna) 
impares = 0
for x in elems:
    if x % 2 != 0:
        impares += 1
sacar_porcentaje = (100 * (impares / len(elems)))
print(f"{sacar_porcentaje}%")

#falta del h en adelante



