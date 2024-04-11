""" Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, solo si este es único  (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar tambien un programa para ingresar tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe. """

# Funciones 
def mayorDeTres(a,b,c):
    if b < a > c:
        return a 
    elif a < b > c:
        return b
    elif a < c > b:
        return c
    else:
        return -1

def ingresar():
    a = int(input("Ingresa el valor de 'a' = "))
    b = int(input("Ingresa el valor de 'b' = "))
    c = int(input("Ingresa el valor de 'c' = "))
    return a,b,c

# Programa
a, b, c = ingresar()  
resultado = mayorDeTres(a,b,c)
if resultado != -1:
    print("El mayor es estricto", resultado)
else:
    print("No existe mayor estricto")        
    
