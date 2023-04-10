""" Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique
al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros,
correspondientes al total de la compra y al dinero recibido. Informar cuentos billetes de cada
denominación deben ser entregados al cliente como vuelto, de tal forma que se minimicen la
cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1.
Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo = si la compra
fuera de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50
1 billete de $20, 1 billete de $10 y 3 billetes de $1. """

def vuelto(compraTotal, dineroRecibido):
    vuelto = dineroRecibido - compraTotal
    cambio = [0, 0, 0, 0, 0, 0, 0]
    while vuelto >= 500:
        vuelto -= 500
        cambio[0] += 1
    while vuelto >= 100:
        vuelto -= 100
        cambio[1] += 1
    while vuelto >= 50:
        vuelto -= 50
        cambio[2] += 1
    while vuelto >= 20:
        vuelto -= 20
        cambio[3] += 1 
    while vuelto >= 10:
        vuelto -= 10
        cambio[4] += 1
    while vuelto >= 5:
        vuelto -= 5
        cambio[5] += 1
    while vuelto >= 1:
        vuelto -= 1
        cambio[6] += 1 
    imprimirResultado(cambio)

def imprimirResultado(vuelto):
    print("El cajero debe entregar al cliente el siguiente cambio.\n$500=", vuelto[0], "$100=", vuelto[1], "$50=", vuelto[2], "$20=", vuelto[3], "$10=", vuelto[4], "$5=", vuelto[5], "$1=", vuelto[6])
                   
def main():
    total = int(input("¿Cuánto cuesta el total de la compra? "))
    abonado = int(input("¿Con cuánto dinero quiere pagar el cliente? "))
    if abonado < total:
        print("Esa cantidad de dinero no alcanza para pagar toda la compra ")
        return
    vuelto(total, abonado)
    
    
#programa
main()