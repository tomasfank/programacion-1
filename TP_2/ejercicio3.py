""" Crear una lista con los cuadrados de los números entre 1 y N (ambos incuidos), donde N se
ingresa desde el teclado. Luego se solicita imprimir los útlimos 10 valores de la lista """

def crearListaCuadrados(n):
    lista = []
    for i in range(1, n+1):
        lista.append(i**2)
    return lista




a = crearListaCuadrados(20)
print(a)

for i in range(a[-1], a[-10]):
    print(a[i], sep=",")