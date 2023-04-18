""" Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los elementos
de la primera que sean impares. El proceso deberá realizarse utilizando listas por comprensión.
Imprimir las dos listas por pantalla. """

import random

lista1 = [random.randint(1, 100) for x in range(50)]

lista2 = list(lista1[x] for x in range(len(lista1)) if lista1[x] % 2 != 0) 

print("Lista completa = ")
print(lista1,"\n")
print("Lista impares = ")
print(lista2)