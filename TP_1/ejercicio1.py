"""
Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, solo si este es único  (mayor estricto).
En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar tambien un programa para
ingresar tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe
"""

#funciones
def devolverMayor(num1=0, num2=0, num3=0):
    """ la función devuelve el mayor de tres valores o -1 si no existe """
    mayor = 0
    if num2 < num1 > num3:
        mayor = num1
    elif num1 < num2 > num3:
        mayor = num2
    elif num1 < num3 > num2:
        mayor = num3
    else:
        mayor = -1
    return mayor

def leerNumeros():
    """ lee un numero ingresado por teclado y los devuelve en fomra de tres enteros """
    numero1 = int(input("Ingrese el primer valor "))
    numero2 = int(input("Ingrese el segundo valor "))
    numero3 = int(input("Ingrese el tercer valor "))
    return numero1, numero2, numero3
    
#programa principal
n1, n2, n3 = leerNumeros()
numMayor = devolverMayor(n1, n2, n3)
if numMayor > 0:
    print("El número mayor estricto de los tres es = ", numMayor)
else:
    print("No se ha encontrado mayor estricto")

        
    
