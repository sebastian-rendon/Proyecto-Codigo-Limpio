from flask import Flask
from flask import render_template, request
import sys
sys.path.append("src")

from model.liquidacion import Liquidacion
from model.logica_liquidador import LiquidacionSalario, calcular_salario
from controller.liquidaciones_controller import LiquidacionesController

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/crear_tablas')
def crear_tablas():
    LiquidacionesController.crear_tabla()
    return "Tablas creadas exitosamente"

@app.route('/crear_liquidacion')
def crear_liquidacion():
    return render_template("crear_liquidacion.html")

@app.route('/guardar_liquidacion')
def guardar_liquidacion():
    salario = float(request.args["salario"])
    horas_extra = float(request.args["horas_extra"])
    bonificaciones = float(request.args["bonificaciones"])
    comisiones = float(request.args["comisiones"])
    auxilios = float(request.args["auxilios"])
    porcentaje_salud = float(request.args["porcentaje_salud"])
    porcentaje_pension = float(request.args["porcentaje_pension"])
    impuestos = float(request.args["impuestos"])

    liquidacion_salario = LiquidacionSalario(
        salario=salario, horas_extra=horas_extra,
        bonificaciones=bonificaciones, comisiones=comisiones,
        auxilios=auxilios, salud=porcentaje_salud,
        pension=porcentaje_pension, impuesto_dinero=impuestos
    )

    total_devengado = salario + horas_extra + bonificaciones + comisiones + auxilios
    salario_neto = calcular_salario(liquidacion_salario)

    liquidacion = Liquidacion(
        salario=salario, horas_extra=horas_extra,
        bonificaciones=bonificaciones, comisiones=comisiones,
        auxilios=auxilios, porcentaje_salud=porcentaje_salud,
        porcentaje_pension=porcentaje_pension, impuestos=impuestos,
        total_devengado=total_devengado, salario_neto=salario_neto
    )

    LiquidacionesController.insertar(liquidacion)
    return render_template("liquidacion_guardada.html", liquidacion=liquidacion)


if __name__ == '__main__':
    app.run(debug=True)