"""
Una fabrica de bicicletas guarda en una matriz la cantidad de unidades producidas en cada
una de sus plantas durante una semana. De este modo, cada columna representa un día de la
semana y cada fila representa una de sus fabricas.
    
    Se solicita:
        a) crear una matriz con datos generados al azar de N fábricas durante una semana,
        considerando que la capacidad máxima de fabricación es de 150 unidades por día y puede
        suceder que ciertos días no se fabrique ninguna.
        b) Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
        c) Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica)
        d) Cuál es el día más productivo, considerando todas las fabricas juntas.
        e) Crear una lista por comprensión que contenga la menor cantidad fabricada por cada
        fábrica.
"""
import random 

def imprimirMatriz(matriz):
    for filas in matriz:
        for elementos in filas:
            print("%03d" %elementos, end=" |  ")
        print()
              
def unidadesProducidas(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(0, 150)

def unidadesPorFabrica(matriz):
    unidades = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma = sum(matriz[i])
            if suma not in unidades:
                unidades.append(suma)
    return unidades

def mayorProduccion(matriz):
    mayor = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if max(matriz[i]) > mayor:
                mayor = max(matriz[j])
    return mayor

def diaMasProductivo(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    sumas = [0] * columnas
    for j in range(columnas):
        for i in range(filas):
            sumas[j] += matriz[i][j]
    return max(sumas), sumas.index(max(sumas))
         
#programa
fabricas = int(input("¿Cuantas fábricas tiene la empresa? "))
matriz = [[0] * 6 for x in range(fabricas)]

#calendario de producción semanal 
print("Lu  |  Ma  |  Mi  |  Ju  |  Vi  |  Sa  |")
unidadesProducidas(matriz)
imprimirMatriz(matriz)
print()

#cantidad de unidades producidas por fábrica
cantUnidades = unidadesPorFabrica(matriz)
fab = 1
for elemento in cantUnidades:
    print("En la Fábrica %03d" %fab,"se produjeron = ", elemento, "bicicletas")
    fab += 1
print()

#Fábrica que más produjo en un día
max_produccion = mayorProduccion(matriz)
posj = 0
posi = 0
dia = ""
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == max_produccion:
            posi = i 
            posj = j 
if posj == 0:
    dia = "Lunes"
elif posj == 1:
    dia = "Martes"
elif posj == 2:
    dia = "Miércoles"
elif posj == 3:
    dia = "Jueves"
elif posj == 4:
    dia = "Viernes"
else:
    dia = "Sábado"
print("La fábrica que más bicicletas produjo fue la %03d" %posi, "el día", dia, ",con una cantidad de", max_produccion, "de unidades")
print()

#dia mas productivo
c , d = diaMasProductivo(matriz)
diaprod = ""
if d == 0:
     diaprod = "Lunes"
elif d == 1:
    diaprod = "Martes"
elif d == 2:
    diaprod = "Miércoles"
elif d == 3:
    diaprod = "Jueves"
elif d == 4:
    diaprod = "Viernes"
else:
    diaprod = "Sábado"
print("El día más productivo fue el", diaprod, "con un total de", c, "de bicicletas producidas")
print()

#lista con menor cantidad producida
menor_produccion = [min(elemento) for elemento in matriz]
f = 1
for elemento in menor_produccion:
    print("La menor cantidad producida por la fabrica %03d" %f, "fue de", elemento)
    f += 1

