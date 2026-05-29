import sys


sys.path.append("src")
from model.logica_liquidador import LiquidacionSalario, calcular_salario
from model.liquidacion import Liquidacion

from controller.liquidaciones_controller import LiquidacionesController


try:    

    # Leer datos de entrada de la tarjeta
    liquidacion = Liquidacion( salario=0, horas_extra=0, bonificaciones=0, comisiones=0, auxilios=0, porcentaje_salud=0, porcentaje_pension=0, impuestos=0, total_devengado=0, salario_neto=0, fecha=None, id=None)

    liquidacion.salario = float(input("Ingrese el salario: "))
    liquidacion.horas_extra = float(input("Ingrese el valor de las horas extra: "))
    liquidacion.bonificaciones = float(input("Ingrese el valor de las bonificaciones: "))
    liquidacion.comisiones = float(input("Ingrese el valor de las comisiones: "))
    liquidacion.auxilios = float(input("Ingrese el valor de los auxilios: "))
    liquidacion.porcentaje_salud = float(input("Ingrese el porcentaje de salud: "))
    liquidacion.porcentaje_pension = float(input("Ingrese el porcentaje de pension: "))
    liquidacion.impuestos = float(input("Ingrese el valor de los impuestos: "))
    liquidacion.total_devengado = sum([
        liquidacion.salario,
        liquidacion.horas_extra,
        liquidacion.bonificaciones,
        liquidacion.comisiones,
        liquidacion.auxilios
    ])

    liquidacion_salario = LiquidacionSalario(
        salario=liquidacion.salario,
        horas_extra=liquidacion.horas_extra,
        bonificaciones=liquidacion.bonificaciones,
        comisiones=liquidacion.comisiones,
        auxilios=liquidacion.auxilios,
        salud=liquidacion.porcentaje_salud,
        pension=liquidacion.porcentaje_pension,
        impuesto_dinero=liquidacion.impuestos
    )

    liquidacion.salario_neto = calcular_salario(liquidacion_salario)

    # Proceso: guadar la liquidacion en la BD
    LiquidacionesController.insertar(liquidacion)


    #Salida: Mostrar si fue exitoso
    print("Liquidación realizada exitosamente!, id de la liquidacion: ", liquidacion.id)

except Exception as e:
    print("Ocurrió un error al realizar la liquidación: ", str(e) )