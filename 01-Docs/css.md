# CSS

## se puede realizar varios cambios en los diseños del html.

### el font-family cambia la fuente del texto

## Elementos
- Los elementos basicamente son nuestros tags de html
- Ejemplo
    * body
    * p
    * head
    * a
    * table
    * div
    * img

## Selectores
- Los selectores son los identificadores de los elementos
- ejemplo:
    * id
    * class
-- ojo: Todos los elementos de html pueden contener un id y un class

- Como accedo a los elementos que tiene selectores?
Esto depende del tipoi de selector
-- Para seleccionar a id's se utiliza el #. Para seleccionar a classes (class) se utiliza el . (punto)

## Display

## position

La propiedad de position nos ayuda a posicionar ul elemento dentro de la página. estos pueden ser:

- absolute: Este se posiciona de manera relativo con el elemento padre que tenga. De no tener, se utilizar el body
- fixed: Se mantiene fijo en la página aún así se desplace.
- relative: Es una posición delativa a donde debería estar el elemento. se junta con propiedades como.
  - left, right, top. Esto con el fin de posicionar al elemento.
- static: Este es el valor por defecto. 
- sticky: Es una mezcla entre relative y fixed. Ya que se queda fijo en la pantalla (como fixed) pero siempre se debe agregar una posición con el:
  - right, left, top. 