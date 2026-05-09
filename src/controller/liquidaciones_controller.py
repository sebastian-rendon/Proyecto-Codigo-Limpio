import sys
sys.path.append(".")
sys.path.append("src")
import psycopg2
from model.liquidacion import Liquidacion

class LiquidacionesController:

    def obtener_cursor():
        """ Crea un objeto cursor para poder ejecutar SQL en la BD """
        connection = psycopg2.connect(
            database='liquidador_nomina_67mk',
            user='liquidador_nomina_67mk_user',
            password='lVWtEYZko9Bxa2b5Tc3igH9aQwb0Fs5P',
            host='dpg-d7v2tu9kh4rs739nbe8g-a.virginia-postgres.render.com',
            port=5432
        )
        cursor = connection.cursor()
        return cursor

    def insertar(liquidacion: Liquidacion):
        cursor = LiquidacionesController.obtener_cursor()
        consulta = f"""INSERT INTO liquidaciones (fecha, salario, horas_extra, bonificaciones,
            comisiones, auxilios, porcentaje_salud, porcentaje_pension, impuestos,
            total_devengado, salario_neto)
            VALUES (NOW(), {liquidacion.salario}, {liquidacion.horas_extra},
            {liquidacion.bonificaciones}, {liquidacion.comisiones}, {liquidacion.auxilios},
            {liquidacion.porcentaje_salud}, {liquidacion.porcentaje_pension},
            {liquidacion.impuestos}, {liquidacion.total_devengado}, {liquidacion.salario_neto})
            RETURNING id"""
        cursor.execute(consulta)
        liquidacion.id = cursor.fetchone()[0]
        #commit para guardar los cambios en la BD
        cursor.connection.commit()



    def buscar_liquidacion(id: int) -> Liquidacion:
        pass

    