""" Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo
número se recibe como parámetro. Los nombres de los meses deberán obtenerse de una lista de cadenas
de caracteres inicializada dentro de la función. Devolver la cadena vacía si el número de mes
es inválido. La detección de meses inválidos deberá realizarse a través de excepciones. """

def nombreMeses(nro):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    try:
        assert 1<= int(nro) <= 12
        mes = meses[int(nro)-1]
    except ValueError:
        print("Dato inválido.")
    except AssertionError:
        mes = ""
    return mes

#programa
nroMes = input("Ingrese el número de mes ")
print(f'El mes es "{nombreMeses(nroMes)}"')
        