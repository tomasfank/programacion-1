""" Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean
multiplos de 5. A y B se ingresan desde el teclado. """

#creamos una función 
def generarLista(a,b):
    """ La función recibe dos números enteros (a y b) y crea una lista con todos los números multiplos de 7 que no sean multiplos de 5 comprendidos entre a y b """ 
    lista = []
    for x in range(a+1 , b+1):
        if x % 7 == 0 and not x % 5 == 0:
            lista.append(x)
    return lista

#programa principal

#Solicitamos los valores 
A = int(input("Ingresar en primer número"))
B = int(input("Ingresar el segundo número"))
#Ejecutamos la función
inicio = generarLista(A,B)
#Imprimimos el resultado 
print(inicio)