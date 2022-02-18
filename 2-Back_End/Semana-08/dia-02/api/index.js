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

app.get('/employee',(req,res)=>{
  mysqlConnection.query('select * from employee',(err,rows,fields)=>{
    if(!err){
      res.json(rows)
    }
    else{
      console.log(err)
    }
  })
})

app.post('/employee',(req,res)=>{
  const {name,salary} = req.body;
  const query = `insert into employee(name,salary) value(?,?)`;

  mysqlConnection.query(query,[name,salary],(err,rows,fields)=>{
    if(!err){
      res.json({
        'status':true,
        'content':'employed inserted'
      })
    }
    else{
      console.log(err);
    }
  })
})

app.put('/employee/:id',(req,res)=>{
  const {name,salary} = req.body;
  const {id} = req.params;
  const query = `update employee set name=?,salary=? where id=?`

  mysqlConnection.query(query,[name,salary,id],(err,rows,fields)=>{
    if(!err){
      res.json({
        'status':true,
        'content':'Employee Updated'
      })
    } else{
      console.log(err);
    }
  })
})

app. delete('/employee/:id',(req,res)=>{
  const {id} = req.params;
  const query = `delete from employee where id=?`

  mysqlConnection.query(query,[id],(err,rows,fields)=>{
    if(!err){
      res.json({
        'status':true,
        'content':'Employee Deleted'
      })
    }
  })
})

app.listen(app.get('port'),()=>{
  console.log(`Server running at http:localhost:${app.get('port')}`)
})
