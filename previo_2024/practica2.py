"""
La Real Academia Española define la palabra anagrama como "Cambio en el orden de las 
letras de una palabra que da lugar a otra palabra distinta". Ejemplos:
    - amor, roma, omar, ramo, armo, mora
    - avenida, enviada, evadian
    - camino, camion, comian, monica
Se solicita escribir un programa para leer un archivo de texto cualquiera e imprimir por 
pantalla un listado de todas las palabras que sean detectadas como anagramas de otras, 
agrupando las mismas tal como muestra el ejemplo anterior.
Notas:
    a. Las mayusculas y minusculas no deberan distinguirse para la deteccion de anagramas.
    b. Las palabras pueden contener letras de la "a" a la "z", incluyendo caracteres regionales como la Ñ. Las vocales con tilde se consideraran como si no lo tuvieran a efectos del analisis de anagramas. Los signos de puntuacion tampoco deben interferir en el proceso.
    c. El listado deber· mostrarse ordenado se menor a mayor segun la cantidad de anagramas hallados. 
A continuacion se suministra un texto a modo de ejemplo, el que puede copiarse y pegarse en un archivo. Recuerde que el programa debe servir para cualquier archivo de texto.
"""

def crearAnagrama(palabra):
    return ''.join(sorted(palabra))

def quitarAcentos(palabra):
    vocales = ["a","e","i","o","u"]
    acentos = ["á","é","í","ó","ú"]
    for x in range(len(acentos)):
        palabra = palabra.replace(acentos[x], vocales[x])
    return palabra

try:
    archivo = open("practica2.txt","rt")
    linea = archivo.readline()
    dic_anagramas = {}
    while linea:
        linea = linea.lower()# Pasar todo a minusculas
        palabras = linea.split(" ")# Armo una lista de palabras de la linea 
        for x in range(len(palabras)):
            palabras[x] = quitarAcentos(palabras[x])
            palabras[x] = ''.join(letra for letra in palabras[x] if letra.isalpha())
            anagrama = crearAnagrama(palabras[x]) 
            if len(dic_anagramas) == 0:
                dic_anagramas[anagrama] = [palabras[x]]
            else: 
                if anagrama not in dic_anagramas:
                    dic_anagramas[anagrama] = [palabras[x]]
                else:
                    if palabras[x] not in dic_anagramas[anagrama]:
                        dic_anagramas[anagrama].append(palabras[x])
        linea = archivo.readline()
    
    for grupo in dic_anagramas.values():
        if len(grupo)>1:
            print(grupo)
except  FileNotFoundError as e:
    print("No se encontro el archivo",e)
except OSError as e:
    print("No se ha podido abrir el archivo",e)
finally:
    try:
        archivo.close()
    except NameError:
        pass


"""
Una de las maneras más simples de medir la complejidad de un programa consiste en 
contar la cantidad de líneas que posee. Escribir un programa que utilice una función recursiva para realizar esta tarea en un programa fuente cualquiera escrito Python, ignorando las líneas en blanco y las que sólo contengan comentarios. Imprimir por pantalla el 
valor devuelto por la función.
"""

def cantidadLineas(codigo,i=0,cantidad=0):
    if len(codigo) == i:
        return print(cantidad)
    else: 
        if codigo[i].strip().find("#") == 0 or codigo[i].strip() == "":
            return cantidadLineas(codigo,i+1,cantidad)
        else:
            return cantidadLineas(codigo,i+1,cantidad+1)
        
programa = """# Funciones 
def mayorDeTres(a,b,c):
    if b < a > c:
        return a 
    elif a < b > c:
        return b
    elif a < c > b:
        return c
    else:
        return -1

def ingresar():
    a = int(input("Ingresa el valor de 'a' = "))
    b = int(input("Ingresa el valor de 'b' = "))
    c = int(input("Ingresa el valor de 'c' = "))
    return a,b,c

# Programa
a, b, c = ingresar()  
resultado = mayorDeTres(a,b,c)
if resultado != -1:
    print("El mayor es estricto", resultado)
else:
    print("No existe mayor estricto")"""

cantidadLineas(programa.split("\n"))