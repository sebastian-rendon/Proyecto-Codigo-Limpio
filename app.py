from flask import Flask
from flask import render_template, request
import sys
sys.path.append("src")

from controller.liquidaciones_controller import LiquidacionesController

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/crear_tablas')
def crear_tablas():
    LiquidacionesController.crear_tabla()
    return "Tablas creadas exitosamente"

if __name__ == '__main__':
    app.run(debug=True)