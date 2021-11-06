// suma(); // ejercicio 1
// promedioNotas(); // ejercicio 2
// areaRectangulo(); // ejercicio 3
// areaTriangulo(); // ejercicio 4
// areaCirculo(); // ejercicio 5
// salario(); // ejercicio 6
// inch_metro(); // ejercicio 7
// dolares(); // ejercicio 8
// años(); // ejercicio 9
// menorEdad(); // ejercicio 10
// bono(); // ejercicio 11
// salarioTotal(); // ejercicio 12
// alumnos(); // ejercicio 13
// focos(); // ejercicio 14
// votacion(); // ejercicio 15

// Ejercicio 1
function suma(){
  alert('Ingrese dos valores para sumar');
  let x = Number(prompt("Ingrese primer valor"));
  let y = Number(prompt("Ingrese segundo valor"));

  console.log(`La suma de ${x} y ${y} es ${x+y}`)
}

// Ejercicio 2
function promedioNotas(){
  let cantidad = prompt("Ingrese cantidad de notas a promediar");
  let promedio = 0;
  let notas = Array(cantidad);
  for (let i=0; i < cantidad; i++){
    notas[i]=Number(prompt(`Ingrese la nota #${i+1}`));
    while (notas[i]<0 || notas[i]>20){
      alert('Nota inválida, rango de notas es de 0 a 20');
      notas[i]=Number(prompt(`Vuelva a ingresar la nota #${i+1}`));
    }
    promedio += notas[i];
  }
  promedio /= cantidad;
  console.log(`El promedio de las notas es ${promedio}`);
  alert(`El promedio de las notas es ${promedio}`);
}

// Ejercicio 3
function areaRectangulo(){
  let base = prompt("Ingrese el valor de la base del rectángulo: ");
  let altura = prompt("Ingrese el valor de la altura del rectángulo: ");
  console.log(`El área del rectángulo es: ${base*altura}`);
  alert(`El área del rectángulo es: ${base*altura}`);
}

// Ejercicio 4
function areaTriangulo(){
  let base = prompt("Ingrese el valor de la base del triángulo: ");
  let altura = prompt("Ingrese el valor de la altura del triángulo: ");
  console.log(`El área del triángulo es: ${base*altura/2}`);
  alert(`El área del triángulo es: ${base*altura/2}`);
}

// Ejercicio 5
function areaCirculo(){
  const pi = 3.1415;
  let radio = prompt("Ingrese el valor del radio: ");
  console.log(`El área del círculo es ${pi*(radio**2)}`);
  alert(`El área del círculo es ${pi*(radio**2)}`);
}

// Ejercicio 6
function salario(){
  let salary_h = prompt("Ingrese el salario ganado por hora (S/)");
  let hora_work = prompt("Ingrese las horas trabajadas por semana (h)");
  console.log(`El salario semanal es de S/ ${salary_h*hora_work}`);
  alert(`El salario semanal es de S/ ${salary_h*hora_work}`);
}

// Ejercicio 7
function inch_metro(){
  let metros = prompt("Ingresar los metros que utilzará para calcular las pulgadas");
  console.log(`Se debe pedir la siguiente cantidad en pulgadas: ${metros*39.3701}`);
  alert(`Se debe pedir la siguiente cantidad en pulgadas: ${metros*39.3701}`);
}

// Ejercicio 8
function dolares(){
  let dinero = prompt("Ingresar cantidad de soles a convertir");
  console.log(`La cantidad de dólares que se puede obtener es ${dinero/4.01}`);
  alert(`La cantidad de dólares que se puede obtener es ${dinero/4.01}`);
}

// Ejercicio 9
function años(){
  let año_nacimiento = prompt("Ingresar el año de nacimiento");
  console.log(`Usted tiene ${2021-año_nacimiento} años`);
  alert(`Usted tiene ${2021-año_nacimiento} años`);
}

// Ejercicio 10
function menorEdad(){
  let cantidad = prompt("Ingrese la cantidad de personas");
  let nombre = Array(cantidad);
  let edad= Array(cantidad);

  for (let i=0;i<cantidad;i++){
    nombre[i]=prompt(`Ingrese el nombre de la persona #${i+1}`);
    edad[i]=Number(prompt(`Ingrese la edad de la persona #${i+1}`));
  }
  let x = 0;
  for (let i=0;i<cantidad;i++){
    if (edad[i] < edad[x]){
      x = i;
    }
    else{x = x;}
  }
  console.log(`La persona con menor edad es ${nombre[x]} ya que tiene ${edad[x]} años`);
  alert(`La persona con menor edad es ${nombre[x]} ya que tiene ${edad[x]} años`);
}

// Ejercicio 11
function bono(){
  let años = prompt("Indique cuántos años viene trabajando en la empresa");
  if (años>0 && años<6){
    console.log(`Recibirá el bono de $${años*100}`);
    alert(`Recibirá el bono de $${años*100}`);
  }
  else{
    console.log(`Recibirá el bono de $1000}`);
    alert(`Recibirá el bono de $1000`);
  }
}

// Ejercicio 12
function salarioTotal(){
  let salario = 1500;
  const años = 6;

  for (let i=0;i<años-1;i++){
    salario += salario*0.1;
    console.log(`Se recibió el salario de ${salario.toFixed(2)} el año ${i+1}`);
  }
  console.log(`Luego de 6 años, se recibirá la cantidad de ${(salario+salario*0.1).toFixed(2)}`);
  alert(`Luego de 6 años, se recibirá la cantidad de ${(salario+salario*0.1).toFixed(2)}`);
}

// Ejercicio 13
function alumnos(){
  let alumnos = prompt("Ingrese cantidad de alumnos");
  let nota, aprobado=0;

  for(let i=0; i<alumnos;i++){
    nota=Number(prompt(`Ingrese la nota del alumno ${i+1}`));
    while (nota<0 || nota>20){
      alert("La nota es inválida, solo se acepta en rango de 0 a 20");
      nota=Number(prompt(`Vuelva a ingrese la nota del alumno ${i+1}`));
    }
    if (nota>10.5){
      aprobado++;
    }
    else{continue;}
  }
  console.log(`Número de alumno(s) aprobado(s) ${aprobado}`);
  console.log(`Número de alumno(s) desaprobado(s) ${alumnos-aprobado}`);
  alert(`${aprobado} alumno(s) aprobado(s) y ${alumnos-aprobado} desaprobado(s)`);
}

// Ejercicio 14
function focos(){
  let cantidad=Number(prompt("Ingrese cantidad de focos en lote"));
  let matrix = Array(3);
  let residuo = 0;
  let count=0;

  for (let i=0;i<3;i++){
    matrix[i]=Number((Math.random()*(cantidad)/3).toFixed(0));
    residuo += matrix[i];
  }
  residuo = cantidad-residuo;
  for (let i=0;i<3;i++){
    matrix[i] += Number((residuo/3).toFixed(0));
    count += matrix[i];
  }
  for (let i=-1;i<2;i++){
    if ((cantidad-count) == i){
      matrix[1] += i;
    }
  }
  console.log(`Se cuenta con ${matrix[0]} focos verdes`);
  console.log(`Se cuenta con ${matrix[1]} focos rojos`);
  console.log(`Se cuenta con ${matrix[2]} focos blancos`);
  alert(`Secuenta con ${matrix[0]} focos verdes, ${matrix[1]} rojos, ${matrix[2]} blancos`);
}

// Ejercicio 15
function votacion(){
  let a = prompt("Ingrese su edad");
  a += 5;
  if (a>=18 || a<=70){
    console.log("Sí podrá votar en las próximas elecciones presidenciales");
    alert("Sí podrá votar en las próximas elecciones presidenciales");
  } else{
    console.log("No podrás votar en las próximas elecciones");
    alert("Sí podrá votar en las próximas elecciones presidenciales");
  }
}