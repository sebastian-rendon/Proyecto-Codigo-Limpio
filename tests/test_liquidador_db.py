import unittest
import sys
sys.path.append("src")
from model.liquidacion import Liquidacion
from controller.liquidaciones_controller import LiquidacionesController

class TestLiquidacion(unittest.TestCase):

    def test_insert_1(self):
        # Crear una liquidacion
        liquidacion = Liquidacion(
            salario= 5000000,
            horas_extra= 150000,
            bonificaciones= 50000,
            comisiones= 100000,
            auxilios= 0,
            porcentaje_salud=4,
            porcentaje_pension=4,
            impuestos=50000,
            total_devengado=5300000,
            salario_neto=4850000
        )

        # Guardarla en la BD
        LiquidacionesController.insertar(liquidacion)

        # Buscarla
        liquidacion_buscada = LiquidacionesController.buscar_liquidacion(liquidacion.id)

        # Verificar si la trajo bien
        self.assertTrue(liquidacion.is_equal(liquidacion_buscada))


    def test_insert_2(self):
        liquidacion = Liquidacion(
            salario= 6200000,
            horas_extra= 100000,
            bonificaciones= 100000,
            comisiones= 20000,
            auxilios= 0,
            porcentaje_salud=4,
            porcentaje_pension=4, 
            impuestos=62000,
            total_devengado=6420000, 
            salario_neto=5862000
        )
        LiquidacionesController.insertar(liquidacion)
        liquidacion_buscada = LiquidacionesController.buscar_liquidacion(liquidacion.id)
        self.assertTrue(liquidacion.is_equal(liquidacion_buscada))

    def test_insert_3(self):
        liquidacion = Liquidacion(
            salario= 4500000,
            horas_extra= 50000,
            bonificaciones= 50000,
            comisiones= 20000,
            auxilios= 0,
            porcentaje_salud=4,
            porcentaje_pension=4, 
            impuestos=45000,
            total_devengado=4620000, 
            salario_neto=4215000
        )
        LiquidacionesController.insertar(liquidacion)
        liquidacion_buscada = LiquidacionesController.buscar_liquidacion(liquidacion.id)
        self.assertTrue(liquidacion.is_equal(liquidacion_buscada))

    def test_insert_4(self):
        liquidacion = Liquidacion(
            salario= 4000000,
            horas_extra= 20000,
            bonificaciones= 60000,
            comisiones= 10000,
            auxilios= 0,
            porcentaje_salud=4,
            porcentaje_pension=4, 
            impuestos=40000,
            total_devengado=4270000, 
            salario_neto=3910000
        )
        LiquidacionesController.insertar(liquidacion)
        liquidacion_buscada = LiquidacionesController.buscar_liquidacion(liquidacion.id)
        self.assertTrue(liquidacion.is_equal(liquidacion_buscada))

if __name__ == '__main__':
    unittest.main()