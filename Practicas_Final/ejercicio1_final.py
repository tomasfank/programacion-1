""" Utilizando recursividad, desarrolle una función que devuelva la palabra más larga
en una frase. No debe convertir la frase en una lista, y no se puede agregar argumentos 
a la función. Además, escribir un programa que solicite una frase al usuario por 
teclado, y que imprima el resultado de la función recursiva."""

def palabra_mas_larga(frase):
    pos_espacio = frase.find(" ")
    #Caso base 
    if pos_espacio == -1:
        return frase 
    #Caso recursivo    
    else:
        palabraLarga = palabra_mas_larga(frase[pos_espacio+1:])
        if len(frase[:pos_espacio]) >= len(palabraLarga):
            return frase[:pos_espacio]
        else:
            return palabraLarga
        

#programa
solicitarFrase = input("Escriba una frase ")

print(f"La palabra más larga es '{palabra_mas_larga(solicitarFrase)}'")


