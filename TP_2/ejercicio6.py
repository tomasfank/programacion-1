""" Escribir una función que reciba una lista de números enteros como parámetro y la normalice,
es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada
elemento tiene el la lista original. Desarrollar también un programa que permita verificar
el comportamiento de la función. Por ejemplo, normalizar([1,1,2]) debe devolver normalizar([0.25, 0.25, 0.50])"""

def normalizar(lista):
    """ la función recibe una lista de números enteros y los normaliza """ 
    # Calculamos la suma de todos los elementos de la lista
    suma = sum(lista)
    normalizados = []
    # Creamos una nueva lista con los elementos normalizados
    for x in range(len(lista)):
        operacion = lista[x] / suma
        normalizados.append(operacion)
    return normalizados

# programa de prueba
lista_original = [1, 3, 6]
lista_normalizada = normalizar(lista_original)
print("La lista original es:", lista_original)
print("La lista normalizada es: ", lista_normalizada)