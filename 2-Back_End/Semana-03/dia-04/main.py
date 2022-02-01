from distutils.log import debug
from pickle import FALSE
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Lapicero0!!!@localhost/db_matricula'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class AlumnoSchema(ma.Schema):
  class Meta:
    fields = ('alumno_id','alumno_nombre','alumno_email')

class ProfesorSchema(ma.Schema)  :
  class Meta:
    fields = ('profesor_id','profesor_nombre')

class CatalogoSchema(ma.Schema):
  class Meta:
    fields = ('id','nombre')

@app.route('/')
def index():
  return jsonify({
    'mensaje':'BIENVENIDO A MI API'
  })

@app.route('/alumno')
def alumno():
    schemaAlumnos = AlumnoSchema(many = True)
    tuplaAlumnos = db.engine.execute('select * from tbl_alumno')
    listaAlumnos = list(tuplaAlumnos)
    dataAlumnos = schemaAlumnos.dump(listaAlumnos)
    return jsonify(dataAlumnos)



@app.route('/profesores')
def profesores():
      schemaProfesores = ProfesorSchema(many=True)
      tuplaProfesores = db.engine.execute("call listar_profesores()")
      listaProfesores = list(tuplaProfesores)
      dataProfesores = schemaProfesores.dump(listaProfesores)
      return jsonify(dataProfesores)

@app.route(('/cursos/<id>'))
def cursosPorAlumno(id):
  schemaCursos = CatalogoSchema(many=True)
  tuplaCursos = db.engine.execute(text("call sp_cursosxalumno(:param)"),param=id)
  listaCursos = list(tuplaCursos)
  dataCursos = schemaCursos.dump(listaCursos)
  return jsonify(dataCursos)

@app.route('/alumno',methods=['POST'])
def registraAlumno():
      nombre = request.json['nombre']
      db.engine.execute(text("Call registrar_alumno(:nom)"),nom=nombre)
      return jsonify({'mensaje':'registro exitoso'})

if __name__ == "__main__":
  app.run(debug=True,port=5000);