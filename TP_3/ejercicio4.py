"""
Una fabrica de bicicletas guarda en una matriz la cantidad de unidades producidas en cada
una de sus plantas durante una semana. De este modo, cada columna representa un díua de la
semana y cada fila representa una de sus fabricas.
    
    Se solicita:
        a) crear una matriz con datos generados al azar de N fabricas durante una semana,
        considerando que la capacidad máxima de fabricación es de 150 unidades por día y puede
        suceder que ciertos días no se fabrique ninguna.
        b) Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
        c) Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica)
        d) Cuál es el día más productivo, considerando todas las fabricas juntas.
        e) Crear una lista por comprensión que contenga la menor cantidad fabricada por cada
        fábrica.
"""

def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end="  ")
        print()
        
def rellenarMatriz(matriz):
    for filas in matriz[0]:
        for columnas in filas:
            columnas[0] = "fabrica1" 
            
        
    
        

#matriz de semana
matriz = [[0] * 6 for x in range(6)]
rellenarMatriz(matriz)
imprimirMatriz(matriz)