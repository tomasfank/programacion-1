import random

def desordenar(palabra):
    letras = list(palabra[1:-1])
    random.shuffle(letras)
    palabra_desordenada = palabra[0] + ''.join(letras) + palabra[-1]
    return palabra_desordenada
    

try:
    archivo = open("previo_2024/texto.txt","rt")
    archivoNuevo = open("previo_2024/nuevotexto.txt","wt")
    linea = archivo.readline()

    lista_de_palabras = []
    apariciones = []

    while linea:
        palabras = linea.split(" ")
        #Parte 2
        for x in range(len(palabras)):
            palabras[x] = ''.join(letra for letra in palabras[x] if letra.isalpha()).lower()
            if palabras[x] not in lista_de_palabras:
                lista_de_palabras.append(palabras[x])
                apariciones.append(1)
            else:
                i = lista_de_palabras.index(palabras[x])
                apariciones[i] = apariciones[i] + 1
        # Parte 1
        desordenadas = [palabra if len(palabra) <= 3 else desordenar(palabra) for palabra in palabras]
        nuevaLinea = ' '.join(desordenadas)+"\n"
        archivoNuevo.write(nuevaLinea)
        linea = archivo.readline()

    for x in range(len(lista_de_palabras)):
        print(f"Palabra '{lista_de_palabras[x]}' = {apariciones[x]} apariciones.")
    
except FileNotFoundError as e:
    print("No se encontro el archivo",e)
except OSError as e:
    print("No se pudo leer el archivo",e)
finally:
    try:
        archivo.close()
        archivoNuevo.close()
    except NameError:
        pass