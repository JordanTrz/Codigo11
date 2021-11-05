let x = parseInt(prompt("Ingrese el primer valor"));
let y = parseInt(prompt("Ingrese el segundo valor"));
maths(x,y);

function maths(alpha,omega){
  suma(alpha,omega);
  resta(alpha,omega);
  multiplicacion(alpha,omega);
  division(alpha,omega);
  potencia(alpha,omega);

  function suma(a,b){
    console.log("La suma es: ",a+b);
  }
  function resta(a,b){
    console.log("La resta es: ",a-b);
  }
  function multiplicacion(a,b){
    console.log("La multiplicación es: ",a*b);
  }
  function division(a,b){
    console.log("La división es: ",a/b);
  }
  function potencia(a,b){
    console.log("La potencia es: ",a**b);
  }
}