""" Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean
multiplos de 5. A y B se ingresan desde el teclado. """

def generarLista(a,b):
    lista = [x*7 for x in range(a,b) if x % 5 != 0]
    for i in range(len(lista)):
        print(lista[i], end=" ")

# Programa 
a = int(input("Ingresa A"))
b = int(input("Ingresa B"))
generarLista(a,b)