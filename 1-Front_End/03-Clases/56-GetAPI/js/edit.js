// OBTENER VALOR DE ID DE URL:
const urlSearchParams = new URLSearchParams(location.search);
console.log('urlSearchParams', urlSearchParams.entries());
const params = Object.fromEntries(urlSearchParams.entries());
console.log('params', params);

// getAlumn
// Función que invoa endpoint alumnos con id de alumno

function getAlumn(id) {
  fetch(`http://localhost:3000/alumnos/${id}`)
    .then((response) => response.json())
    .then((alumno) => {
      console.log('alumno', alumno);
      setForm(alumno);
    });
}

// updateAlumn
// Función que recibe id y datos a actualizar

function updateAlumn(id, payload){
  fetch(`http://localhost:3000/alumnos/${id}`,{
    method: 'PUT',
    body: JSON.stringify(payload),
    headerhs: {
      'Content-type' : 'application/json ; charset = UTF-8',
    }
  }).then(()=>{
    location.replace('/03-Clases/56-GetAPI/listar.html');
  });
}


// SetForm
// Función que setea valor de alumno en formulario

function setForm(alumno){
  const name = document.querySelector('.js_name');
  const lastName = document.querySelector('.js_lastName');
  const age = document.querySelector('.js_age');
  const form = document.querySelector('form');

  // Seteo formulario
  name.value = alumno.name;
  lastName.value = alumno.lastName;
  age.value = alumno.age;

  // Registra evento de formulario
  form.onsubmit = function (e) {
    e.preventDefault();

    // envío de datos al servicio
    updateAlumn(alumno.id, {
      name: name.value,
      lastname: lastName.value,
      age: age.value
    });
  };
}

// Se invoca a la función
getAlumn(params.id);