""" Escribir una función que reciba una lista de números enteros como parámetro y la normalice,
es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada
elemento tiene el la lista original. Desarrollar también un programa que permita verificar
el comportamiento de la función. Por ejemplo, normalizar([1,1,2]) debe devolver normalizar([0.25, 0.25, 0.50])"""

# Funciones 
def normalizar(lista):
    suma = sum(lista)
    normalizada = []
    for i in range(len(lista)):
        operacion = lista[i] / suma 
        normalizada.append(operacion)
    return  normalizada

# Programa 
lista = [1,2,2]
normalizada = normalizar(lista)

print(f"La lista original es = {lista}")
print(f"La lista normalizada es = {normalizada}")
