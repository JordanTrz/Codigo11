# importamos la clase Blueprint que nos permitirá registrar nuestro módulo al ŕoyecto principal
from flask import Blueprint

admin = Blueprint('admin',__name__,url_prefix='/admin')

from . import views