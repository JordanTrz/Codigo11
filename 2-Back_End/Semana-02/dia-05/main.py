# Importamos flask
from flask import render_template

# Importar la función create_app de mi aplicación app
from app import create_app

app = create_app()

# creamos las rutas
@app.route('/')
def index():
  return render_template('index.html')