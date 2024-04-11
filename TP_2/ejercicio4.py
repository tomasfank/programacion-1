""" Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista.
Imprimir la lista original, la lista de palabras a eliminar y la resultante """

# Funciones
def eliminarIguales(lista1, lista2):
    lista3 = list(lista1)
    for i in range(len(lista2)):
        if lista2[i] in lista1:
            lista3.remove(lista2[i])
    return lista3

# Programa 
lista1 = ["Hola","Pera","Taza","Calculadora","Cuaderno"]

lista2 = ["Pera","Calculadora"]

resultante = eliminarIguales(lista1, lista2)

print(lista1)
print("")
print(lista2)
print("")
print(resultante)