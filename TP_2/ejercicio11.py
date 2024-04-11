"""
Resolver el siguiente problema, diseñando las funciones a utilizar:

Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se
anuncia en la recepción indicando su número de afiliado (número entero de 4 dígitos) y además
indica si viene por una urgencia (ingresando 0) o con turno (ingresando 1). Para finalizar se
ingresa -1 como número de socio. Luego se solicita:

    a) Mostrar un listado de los pacientes atendidos por urgencia y un listado de pacientes
    atendidos por turno en el orden que llegaron a la clínica.
    
    b) Realizar la búsqueda de un número de afiliado e infomrar cúantas veces fue atendido por
    turno y cuantas veces por urgencia. Repetir la busqueda hasta que se ingrese -1 como número
    de afiliado
"""

# Funciones
def ingresaPaciente(afiliados, urgencias):
    while True:
        nroAfiliado = int(input("Ingrese su número de afiliado = "))
        if (9999 < nroAfiliado or nroAfiliado < 999):
            if nroAfiliado != -1:
                print("El número de afiliado debe ser de 4 caracteres")
                continue
            else:
                print("Carga terminada. Gracias!")
                break
        tipoAtencion = int(input("Ingrese 0 si se trata de una urgencia o de lo contrario ingrese 1 = "))
        afiliados.append(nroAfiliado)
        urgencias.append(tipoAtencion)
        print("Gracias!... Para continuar ingrese el número del siguiente afiliado o '-1' para terminar")


def imprimirListado(afiliados, urgencias):
    for i in range(len(afiliados)):
        if urgencias[i] == 0:
            print(f"Afiliado = {afiliados[i]} - Tipo de atención = Urgencia.")
        else:
            print(f"Afiliado = {afiliados[i]} - Tipo de atención = Consulta con turno.")

def buscarPaciente(afiliados, urgencias):
    while True:
        paciente = int(input("Ingrese el número de afiliado que desea consultar o '-1' para terminar = "))
        if paciente != -1:
            vecesAtendido = [urgencias[x] for x in range(len(afiliados)) if afiliados[x] == paciente]
            print(f"El paciente {paciente} fue atendido {len(vecesAtendido)} veces.")
        else:
            print("Programa finalizado.")
            break

# Programa 
afiliados = []
tipoAtencion = []
ingresaPaciente(afiliados, tipoAtencion)
imprimirListado(afiliados, tipoAtencion)
buscarPaciente(afiliados, tipoAtencion)