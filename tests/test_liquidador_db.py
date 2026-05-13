import unittest
import sys
sys.path.append("src")
from model import liquidacion
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

# ─── BUSCAR ───────────────────────────────────────────

    def test_buscar_1(self):
        """ Busca una liquidacion y verifica que el salario neto es correcto """
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
        LiquidacionesController.insertar(liquidacion)
        liquidacion_buscada = LiquidacionesController.buscar_liquidacion(liquidacion.id)
        self.assertEqual(float(liquidacion_buscada.salario_neto), 4850000)

    def test_buscar_2(self):
        """ Busca una liquidacion y verifica que el total devengado es correcto """
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
        self.assertEqual(float(liquidacion_buscada.total_devengado), 6420000)

    def test_buscar_3(self):
        """ Busca una liquidacion y verifica que el salario base es correcto """
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
        self.assertEqual(float(liquidacion_buscada.salario), 4500000)

    def test_buscar_4(self):
        """ Busca una liquidacion y verifica que el salario base es correcto """
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
        deduccion_esperada = float(liquidacion_buscada.total_devengado) - float(liquidacion_buscada.salario_neto)
        self.assertEqual(deduccion_esperada, 360000)


    def test_buscar_id_inexistente(self):
        """ Verifica que buscar un id que no existe retorna None """
        liquidacion_buscada = LiquidacionesController.buscar_liquidacion(999999)
        self.assertIsNone(liquidacion_buscada)
if __name__ == '__main__':
    unittest.main()