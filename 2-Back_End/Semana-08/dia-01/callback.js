function hola2(nombre,primer_callback){
  setTimeout(function(){
    console.log('hola' + nombre);
    primer_callback(nombre);
  },1000)
}

function hablar2(nombre,segundo_callback){
  setTimeout(function(){
    console.log('Cómo te va ' + nombre);
    segundo_callback(nombre)
  },1000);
}

function adios2(nombre){
  setTimeout(function(){
    console.log("Adiós " + nombre)
  }, 1000);
}

hola2("Jordan", (nombre)=>{hablar2(nombre,(nombre)=>{adios2(nombre)})})

// function hola(nombre,primer_callback){
//   setTimeout(function(){
//     console.log('hola' + nombre);
//     primer_callback(nombre);
//   },1000)
// }

// function hablar(nombre,segundo_callback){
//   setTimeout(function(){
//     console.log("Cómo te va "+ nombre);
//     segundo_callback(nombre)
//   },1000);
// }

// function adios(nombre,tercer_callback){
//   setTimeout(function(){
//     console.log("Adios " + nombre);
//     tercer_callback()
//   },1000);
// }

// // Call back hell
// hola('César',
//   function(nombre)
//   {
//     hablar(nombre,
//       function(nombre){
//         adios(nombre,function(){
//           console.log('fin ...');
//         })
//       })
//   })