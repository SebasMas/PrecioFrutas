#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.


frutas = {
    "Plátano":	1.35,
    "Manzana":	0.80,
    "Pera":	0.85,
    "Naranja":	0.70,
    }

print(frutas)
print("----------------")

fruta = input("Qué fruta desea llevar?: ")
kilos = float(input("Cuántos kilos de fruta va a llevar?: "))
for i in frutas:
    #precio = frutas[fruta]
    costo = (frutas[fruta]) * kilos
print("El monto a pagar por los ",kilos,"kg de ",fruta," es: ",costo)
    