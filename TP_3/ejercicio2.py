""" Para cada una de las siguientes matrices, desarrollar una función que la genere y escribir
un programa que invoque a cada una de ellas y muestre por pantalla la matriz obtenida. El tamaño
de las matrices debe establecerse como NxN, y las funciones deben servir aunque este valor se
modifique.

    a) 1 | 0 | 0 | 0    b) 0 | 0 | 0 | 27    c) 4 | 0 | 0 | 0 
       0 | 3 | 0 | 0       0 | 0 | 9 | 0        3 | 3 | 0 | 0
       0 | 0 | 5 | 0       0 | 3 | 0 | 0        2 | 2 | 2 | 0
       0 | 0 | 0 | 7       1 | 0 | 0 | 0        1 | 1 | 1 | 1
 

"""

def imprimirMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print("%3d" %columna, end="")
        print()
        
def matrizA(tam):
    matriz = [[0]* tam for i in range(tam)]
    filas = len(matriz)
    columnas = len(matriz[0])
    x = 1
    for i in range(filas):
        for j in range(columnas):
            if i == j:
                matriz[i][j] = x
                x += 2
    return matriz
                
def matrizB(tam):
    matriz = [[0]* tam for i in range(tam)]
    filas = len(matriz)
    columnas = len(matriz[0])
    x = 3**(len(matriz)-1) 
    for i in range(filas):
        for j in range(columnas):
            if i + j == (len(matriz)-1):
                matriz[i][j] = x
                x //= 3
    return matriz

def matriz_con_escalera(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(i + 1):
            fila.append(j + 1)
        for j in range(i + 1, n):
            fila.append(0)
        matriz.append(fila)
    return matriz
                
                
                
            

#programa principal
tam = int(input("Que tamaño NxN desea que tenga la matriz? "))
print("punto a)")
imprimirMatriz(matrizA(tam))
print("punto b)")
imprimirMatriz(matrizB(tam))

print()
imprimirMatriz(matriz_con_escalera(tam))



            

            