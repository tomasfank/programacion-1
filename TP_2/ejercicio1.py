""" Desarrolar cada una de las siguientes funciones y escribir un programa que permita verificar
su funcionamiento imprimiendo la lista luego de invocar a cada función:
    
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también
    será un número al azar de dos dígitos.
    
    b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
    
    c. Eliminar todas las apariciones de un valor en la lista anterior. El valor eliminado se
    ingresa desde el teclado y la función los recibe como parámetro.
    
    d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares.
    Un ejemplo de capicúa es [50, 17, 91, 17, 50]. """

import random

def  numerosAzar(n):
    lista = []
    for x in range(n):
        lista.append(random.randint(1000, 9999))
    return lista

def sumatoria(lista):
    sumatoria = 0
    for x in range(len(lista)):
        sumatoria += lista[x]
    return sumatoria

def eliminarNumero(lista, borrar):
    while borrar in lista:
        lista.remove(borrar)
    return lista
        

a = numerosAzar(5)
print(a)
b = sumatoria(a)
print(b)
c = eliminarNumero(a, 3245)
print(c)
