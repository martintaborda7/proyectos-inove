# IMPORTANTE: NO borrar los comentarios

# IMPORTANTE: Utilice la carpeta templates del repositorio
# como parte del desafio

import traceback
from datetime import datetime
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for

# Base de datos
from flask_sqlalchemy import SQLAlchemy

# Crear el server Flask
app = Flask(__name__)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gastos.db"

# Asociamos nuestro controlador de la base de datos con la aplicacion
db = SQLAlchemy()
db.init_app(app)


# ------------ Base de datos ----------------- #
class Gastos(db.Model):
    __tablename__ = "gastos"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    categoria = db.Column(db.String)
    gasto = db.Column(db.Integer)


# ------------ Rutas o endpoints ----------------- #
# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        # Renderizar el temaplate HTML index.html
        print("Renderizar index.html")
        return render_template('index.html')
    except:
        # En caso de falla, retornar el mensaje de error
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos
@app.route("/gastos")
def gastos():
    try:
        print("Endpoint gastos")
        # Alumno:
        # Leer todos los datos dentro de la base de datos
        # utilizando un bucle y extraer los datos
        # En cada caso extraer --> fecha, categoria, gasto
        # almacenando cada fila en un diccionario
        # agregando cada uno de ellos a la lista "datos"
        # (lista de diccionarios)
        datos = []

        # implementar aquí su código...
        
        gastos = Gastos.query.all()

        # Recorrer los resultados y almacenarlos en la lista de diccionarios
        for gasto in gastos:
            dato = {
                'fecha': gasto.fecha.strftime('%Y-%m-%d'),  
                'categoria': gasto.categoria,
                'gasto': gasto.gasto
            }
            datos.append(dato)
        return render_template('tabla.html', datos=datos)
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos/agregar
@app.route("/gastos/agregar", methods=['GET', 'POST'])
def gastos_agregar():
    if request.method == 'GET':
        # Si entré por "GET" es porque acabo de cargar la página
        try:
            # Renderizar el temaplate HTML agregar.html
            return render_template('agregar.html')
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == 'POST':
        try:
            # Alumno:
            # Obtener del HTTP POST del formulario (request.form)
            # la categoria (en minisculas) y el gasto
            gasto = str(request.form.get('gasto'))
            categoria = str(request.form.get('categoria'))
            
            if not gasto or not categoria or not categoria.isalpha():
                return Response(status=400)

            # Alumno:
            # Obtener la fecha y hora actual
            fecha = datetime.now()

            # Alumno
            # Crear un nuevo registro de gastos utilizando
            # los datos capturados (fecha, categoria, gasto)
            # para crear una nueva entrada ne la base de datos
            
            gasto = Gastos(fecha=fecha, categoria=categoria, gasto=int(gasto))

            # Agregar el registro de pulsaciones a la DB
            db.session.add(gasto)
            db.session.commit()



            # Como respuesta al POST devolvemos la tabla de valores
            return redirect(url_for('gastos'))
        except:
            return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos/<categoria>
@app.route("/gastos/<categoria>")
def gastos_categoria(categoria):
    try:
        print("Endpoint gastos_categoria")
        # Alumno:
        # El endpoint debe devolver un JSON unicamente
        # con los gastos asociados a la categoria
        # pasada por la URL
        datos = []
        
        # implementar aquí su código...
        gastos = Gastos.query.filter_by(categoria=categoria).all()
        datos = [{"fecha": gasto.fecha.strftime('%Y-%m-%d'), "categoria": gasto.categoria, "gasto": gasto.gasto} for gasto in gastos]
        
        
        return jsonify(datos)
    except:
        return jsonify({'trace': traceback.format_exc()})


# Este método se ejecutará la primera vez
# cuando se construye la app.
with app.app_context():
    # Crear aquí la base de datos
    db.create_all()
    print("Base de datos generada")


if __name__ == '__main__':
    print('¡Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)
