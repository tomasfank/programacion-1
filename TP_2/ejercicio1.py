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

# Funciones
def cargaLista(lista):
    for i in range(random.randint(10,99)):
        lista.append(random.randint(1000,9999))
    
def sumatoria(lista):
    sumar = sum(lista)
    return sumar

def eliminaElemento(lista, elemento):
    while elemento in lista:
            lista.remove(elemento)

def capicua(lista):
    izq, der = 0,  len(lista) - 1
    while izq < der:
        if lista[izq] != lista[der]:
            return False
        izq += 1
        der -= 1
    return True
 

 # Ejecución 
lista = []

# a
cargaLista(lista)
print(lista)

# b
print(sumatoria(lista))

# c
eliminaElemento(lista, int(input("¿Qué elemento desea eliminar? = ")))
print(lista)

# d
lista1 =  [50, 17, 91, 17, 50] # Datos de prueba
print(capicua(lista1))
    