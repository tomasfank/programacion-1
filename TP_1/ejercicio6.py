""" Desarrollar una función que reciba como parámetro dos númerso enteros positivos y devuelva el número que resulte de concatenar ambos valores. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utizilar facilidades de python no vistas en clase """

# Funciones
def concatenar(a,b):
    print(a,b,sep="")

# Programa
while True:
    a = int(input("Ingrese un valor"))
    b = int(input(f"Ingrese el valor que desea concatenar a '{a}' = "))
    concatenar(a,b)
    continuar = input("¿Desea continuar? S/N = ")
    if continuar.lower() == "n":
        break