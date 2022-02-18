console.log("Hola Mundo");
let i = 0;

// for(i=1;i<=5;i++){
//   console.log(i);
// }

var id = setInterval(function(){
  i++;
  console.log(i);
  if(i === 5){
    clearInterval(id);
  }
},1000);
console.log("Bye world");