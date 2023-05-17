""" Todo programa Python es susceptible a ser interrumpido mediane la pulsación de las teclas
Ctrl-C, lo que genera una excepción del tipo "KeyboardInterrupt". Realizar un programa para
imprimir los números entre 1 y 100000, y que solicite confirmación antes de detenerse cuando se
presione Ctrl-C. """

contador = 1
while contador <= 100000:
    try:
        print(contador, end=" ")
        contador += 1
    except KeyboardInterrupt:
        control = input("¿Desea dejar de contar: S/N?")
        if control.upper() == "S":
            break
    
