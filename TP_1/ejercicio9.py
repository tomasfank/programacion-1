""" Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso para poder cargar el camión de reparto. La empresa cuenta con N camiones, y cada uno puede transportar media tonelada (500 kilogramos). En un cajon caben 100 naranjas con un peso entre 200 y 300 gramos cada una. Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo. Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se pueden llenar, cuantas naranjas son para jugo y si hay algún sobrante de naranas que deba considerarse para el siguiente reparto. Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.

Además, se desea saber cuántos camiones se necesitan para transportar la cosecha. considerando que la ocupación del camión no debe ser inferior al 80%; en caso contrario el camión no será despachado por su alto costo. """

import random

def cajones_de_naranjas(cantidad_naranjas):
    para_jugo = 0
    para_cajon = 0
    cajones = 0
    peso_total = 0
    for x in range(cantidad_naranjas):
        peso = random.randint(150,350)
        peso_total += peso
        if peso < 200  or peso > 300:
            para_jugo += 1
        else:
            para_cajon += 1 
            if para_cajon == 100:
                cajones += 1
                para_cajon = 0
    return cajones, para_cajon, para_jugo, peso_total


def carga_de_camion(peso_cosecha):
    camiones_llenos = 0
    peso_en_kg = peso_cosecha / 1000
    while peso_en_kg > 0:
        if peso_en_kg > 500:
            camiones_llenos += 1
            peso_en_kg -= 500 
        elif peso_en_kg > 400:#el 80% de 500kg es 400kg
            camiones_llenos += 1
            peso_en_kg = 0
        else:
            break
    return camiones_llenos, peso_en_kg



#programa 
cantidad_de_naranjas = int(input("¿Cuántas naranjas se han cosechado? = "))
cant_cajones, cant_sobrante, cant_para_jugo, peso_de_carga = cajones_de_naranjas(cantidad_de_naranjas)
camiones_llenados, carga_sobrante = carga_de_camion(peso_de_carga)

print(f"""La cantidad de cajones que se llenaron fue de {cant_cajones} cajones de 100 naranjas.
La cantidad de naranjas que sobran para el siguiente envío es de {cant_sobrante} naranjas.
La cantidad de naranjas que se destinaron para hacer jugo es de {cant_para_jugo} naranjas.
El peso total de la cosecha es de {peso_de_carga/1000:.2f} kilogramos
La cantidad de camiones necesarios para transportar la carga es de {camiones_llenados} camiones.
La cantidad de kg de carga que no son rentables de transportar es de {carga_sobrante:.2f} kg.""")