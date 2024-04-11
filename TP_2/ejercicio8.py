""" Utilizar la técnica de listas por comprensión para construir una lista con todos los números
impares comprendidos entre 100 y 200 """

#  Lista por comprensión
lista = [x+1 for x in range(5)] # Crea una lista de números del 1 al 5
print(lista)

lista2 = [(x+1)**2 for x in range(10)] # Crea una lista de los cuadrados del 1 al 10
print(lista2)

lista3 = [x+1 for x in range(100) if x % 2 != 0] # Crea una lista de números pares entre 1 y 100
print(lista3)