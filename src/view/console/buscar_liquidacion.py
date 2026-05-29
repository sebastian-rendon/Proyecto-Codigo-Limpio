import sys

sys.path.append("src")

from model import liquidacion
from controller.liquidaciones_controller import LiquidacionesController

try:

    id_liquidacion = int(input("Ingrese el id de la liquidacion que desea buscar: "))

    liquidacion_buscada = LiquidacionesController.buscar_liquidacion(id_liquidacion)

    if liquidacion_buscada is None:
        print("No se encontró la liquidación")
    else:
        print("Liquidación encontrada:")
        print(f"ID: {liquidacion_buscada.id}")
        print(f"Salario: {liquidacion_buscada.salario}")
        print(f"Salario neto: {liquidacion_buscada.salario_neto}")

except Exception as err:
    print("Error:")
    print(str(err))