const button = document.querySelector('button');
const dropdown = document.querySelector('.js_dropdown');


button.onclick = function(){
  if(dropdown.style.display === 'block'){
    dropdown.style.display = 'none';
    this.textContent = 'ABRIR DROPDOWN';
    // console.log("if",dropdown.style.display);
  }
  else{
    dropdown.style.display = 'block';
    this.textContent = 'CERRAR DROPDOWN';
    // console.log("else",dropdown.style.display);
  }
};

const input = document.querySelector('input[type="text"]');
console.log('input',input);
input.onkeyup = function (evt){
  console.log('input_f', evt.target.value);
};

const inputcheck = document.querySelector('input[type="checkbox"]');
console.log('check',input);
inputcheck.onchange = function (){
  console.log('check_f',this.checked);
};

window.onresize = function (){
  console.log('resize!!',window.innerWidth, window.innerHeight);
};

const form = document.querySelector('form');

form.onsubmit = function(evt){
  evt.preventDefault();
  console.log('nombre',this.querySelector('input[placeholder = "Nombre"]').value);
  console.log('apellido', this.querySelector('input[placeholder = "Apellido"]').value);
};

function fnOne(){
  console.log("fnOne!")
}

function fnTwo(){
  console.log("fnTwo!")
}

function fnThree(){
  console.log("fnThree!")
}

button.addEventListener('click',fnOne);
button.addEventListener('click',fnTwo);
button.addEventListener('click',fnThree);

const btnQuit = document.querySelector(".js_quit");
btnQuit.addEventListener('click',function(){
  console.log("removiendo function");
  button.removeEventListener('click',fnThree);
});

document.querySelector('body').addEventListener('mousemove',function(evt){
  this.style.backgroundColor =`rgba(
    ${Math.floor(Math.random()*255)},
    ${Math.floor(Math.random()*255)},
    ${Math.floor(Math.random()*255)},
    1
  )`;
});