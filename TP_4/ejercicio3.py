""" Los números de dos cajas fuertes están intercalados dentro de un número llamado "clave
maestra", cuya longitud no se conoce. Realizar un programa para obtener ambas claves, donde
la primera se construye con los dígitos ubicados en posiciones impares de la clave maestra y la
segunda con los dígitos ubicados en las posiciones pares. Los dígitos se numeran desde la izquierda
Ejemplo: si la clave maestra fuera 18293, la calve 1 sería 123 y la clave 2 sería 89 """

def crearClaves(maestra):
    c1 = ""
    c2 = ""
    for i in range(len(maestra)):
        if (i + 1) % 2 == 0:
            c1 = c1 + maestra[i]
        else:
            c2 = c2 + maestra[i]
    return c1, c2

#programa
claveMaestra = input("ingrese la clave maestra ")
c1 , c2 = crearClaves(claveMaestra)
print("La clave 1 es =", c1)
print("La clave 2 es =", c2)
