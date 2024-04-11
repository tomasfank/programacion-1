""" Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año). Devolver Ture o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función. """

# Funciones
def validarFecha(d,m,a):
    if 0 < a:
        if 0 < m < 13:
            if m == 2:
                if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
                    if 0 < d < 30:
                        return True
                else: 
                    if 0 < d < 29:
                        return True
            elif m in [1,3,5,7,8,10,12]:
                if 0 < d < 32:
                    return True
            else:
                if 0 < d < 31:
                    return True

    # Salida por defecto
    return False

def ingresar():
    while True:
        a = int(input("Ingresa un día = "))
        b = int(input("Ingresa un mes = "))
        c = int(input("Ingresa un año = "))
        if a <= 0 or b <= 0 or c <= 0:
            print("Solamente puede ingresar números positivos.")
            continue
        else:
            return a, b, c

# Programa
a,b,c = ingresar()
resultado = validarFecha(a,b,c)
if resultado == True:
    print(f"{a}/{b}/{c} es una fecha válida.")
else:
    print(f"{a}/{b}/{c} no es una fecha válida.")