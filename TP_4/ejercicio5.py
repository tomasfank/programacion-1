""" Escribir una función  filtar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con palabras que tengana N o más caracteres de la cadena original. Escribir también un programa para verificar el comportamiento de la misma. """

def filtrar_palabras(cadena, N):
    listaDePalabras = cadena.split()
    cadenaNueva = ""
    for palabra in listaDePalabras:
        if len(palabra) >= N:
            cadenaNueva = cadenaNueva + palabra + " "
    return cadenaNueva


#programa 
frase = input("Ingrese una frase = ")
nro = int(input("Ingrese un número entero = "))

fraseNueva = filtrar_palabras(frase, nro)

print(fraseNueva)