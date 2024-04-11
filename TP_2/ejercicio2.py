""" Escribir funciones para:
    
    a. Generar una lista de 50 números aleatorios del 1 al 100.
    
    b. Recibir una lista como parámetro y devolver True si la misma contiene algun elemento
    repetido. La función no debe modificar la lista.
    
    c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de
    la lista original, sin importar el orden.
    
Combinar estas tres funciones en un mismo programa """

import random

# Funciones
def generarLista(lista):
    for i in range(50):
        lista.append(random.randint(1,100))

def tieneRepetidos(lista):
    aux = []
    for i in range(len(lista)):
        if lista[i] in aux:
            return True
        aux.append(lista[i])
    return False

def elementosUnicos(lista):
    aux = []
    for i in range(len(lista)):
        if lista[i] not in aux:
            aux.append(lista[i])
    return aux

# Programa
lista = []
generarLista(lista)
print(lista)

print(tieneRepetidos(lista))

listaUnica = elementosUnicos(lista)
print(listaUnica)