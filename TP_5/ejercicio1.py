""" Desarrollar una función para ingresar a través del teclado un número natural. La función
rechazará cualquier ingreso inválido de datos utilizando excepciones y mostrará la razón exacta
del error. Controlar que se ingrese un número, que ese sea entero y que sea mayor que 0. Devolver
el valor ingresado cuando esté sea correcto. Escribir también un programa que permita probar el
correcto funcionamiento de la misma """


def leerEntero(msj="Ingrese un número entero natural: "):
    while True:
        try:
            nro = int(input(msj))
            if nro <= 0:
                raise AssertionError 
        except ValueError:
            print("Dato inválido. Sólo se permiten números enteros")
        except AssertionError:
            print("El número debe ser mayor que 0")
        except:
            print("Error desconocido")
        else:
            break
    return nro

#programa
print(f"El número ingresado es {leerEntero()}")
    
