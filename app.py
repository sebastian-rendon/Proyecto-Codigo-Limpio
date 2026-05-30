from flask import Flask

import sys
sys.path.append("src")

from view.web import vista_liquidaciones

# Flask constructor: crea una variable que servira para comunicar el servidor con el cliente, es decir, con el navegador
app = Flask(__name__)

app.register_blueprint(vista_liquidaciones.blueprint)

#permite que la aplicacion se ejecute indipendientemente, es decir, que se ejecute solo si se ejecuta este archivo y no si se importa desde otro archivo
if __name__ == '__main__':
    app.run(debug=True)