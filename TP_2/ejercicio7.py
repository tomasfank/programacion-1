""" Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá
realizarse exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva sino
que se modificará la primera. Por ejemplo, si lista1 = [8,1,3] y lista2 = [5,9,7], lista1 deberá
quedar como [8,5,1,9,3,7] """

# Funciones
def intercalar(lista1,lista2):
    for i in range(len(lista1)):
        x = i*2+1 # "x" es la posición siguiente a "i"
        lista1[x:x:2] = lista2[i:i+1]
    

# Programa
# Requisito previo => Las listas deben tener el mismo tamaño
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

print(f"Lista 1 = {lista1}")
print(f"Lista 2 = {lista2}")

intercalar(lista1,lista2)

print(f"Lista intercalada = {lista1}")