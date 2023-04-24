""" Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar
cadenas auxiliares ni rebanadas. Escribir además un programa que permita verificar su funcionamiento """

def esCapicua(cadena):
    largo = len(cadena)
    capicua = True
    for i in range(largo // 2):
        if cadena[i] != cadena[largo-i-1]:
            capicua = False
    return capicua
                        
#programa         
a = input("escribe una cadena de caracteres ")
b = esCapicua(a)
if b == True:
    print("Es capicua")
else:
    print("No es capicua")


    
    