// Forma de almacenar información en el navegador

// SESSION STORAGE - se guarda la información mientras la seción/pestaña
// se mantenga abierta

sessionStorage.setItem('clave', 1234); // Es para setear un valor
console.log(sessionStorage.getItem('clave')); // Obtener el valor
console.log(sessionStorage);
sessionStorage.removeItem('clave'); // Remueve el valor
console.log(sessionStorage);
sessionStorage.setItem('nombre','jordan')
console.log(sessionStorage);

// LOCAL STORAGE
// La información persiste aunque la pestaña se cierre
localStorage.setItem('clave',1234);
console.log(localStorage.getItem('clave'));
console.log(localStorage);
localStorage.removeItem('clave');
console.log(localStorage)

// JSON STRINGIFY: Guarda en formato JSON
// Esto solo utilizar con los arrays y objetos
// Se tiene que definir el valor con el JSON.STRINGIFY
// Luego cuando se quiere visualizar el valor, se parsea con: JSON.parse()

const numeros = [0, 1, 2, 3, 4];
sessionStorage.setItem('numeros', JSON.stringify(numeros));
JSON.parse(sessionStorage.getItem('numeros'));

const objeto = {name: 'jordan'};
sessionStorage.setItem('objeto', JSON.stringify(objeto));
JSON.parse( sessionStorage.getItem('objeto'));