""" Desarrollar un programa para rellenar una matriz de NxN con números enteros al azar
comprendidos en el intervalo [0,N^2), de tal fomra que ningún número se repita. Imprimir la
matriz por pantalla """

import random

def imprimirMatriz(matriz):
    for filas in matriz:
        for elementos in filas:
            print("%02d" %elementos, end=" ")
        print()
        
def rellenarMatriz(matriz):
    matriz_aux = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elem = random.randint(0,(len(matriz)**2))
            while elem in matriz_aux:
                elem = random.randint(0,(len(matriz)**2))
            else:
                matriz[i][j] = elem
                matriz_aux.append(elem)
                     
#programa             
n = int(input("Tamaño de la matriz = "))             
matriz = [[0] * n for i in range(n)]
rellenarMatriz(matriz)
imprimirMatriz(matriz) 