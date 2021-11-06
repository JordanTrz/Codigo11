// Operadores aritméticos
let a = 2;
let b = 3;
let nombre = "Jordan";
let edad = 30;
console.log("a",a);
console.log("b",b);
console.log("nombre",nombre);
console.log("edad",edad);

console.log("a + b",a + b) // 5
console.log("a - b",a - b) // -1
console.log("a* b",a* b) // 6
console.log("a / b",a / b) // 0.666
console.log("a % b",a % b) // 2
console.log("a ** b",a ** b) // 8

// COMPARACIÓN

console.log("a > b", a > b);
console.log("a < b", a < b);
console.log("a >= b",a >= b);
console.log("a <= b",a <= b);
console.log("a == b",a == b); // compara valor
console.log("a === b",a === b); // compara valor como tipo (ya sean number, string, bool, etc)
console.log("a != b",a != b); // diferente
console.log("a != b",a !== b); // diferencia el valor como el tipo

// COMPARADORES LÓGICOS

// comparador and (&)
console.log("and (&&)",a > b && nombre=="Jordan" && edad>=30);

// comparador or (||)
console.log("or (||)",a > b || nombre=="Jordan" || edad>=30);

// negar datos (NOT)
console.log(!(a > b && edad > 30)); // si es falso, te devuelve true
console.log("!(true)",!(true)); // False
console.log("!(true)",!(false)); // true