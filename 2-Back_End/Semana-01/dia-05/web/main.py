from flask import Flask,render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

# CONFIGURAR CONEXIÓN CON BASE DE DATOS
app.config['MYSQL_HOST']="b6x76wsyqtbgqvhllf4c-mysql.services.clever-cloud.com"
app.config['MYSQL_USER']="uace4ksuaz8nk67m"
app.config['MYSQL_PASSWORD']="0vcrX0k96bzMjd7UpDB1"
app.config['MYSQL_DB']="b6x76wsyqtbgqvhllf4c"

mysql = MySQL(app)

@app.route('/')
def index():
      cursor = mysql.connection.cursor()
      cursor.execute('select id,sistema,procesador,memoria from computadoras')
      data = cursor.fetchall()
      cursor.close()

      print(data)

      context = {
        'data':data
      }

      return render_template('index.html',**context)

app.run(debug=True, port=4000)