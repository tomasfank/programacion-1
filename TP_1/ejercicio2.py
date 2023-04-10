""" Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha válida (día, mes, año). Devolver Ture o False según la
fecha sea correcta o no. Realizar también un programa para verificar el comportamiento
de la función """

def fechaValida(d, m, a):
    """ recibe tres numeros enteros y comprueba si es una fecha válida """
    validez = False
    if 1 <= d <= 31 and 1 <= m <= 12 and 0 < a <= 2099:
        validez = True
    return validez

#programa principal
inicio = fechaValida(24, 3, 2099)
if inicio == True:
    print("La fecha es válida")
else:
    print("La fecha es inválida") 