# linear and radial gradient

## linear-gradient

Esta propiedad es para poder poner colores como una gradiente lineal, esto quiere decir, con una transición suave para fondos de texto, títulos, etc.

Se utiliza con la propiedad background

Ejemplo:

background: linear-gradient(90deg, transparent, blue, pink, red, orange, brown)

hay varios espacios para poder definir lo que se quiere hacer con esta propiedad, pero las principales son:

syntax:

background: linear-gradient(direction, colors-top1, color-stop2 ...);

El "direction" por defecto es "top-to-bottom"
luego se puede definir:

#grad {
  background-image: linear-gradient(to bottom right, red, yellow);
}

## Angulo

Se puede tener mayor control de la transición de los colores del linear-gradient

### radial-gradient
De igual manera como el linear, se puede realizar gráficas con forma radial, en este caso la sintaxis es:

background-image: radial-gradient(shape size at position, start-color, ..., last-color);