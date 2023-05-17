""" Escribir un programa que juegue con el usuario a adivinar un número. El programa debe generar
un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para eso, cada vez que se introduce
un valor se muestra un mesnaje indicando si el número que tiene que adivinar es mayor o menor que
el ingresado. Cuando se consiga adivinarlo, se debe imprimir en pantalla la cantidad de intentos
que le tomó hallar el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más. """

import random

nro = random.randint(1, 500)
print(nro) #pista guiño guiño
intentos = 0 
while True:
    try:
        adivina = input("¿Cúal crees que es el número? ")
        if int(adivina) > nro:
            intentos += 1
            print(f"El número es menor que {adivina}. Llevas {intentos} intentos")
        elif int(adivina) < nro:
            intentos += 1
            print(f"El número es mayor que {adivina}. Llevas {intentos} intentos")
        else:
            print("Es correcto! Has adivinado.")
            print(f"Has tardado {intentos} intentos en adivinar.")
            break
    except ValueError:
        intentos += 1
        print(f"Dato inválido!. Llevas {intentos} intentos")
        
        



