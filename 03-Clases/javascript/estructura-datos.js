let numbers = [0,1,2,3,4,5,6,7,8,9,10];
let nombres = ['Jordan', 'Ethan', 'Lucero', 'Mario'];
let sabores = ['uva', 'melon', 'sandia'];
let prueba = [['zero',1,2,3],0,[0,1,2,3],[4,5,6,7]];

console.log(nombres[0]);
console.log(nombres[1]);
console.log(nombres[2]);
console.log(nombres[3]);

console.log('prueba', prueba[2][2]);

// formas de modificar valores del array

// LENGTH
numbers.length; // longitud del array

// PUSH
numbers.push(11); // agrega número al final del array

// UNSHIFT
numbers.unshift(11); // agrega número al inicio del array

// POP
numbers.pop(); // Elimina el último elemento de una array

// SHIFT
numbers.shift(); // Elimina el primer elemento de un array

// SPLICE
numbers.splice(2,2);

let alumno = {
  nombre: 'Jordan',
  lastname: 'Yabiku',
  age: 35,
  grade: 5,
  sex: 'm',
  getName: function(){
    return this.name;
  },
  getFullName: function(){
    return `${this.name} ${this.lastname}`;
  }
};

console.log('alumno.nombre', alumno.nombre);
console.log('alumno.nombre', alumno.lastname);
console.log('alumno.nombre', alumno.getName());

let profesor = {
  nombre: 'Jordan',
  lastname: 'Yabiku',
  age: 35,
  grade: 5,
  sex: 'm',
  experience: [
    {
      college: 'latinoamericano',
      age: 2022,
    },
    {
      college: 'recoleta',
      age: 2000,
    }
  ]
};

const alumnos = [
  {
    nombre: 'Jordan',
    lastname: 'Yabiku',
    age: 35,
    grade: 5,
    sex: 'm',
    getName: function(){
      return this.nombre;
    },
    getFullName: function(){
      return `${this.nombre} ${this.lastname}`;
    }
  },
  {
    nombre: 'lucero',
    lastname: 'Yabiku',
    age: 35,
    grade: 5,
    sex: 'm',
    getName: function(){
      return this.nombre;
    },
    getFullName: function(){
      return `${this.nombre} ${this.lastname}`;
    }
  },
  {
    nombre: 'Ethan',
    lastname: 'Yabiku',
    age: 35,
    grade: 5,
    sex: 'm',
    getName: function(){
      return this.nombre;
    },
    getFullName: function(){
      return `${this.nombre} ${this.lastname}`;
    }
  },
  {
    nombre: 'Mario',
    lastname: 'Yabiku',
    age: 35,
    grade: 5,
    sex: 'm',
    getName: function(){
      return this.nombre;
    },
    getFullName: function(){
      return `${this.nombre} ${this.lastname}`;
    }
  },
  {
    nombre: 'Elizabeth',
    lastname: 'Yabiku',
    age: 35,
    grade: 5,
    sex: 'm',
    getName: function(){
      return this.nombre;
    },
    getFullName: function(){
      return `${this.nombre} ${this.lastname}`;
    }
  }
]

console.log('alumnos',alumnos)