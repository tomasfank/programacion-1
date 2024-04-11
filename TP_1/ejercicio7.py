""" Escribir una función diaSiguiente(...) que reciba como parámetro una fecha cualquiera expresada por tres enteros (correspondientes al día, mes y año), calcule y devuelva tres enteros correspondientes al día siguiente al dado. Utilizando esta función, desarrollar programas que permitan:

    a) Sumar N días a una fecha.
    b) Calcular la cantidad de días existentes entre dos fechas cualquiera.
"""

# Funciones 
def diaSiguiente(d,m,a):
    """ Devuelve el día siguiente """
    if m == 2 and (d == 29 and ((a % 4 == 0 and a % 100 != 0) or a % 400 == 0)): # 29 de Febrero
        d = 1 
        m = 3
    elif m == 2 and d == 28:
        d = 1 
        m = 3
    elif m in [1,3,5,7,8,10,12] and d == 31:
        d = 1
        if m == 12:
            m = 1
        else:
            m += 1
    elif m in [4,6,9,11]  and d == 30:
        d = 1
        m += 1 
    else:
        d += 1 # En cualquier otro caso simplemente sumamos 1 día   
    return d, m, a

def sumarDias(fecha, suma):
    """ Suma una 'x' cantidad de días a una fecha """
    fecha = fecha.split("/")
    d, m, a = int(fecha[0]), int(fecha[1]), int(fecha[2])
    for  i in range(1, suma+1):
        d, m, a = diaSiguiente(d, m, a)
    return f"{d}/{m}/{a}"

def diferenciaDias(fecha1, fecha2):
    """ Devuelve la diferencia en días entre una fecha 'a' y una fecha 'b' """
    fecha1 = fecha1.split("/")
    fecha2 = fecha2.split("/")
    d1, m1, a1 = int(fecha1[0]), int(fecha1[1]), int(fecha1[2])
    d2, m2, a2 = int(fecha2[0]), int(fecha2[1]), int(fecha2[2])
    cantDias = 0
    while d1 != d2 or m1 != m2 or a1 != a2: 
        d1, m1 , a1 = diaSiguiente(d1, m1, a1)
        cantDias += 1
    return cantDias

print(sumarDias("28/2/1998",10))
print(diferenciaDias("30/04/1998","31/05/1998"))