// getAlumnos
// Función que invoca endpoint alumnos

function getAlumns(){
  fetch('http://localhost:3000/alumnos')
  .then((response) => response.json())
  .then((alumnos) => {
    alumnos.reverse().map((alumno) => {
      addElementDom(makeCard(alumno));
    });
  });
}

// deleteAlumn
// Función que elimina al alumno

function deteleAlumn(id){
  fetch(`http://localhost:3000/alumnos/${id}`,{
    method: 'DELETE',
  });
};

// makeCard
// Función constriye nodo con valores de alumno

function makeCard(alumno){
  const {name, lastname , age, id} = alumno;

  const article = document.createElement('article');
  article.classList.add('article');
  article.innerHTML = `
    <h2><span>Nombre</span> ${name} ${lastname}</h2>
    <h2><span>Edad</span> ${age}</h2>
    <button class = "js_edit edit">Edit</button>
    <button class = "js_delete delete">Delete</button>
  `;

  article.querySelector('.js_delete').onclick = (e) =>{
    // console.log('eliminar');
    // confirm("Seguro que quiere eliminar")? deteleAlumn(id):'';
    if(confirm("Desdea eliminar?")) deteleAlumn(id);
  };

  article.querySelector('.js_edit').onclick = () => {
    // console.log('edit');
    location.replace("/03-Clases/56-GetAPI/edit.html")
  };



  return article;
}

// addElementDom
// Function que agrega elemento al dom #container

function addElementDom(element){
  const container = document.querySelector('#container');
  container.appendChild(element);
}

getAlumns();

