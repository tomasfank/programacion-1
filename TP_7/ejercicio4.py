""" Escribir una función que devuelva el resto de dos números enteros por
sumas sucesivas. """

def producto(num1,num2):
    if num2 == 1:
        return num1
    else:
        return num1 + producto(num1, num2 - 1)
    
#programa
numero_1 = 4
numero_2 = 5
print(f"{numero_1} x {numero_2} = {producto(numero_1, numero_2)}")