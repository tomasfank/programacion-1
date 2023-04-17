""" Escribir una función que reciba una lista como parámetro y devuelva True si la lista esta
ordenada en forma ascendente o False en caso contrario. Por ejemplo,  ordenada([1,2,3]) retorna
True y ordenada(['b','a']) retorna False. Desarrollar además un programa para verificar el
comportamiento de la función """

def listaOrdenada(lista):
    """ la función recibe una lista (ordenada o desordenada), la ordena en forma ascendente y compara si la lista que ordenó es igual a la que recibió """  
    ordenada = False
    nuevaLista = sorted(lista) 
    if nuevaLista == lista:
        ordenada = True
    return ordenada


#valores de prueba 
a = [1,2,3,4]
b = ["a", "b", "c"]
c = [4,3,2,1]
d = ["c","b","a"]

#programa de prueba
inicio = listaOrdenada(d)
print(inicio)