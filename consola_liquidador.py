import logica_liquidador

try:
    entrada_salario = input("Ingrese el valor del salario mensual: ")

    if entrada_salario == "":
        raise ValueError("ERROR, El salario es obligatorio")

    salario = float(entrada_salario)

    horas_extra = float(input("Ingrese el valor de las horas extra: "))
    bonificaciones = float(input("Ingrese el valor de las bonificaciones: "))
    comisiones = float(input("Ingrese el valor de las comisiones: "))
    auxilios = float(input("Ingrese el valor de los auxilios: "))

    salud = float(input("Ingrese el valor de la salud que usted paga (en decimal): "))
    pension = float(input("Ingrese el valor de la pension que usted paga (en decimal): "))
    impuesto_dinero = float(input("Ingrese el valor de los impuestos que usted paga: "))

    salario_neto = logica_liquidador.calcular_salario(
        salario,
        horas_extra,
        bonificaciones,
        comisiones,
        auxilios,
        salud,
        pension,
        impuesto_dinero
    )

    print("El salario neto es:", salario_neto)

except Exception as e:
    print("Ocurrió un error:", e)