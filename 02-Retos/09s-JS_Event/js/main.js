const button1 = document.querySelector('.btn1');
const button2 = document.querySelector('.btn2');

function alert1(){
  alert("Hola Mundo");
}

button1.addEventListener('click',alert1);
button2.addEventListener('click',function(){
// console.log(button2.previousElementSibling.style.display)
  if(button2.previousElementSibling.style.display === 'none'){
    button2.previousElementSibling.style.display = 'block';
  } else{
    button2.previousElementSibling.style.display = 'none';
  }
})

let x = Number(document.querySelector('div').firstElementChild-document.querySelector('div').firstElementChild);
console.log("tipo",x);

let node = document.body;

nextNode = function(node){
  if(node.firstElementChild){
    return node.firstElementChild;

  }
}

// while(node != null){

  console.log(nextNode(node));
// }