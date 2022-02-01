import {BrowserRouter as Router, Switch, Route, Link, Redirect} from 'react-router-dom';

import "./app.css";

function Header(){
  return (
    <header>
      <nav>
        <ul>
          <li>
            <link to="/productos">Productos</link>
          </li>
          <li>
            <link to="/agregar-producto">Productos</link>
          </li>
        </ul>
      </nav>
    </header>
  )
}

function App(){
  return (
    <Router>
      <Header />
    </Router>
  )
}

export { App };