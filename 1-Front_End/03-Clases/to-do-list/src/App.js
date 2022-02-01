import { useState } from "react";

function Task(props){
  const {tarea, onTarea = () => {}} = props;

  return (
    <div>
      {tarea} <button onClick={() => onTarea(tarea)}>x</button>
    </div>
  );
}

function App(){
  const [tareas, setTareas] = useState([]);
  const [inputValue, setInputValue] = useState('');

  function handleSubmit(event){
    event.preventDefault();

    setTareas((state) => {
      console.log('state setTarea', state)
      return [
        ...tareas,
        {
          tarea: inputValue,
        },
      ];
    });

    setInputValue('');
    console.log('tareas',tareas);
    console.log('setTareas',setTareas)
  }

  function deleteTask(tarea, tareas){
    console.log('tarea',tarea);
    console.log('tareas',tareas);
    setTareas(tareas.filter((itemTarea) => itemTarea.tarea !== tarea));
    console.log(tareas);
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          value={inputValue}
          type="text"
          placeholder="Ingresar tarea"
          required
          onChange={(e) => {
            console.log('e', e.target.value);
            setInputValue(e.target.value);
          }}
        />
        <button>+ Agregar tarea</button>
      </form>

      {tareas.length > 0 ? tareas.map((item) => (
        <Task
          tarea = {item.tarea}
          onTarea = {(tarea) => {
            console.log('tarea', tarea);
            deleteTask(tarea, tareas);
          }}
        />
      )) : "No hay tareas pendientes"

      }
    </div>
  )
}

export { App };