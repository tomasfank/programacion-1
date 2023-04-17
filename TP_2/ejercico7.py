""" Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá
realizarse exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva sino
que se modificará la primera. Por ejemplo, si lista1 = [8,1,3] y lista2 = [5,9,7], lista1 deberá
quedar como [8,5,1,9,3,7] """


lista1 = [1,2,3]
lista2 = [4,5,6]

lista1[1::2]
for x in range(len(lista1)):
    lista1.insert(x*2,lista2[0::1])

print(lista1)
#consultar con el profesor 