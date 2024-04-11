""" Crear una lista con los cuadrados de los números entre 1 y N (ambos incuidos), donde N se
ingresa desde el teclado. Luego se solicita imprimir los útlimos 10 valores de la lista """

# Funciones
def listaCuadrados(lista, n):
    for i in range(1, n+1):
        lista.append(i**2)


# Programa
lista = [] 
listaCuadrados(lista, int(input("Ingrese el valor de N = ")))

print(lista)

der = len(lista) - 1

for i in range(10):
    print(lista[der], end=" ")
    der -= 1





