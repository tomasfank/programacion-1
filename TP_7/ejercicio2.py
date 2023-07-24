""" Desarrollar una función que reciba un número binario y lo devbuelva convertido a base
decimal """

def binario_a_decimal(numero, pos=0):
    if numero == 0:
        return 0
    else:
        ultimoDigito = numero % 10
        return ultimoDigito * (2 ** pos) + binario_a_decimal(numero // 10, pos + 1)
    
#programa
binario = 101011
decimal = binario_a_decimal(binario)
print(decimal)