""" Escribir una función que reciba una lista como parámetro y devuelva True si la lista esta
ordenada en forma ascendente o False en caso contrario. Por ejemplo,  ordenada([1,2,3]) retorna
True y ordenada(['b','a']) retorna False. Desarrollar además un programa para verificar el
comportamiento de la función """

# Funciones
def estaOrdenada(lista):
    for i in range(1,len(lista)):
        if lista[i] < lista[i-1]:
            return False
    return True

# Programa 
lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [1,3,2,4,5,7,6,8,9]
lista3 = [1,1,2,3,4,5,6,7,8]

print(estaOrdenada(lista1))
print(estaOrdenada(lista2))
print(estaOrdenada(lista3))