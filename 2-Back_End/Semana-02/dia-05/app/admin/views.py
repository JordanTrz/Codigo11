# Importamos render_template para renderizar plantillas en jinja2
from flask import render_template, flash, redirect, url_for, session

from . import admin

# importamos los formularios
from app.forms import LoginForm, ProyectoForm

# firebase
import pyrebase

config = {
  "apiKey": "AIzaSyBKagCPpFS6CCcgW8-dItHbQPBtf6aMR9A",
  "authDomain": "portafolio-22b64.firebaseapp.com",
  "databaseURL": "https://portafolio-22b64-default-rtdb.firebaseio.com",
  "projectId": "portafolio-22b64",
  "storageBucket": "portafolio-22b64.appspot.com",
  "messagingSenderId": "203389337090",
  "appId": "1:203389337090:web:276614af6a2d1d342f711b",
  "measurementId": "G-WWW7HJBFRF"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

####################### FIRESTORE #######################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebasetoken.json")
firebase_admin.initialize_app(cred)
db = firestore.client()



# @admin.route('/proyectos')
# def portafolio():
#     if('token' in session):
#       colProyectos = db.collection('proyectos')
#       docProyectos = colProyectos.get()

#       # print(docProyectos)
#       lstProyectos = []
#       for doc in docProyectos:
#             print(doc.to_dict())
#             dicProyecto = doc.to_dict()
#             lstProyectos.append(dicProyecto)

#       print(lstProyectos)
#       context = {
#         'proyectos' : lstProyectos
#       }

#       return render_template('admin/proyectos.html',**context)
#     else:
#       return redirect(url_for('admin.login'))
#########################################################

@admin.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form':login_form
    }

    # Código para realizar el login de usuarios
    if login_form.validate_on_submit():
          usuarioData = login_form.usuario.data
          passwordData = login_form.password.data

          print("DATOS DE LOGIN : ")
          print("usuario : " + usuarioData)
          print("password: " + passwordData)

          # realizamos el login de usuario
          try:
            usuario = auth.sign_in_with_email_and_password(usuarioData,passwordData)
            session['token'] = usuario['idToken']

            return redirect(url_for('admin.proyectos'))
            # flash(auth.get_account_info(usuario['idToken']))
          except:
            flash("usuario o password inválidos")

    return render_template('admin/login.html',**context)

@admin.route('/proyectos',methods=['GET','POST'])
def proyectos():
    if('token' in session):

        colProyectos = db.collection('proyectos')
        proyecto_form = ProyectoForm()

        if proyecto_form.validate_on_submit():
            #CAPTURAMOS VALORES DE USUARIO Y PASSWORD
            nombreData = proyecto_form.nombre.data
            descripcionData = proyecto_form.descripcion.data
            urlData = proyecto_form.url.data

            #CREAR DICCIONARIO
            data = {
                'nombre': nombreData,
                'descripcion':descripcionData,
                'url':urlData
            }

            colProyectos.document().set(data)




        docProyectos = colProyectos.get()

        lstProyectos = []
        for doc in docProyectos:
            dicProyecto = doc.to_dict()
            lstProyectos.append(dicProyecto)

        print(lstProyectos)



        context = {
            'proyectos':lstProyectos,
            'proyecto_form':proyecto_form
        }



        return render_template('admin/proyectos.html',**context)
    else:
        return redirect(url_for('admin.login'))
@admin.route('/logout')
def logout():
  session.pop('token')
  return redirect(url_for('admin.login'))