# importamos dependencias para Flask y SQLAlchemy
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# configuramos el acceso a la base de datos en clever cloud con sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI']='mysql://u9oloxxccou8y5ps:UN2xoGyjShIDDgF9F2Ml@b3awaetq4gvn9uxphtsr-mysql.services.clever-cloud.com:3306/b3awaetq4gvn9uxphtsr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# CREAMOS TABLAS EN LA BASE DE DATOS
class Alumno(db.Model):
      id = db.Column(db.Integer,primary_key=True)
      nombre = db.Column(db.String(100),nullable=False)
      email = db.Column(db.String(100),unique=True)

      def __init__(self,nombre,email):
            self.nombre = nombre
            self.email = email

db.create_all()
print("Se crearon las tablas en la base de datos")

# Creamos schemas
class AlumnosSchema(ma.Schema):
  class Meta:
    fields = ('id','nombre','email')

alumno_schema = AlumnosSchema()

@app.route('/')
def index():
  return jsonify(
    {
      'status':'OK',
      'mensaje': 'Bienvenido a mi APIREST con Flask'
    }
  )

# METODO PARA PODER PUBLICAR ALUMNOS
@app.route('/alumno',methods=['POST'])
def alumno():
  # Capturamos valores
  nombre = request.json['nombre']
  email = request.json['email']

  # insertar el registro en la base de datos
  nuevoAlumno = Alumno(nombre, email)
  db.session.add(nuevoAlumno)
  db.session.commit()

  return alumno_schema.jsonify(nuevoAlumno)


alumnos_schema = AlumnosSchema(many = True)

# METODO PARA PODER VISUALIZAR A TODOS LOS ALUMNOS
@app.route('/alumnos')
def alumnos():
      lstAlumnos = Alumno.query.all()
      print(lstAlumnos)
      dataAlumnos = alumnos_schema.dump(lstAlumnos)
      print(dataAlumnos)
      return jsonify(dataAlumnos)

# METODO PUT PARA ACTUALIZAR ALUMNOS
@app.route('/updalumno/<id>',methods=['PUT'])
def updateAlumno(id):
      alumno = Alumno.query.get(id)
      print(alumno)
      nombre = request.json['nombre']
      email = request.json['email']

      # ACTUALIZAMOS EL ALUMNOS
      alumno.nombre = nombre
      alumno.email= email

      db.session.commit()

      return alumno_schema.jsonify(alumno)

# METODO PARA ELIMINAR ALUMNOS
@app.route('/deleteAlumno/<id>',methods=['DELETE'])
def deleteAlumno(id):
      alumno = Alumno.query.get(id)
      # ELIMINAMOS EL ALUMNOA
      db.session.delete(alumno)
      db.session.commit()

      return alumno_schema.jsonify(alumno)

# METODO PARA VISUALIZAR 1 ALUMNO
@app.route('/alumno/<id>')
def gelAlumno(id):
      alumno = Alumno.query.get(id)
      return alumno_schema.jsonify(alumno)

if __name__ == "__main__":
  app.run(debug=True,port=5000)