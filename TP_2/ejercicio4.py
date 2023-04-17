""" Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista.
Imprimir la lista original, la lista de palabras a eliminar y la resultante """

#Arrays 
listaPalabras = ["pera", "tomate", "papa", "manzana", "cebolla"]

eliminarPalabras = ["pera", "manzana"]

listaResultante = []

#programa
for x in range(len(listaPalabras)):
    if listaPalabras[x] not in eliminarPalabras:
        listaResultante.append(listaPalabras[x])
        
print("Lista original =")       
print(listaPalabras, "\n")
print("Lista de objetos a eliminar =")
print(eliminarPalabras, "\n")
print("Lista resultante =")
print(listaResultante, "\n")