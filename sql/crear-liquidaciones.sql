create table if not exists liquidaciones (
    id serial primary key,
    fecha timestamp not null,
    salario decimal not null,
    horas_extra decimal not null,
    bonificaciones decimal not null,
    comisiones decimal not null,
    auxilios decimal not null,
    porcentaje_salud decimal not null,
    porcentaje_pension decimal not null,
    impuestos decimal not null,
    total_devengado decimal not null,
    salario_neto decimal not null
);