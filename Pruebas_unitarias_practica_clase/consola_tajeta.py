import logica_tarjeta

compra= input("ingrese el valor de la compra: ")
interes = input("ingrese el valor del interés mensual en porcentaje: ")
plazo = input("ingrese el número de meses para pagar la compra: ")

cuota = logica_tarjeta.calcular_cuota(compra, interes, plazo)

print( cuota)