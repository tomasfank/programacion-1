""" Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo
dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas
decrecientes se solicita desarrolar una función que reciba como parámetro la cantidad de viajes
realizados en un determinado mes y devuelva el total gastado en viajes. Realizar también un
programa para verificar el comportamiento de la función. """

"""
* Esquema de tarifas =
    | Cantidad de viajes   | Valor de pasaje                         |
    | 1 a 20               | $58                                     |
    | 21 a 30              | 20% de descuento sobre la tarifa máxima |
    | 31 a 40              | 30% de descuento sobre la tarifa máxima |
    | Más de 40            | 40% de descuento sobre la tarifa máxima |
"""

def totalGastado(viajes):
    """ Recibe la cantidad de viajes realizados y devuelve el total gastado en esos viajes teniendo en cuenta un esquema de tarifas decrecientes """ 
    tarifaEstandar = 58
    totalGastado = 0
    contadorViajes = viajes
    while contadorViajes > 40:
        totalGastado = (tarifaEstandar * 0.6) + totalGastado
        contadorViajes = contadorViajes - 1 
    while 31 <= contadorViajes <= 40:
        totalGastado = (tarifaEstandar * 0.7) + totalGastado
        contadorViajes = contadorViajes - 1
    while 21 <= contadorViajes <= 30:
        totalGastado = (tarifaEstandar * 0.8) + totalGastado
        contadorViajes = contadorViajes - 1
    while 1 <= contadorViajes <= 20:
        totalGastado = tarifaEstandar + totalGastado
        contadorViajes = contadorViajes - 1
    return totalGastado

#programa principal
inicio = totalGastado(44)
print("El total gastado en viajes es de $", inicio)
# 100% = 58 | 80% =  46,40 | 70% = 40,60 | 60% = 34,80