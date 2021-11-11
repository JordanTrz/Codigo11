// FOR

const users = [
  {
    name: 'Jordan',
    lastname: 'Terrazos',
    age: 27
  },
  {
    name: 'Lucero',
    lastname: 'Yabrhuen',
    age: 28
  },
  {
    name: 'Ethan',
    lastname: 'Terrazos',
    age: 5
  },
  {
    name: 'Mario',
    lastname: 'Terrazos',
    age: 62
  },
  {
    name: 'Elizabeth',
    lastname: 'Acuña',
    age: 63
  },
  {
    name: 'Leu',
    lastname: 'Ybarhuen',
    age: 32
  },
  {
    name: 'Jovita',
    lastname: 'Tellez',
    age: 55
  },
  {
    name: 'Sylvana',
    lastname: 'Moya',
    age: 25
  },
]

function esMAyor30(edad){
  return edad > 30;
}

for (let i = 0; i < users.length; i++){
  console.log(`idex element ${i} edad ${users[i].age} ${esMAyor30(users[i].age)}`);
}

const number = [
  [0,1,2,3,4,5],
  [6,7,8,9,10]
]

for (let i = 0; i < number.length; i++){
  console.log(number[i]);
  for (let j=0; j<number[i].length;j++){
    console.log(`array of array`, number[i][j])
  }
}

// WHILE
let n = 0;
while(n<3){
  n++;
  console.log('Hasta que la condición se cumpla');
}

// DO WHILE
let xx=0;
do{
  console.log(`Al menos una sola vez ${xx}`);
  xx++;
} while(xx<5);

// BREAK
for (let index = 0; index < 10; index++){
  console.log('index', index);

  if(index >= 4) break;
}

// CONTINUE
for (let index = 0; index < 10; index++){
  if(index == 4 || index==5 || index == 6) continue;
  console.log('continue', index);
}

// FOR IN
const perro={
  raza: 'doberman',
  edad: 3,
  color: 'negro',
  altura: '80cm',
  país: 'Perú'
};


for (const key in perro){
  console.log('key', key);
  console.log('value', perro[key])
}