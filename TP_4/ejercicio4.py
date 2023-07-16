""" Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y lo convierta
en un número romano, devolviéndolo en una cadena de caracteres. ¿En qué cambiaría la función si
el rango de valores fuese diferente? """

# I = 1 | V = 5 | X = 10 | L = 50 | C = 100 | D = 500 | M = 1000

def convertir_romano(numero):
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    millares = ["", "M", "MM", "MMM"]

    resultado = millares[numero // 1000] + centenas[(numero % 1000) // 100] + decenas[(numero % 100) // 10] + unidades[numero % 10]

    return resultado




#programa 
while True:
    nro = int(input("Ingrese un número entre 0 y 3999 = "))
    if 0 <= nro <= 3999:
        break
 
print(f"{nro} en números romanos = {convertir_romano(nro)}")
