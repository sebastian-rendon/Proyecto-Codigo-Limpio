# Liquidador de Nómina


## Autores

* **Luis Alejandro Correa Arrieta** (Interfaz gráfica)
* **Juan Felipe Santiago Pinzon** (Interfaz gráfica)
* **Juan Camilo Gomez** (dueño)
* **Sebastian Rendon** (dueño)

---

## Descripción

Este proyecto corresponde a una aplicación web para el curso **Código Limpio** de la **Universidad de Medellín**.

El **Liquidador de Nómina** permite calcular el valor total a pagar a un empleado, teniendo en cuenta:

1.  **Valores Devengados:** Salario base, horas extra (recargos), bonificaciones, comisiones y auxilios (transporte/otros).
2.  **Deducciones de Ley:** Descuentos obligatorios de salud, pensión e impuestos aplicables.

El valor final de la nómina se obtiene como la diferencia entre los valores devengados y las deducciones.

---

## Objetivo

Desarrollar una aplicación clara, funcional y bien estructurada que aplique los principios de **Código Limpio**.

## Funcionalidades principales

* Cálculo del total devengado por el empleado
* Cálculo del valor neto a pagar
* Separación clara de responsabilidades
* Código legible y modular
---

## Ejecución

### Prerrequisitos
 
Antes de ejecutar el proyecto, asegúrese de tener instalado lo siguiente:
 
- **Python 3.8** o superior. Puede verificar su versión con:
 
```
python --version
```

## Base de datos

Esta aplicación requiere una base de datos PostgreSQL y el paquete `psycopg2`.

Instale el paquete con:

```
pip install psycopg2
```

- **PostgreSQL**: base de datos remota (se usa Render.com)

Asegúrese de tener una base de datos PostgreSQL y sus respectivos datos de acceso.

Copie el archivo `secret_config_sample.py` como `secret_config.py` y establezca en este archivo los datos de conexión a su base de datos.

Antes de ejecutar la aplicación por primera vez, ejecute el script SQL para crear la tabla:
```
sql\crear-liquidaciones.sql
```
---

## Funcionalidades con base de datos

- Guardar liquidaciones en PostgreSQL
- Buscar liquidaciones por ID
- Validar datos de entrada
- Ejecutar pruebas automáticas

---

## Uso de funcionalidades

### Guardar una liquidación

Ejecute:

```bash
py src/view/guardar_liquidacion.py
```

El programa solicitará los datos de la liquidación, calculará automáticamente el total devengado y el salario neto, y guardará la información en PostgreSQL.

---

### Buscar una liquidación

Ejecute:

```bash
py src/view/buscar_liquidacion.py
```

El programa solicitará el ID de la liquidación y mostrará la información almacenada en la base de datos.

---

## Configuración de credenciales

Copie el archivo `secret_config_sample.py` como `secret_config.py` 
y reemplace los valores con sus credenciales de PostgreSQL:

PGHOST='su host aqui'

PGDATABASE='su base de datos aqui'

PGUSER='su usuario aqui'

PGPASSWORD='su contraseña aqui'

PGPORT=5432

⚠️ Nunca suba `secret_config.py` al repositorio.
---
### Ejecución del programa con base de datos
 
Ubicados en la carpeta raíz del proyecto, ejecute:
 
```
py src/view/consola_liquidador.py
```

---
 
## Ejecución de pruebas
 
Para ejecutar las pruebas unitarias, diríjase a la carpeta raíz y use el siguiente comando:
 
```
py tests\test_liquidador.py
```

Para poder ejecutarlas desde la carpeta raíz, debe indicar la ruta de búsqueda donde se encuentran los módulos. Incluya las siguientes líneas al inicio del módulo de pruebas:
 
```python
import sys
sys.path.append("src")
```
 
## Ejecución de pruebas de base de datos

Para ejecutar las pruebas de la base de datos, use:

```
py tests\test_liquidador_db.py
```
## Aplicación Web

Esta aplicación requiere instalar `Flask`.

Instale el paquete con:

```
pip install flask
```
Para ejecutar la aplicación localmente:
```
python app.py
```
Luego abra su navegador en `http://localhost:5000`

---
## Arquitectura

### Bibliotecas usadas
- `unittest`: pruebas automatizadas (incluida en Python, no requiere instalación)

### Organización de módulos

- **`docs/`**: Contenido de apoyo al proyecto. Contiene los casos de prueba en Excel y la entrevista con el experto.

- **`src/`**: Código fuente de la aplicación, dividido en dos capas:
  - **`model/`**: Capa de lógica y datos.
    - `errores.py`: Define las excepciones personalizadas y las constantes del dominio.
    - `logica_liquidador.py`: Contiene la clase `LiquidacionSalario`, las validaciones y el cálculo del salario neto.
  - **`view/`**: Capa de interacción con el usuario.
    - `consola_liquidador.py`: Interfaz por consola que recibe los datos del usuario y muestra el resultado.

- **`tests/`**: Pruebas unitarias de la aplicación.
  - `test_liquidador.py`: Casos de prueba para validaciones y cálculo del salario neto.
---
 - **`sql/`**: Scripts SQL para la base de datos.
  - `crear-liquidaciones.sql`: Crea la tabla de liquidaciones.
  - `borrar-liquidaciones.sql`: Elimina la tabla de liquidaciones.
- **`src/controller/`**: Capa de acceso a datos.
  - `liquidaciones_controller.py`: Operaciones de inserción y consulta en la BD.
- **`src/model/`**:
  - `liquidacion.py`: Clase que representa una liquidación almacenada en la BD.

Cada carpeta de código fuente contiene un archivo `__init__.py` que permite que Python reconozca la carpeta como un módulo y pueda realizar importaciones correctamente.


---
### Estructuracion de carpetas

```text
PROYECTO-LIQUIDADOR-NOMINA/
│
├── .github/
├── .venv/
├── .vscode/
│   └── settings.json
│
├── aplicacion_android/
│   └── main-0.1-arm64-v8a_armeabi-v7a-debug.apk
│
├── docs/
│   ├── CASOS DE PRUEBA PROYECTO_1.xlsx
│   └── Entrevista.m4a
│
├── sql/
│   ├── crear-liquidaciones.sql
│   └── borrar-liquidaciones.sql
│
├── src/
│   ├── controller/
│   │   ├── __init__.py
│   │   └── liquidaciones_controller.py
│   │
│   ├── model/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── errores.py
│   │   ├── liquidacion.py
│   │   └── logica_liquidador.py
│   │
│   └── view/
│       ├── __pycache__/
│       ├── gui/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   └── My_App.py
│       ├── __init__.py
│       └── consola_liquidador.py
│
├── tests/
│   ├── __init__.py
│   ├── test_liquidador_db.py
│   └── test_liquidador.py
│
├── .gitignore
├── buildozer.spec
├── main.py
├── main.spec
├── README.md
├── secret_config.py
└── secret_config_sample.py
```

---
## 📤 Entradas y salidas
 
### Entradas
 
| Campo | Descripción |
|---|---|
| Salario | Salario base del empleado |
| Horas extras | Cantidad y tipo de horas extras trabajadas |
| Bonificaciones | Bonos adicionales al salario |
| Comisiones | Comisiones generadas |
| Auxilios | Auxilios (transporte u otros) |
| Salud (%) | Porcentaje de descuento por salud |
| Pensión (%) | Porcentaje de descuento por pensión |
| Impuestos (%) | Porcentaje de descuento por impuestos (si aplica) |
 
### Proceso
 
Se realiza la suma del salario base con los beneficios extra (**valores devengados**): horas extra, bonificaciones, comisiones y auxilios. A este subtotal se le restan las **deducciones de ley**: salud, pensión e impuestos (en caso de que apliquen).
 
```
Nómina neta = (Salario + Horas extra + Bonificaciones + Comisiones + Auxilios)
            - (Salud + Pensión + Impuestos)
```
 
### Salidas
 
- **Salario Neto** a pagar al empleado
 
---

## Entrevista

Este repositorio incluye una entrevista relacionado al proyecto a un invitado con mas experiencia, es un intercambio de ideas antes de la construcción del mismo para aclarar dudas y generar nuevas ideas de construcción.

📁 La entrevista completa se encuentra en `docs/Entrevista.m4a`.

---
## Documento casos de prueba

Este repositorio incluye el documento de excel el cual tiene los casos de pruebas propuestos para el proyecto.

📁 El documento de excel se encuentra en `docs/CASOS DE PRUEBA PROYECTO_1.xlsx`

---
## 🏫 Institución

**Universidad de Medellín**

Curso: **Código Limpio**

---

**Objetivo Técnico:** Desarrollar una aplicación clara y bien estructurada que aplique los principios de modularidad, validación de datos y legibilidad para entregar una herramienta funcional y fácil de mantener.

---

## 🚀 Guía de Ejecución y Despliegue

### 1. Ejecución desde Código Fuente (Consola)
Ideal para entornos de desarrollo y depuración rápida de la lógica de negocio.
* **Prerrequisito:** Python 3.8 o superior instalado en el sistema.
* **Comando de ejecución:**
  ```bash
  python src/view/consola_liquidador.py

---

## Requisitos del sistema

- Python **3.8 o superior**
- Pip (gestor de paquetes de Python)

Verificar versión:

```bash
python --version
