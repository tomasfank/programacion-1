""" La función 'diadelasemana()', que se utiliza para averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para imprimir por patalla el calendario de un mes completo, correspondiente a un mes y año cualquiera basándose en la función suministrada. Considerar que la semana empieza en domingo. """

#función brindada por el profesor
def diadelasemana(dia,mes,año):
    if mes < 3:
        mes += 10 
        año -= 1
    else:
        mes -= 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem += 7
    return diasem

#función para imprimir días
def imprimir_calendario(mes, año):
    lista_dias = ["DOM", "LUN", "MAR", "MIE", "JUE", "VIE", "SAB"]
    print(f"--- MES = {mes} ---")
    for dia in range(1,32):
        dia_sem = diadelasemana(dia, mes, año)
        print(lista_dias[dia_sem], dia)


#programa
a = imprimir_calendario(7,2023)  


    

