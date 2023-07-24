""" Escribir una función que devuelva la suma de los N primeros números naturales """

def suma_naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_naturales(n-1)
    
numero = 3
print(suma_naturales(numero))