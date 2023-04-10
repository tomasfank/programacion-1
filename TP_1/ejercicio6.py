""" Desarrollar una función que reciba como parámetro dos númerso enteros positivos y devuelva
el número que resulte de concatenar ambos valores. Por ejemplo, si recibe 1234 y 567 debe devolver
1234567. No se permite utizilar facilidades de python no vistas en clase """

#funciones
def concatenar(valor1, valor2):
    print(valor1,valor2, sep="")
    
#programa
enterosUno = int(input("Ingrese números enteros positivos "))
enterosDos = int(input("Ingrese números enteros positivos "))

#condición
while enterosUno < 0 or enterosDos < 0:
    print("Has ingresado valores no permitidos")
    enterosUno = int(input("Ingrese números enteros positivos "))
    enterosDos = int(input("Ingrese números enteros positivos "))
    
#llamamos a la función    
concatenar(enterosUno, enterosDos)
