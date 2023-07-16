""" Desarolle un programa que permita reazliar reservas en una sala de cine de barrio con N filas y M columnas por cada fila. Desarrollar las siguientes funciones y utilizarlas en un mismo programa:

    + mostrar_butacas: mostrará por pantalla el estado de cada una de las butacas del cine. Se deberá mostrar antes de que el usuario realice la reserva y se volverá a mostar luegho de la misma, con los estados actualizados

    + reservar: deberá recibir una matriz y la butaca seleccionada, y actualizará la matriz en caso de estar disponible dicha butaca. La función devolverá True/False si logro o no reservar la butaca.

    + cargar_sala: recibirá una matriz como parámetro y la cargará con valores aleatorios para simular una sala con butacas ya reservadas.

    + butacas_libres: recibirá como parámetro la matriz y retornará cuántas butacas desocupadas hay en la sala.

    + butacas_contiguas: buscará la secuencia más larga de butacas libres contiguas en una misma fila y devolverá las coordenadas de inicio de la misma."""


import random

def mostrar_butacas(sala):
    for fila in sala:
        for butaca in fila:
            if butaca == 0:
                print("L", end=" ")
            else:
                print("O", end=" ") 
        print()

def reservar(sala, fila, columna):
    butaca = sala[fila][columna]
    estado = 0
    if butaca == 0:
        estado = True
    else:
        estado = False
    return estado

def cargar_sala(sala):
    filas = len(sala)
    columnas = len(sala[0])
    for i in range(filas):
        for j in range(columnas):
            generar_estado = random.randint(0,1)
            sala[i][j] = generar_estado

def butacas_libres(sala):
    butacas_vacias = 0
    for fila in sala:
        for butaca in fila:
            if butaca == True:
                butacas_vacias += 1
    return butacas_vacias

#Falta termirar esta función (está mal planteada)
"""
def butacas_contiguas(sala):
    contiguas = []
    sumador = 0
    for fila in sala:
        for butaca in fila:
            if butaca == True:
                sumador += 1
            else: 
                contiguas.append(sumador)
                sumador = 0
    return contiguas
"""
    


#programa
filas_de_sala = 4
columnas_de_sala = 4
crear_sala = [[0] * columnas_de_sala for i in range(filas_de_sala)]
cargar_sala(crear_sala)
print(mostrar_butacas(crear_sala))
print(f"La cantidad de butacas libres en la sala es de = {butacas_libres(crear_sala)}")
#programa de reservas
while True:
    f = int(input("En que fila desea reservar el asiento? "))
    c = int(input("En que columna desea reservar el asiento? "))
    reservar_asiento = reservar(crear_sala, f, c)
    if reservar_asiento == False:
        print("Ese asiento esta ocupado, elige otro")
    else:
        print("El asiento fue reservado con exito")
        crear_sala[f][c] = 1
        mostrar_butacas(crear_sala)
        continuar = input("Desea continuar reservando SI/NO?")
        if continuar.lower() == "no":
            print("Gracias por su reserva. Disfrute de la función!")
            break
    
