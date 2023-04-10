""" Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de
asteriscos, donde la cantidad de filas se recibe como parámetro:

**********                **
**********                ****
**********                ******
**********                ********
**********                **********

"""

#funciones 
def patronUno(filas):
    """ imprime 'x' cantidad de filas de 10 "*" """ 
    while filas > 0:
        for i in range(10):
            print("*", end="")
        filas -= 1
        print()
        
def patronDos(filas):
    """ imprime 'x' cantidad de filas de "*", incrementando la cantidad de los mismos de dos en dos """ 
    x = 0
    while filas > 0:
        x += 2
        for i in range(x):
            print("*", end="")
        filas -= 1
        print()
        
#programa de prueba
patronUno(3)
patronDos(5)
        
