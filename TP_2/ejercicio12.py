"""
Resolver el siguiente problema, utilizando funciones:

Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa
el número de socio de cinco digitos hasta ingresar un cero como fin de carga. Se solicita:
        
    a) Informar para cada socio, cuántas veces ingreso al club (cada socio debe aparecer una
    sola vez en el informe)
        
    b) Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos.
    Mostrar los registros de entrada al club antes y después de eliminarlo. Informar cuántos
    ingresos se eliminaron.     
"""

# Funciones
def ingresar(ingresos, socios, nroSocio):
    if nroSocio not in socios: # No hay registros de ingreso
        socios.append(nroSocio)
        ingresos.append(1)
    else: # Hay almenos un registro
        i = socios.index(nroSocio)
        ingresos[i] = ingresos[i] + 1

def imprimirIngresos(socios, ingresos):
    print("Cantidad de ingresos por socio = ")
    for i in range(len(socios)):
        print(f"+ Socio N° {socios[i]} = {ingresos[i]}")
        
def eliminarSocio(socios, ingresos, nroSocio):
    if nroSocio in socios:
        i = socios.index(nroSocio)
        cant = ingresos[i]
        socios.pop(i)
        ingresos.pop(i)
        print(f"El socio {nroSocio} tenía {cant} ingresos")
    else:
        print(f"No hay ningun socio {nroSocio} en la lista.")


# Programa
socios = []
ingresos = []

while True:
    nroSocio = int(input("Ingrese el número del socio que desea entrar en el predio ó -1 para terminar = "))
    if nroSocio != -1:
        if nroSocio < 10000 or nroSocio > 99999:
            print("El número de socio debe ser un número de 5 dígitos.")
            continue
        else:
            ingresar(ingresos, socios, nroSocio)
    else:
        break

imprimirIngresos(socios, ingresos)

while True:
    eliminar = int(input("Ingrese el número de socio a dar de baja ó -1 para terminar = "))
    eliminarSocio(socios, ingresos, eliminar)
    if eliminar == -1:
        break

imprimirIngresos(socios, ingresos)