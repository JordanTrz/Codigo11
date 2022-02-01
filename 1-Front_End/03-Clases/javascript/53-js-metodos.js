// SON MÉTODOS QUE TIENEN LOS TIPOS DE DATOS

// STRING
const cadena = "                      jordan terrazos            ";
console.log('longitud',cadena.length);
console.log('concat',cadena.concat('acuña'));
console.log('includes',cadena.includes('jordan'));
console.log('endsWith',cadena.endsWith('ian'));
console.log('startsWith',cadena.startsWith('jor'));
console.log('indexOf',cadena.indexOf('d'));
console.log('lastIndexOf',cadena.lastIndexOf('n'));
console.log('replace',cadena.replace('jordan','Ethan'));
console.log('slice',cadena.slice(2,4));
console.log('split',cadena.split('o'));
console.log('toLowerCase',cadena.toLowerCase());
console.log('toUpperCase',cadena.toUpperCase());
console.log('trim',cadena.trim());

// ARRAY

console.log('===============================')
console.log('ARRAY');
console.log('===============================')
const num = [0,1,2,3,4,5,6];
const num2 = [7,8,9];

console.log('length', num.length);
console.log('isArray', Array.isArray(num));
console.log('Array.of', Array.of('sebastian'));
console.log('concat', num.concat(num2));
console.log('includes', num.includes(0));
console.log('indeOf', num.indexOf(1));
console.log('join',num.join('/'));
console.log('keys',num.keys().next());
console.log('lastIndex()', num.lastIndexOf(10));
console.log('reverse()', num.reverse());
console.log('shift', num.shift());
console.log('slice()',[0,1,2,3,4].slice(1, 3));
const spliceVar = [0,1,2,3,4];
console.log('splice()',spliceVar.splice(1, 1));
console.log('spliceVar()', spliceVar);
console.log('unshift()',num.unshift());
console.log('push()', num.push(2));
console.log('pop()', num.pop(2));

// ARRAY MÉTODOS

const alumnos = [
  {
    name: 'Jordan',
    age: 27,
    gender: 'm',
  },
  {
    name: 'Ethan',
    age: 5,
    gender: 'm',
  },
  {
    name: 'Lucero',
    age: 28,
    gender: 'f',
  },
  {
    name: 'Jovita',
    age: 51,
    gender: 'f',
  }
];

const alumnosFullData = alumnos.map((alumno) => {
  return{
    ...alumno,
    grade: '5',
    school: 'miguel de cervantes',
  };
});

console.log('alumnos', alumnos);
console.log('alumnosFullData', alumnosFullData);

// FILTER
const alumnosMayores30 = alumnos.filter((alumno) => alumno.age>30)
console.log('alumnosMayores30', alumnosMayores30);
console.log('alumnnos',alumnos);

// FIND
const alumnoJordan = alumnos.find((alumno) => alumno.name === 'Jordan');
console.log('find',alumnoJordan)

// FINDINDEX
const alumnoJordanIndex = alumnos.findIndex((alumno) => alumno.name.toLowerCase === 'lucero');
console.log('findIndex', alumnoJordanIndex)

// SOME
const someMayor30 = alumnos.some((alumno) => alumno.age > 30);
console.log(someMayor30);

// EVERY
const everyMayor30 = alumnos.every((alumno) => alumno.age > 30);
console.log(everyMayor30);

// REDUCE
const numeros = [0,1,2,3,4,5,6];
const resultado = numeros.reduce((acumulado, valorActual) => {
  console.log('acumulado', acumulado)
  console.log('valor actual', valorActual)
  return acumulado + valorActual
},0)

console.log('resultado', resultado);

// objetc
console.log('=======================')

const objeto = {
  name: 'sebastian',
  lastName: 'yabiku'
};

const objeto2 = {
  age: 3,
  country: 'peru'
};

const objeto3 = {
  age: 44,
  country: 'Australia'
};

// Objetc.assign =crea copia de objetos
const copia = Object.assign({}, objeto, objeto2, objeto3);
console.log('copia',copia);

// Object.entries = entrega colección de clave, valor
console.log('object.entries',Object.entries(copia));

// Object.keys = entrega colección con las llaves del objeto
console.log('Object.keys',Object.keys(copia));

// Object.values = Entrega colección con valores del objeto
console.log('Object.values', Object.values(copia));

// Object.hasOwnProperty = Entrega valor booleano si la prpopiedad existe en el objeto
console.log('Object.hasOwnProperty',copia.hasOwnProperty('age'));

// Number
// parseInt = convierte el valor en número
console.log(Number.parseInt('3'));

// parseFloat = covierte el valopr en flotante
console.log(Number.parseFloat('3.14'));

// toFixed = indica la cantidad de números decimales se va a tener
console.log(Number.parseFloat('3.14').toFixed(5));

// MATH
// pow = es para realizar esponencial
console.log(Math.pow(9,2))
// round = es para redondear un número
console.log(Math.round(5.5))

// DATE
console.log('getData',new Date().getDate())
console.log('getMonth', new Date().getMonth())
console.log('getDay', new Date().getDay())
console.log('getHours', new Date().getHours())
console.log('getMinutes', new Date().getMinutes())
console.log('getSeconds', new Date().getSeconds())

// Ejercicios

console.log('============================');
console.log('Ejercicios');
console.log('============================');

let array = [1,2,3,4,5,6,7];

console.log(array.length);

let stringName = ('Jordan Terrazos')
console.log(stringName.length)

console.log(stringName.toUpperCase())

// WINDOW

// alert
// prompt
// confirm

setTimeout(() => {
  console.log('ejecutar aquí', new Date(),getSeconds());
}, 1000)

let refInterval = setInterval(() => {
  console.log('ejecutar aquí', new Date().getSeconds())
}, 1000)

document.querySelector('button').onclick = function(){
  clearInterval(refInterval)
}

document.querySelector('a').onclick = (e) => {
  e.preventDefault()
  window.open('https://www.google.com')
}