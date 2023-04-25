import random

def imprimirMatriz(matriz):
    for filas in matriz:
        for elementos in filas:
            nro, txt = elementos
            print("%2d" %nro, "%8s" %txt, end="  |  ")
        print()
            
def repartirCartas(matriz):
    palos = ["Espadas", "Bastos", "Copas", "Oro"]
    aux = []
    compara = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            cartaNro = random.randint(1,12)
            while cartaNro == 8 or cartaNro == 9:
                cartaNro = random.randint(1,12)
            cartaPalo = random.randint(0,3)
            compara = [cartaNro, palos[cartaPalo]]
            while compara in aux:
                cartaNro = random.randint(1,12)
                while cartaNro == 8 or cartaNro == 9:
                    cartaNro = random.randint(1,12)
                cartaPalo = random.randint(0,3)
                compara = [cartaNro, palos[cartaPalo]]
            else:    
                aux = aux + [[cartaNro, palos[cartaPalo]]]
                matriz[i][j] = [cartaNro, palos[cartaPalo]]
  
            
            
#programa
cant_jugadores = int(input("¿Cuántos jugadores tiene la partida? "))
while cant_jugadores < 2 or cant_jugadores > 6:
    print("Cantidad no permitida. Ingrese nuevamente ")
    cant_jugadores = int(input("¿cuántos jugadores tiene la partida? "))
miMatriz = [[0] * 3 for i in range(cant_jugadores)]
repartirCartas(miMatriz)
print()
print("------------Se reparten las cartas------------")
print()
imprimirMatriz(miMatriz)
    
