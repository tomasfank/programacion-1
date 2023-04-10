"""
Escribir una función diaSiguiente(...) que reciba como parámetro una fecha cualquiera expresada
por tres enteros (correspondientes al día, mes y año), calcule y devuelva tres enteros correspondientes
al día siguiente al dado. Utilizando esta función, desarrollar programas que permitan:

    a) Sumar N días a una fecha
    b) Calcular la cantidad de días existentes entre dos fechas cualquiera
"""

def diaSiguiente(d, m , a):
    """ Recibe una fecha y da como resultado la fecha del día siguiente """
    #Primero trataremos al mes de Febrero que es el más particular caso de todos los meses.
    if m == 2 and ((a % 4 == 0 and a % 100 != 0) or a % 400 == 0): #Primero verificamos si el año es bisiesto.
        #En caso afirmativo =
        if d == 29: #Si estamos en el día 29 de Febrero, pasamos al 1 de Marzo.
            m +=1
            d = 1
        else: #Agregamos este "else" en caso de que sea 28 de febrero, sume un día y se convierta en 29.
            d += 1
    #En caso de que no sea año bisiesto
    elif m == 2 and d == 28: #El útlimo día sería el 28 de Febrero. 
        m +=1
        d = 1
    #Después verificamos si se trata de un mes de 31 días. 
    elif d >= 31 and  (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12): #De ser el día 31, pasamos al 1° del siguiente mes.
        d = 1
        if m == 12: #De ser el mes 12, pasamos al mes 1 del siguiente año.
             m = 1
             a += 1
        else: #De no ser el mes 12 simplemente sumamos uno al mes actual.
            m += 1
    #Luego verificamos si no es un mes de 31 días, sólo nos quedan los meses de 30 días, por lo que verificamos si estamos en el último día del mes       
    elif d >= 30 and (m == 2 or m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12): 
        d += 1 #Si no es el día 30, sumamos un dia. 
    elif d >= 30:#Si es el día 30, pasamos al primer día del mes siguiente.
        d = 1
        m += 1
    else: #Por último, en cualquier otro caso simplemente sumamos un día.
        d += 1
    return d, m, a

def sumarDias(d, m, a, suma):
    """ Recibe una fecha, le suma una X cantidad de días y devuelve una nueva fecha """ 
    for i in range(1, suma+1): #Para que sume la cantidad de días que pedimos correctamente colocamos "suma+1", de lo contrario faltaría un día 
        d, m, a= diaSiguiente(d, m, a) #usamos la funcion diaSiguiente para realizar el conteo de las fechas. 
    return d, m, a

def diferenciaDias(d1, m1, a1, d2, m2, a2):
    """ recibe 2 fechas diferentes y devuelve la cantidad de días que hay entre ambas """
    cantDias = 0 
    while d1 != d2 or m1 != m2 or a1 != a2:
        d1, m1, a1 = diaSiguiente(d1, m1, a1)
        cantDias += 1
    return cantDias

            
        
#programa principal
dia = int(input("Día = "))
mes = int(input("Mes = "))
anio = int(input("Año = "))
print("El día siguiente a la fecha ingresada es = ")
print(diaSiguiente(dia, mes, anio))
print()

suma = int(input("Cuantos días quieres sumar? = "))
print("La nueva fecha es = ")
print(sumarDias(dia, mes, anio, suma))
print()

print("Ahora ingresa una fecha futura y se calculara la cantidad de días que hay entre ambas")
dia2 = int(input("Día = "))
mes2 = int(input("Mes = "))
anio2 = int(input("Año = "))
print("La cantidad de días de diferencia es de = ")
print(diferenciaDias(dia, mes, anio, dia2, mes2, anio2))

