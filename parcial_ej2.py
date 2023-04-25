def secuenciaNormal(copias, pags):
    secuencia = []
    for i in range(pags):
        for j in range(copias):
            secuencia.append(i+1)
    return secuencia

def secuenciaIntercalada(copias, pags):
    secuencia = []
    for i in range(copias):
        for j in range(pags):
            secuencia.append(j+1)
    return secuencia 

#programa
nro_paginas = int(input("¿Cuántas páginas vas a imprimir? "))
nro_copias = int(input("¿Cuántas copias necesitas? "))
print(secuenciaNormal(nro_copias, nro_paginas))
print(secuenciaIntercalada(nro_copias, nro_paginas))    