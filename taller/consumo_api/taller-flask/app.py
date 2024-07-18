from flask import Flask, redirect, render_template, jsonify, request
import requests
import json
from config import usuario, clave

app = Flask(__name__, template_folder='templates')

# Rutas para consumir servicios de Django

@app.route("/")
def hello_world():
    return render_template("index.html")

# Listar Edificios desde Django
@app.route("/listar_edificios")
def listar_edificios():
    r = requests.get("http://127.0.0.1:8000/api/edificios/", auth=(usuario, clave))
    edificios = json.loads(r.content)['results']
    contarEdificio = json.loads(r.content)['count']
    return render_template("listarEdificios.html", edificios=edificios, contarEdificio=contarEdificio)

# Listar Departamentos desde Django
@app.route("/listar_departamentos")
def listar_departamentos():
    r = requests.get("http://127.0.0.1:8000/api/departamentos/", auth=(usuario, clave))
    departamentos = json.loads(r.content)['results']
    contarDepartamentos = json.loads(r.content)['count']
    datos2 = []
    for d in departamentos:
        datos2.append({
            'nombre_propietario': d['nombre_propietario'],
            'costo': d['costo'],
            'numero_cuartos': d['numero_cuartos'],
            'edificio': obtener_edificio(d['edificio'])
        })
    return render_template("listarDepartamentos.html", departamentos=datos2, contarDepartamentos=contarDepartamentos)

# Obtener Edificios
def obtener_edificio(url):
    r = requests.get(url, auth=(usuario, clave))
    nombre_edificio = json.loads(r.content)['nombre']
    cadena = "%s" % (nombre_edificio)
    return cadena

# Crear Edificio en Django
@app.route("/crear_edificio", methods=["GET", "POST"])
def crear_edificio():
    if request.method == 'POST':
        data = {
            "nombre": request.form['nombre'],
            "direccion": request.form['direccion'],
            "ciudad": request.form['ciudad'],
            "tipo": request.form['tipo']
        }
        r = requests.post("http://127.0.0.1:8000/api/edificios/", auth=(usuario, clave), json=data)
        if r.status_code == 201:
            return redirect("/listar_edificios")
        else:
            return "Error al crear el edificio."
    return render_template("crearEdificio.html")

if __name__ == "__main__":
    app.run(debug=True)
