"""Ejercicio 1:  Desarrollar una función recursiva para retornar una lista que contenga solo las vocales de una palabra que recibe por parámetro. Las vocales no deben estar repetidas en la lista.  
"""
def obtenerVocales(palabra, vocal=[], i=0):
    vocales = ["a","e","i","o","u"]

    if len(palabra)==i: # Condición: que el largo de "palabra" sea igual a "i", o sea que no haya más letras.
        return vocal # Valor de retorno, la lista de vocales.
    else:
        if palabra[i].lower() in vocales and palabra[i].lower() not in vocal:
            vocal.append(palabra[i].lower())
    return obtenerVocales(palabra, vocal, i+1)# Llamo a la función dentro de la función


a = "Lapida"
b = "Muercielago"
print(obtenerVocales(a))
print(obtenerVocales(b))

"""Ejercicio 2: Procesar un archivo que contiene un mail por registro e informe  
    1. Cantidad de mails por país 
    2. Cantidad de mails no válidos.  
    Una dirección de mail se considera válida cuando por ejemplo usuario@dominio.com.ar 
    - el nombre del usuario debe contener solo caracteres alfanuméricos 
    - la dirección completa debe tener un solo @ 
    - el dominio debe tener al menos un caracter 
    - las ultimas dos letras del país puede o no estar. 
En caso de no estar se considera de USA. Procesar el archivo utilizando excepciones."""

try:
    archivo = open("practica1.txt","rt")
    linea = archivo.readline()
    invalidos = 0
    paises = ["usa"]
    cantidad_por_pais = [0]
    while linea:
        linea = linea.rstrip("\n")
        if linea.count("@") > 1:
            invalidos += 1 
        else:
            usuario, dominio = linea.split("@")  
            if len(usuario) < 1 or not(usuario.isalnum()) or len(dominio) < 1:
                invalidos += 1 
            else:
                if dominio[-3] == ".":
                    dominio = dominio.split(".")
                    if len(dominio) > 2:
                        pais = dominio[-1]
                    if pais not in paises:
                        paises.append(pais)
                        cantidad_por_pais.append(1)
                    else:
                        i = paises.index(pais)
                        cantidad_por_pais[i] = cantidad_por_pais[i] + 1  
                else:
                    cantidad_por_pais[0] = cantidad_por_pais[0] + 1        
        linea = archivo.readline()
    print(f"Cantidad de correos invalidos = {invalidos}")
    print("Cantidad de dominios por pais = ")
    for x in range(len(paises)):
        print(f"- {paises[x]} = {cantidad_por_pais[x]}")
except FileNotFoundError as e:
    print("No se ha encontrado el archivo",e)
except OSError as e:
    print("No se pudo leer el archivo",e)
finally:
    try:
        archivo.close()
    except NameError:
        pass

