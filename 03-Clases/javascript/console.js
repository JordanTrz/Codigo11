function fn(){
  console.log(arguments.length)
  if (arguments.length>2){
    console.log('No se puede agregar más de 2 argumentos en la función')
  }
}

fn(2,3,4,5,6,7, "Jordan")

function fn2(a, ...b){
  console.log('a fn2',a)
  console.log('b fn2',b)
}

fn2(1,2,4,5,6,7,8)

// CONSOLE.LOG

console.log("SUMA",2)
console.log('%c oh my heavens! ', 'background: #222; color: #bada55');
console.warn("Esto es un warning")
console.error("Esto es un error")
console.info("Hola mundo")
console.log("acaa")