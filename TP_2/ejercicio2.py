""" Escribir funciones para:
    
    a. Generar una lista de 50 números aleatorios del 1 al 100.
    
    b. Recibir una lista como parámetro y devolver True si la misma contiene algun elemento
    repetido. La función no debe modificar la lista.
    
    c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de
    la lista original, sin importar el orden.
    
Combinar estas tres funciones en un mismo programa """

import random 

def numerosAzar(x):
    lista = []
    for i in range(x):
        lista.append(random.randint(1, 100))
    return lista

def repetidos(lista):
    r = False
    for x in range(len(lista)):
        if lista.count(lista[x]) > 1:
            r = True
    return r

def sinRepetidos(lista):
    listaNueva = []
    for i in range(len(lista)):
        if lista[i] not in listaNueva:
            listaNueva.append(lista[i])
    return listaNueva

#programa principal
a = numerosAzar(50)
print(a)
b = repetidos(a)
if b == True:
    print("La lista contiene elementos repetidos")
    c = sinRepetidos(a)
    print(c)
    #para facilitar el análisis imprimo las listas nuevamente, pero de manera ordenada
    print()
    a.sort()
    c.sort()
    print(a) 
    print(c)
else:
    print("La lista no contiene elementos repetidos")

