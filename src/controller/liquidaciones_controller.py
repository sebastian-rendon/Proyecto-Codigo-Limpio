import sys

from model import liquidacion
sys.path.append(".")    
sys.path.append("src")
import psycopg2
from model.liquidacion import Liquidacion
import secret_config


class LiquidacionesController:

    def crear_tabla():
        cursor = LiquidacionesController.obtener_cursor()

        #Lee el contenido del archivo y lo guarda en una variable sql
        with open( "sql/crear-liquidaciones.sql", "r") as archivo:
            sql = archivo.read()

        cursor.execute( sql )
        cursor.connection.commit()

    def borrar_tabla():
        cursor = LiquidacionesController.obtener_cursor()

        #Lee el contenido del archivo y lo guarda en una variable sql
        with open( "sql/borrar-liquidaciones.sql", "r") as archivo:
            sql = archivo.read()

        cursor.execute( sql )
        cursor.connection.commit()


    def obtener_cursor():
        """ Crea un objeto cursor para poder ejecutar SQL en la BD """

        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
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
        cursor = LiquidacionesController.obtener_cursor()
        consulta = f"""SELECT id, fecha, salario, horas_extra, bonificaciones, comisiones,
            auxilios, porcentaje_salud, porcentaje_pension, impuestos, total_devengado, salario_neto
            FROM public.liquidaciones WHERE id = {id}"""
        cursor.execute(consulta)
        fila = cursor.fetchone()
        if fila is None:
            return None
        liquidacion = Liquidacion(
            id=fila[0], fecha=fila[1], salario=fila[2],
            horas_extra=fila[3], bonificaciones=fila[4],
            comisiones=fila[5], auxilios=fila[6],
            porcentaje_salud=fila[7], porcentaje_pension=fila[8],
            impuestos=fila[9], total_devengado=fila[10],
            salario_neto=fila[11]
        )
        return liquidacion
    
    def actualizar(liquidacion: Liquidacion):
        cursor = LiquidacionesController.obtener_cursor()
        consulta = f"""UPDATE liquidaciones SET
            salario = {liquidacion.salario},
            horas_extra = {liquidacion.horas_extra},
            bonificaciones = {liquidacion.bonificaciones},
            comisiones = {liquidacion.comisiones},
            auxilios = {liquidacion.auxilios},
            porcentaje_salud = {liquidacion.porcentaje_salud},
            porcentaje_pension = {liquidacion.porcentaje_pension},
            impuestos = {liquidacion.impuestos},
            total_devengado = {liquidacion.total_devengado},
            salario_neto = {liquidacion.salario_neto}
            WHERE id = {liquidacion.id}"""
        cursor.execute(consulta)
        cursor.connection.commit()
    