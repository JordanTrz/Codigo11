const h1 = document.querySelector('h1');

console.log('h1 %o',h1);

h1.textContent = 'Texto modificado desde js';
h1.style.color = 'red';
h1.style.fontSize = '50px';
h1.style.background = 'orange';

h1.onclick = function(){
  this.style.fontSize = `${Number(this.style.fontSize.replace('px',''))+10}px`;
};

h1.onmouseenter = function (){
  console.log(`entra`);
  this.style.background = 'pink'
}

h1.onmouseout = function(){
  console.log(`sale`);
  this.style.background='blue'
}

h1.innerHTML = "<a href='https://google.com'>AGREGAR HTML</a>";
h1.setAttribute('class','hola hola2');
h1.setAttribute('id','hola hola2');
h1.removeAttribute('id');
h1.removeAttribute('clas');
console.log('h1 getAttribute', h1.getAttribute('style'));
console.log('h1 clientWidth', h1.clientWidth);
console.log('h1 clientHeight', h1.clientHeight);

function SubmitForm(){
  let form = document.querySelector('form');
  const inpname = document.querySelector('.js_name');
  const inplastName = document.querySelector('.js_lastName');
  const inppassword = document.querySelector('.js_password');

  form.onsubmit = function (event) {
    event.preventDefault();
    console.log('nombre', inpname.value);
    console.log('nombre', inplastName.value);
    console.log('nombre', inppassword.value);
  }
}

SubmitForm();

// getElementById - captura por id
const h2 = document.getElementById('h2');
console.log('h2',h2);

// getElementByTagName - captura por tag
const links = document.getElementsByTagName('a');
console.log('links',links);
for(let i=0;i<links.length;i++){
  links[i].style.color = 'white';
  links[i].style.display = 'block';
  links[i].style.padding = '20px';
}

// querySelector
const titulo = document.querySelector('h1');
console.log('titulo',titulo);

// querySelectorAll - entrega colección de itemas
const lists = document.querySelectorAll('li');
for (let i=0;i<lists.length;i++){
  lists[i].style.color = 'white';
  lists[i].style.background = 'purple';
}

// Selectores Relativos

// Se guarda primero el ul con el queryselector
const ul = document.querySelector('ul');
// childNode
console.log('chilNodes',ul.childNodes);
// children
console.log('chilNodes',ul.children);
// first chdild
console.log('firstChild',ul.firstChild);
// firstElementChild
console.log('firstelElementChild', ul.firstElementChild);
// lastChild
console.log('lastChild',ul.lastChild);
// lastElementChild
console.log('lastElementChild',ul.lastElementChild);
// nextElementSibling
console.log('nextElementSibling',ul.firstElementChild.nextElementSibling.nextElementSibling);
// parentElement
console.log('parentElement',ul.parentElement);
console.log('parentElement',ul.firstElementChild.parentElement);
// closest
console.log('parent',document.querySelector('a').closest('body'));
console.log('parent',document.querySelector('a').closest('body').querySelector('form'));