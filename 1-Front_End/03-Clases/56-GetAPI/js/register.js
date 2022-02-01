function registerAlumn(){
  const name = document.querySelector('.js_name');
  const lastName = document.querySelector('.js_lastName');
  const age = document.querySelector('.js_age');
  const form = document.querySelector('form');

  form.addEventListener('submit', function(e){
    e.preventDefault();
    const body = {
      name: name.value,
      lastname: lastName.value,
      age: age.value
    }

    fetch('http://localhost:3000/alumnos',{
      method: 'POST',
      body: JSON.stringify(body),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    .then((response) => {
      return response.json(),
      console.log('response')
    }).catch(() => {
      alert('error en guardar dato');
    });
  });
}
registerAlumn();