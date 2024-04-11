""" 
Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:

**********                **
**********                ****
**********                ******
**********                ********
**********                **********

"""

# Funciones
def patronUno(f):
    for x in range(f):
        print("*" * (f*2))
        
def patronDos(f):
    for x in range(f):
        print("*" * ((x+1)*2))        

# Ejecución
print("Patron 1:")
patronUno(4)
print("Patron 2:")
patronDos(5)