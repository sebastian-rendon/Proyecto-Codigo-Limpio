import unittest
import sys
sys.path.append("src")
from model.liquidacion import Liquidacion
from controller.liquidaciones_controller import LiquidacionesController

class TestLiquidacion(unittest.TestCase):

    def test_insert_1(self):
        # Crear una liquidacion
        liquidacion = Liquidacion(
            salario=2000000,
            horas_extra=100000,
            bonificaciones=50000,
            comisiones=30000,
            auxilios=100000,
            porcentaje_salud=4,
            porcentaje_pension=4,
            impuestos=50000,
            total_devengado=2280000,
            salario_neto=2070000
        )

        # Guardarla en la BD
        LiquidacionesController.insertar(liquidacion)

        # Buscarla
        liquidacion_buscada = LiquidacionesController.buscar_liquidacion(liquidacion.id)

        # Verificar si la trajo bien
        self.assertTrue(liquidacion.is_equal(liquidacion_buscada))

if __name__ == '__main__':
    unittest.main()