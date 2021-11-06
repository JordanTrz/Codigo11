const AGE_MAX = 18;
const SEX = 'm';

function Welcome(name){
  return `Bienvenido al bar ${name}`;
}
function notWelcome(name){
  return `No eres bienvenido al bar ${name}`;
}
function notSupportAge(name){
  return `Eres menor para entrar al bar ${name}`;
}

function ElBar(){
  //debugger; // Se utiliza para poder abrir el debugger en el navegador
  let name = prompt("Ingresa tu nombre");
  let age = Number(prompt("Ingresa tu edad"));
  let gender = prompt("Ingresa tu sexo");

  if(age>AGE_MAX && gender.toLocaleLowerCase() == SEX){
    alert(Welcome(name));
  } else if(age<AGE_MAX){
    alert(notSupportAge(name));
  } else{
    alert(notWelcome(name));
  }
}

// ElBar();

function flavorChose(flavor){
  return `El sabor elegido es ${flavor}`;
}

function flavorNotFound(flavor){
  return `El sabor ${flavor} no lo tenemos aún`;
}

function LaHeladeria(){
  let flavor = prompt(
    "Ingrese el sabor que quieres (fresa, melon, sandia, naranja, kiwi)"
  );

  switch(flavor){
    case 'fresa':
      alert(flavorChose(flavor));
      break;
    case 'melon':
      alert(flavorChose(flavor));
      break;
    case 'sandia':
      alert(flavorChose(flavor));
      break;
    case 'naranja':
      alert(flavorChose(flavor));
      break;
    case 'kiwi':
      alert(flavorChose(flavor));
      break;
    default:
      alert(flavorNotFound(flavor));
      break;
  }

  alert('Vuelva Pronto');
}

// LaHeladeria();

// Funciónque grabará nombres con una longitud entre 7 a 9 caracteres

function saveName(name){
  let message = '';
  try{
    if (name.length < 6) throw 'SHORT';
    if (name.length > 10) throw 'LONG';
    message = `El nombre ${name} es correcto`;
  }
  catch (err){
    if(err === 'SHORT'){
      message = `El nombre ${name} es muy corto`;
    };
    if(err === 'LONG'){
      message = `El nombre ${name} es muy largo`;
    };
  } finally{
    console.log('Nombre evaluado: ',message);
  }
}

// saveName('ana');
// saveName('luis');
// saveName('pedro');
// saveName('sebastian');

function revisionEdad(edad){
  let message = "";
  try{
    if (edad < 18){
      throw 'menorEdad'
    }
    else if (edad>70){
      throw 'mayorEdad'
    }
  message = `Tu edad es ${edad}, puede ir a votar`;
  } catch(err){
    if(err=='menorEdad'){
      message = `Tienes ${edad}, no puedes votar`
    }
    else if(err=='mayorEdad'){
      message = `No es obligatorio que vayas a votar`
    }
  } finally{
    console.log(message);
  }
}

revisionEdad(16);
revisionEdad(20);
revisionEdad(80);
