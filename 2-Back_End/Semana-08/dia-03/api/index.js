const express = require('express');
const app = express();

// settings
app.set('port',process.env.PORT || 5000);

// Middlewares
app.use(express.json());

// Routes
app.get('/',(req,res)=>{
  res.json({
    'status':true,
    'content':'Bienvenidos a mi api'
  })
})

const mysqlConnection = require('./database');

app.get('/alumno',(req,res)=>{
  mysqlConnection.query('select * from tbl_alumno',(err,rows,fields)=>{
    if(!err){
      res.json(rows)
    }
    else{
      console.log(err)
    }
  })
})

app.post('/alumno',(req,res)=>{
  const {alumno_nombre,alumno_email} = req.body;
  const query = `insert into tbl_alumno(alumno_nombre,alumno_email) value(?,?)`;

  mysqlConnection.query(query,[alumno_nombre,alumno_email],(err,rows,fields)=>{
    if(!err){
      res.json({
        'status':true,
        'content':'Alumno created'
      })
    }else{
      console.log(err)
    }
  })
})

app.put('/alumno/:id',(req,res)=>{
  const {alumno_nombre,alumno_email} = req.body;
  const {id} = req.params;
  const query = `update tbl_alumno set alumno_nombre=?,alumno_email=? where alumno_id=?`;

  mysqlConnection.query(query,[alumno_nombre,alumno_email,id],(err,rows,fields)=>{
    if(!err){
      res.json({
        'status':true,
        'content':'Alumno Updated'
      })
    } else{
      console.log(err);
    }
  })
})

app.delete('/alumno/:id',(req,res)=>{
  const {id} = req.params;
  const query = `delete from tbl_alumno where alumno_id=?`;

  mysqlConnection.query(query,[id],(err,rows,fields)=>{
    if(!err){
      res.json({
        'status':true,
        'content':'Alumno Deleted'
      })
    }
  })
})

app.listen(app.get('port'),()=>{
  console.log(`Server running at http:localhost:${app.get('port')}`)
})