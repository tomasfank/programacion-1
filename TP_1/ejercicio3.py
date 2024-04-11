""" Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes se solicita desarrolar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función. """

"""
* Esquema de tarifas =
    | Cantidad de viajes   | Valor de pasaje                         |
    | 1 a 20               | $58                                     |
    | 21 a 30              | 20% de descuento sobre la tarifa máxima |
    | 31 a 40              | 30% de descuento sobre la tarifa máxima |
    | Más de 40            | 40% de descuento sobre la tarifa máxima |
"""

# Funicones
def calcularGastos(viajes):
    total = 0
    for x in range(viajes):
        print(x)
        if (x+1) < 21:
            total = total + 58 
        elif 20 < (x+1) < 31:
            total = total + (58 * 0.80)
        elif 30 < (x+1) < 41:
            total = total + (58 * 0.70)
        else:
            total = total + (58 * 0.60)
    return total

def ingresar():
    while True:
        a = int(input("¿Cuántos viajes realizaste? = "))
        if a <= 0:
            print("Debes ingresar números mayores a 0.")
            continue
        else:
            return a
        
# Programa
cantidad = ingresar()
gastos = calcularGastos(cantidad)
print(f"En los últimos 30 días has gastado ${gastos}.")