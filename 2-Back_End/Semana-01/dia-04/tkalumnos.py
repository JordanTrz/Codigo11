from tkinter import *
import sqlite3

class Alumnos:

  def ejectuarSql(self,sql,parametros = ()):
    with sqlite3.connect(self.db_name) as conn:
      cursor = conn.cursor()
      resultado = cursor.execute(sql,parametros)
      conn.commit()
    return resultado

  def registrarAlumno(self):
        sqlInsertarAlumno = "insert into alumnos(nombre,email) values(?,?)"
        parametros = (self.nombre.get(),self.email.get())
        self.ejectu

  def __init__(self,window):
    self.wind = window
    self.wind.title('Alumnos')

    # FRAME
    frame = LabelFrame(self.wind,text="Registro de Nuevo Alumno")
    frame.grid(row=0, column=0,columnspan=3,pady=10)

    ############## CAMPO NOMBRE ##############
    # LABEL NOMBRE
    lbNombre = Label(frame,text="Nombre: ")
    lbNombre.grid(row=1, columns=0)
    # TEXTO NOMBRE
    self.nombre = Entry(frame)
    self.nombre.grid(row=1, column=1)

    ############## CAMPO EMAIL ##############
    # LABEL NOMBRE
    lbEmail = Label(frame,text="Email: ")
    lbEmail.grid(row=2, columns=0)
    # TEXTO NOMBRE
    self.nombre = Entry(frame)
    self.nombre.grid(row=2, column=1)

    ############## BOTON DE REGISTRO DE ALUMNO ##############
    btnNuevoAlumno = Button