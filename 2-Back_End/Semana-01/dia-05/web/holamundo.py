from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>hola mundo web</h1>'

app.run()