// VARIABLES

// Las variables son contenedores de valores, existen diferentes tipos de variables.
// entre ellas tenemos la variable tipo let y tipo const

// let

let nombre = 'JORDAN';
let terrazos;
let edad = 32;
console.log(nombre);
console.log(terrazos);

terrazos = 'CUALQUIER VALOR';
console.log(terrazos);

// const
const PI = 3.14;
console.log(PI);
// PI=2 // No se puede reasignar un valor a un const

// TIPOS DE DATOS
// existen tipos de datos primitivos y de objeto
let user = 'Jordan'; // string
let age = 35; // number
let isMan= true; // boolean - true or false
let account = null; //nul
let married; // undefined
let hash = Symbol('123456'); // Symbol
let alumno = {
  sexo: 'f',
  edad:  35,
  grado: 5,
} // Objetc

console.log(user,typeof user);
console.log(age, typeof age);
console.log(isMan, typeof isMan)
console.log(account, typeof account)
console.log(married, typeof married)
console.log(hash, typeof hash)
console.log(alumno, typeof alumno)

// Cambiar tipos de datos

let age2 = 30;
let age3 ='30';
console.log(age2, typeof age2);
console.log(age2, String(age2).replace(age2,200))
console.log(age2, typeof Boolean(age2));
console.log(age3, Number(age3).toFixed(2))