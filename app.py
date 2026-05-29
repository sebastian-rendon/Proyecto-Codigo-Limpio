from flask import Flask

import sys
sys.path.append("src")

from view.web import vista_liquidaciones

app = Flask(__name__)

app.register_blueprint(vista_liquidaciones.blueprint)

if __name__ == '__main__':
    app.run(debug=True)