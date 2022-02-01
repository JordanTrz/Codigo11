// setTimeout(function(){
//   console.log('dentro 1')
// }, 0);
// console.log('1')
// console.log('2')
// console.log('3')
// setTimeout(function(){
//   console.log('dentro 2')
// }, 0);
// console.log('4');

function createPeople(people){
  console.log('people', people);
  console.log('%0', JSON.parse(people).results);
  JSON.parse(people).results.map((person) =>{
    const card = document.createElement('article');
    card.innerHTML = `
      <p>Nombre ${person.name}</p>
      <p>Altura ${person.height}</p>
      <button>Mostrar filmer</button>
    `;

    card.querySelector('button').onclick = function(){
      console.log('person', person);
      let xhrfil = new XMLHttpRequest();
      xhrfil.open('GET', person.films[0]);
      xhrfil.send(null);
      xhrfil.onload = () => {
        console.log(xhrfil.response);
      };
    };
    // FALTA TERMINAR EL APPEND CHILD
    document.querySelector('#container').appendChild(card);
  });
}

function getResponse(){
  createPeople(xhr.response);
}

function getError(){
  alert('Intentelo más tarde');
}

let xhr = new XMLHttpRequest();
xhr.open('GET', 'https://swapi.dev/api/people');
xhr.send(null);
xhr.onload = getResponse;
xhr.onerror = getError;

document.querySelector('button').onclick = function(){
  console.log('click!')
};

console.log('más código');
console.log('más código 2');