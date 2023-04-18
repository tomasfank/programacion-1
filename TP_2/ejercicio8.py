""" Utilizar la técnica de listas por comprensión para construir una lista con todos los números
impares comprendidos entre 100 y 200 """

#creamos la lista
numerosImpares = [x for x in range(100,200) if x % 2!= 0]

#Imprimimos 
print(numerosImpares)