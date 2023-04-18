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

#funciones
def pacientesAtendidos(turno, urgencia):
    atendiendo = True
    while atendiendo == True:
        afiliado = int(input("Ingrese el número de afiliado o -1 para finalizar: "))
        if afiliado == -1:
            atendiendo = False
        else:
            tipo_atencion = int(input("¿Viene con turno (1) o por una urgencia (0): "))
            if tipo_atencion == 1:
                turno.append(afiliado)
                print("Atendidos con turno = ", turno)
            elif tipo_atencion == 0:
                urgencia.append(afiliado)
                print("Atendidos por urgencia = ", urgencia)
    print("Pacientes atendidos por una urgencia = ", urgencia)
    print("Pacientes atendidos por turno = ", turno)
    return turno, urgencia 

def busquedaPaciente(turno, urgencia):
    busqueda = True 
    while busqueda == True: 
        num_afiliado = int(input("Ingrese el número de afiliado que desea buscar (o -1 para finalizar)"))
        if num_afiliado == -1:
            busqueda = False
            break
        else:
            atendidoUrgencia = urgencia.count(num_afiliado)
            atendidoTurno = turno.count(num_afiliado)
        print("El paciente", num_afiliado, "fue atendido", atendidoTurno, "veces por turno, y", atendidoUrgencia, "veces por urgencia.")
        
#listas necesarias   
lista_de_turno = []
lista_de_urgencia = []

#programa
lista_de_turno, lista_de_urgencia = pacientesAtendidos(lista_de_turno, lista_de_urgencia)
busquedaPaciente(lista_de_turno, lista_de_urgencia)