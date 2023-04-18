""" Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá
realizarse exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva sino
que se modificará la primera. Por ejemplo, si lista1 = [8,1,3] y lista2 = [5,9,7], lista1 deberá
quedar como [8,5,1,9,3,7] """

#Creamos ambas listas
lista1 = [1,2,3]
lista2 = [4,5,6]

#Intercalamos las posiciones 
lista1[1:1] = lista2[0:1]
lista1[3:3] = lista2[1:2]
lista1[5:5] = lista2[2:3]

#imprimimos lista1
print(lista1)

#otra manera de resolver el mismo ejercicio
lista1 = [1,2,3]
lista2 = [4,5,6]

for x in range(0, len(lista1)):
    I = x*2+1
    lista1[I:I] = lista2[x:x+1]
    
print(lista1)

