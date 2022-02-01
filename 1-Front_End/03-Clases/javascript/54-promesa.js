// const promesa = new Promise(function(resolve, reject){
//   setTimeout(() => {
//     resolve([0, 1, 2, 3]);
//   }, 3000);
// });

// promesa
//   .then((response) => {
//   console.log('response', response);
// }).catch((err) => {
//   console.log('error', err);
// });

// fetch('https://swapi.dev/api/people')
//   .then((resolve) => {
//   return resolve.json();
// })
//   .then((people) => {
//   console.log('people', people);
// })
//   .catch((err) => {
//   console.log('error en promesa', err);
// });

async function main(){
  function createPokemon(pokemons){
    pokemons.results.map(async (pokemon) => {
      const response = await fetch(pokemon.url);
      const pokemonDetail = await response.json();

      let article = document.createElement('article');
      article.innerHTML = `
          <figure>
            <img src=${pokemonDetail.sprites.front_default} alt=${pokemonDetail.name}
          </figure>
        ${pokemonDetail.name}
      `;

      article.onclick = () => {
        container.innerHTML = '';
        console.log('pokemonDetail', pokemonDetail);

        container.appendChild(article);
      };

      container.appendChild(article);

    });
  }

  const responseJsonPokemon = await fetch(
    "https://pokeapi.co/api/v2/pokemon/"
  );
  const responsePokemons = await responseJsonPokemon.json();
  createPokemon(responsePokemons);
  console.log('responsePokemons', responsePokemons);


  // ES UNA FORMA DE REALIZAR/CONSUMIR API CON FETCH Y THEN

  // fetch('https://pokeapi.co/api/v2/pokemon/')
  //   .then((resolve) => {
  //     return resolve.json();
  //   })
  //   .then((pokemon) => {
  //     createPokemon(pokemon);
  //   })
  //   .catch((err) => {
  //     console.log('error en promesa', err)
  //   });
}

main();

async function prueba(){
  const promesa = new Promise(function(resolve, reject){
    setTimeout(() => {
      resolve([0,1,2,3,4]);
    }, 2000);
  });

  try {
    const response = await promesa;
    console.log('responde', response);

  } catch (error) {
    console.log('error', error);
  }

  // Otra forma de hacerlo con fetch y then
  // promesa.then((response) => {
  //   console.log('response',response);
  // }).catch((error) => {
  //   console.log('error',error)
  // });
}

prueba();