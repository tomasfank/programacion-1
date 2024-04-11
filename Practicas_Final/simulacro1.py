def imprimirMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=" ")
        print("")

def cuadradoMagico(matriz):
    suma = sum(matriz[0]) # Suma de la primera fila
    for i in range(len(matriz)):
        if sum(matriz[i]) != suma or sum(fila[i] for fila in matriz) != suma:
            return False

    diagonal_principal = [matriz[i][i] for i in range(len(matriz))]
    diagonal_secundaria = [matriz[i][len(matriz) - i - 1] for i in range(len(matriz))] 
    if sum(diagonal_principal) != suma or sum(diagonal_secundaria) != suma:
        return False
       
    return True


matriz = [[4,3,8],[9,5,1],[2,7,6]]
imprimirMatriz(matriz)
print(cuadradoMagico(matriz))
# secuencia(matriz[0])
