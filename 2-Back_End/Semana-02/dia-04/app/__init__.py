# importamos el framework Flask
from flask import Flask

# importamos flask bootstrap
from flask_bootstrap import Bootstrap

# importamos los blueprints
from .admin import admin

from .config import Config

# Función para crear la app de flask
def create_app():
  app = Flask(__name__)

  # agregamos bootstrap a mi app
  bootstrap = Bootstrap(app)

  app.config.from_object(Config)
  # app.config['SECRET_KEY'] = 'any secret string'

  # registramos los blueprints
  app.register_blueprint(admin)

  return app