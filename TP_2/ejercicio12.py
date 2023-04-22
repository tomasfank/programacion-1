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

#funciones
def informeIngresos(ingresos):
    carga_datos = True
    while carga_datos == True:
        num_socio = int(input("Ingrese el número de socio que desea ingresar al club = "))
        if num_socio == 0:
            carga_datos = False
        else:
            while num_socio < 9999 or num_socio > 100000:
                num_socio = int(input("El número de socio debe contener 5 carácteres. Ingrese el número de socio que desea ingresar al club = "))
                if num_socio == 0:
                    carga_datos = False
                    break
            else:
                ingresos.append(num_socio)
    return ingresos

def imprimirInforme(lista):
    lista_aux = []
    for socio in lista:
        if socio not in lista_aux:
            print("El socio", socio, "ingreso", lista.count(socio), "veces")
        lista_aux.append(socio)
        
def darBajaSocio(lista):
    baja_socio = int(input("¿Que socio desea darse de baja? = "))
    nueva_lista = [socio for socio in lista if baja_socio != socio]
    print("Se dío de baja al socio nro =", baja_socio)
    return nueva_lista
    
#listas
ingreso_socios = []

#programa 
informeIngresos(ingreso_socios)
imprimirInforme(ingreso_socios)
bajas = darBajaSocio(ingreso_socios)
imprimirInforme(bajas)
