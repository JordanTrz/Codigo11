// import React from 'react';
// import ReactDOM from 'react-dom';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();

import React from 'react'; // importado librería react
import ReactDOM from 'react-dom'; // importador funcionalidad para renderizar elementos en el virtual dom
import "./index.css"; // importando css en js

// En javascript se realizaría los siguientes pasos

// const root = document.getElementById('root');
// const h1 = document.createElement('h1');
// h1.textContent = 'Hola Mundo';
// root.appendChild(h1);

// Con react:
// ReactDOM.render(<h1>HOLA MUNDO</h1>, document.getElementById('root'));


// Nueva clase

// function Header() {
//   return <header>HEADER</header>
// }

// function Main(props){
//   console.log('props', props);
//   const{children} = props;
//   return <main>{children}</main>;
// }

// function Footer(){
//   return <footer>FOOTER</footer>;
// }

// function Card(){
//   return <article>CARD</article>;
// }

// function App(){
//   return(
//     <div className='app'>
//       {/* {Header()} */}
//       <Header/>
//       {/* {Main()} */}
//       <Main>
//         Cualquier texto o componente
//         <Card/>
//         <Card/>
//         <Card/>
//         <Card/>
//         <Card/>
//         <Card/>
//         {new Date().toLocaleTimeString()}
//       </Main>
//       {/* {Footer()} */}
//       <Footer/>
//     </div>
//   )
//   ReactDOM.render(<App/>,document.getElementById('root'));
// }



// function Appjs(){
//   const header = document.createElement('header');
//   header.innerHTML = 'HEADER';

//   const main = document.createElement('main');
//   main.innerHTML = `
//   MAIN
//     ${new Date().toLocaleTimeString()}
//   `;

//   const footer = document.createElement('footer');
//   footer.innerHTML = 'FOOTER';

//   const ren = document.createElement('div');
//   ren.innerHTML = `
//     ${header.outerHTML}
//     ${footer.outerHTML}
//   `;
//   // ren.appendChild(header);
//   ren.appendChild(main);
//   // ren.appendChild(footer);

//   document.querySelector('#root').innerHTML = '';
//   document.querySelector('#root').appendChild(ren);
// }

// // setInterval(Appjs,1000);

// ReactDOM.render(<app/>, document.getElementById('root'));

// Nueva clase / repaso

function Header(){
  return(
    <header>
      <ul>
        <li> Quienes somos </li>
        <li> Contacto</li>
        <li> Más</li>
      </ul>
    </header>
  )
}

function Main(props){
  const { children } = props;
  return <main>{children}</main>
}

function Footer(){
  return <footer>Footer</footer>
}

function Card(props){
  const { name, lastname, age} = props
  return(
  <article>
    <h2>Nombre completo: {name} {lastname}</h2>
    <h2>Edad: {age}</h2>
  </article>
  );
}

function SayHello(props){
  const { name = 'Gianmarco', sex = 'f'} = props;

  return(
    <div>
      {name === 'Gianmarco' ? <h2>Hola Gianmarco</h2> : <h2>Hola Extraño</h2>}
      {sex == 'f' && <h2>Eres Mujer!!!</h2>}
    </div>
  )
}

function App(){
  const users = [{
    name: 'Jordan',
    lastname: 'terrazos',
    age: 37
  },
  {
    name: 'jose',
    lastname: 'Escate',
    age: 28
  },
  {
    name: 'Sylvana',
    lastname: 'Moya',
    age: 27
  }
]

  return(
    <div className='app'>
      <Header/>
      <Main>
        {users.map((user)=>(
          <Card name={user.name} lastname={user.lastname} age={user.age}/>
        ))}
        <SayHello name='Monica' sex='f' />
        <SayHello />
      </Main>
      <Footer/>
    </div>
  )
}

ReactDOM.render(<App/>,document.getElementById('root'))