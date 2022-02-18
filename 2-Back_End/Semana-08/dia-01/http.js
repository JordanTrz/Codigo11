const http = require('http');

http.createServer(function(req,res){
  console.log("levantamos servidor http");
  res.write('<h1>Hola Mundo Node </h1>');
  res.end();
}).listen(5000);

