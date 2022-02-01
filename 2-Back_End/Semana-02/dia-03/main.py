from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebasetoken.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)

@app.route('/')
def home():
  context = {
      'nombre':'Jordan Terrazos',
      'imagen': 'https://firebasestorage.googleapis.com/v0/b/portafolio-22b64.appspot.com/o/proyectos%2F1516869724668.jpeg?alt=media&token=ff5ba63e-f8c9-45c4-9e08-116d40d96f64',
      'bio':'Road to Full Stack Developer in 2022'
    }
  return render_template('home.html', **context)

@app.route('/portafolio')
def portafolio():
      colProyectos = db.collection('proyectos')
      docProyectos = colProyectos.get()

      # print(docProyectos)
      lstProyectos = []
      for doc in docProyectos:
            print(doc.to_dict())
            dicProyecto = doc.to_dict()
            lstProyectos.append(dicProyecto)

      context = {
        'proyectos' : lstProyectos
      }

      return render_template('portafolio.html', **context)

@app.route('/about')
def about():
      return render_template('about.html')

@app.route('/contact')
def contact():
      return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True, port=5000)