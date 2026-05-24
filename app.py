from flask import Flask
from flask import render_template, request
import sys
sys.path.append("src")

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo"

if __name__ == '__main__':
    app.run(debug=True)