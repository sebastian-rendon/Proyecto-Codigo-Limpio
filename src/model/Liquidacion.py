import datetime

class Liquidacion:

    def __init__(self,
        salario: float,
        horas_extra: float,
        bonificaciones: float,
        comisiones: float,
        auxilios: float,
        porcentaje_salud: float,
        porcentaje_pension: float,
        impuestos: float,
        total_devengado: float,
        salario_neto: float,
        fecha: datetime = None,
        id: int = None):
        """ Representa una liquidación de nómina almacenada en la tabla liquidaciones """

        self.id = id
        self.fecha = fecha
        self.salario = salario
        self.horas_extra = horas_extra
        self.bonificaciones = bonificaciones
        self.comisiones = comisiones
        self.auxilios = auxilios
        self.porcentaje_salud = porcentaje_salud
        self.porcentaje_pension = porcentaje_pension
        self.impuestos = impuestos
        self.total_devengado = total_devengado
        self.salario_neto = salario_neto

    def is_equal(self, otro) -> bool:
        """ Verifica cada atributo de self contra otra instancia de esta clase y dispara una excepcion si no son iguales """

        assert(self.id == otro.id)
        assert(str(self.fecha) == str(otro.fecha))
        assert(float(self.salario) == float(otro.salario))
        assert(float(self.horas_extra) == float(otro.horas_extra))
        assert(float(self.bonificaciones) == float(otro.bonificaciones))
        assert(float(self.comisiones) == float(otro.comisiones))
        assert(float(self.auxilios) == float(otro.auxilios))
        assert(float(self.porcentaje_salud) == float(otro.porcentaje_salud))
        assert(float(self.porcentaje_pension) == float(otro.porcentaje_pension))
        assert(float(self.impuestos) == float(otro.impuestos))
        assert(float(self.total_devengado) == float(otro.total_devengado))
        assert(float(self.salario_neto) == float(otro.salario_neto))
        return True