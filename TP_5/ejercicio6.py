""" El método index permite buscar un elemento dentro de una lista, devolviendo la posición que
éste ocupa. Sin embargo, si el elemento no pertenece a la lista se produce una excepcion del
tipo ValueError. Desarrollar un programa que cargue una lista con números enteros ingresados a
través del teclado (terminando con -1) y permita que el usuario ingrese el valor de algunos
elementos para visualizar la posición que ocupan, utilizando el método index. Si el número no
pertenece a la lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar
el proceso al tercer error detectado. No utilizar el operador "in" durante la busqueda. """

def cargarLista():
    """ Permite cargar valores enteros a una lista """
    lista = []
    while True:
        try:
            valor = input("Ingrese un número: ")
            if int(valor) != -1:
                assert int(valor) > 0, "Sólo se permiten números enteros"
                lista.append(int(valor))
            else:
                break
        except ValueError:
            print("El tipo de dato es inválido")
        except AssertionError as mensaje:
            print(mensaje)
    return lista

def buscarDato(lista):
    """ Permite buscar un dato en una lista """ 
    intentos = 0 
    while True:
        try:
            if intentos == 3:
                raise AssertionError
            else:
                a = input("¿Qué dato busca?")
                pos = lista.index(int(a))
                print(f"El valor {a} está en la posición {pos}")
        except ValueError:
            intentos +=1
            print(f"Dato inválido. Te quedán {3 - intentos} intentos")
        except AssertionError:
            print("Te quedaste sin intentos")
            break
                      
#programa           
a = cargarLista()
b = buscarDato(a)


