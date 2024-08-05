# IMPORTANTE: NO borrar los comentarios

# IMPORTANTE: Utilice la carpeta templates del repositorio como parte del desafio

# Alumno: Arreglar el código a continuación para que funcione
# en el editor de código:

import traceback
from datetime import datetime
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for

# Crear el server Flask
app = Flask(__name__)


# ------------ Rutas o endpoints ----------------- #
# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        # Alumno:
        # Renderizar el temaplate HTML index.html
        print("Renderizar index.html")
        return 'index.html'
    except:
        # En caso de falla, retornar el mensaje de error
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos
@app.route("/gastos")
def gastos():
    try:
        print("Endpoint gastos")
        return render_template('tabla.html')
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos/agregar
@app.route("/gastos/agregar")
def gastos_agregar():
    try:
        # Renderizar el temaplate HTML agregar.html
        return render_template('agregar.html')
    except:
        return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':
    print('¡Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)

