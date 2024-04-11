lista = [x for x in range(1, 100) if x % 7 == 0 or x % 10 == 7]
print(lista)

lista.sort(key=lambda n : sum(int(d) for d in str(n)))
print(lista)