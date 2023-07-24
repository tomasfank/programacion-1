""" Escribir un progrma que permita grabar en un archivo los datos de lluvia caída durante un año.
Cada línea del archivo se grabará con el siguiente formato:

        <dia>;<mes>;<lluvia caída en mm> por ejemplo 25;5;319
        
Los datos se generarán mediante números al azar, asegurándose que las fechas sean válidas. La
cantidad de registros también será un número al azar entre 50 y 200. Por último se solicita leer
el archivo generado e imprimir un informe en formato matricial donde cada columna represente a un
mes y cada fila corresponda a los días del mes. Imprimir además el total de lluvia caida en todo
el año. """

#boceto de matriz
"""
    Enero Febrero Marzo Abril ...
      1     1
      2     2
      3     3
      4     4
      5     5
      ...   ...
"""

#modulos
import random

#Funciones
def generar_matriz(matriz):
    """ genera una matriz vacía con un formato de "calendario" """ 
    meses = ["DIA / MES", "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]#encabezado
    filas = len(matriz)
    columnas = len(matriz[0])
    sumadorDias = 1 
    for i in range(filas):
        for j in range(columnas):
            if i == 0:
                matriz[i][j] = meses[j]
            elif j == 0:
                matriz[i][j] = sumadorDias
                sumadorDias += 1    

def rellenar_matriz(dia,mes,lluvia,matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if i == int(dia) and j == int(mes):
                matriz[i][j] = lluvia + " mm"
    
                 
def imprimir_informe(matriz):
    """ imprime prolijamente los datos """ 
    for fila in matriz:
        for columna in fila:
              print(f"{columna:^10}", end=" ")
        print()
        

#programa principal
matriz = [[0] * 13 for x in range(32)]
generar_matriz(matriz)

#generar el archivo 
try:
    archivo = open("ejercicio2.txt", "wt")
    registros = random.randint(50, 200)
    
    for x in range(registros):
        lluvia = random.randint(1, 50)
        mes = random.randint(1,12)
        if mes == 2:
            dia = random.randint(1,28) #suponiendo que hablamos de este año 2023 Febrero tiene 28 días
        elif mes in [1,3,5,7,9,10,12]:
            dia = random.randint(1,31)
        else:
            dia = random.randint(1,30)
        archivo.write(str(dia) + ";" + str(mes) + ";" + str(lluvia) + "\n")
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo = ", mensaje)
except OSError as mensaje:
    print("ERROR = ", mensaje)
finally:
    try:
        archivo.close()
    except NameError:
        pass

#acceder al archivo y imprimir informe
try:
    archivoLectura = open("ejercicio2.txt", "rt")
    linea = archivoLectura.readline()
    lluviaTotal = 0
    while linea:
        dia, mes, lluvia = linea.split(";")
        lluvia = lluvia.rstrip("\n")
        lluviaTotal += int(lluvia)
        rellenar_matriz(dia,mes,lluvia,matriz)
        linea = archivoLectura.readline()
    imprimir_informe(matriz)
    print(f"El total de mm de lluvia anual fue de {lluviaTotal} mm.")
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo = ", mensaje)
except OSError:
    print("ERROR = ", mensaje)
finally:
    try:
        archivoLectura.close()
    except NameError:
        pass
        
        
       
    


