""" Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene
80 columas. """

cadena = input("Ingrese una cadena de caracteres ")

espacio = (80 - len(cadena)) // 2

nueva_cadena = "-" * espacio + cadena + "-" * espacio

print(nueva_cadena)
print(len(nueva_cadena))
    
