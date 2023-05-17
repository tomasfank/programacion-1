""" Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números
reales, sume ambos valores y devuelva el resultado como un número real. Devolver -1 si alguna
de las cadenas no contiene un número válido, utilizando el manjeo de excepciones. """

def sumaReales(cad1, cad2):
    try:
        suma = float(cad1) + float(cad2)
    except ValueError:
        suma = -1
    return suma
   
        
    
#programa
a = input("Ingrese el primer número ")
b = input(f"¿Que número desea sumar a {a}? ")
print(sumaReales(a, b))
        