""" Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido. Informar cuentos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimicen la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. 
Ejemplo = si la compra fuera de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1. """

# Funciones
def calcularVuelto(compra, pago, billetes):
    vuelto = []
    for x in range(len(billetes)):
        vuelto.append(0)
    diferencia = pago - compra 
    i = 0
    while diferencia != 0:
        if diferencia >= billetes[i]:
            diferencia -= billetes[i]
            vuelto[i] = vuelto[i]+1
        else:
            i+=1
    return vuelto

# Programa 
billetes = [500,100,50,20,10,5,1]
while True:
    total = float(input("Ingrese el valor de la compra = "))
    paga = float(input("¿Con cuánto pagará el cliente? = "))
    if paga >= total:
        vuelto = calcularVuelto(total, paga, billetes)
        print("El cliente pagará con:")
        for i in range(len(vuelto)):
            print(f"${billetes[i]} = {vuelto[i]}")
        continuar = input("¿Desea continuar S/N?")
        if continuar.lower() == "n":
            print("Programa finalizado.")
            break
    else:
        print(f"Faltan ${total-paga} para cubrir el total compra.")