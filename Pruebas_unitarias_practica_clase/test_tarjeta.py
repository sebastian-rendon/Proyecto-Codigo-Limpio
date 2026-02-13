import unittest
import logica_tarjeta

class TestCalculoCuotaTarjeta( unittest.TestCase):

    def test_normal_1(self):

        #definir entradas
        compra = 200000
        interes = 0.031
        plazo = 36

        #proceso
        cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)

        #Datos de salida esperados
        cuota_esperada = 9297.96

        #verificar la salida
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)



if __name__ == '__main__':
    unittest.main()