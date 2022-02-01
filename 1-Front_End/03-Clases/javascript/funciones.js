function sumar(a,b){
  return a+b;
}

function restar(a,b){
  return a-b;
}

console.log(sumar(2,5));
console.log(sumar(4,8));
console.log(sumar(9,2));

console.log(restar(2,5));
console.log(restar(3,1));
console.log(restar(8,5));

// Funciones de ejecución, no retornan valores, lo ejecutan

// function calculadora(){
//   let a = parseFloat(prompt("Ingresa el primer numero"));
//   let b = parseFloat(prompt("Ingresa el segundo número"));
//   console.log('Sumar a+b =', sumar(a,b));
//   console.log('Restar a-b =', restar(a,b))
// }

// calculadora();

// Función autoejecutables, es una forma de protección de funciones para que no los tome el global

(function(){
  // solo ejecuta comandos
  function calculadora(){
    let a = parseFloat(prompt("Ingresa el primer numero"));
    let b = parseFloat(prompt("Ingresa el segundo número"));
    console.log('Sumar a+b =', sumar(a,b));
    console.log('Restar a-b =', restar(a,b));
  }

  calculadora();
})();