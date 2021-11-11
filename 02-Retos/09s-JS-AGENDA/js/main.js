const form = document.querySelector('form');
const inputName = document.querySelector('.js_name');
const inputLastName = document.querySelector('.js_lastName');
const inputPhone = document.querySelector('.js_phone');
const inputAddress = document.querySelector('.js_address');
const inputPhoto = document.querySelector('.js_photo');
const inputNick = document.querySelector('.js_nickName');
const app = document.querySelector('.app');
const app_wrapper = document.querySelector('.app-wrapper');

form.addEventListener('submit',function(event){
  event.preventDefault();

  const article = document.createElement('article');
  article.innerHTML = `
    <figure>
      <img src="${inputPhoto.value}" alt="${inputName.value} ${inputLastName.value}">
    </figure>
    <h3>${inputName.value} ${inputLastName.value}</h3>
    <h4>${inputNick.value}</h4>
    <span>
      <i class="fas fa-phone"></i>
      <h3>${inputPhone.value}</h3>
    </span>
    <span>
      <i class="fas fa-home"></i>
      <h3>${inputAddress.value}</h3>
    </span>
    <div>
      <button>x</button>
    </div>`;
    article.classList.add('box-contact');
    article.querySelector('button').addEventListener('click',function(){
      const flag = confirm("Está seguro que desea eliminar contacto?");
      if(flag) app.removeChild(article);
    });

    app.appendChild(article);
    this.reset();
});