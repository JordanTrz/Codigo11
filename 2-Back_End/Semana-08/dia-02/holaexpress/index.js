const express = require('express')

const app = express()
const port = 5000

app.get('/',(req,res)=>{
  res.send(`<center><h1>Bienvenidos a mi servidor: Jordan Terrazos</h1><center>`)
})

app.get('/json',(req,res)=>{
  res.json({
    "nombre":"Jordan",
    "email":"jt@gmail.com"
  })
})

app.get('/saludar/:nombre',(req,res)=>{
  res.send('Hola '+ req.params.nombre)
})

app.get('/formulario',(req,res)=>{
  html = "<form action='http://localhost:5000/saludopostjson' method='POST'>"
  html += "<input type='text' name='nombre'/>"
  html += "<input type='submit' name='saludar'/>"
  html += "</form>"
  res.send(html)
})

const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended:true }));

app.post('/saludopost',(req,res)=>{
  html = "<h1>Hola como estás " + req.body.nombre + "</h1>"
  res.send(html)
})

// Utilizando JSON

app.use(express.json())
app.post('/saludopostjson',(req,res)=>{
  const nombre = req.body.nombre;
  res.json({
    'saludo':'hola ' + nombre
  })
})

app.listen(port,
  ()=> console.log('servidor corriendo en http://localhost:' + port)
)
