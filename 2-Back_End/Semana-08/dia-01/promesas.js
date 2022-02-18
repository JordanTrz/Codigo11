function hola(nombre){
  return new Promise(function(resolve,reject){
    setTimeout(function(){
      console.log('Hola ' + nombre);
      resolve(nombre)
      reject('Hay un error')
    },1000)
  })
}

function hablar(nombre){
  return new Promise( (resolve,reject) => {
    setTimeout(()=>{
      console.log('Como te va ' + nombre);
      resolve(nombre);
      reject('no te entiendo')
    },1000)
  })
}

function adios(nombre){
  return new Promise( (resolve,reject) => {
    setTimeout(()=>{
      console.log('Adiós ' + nombre);
      resolve(nombre);
      reject('no te entiendo')
    },1000)
  })
}

hola("Jordan")
.then(hablar)
.then(adios)
.then(() => {
  console.log('fin ...')
})