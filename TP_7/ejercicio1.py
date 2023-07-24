""" Escribir una función que devuelva la cantidad de dígitos de un número entero, sin utilizar
cadenas de caracteres. """

def recursiva(num):
    if num == 0:
        return 0
    else:
        return 1 + recursiva(num//10)
    
#programa
a = recursiva(123456789)
print(a)
        
        
    