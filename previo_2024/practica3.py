"""Desarrollar una función recursiva para buscar el elemento mayor par de la lista, si no existe debe retornar 
-1, Recuerde que se espera la soluciÛn recursiva a este problema. 
Crear un pequeño programa principal para probar la funciÛn creando la lista por comprensiÛn con 
n˙meros al azar."""

def mayorPar(lista, mayor=-1, i=0):
    if len(lista) == i:
        return mayor
    else:
        if lista[i] % 2 == 0 and lista[i] > mayor:
            mayor = lista[i]
            return mayorPar(lista, mayor, i+1)
        else:
            return mayorPar(lista, mayor, i+1)
        
lista = [1,3,5,7]

print(mayorPar(lista))

"""
Escribir un programa que lea un archivo de texto conteniendo el siguiente formato: 
legajo;apellido;nombre;nota1;nota2 
genere dos archivos nuevos seleccionado de la siguiente forma: 
aprobados.txt (los registros que tienen ambos parciales mayor o igual a 4) 
desaprobados.txt (los registros que tienen al menos un parcial desaprobado, agregando un campo mas 
indicando cu·l debe recuperar: PRIMERO, SEGUNDO, AMBOS) 
En los nuevos archivos tanto el nombre como el apellido de estar sÛlo en may˙scula la primera letra. 
Ejemplo: alumnos.txt contiene 
1000;perez;juan;5;8 
3500;Garcia;Marcelo;2;5 
2400;pato;Miriam Alejandra;2;2
"""

try:
    archivo = open("previo_2024/practica3.txt","rt")
    aprobados = open("previo_2024/aprobados.txt","wt")
    desaprobados = open("previo_2024/desaprobados.txt","wt")
    linea = archivo.readline()
    while linea:
        lu,nombre,apellido,nota1,nota2 = linea.split(";")
        nombre, apellido = nombre.title(), apellido.title()
        if int(nota1) > 4 and int(nota2) > 4:
            lineaNueva = f"{lu};{nombre};{apellido};{nota1};{nota2}\n"
            aprobados.write(lineaNueva)
        else:
            if int(nota1) < 4 and int(nota2) < 4:
                recupera = 'AMBOS'
            elif int(nota1) < 4:
                recupera = 'PRIMERO'
            else:
                recupera = 'SEGUNDO'
            lineaNueva = f"{lu};{nombre};{apellido};{nota1};{nota2};{recupera} \n" 
            desaprobados.write(lineaNueva)
        linea = archivo.readline()
except OSError as e:
    print(f"Error, no se pudo leer el archivo {e}")
finally:
    try:
        archivo.close()
        aprobados.close()
        desaprobados.close()
    except NameError:
        pass