""" La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del módulo math.
Escribir un programa que utilice esta función para calcular la raíz cuadrada de un número
cualquiera ingresado a través del teclado. El programa debe utilizar manejo de excepciones para
evitar errores si se ingresa un número negativo. """

import math

while True:
    try:
        a = input("Ingrese el número del que desea calcular la raíz cuadrada: ")
        if float(a) <= 0:
            raise AssertionError
        raiz = math.sqrt(float(a))
    except (ValueError, AssertionError):
        print("Error, ingrese nuevamente")
    else:
        print(f"La raíz cuadrada de {a} es {raiz}")
        break

        

