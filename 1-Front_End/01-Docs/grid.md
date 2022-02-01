# Grid

El grid sirve para poder dividir en celdas de filas y columnas 

# display: grid;
Para utilizar esta función se debe de colocar la propiedad grid

una vez se coloca el grid se puede 


# Alineaciones con grid

Se puede realizar alineaciones dentor de los box con la propiedad grid

## justify-items:
Para poder alinear los items de manera horizontal.
Esta propiedad cuenta con valores como:

- center
- start
- end
- stretch (valor por defecto)

## align-items:
Para poder alinear los items de manera vertical.
Esta propiedad cuenta con valores como:
- center
- start
- end
- stretch

## align-content:
Es para alinear pero varios items, estos forman un content
- center
- start
- end
- stretch

## justify-self y align-self

Se puede utilizar con los nth-child

."clase" div:first-child{
    justify-self: center;
}

# unidades de medida

## Autofill
cuando se aumenta la dimensión de la pantalla, completa con box vaciós en su lugar.

## Autofit
Cuando se aumenta la dimensión de la pantalla, se autocompleta y se redimensiona a todo el espacio disponible de la pantalla.

# Juego GRID SS

## grid-template-columns
## grid-template-rows
Se puede definir cantidad de columnas y filas con esta propiedad.

grid-template-columns: 20% 20% 20% 20% 20%
Esto formaría 5 columnas con un espacio del 20%

## grid-template
junta las propiedades de grid-template-columns y grid-template-rows

## repeat(#,#)
Con repeat se puede especificar lo mismo pero en menor código:

grid-template-columns: repeat(8,12.5%)

## grid-column
## grid-row
Este puede aceptar un solo valor para indicar una posición única en el grid.

grid-column: 2;
grid-row: 5;

O también puede aceptar dos valores, que indican el start y end, pudiendo generar una área:

grid-column: 2/6;
grid-row: 1/6;

## span
En vez de definir un elemento en la cuadrícula basado en start y end, se puede definir basado en la longitud de columnas deseadas usando SPAN.

grid-column: span 3/5;

- Esto quiere decir que tendrá 3 cuadrículas y terminará en la línea 5

## grid-area
Esta propiedad acepta 4 valores, que sería:
grid-row-start, grid-column-start, grid-row-end, grid-column-end.

