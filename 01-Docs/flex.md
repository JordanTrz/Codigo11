# Aprendiendo FLEX

Para poder utilizar las propiedades de flex, se debe comenzar colocando:

#pond{
display: flex;
}

## justify-content:

- Esta propiedad se utiliza para poder alinear los items/imagenes que se tenga de forma horizontal. Pudiéndose ordenar por:

-- start: Se colocan al inicio
-- end: Se colocan al final
-- center: Al centro
-- space-between: coloca el mismo espacio entre los elementos
-- space-around: inserta espacios de gual manera alrededor de los elementos.

## align-items:

- De igual manera, esta propiedad alinea los items de manera vertical. Y contiene los mismos valores FLEX.

-- start: Se colocan al inicio
-- end: Se colocan al final
-- center: Al centro
-- space between: coloca el mismo espacio entre los elementos
-- space-around: inserta espacios de gual manera alrededor de los elementos.

# flex-direction

El flex-direction se utiliza para poder reorganizar los items:

-- row: Se utiliza el row para poder colocar a los items en forma de fila.
-- row-reverse: Hace que la fila comience del final hacia el inicio.
-- column: Coloca a los items en forma de columna.
-- column-reverse: Coloca a los items en forma de columna pero comenzando del final hacia el inicio.

# order

- El order se utiliza para poder cambiar el orden pero de un solo item, es decir, a objetos individuales, esta propiedad acepta números, ejemplo:

obejo-yellow {
    order: 1
}

Este ejemplo haría que el objeto amarillo se desplace a la derecha por una unidad, colocando negativos hace que se desplace hacia la izquierda.

# align-self

- Así como se puede realizar el orden de un objeto individual, se puede realizar de uno solo, en este caso, el cumpliría la función del "align-items" pero considerando solo un objeto.

yellow{
    align-self: end;
}

Acepta los mismos comandos que el justify-content y el align-items

# flex-wrap

- El flex-wrap, wrap:envolura,envuelve los objetos para que entren todos en una fila/columna, o los separa. Acepta los siguientes valores:

-- nowrap: cada elemento se ajusta a una sola línea
-- wrap: Los elementos se envuelven alrededor de líneas adicionales
-- wrap-reverse: Los elementos se envuelven alrededor de líneas adicionales pero comenzando del final hacia el inicio

# flex-flow

- Esta propiedad fue creada para combinar al flex-direction y el flex-wrap, colocando los valores separados por un espacios:

# align-content:
Cuando los objetos están separados por defecto, se puede utilizar esta propiedad:

    -- flex-start: Las líneas se posicionan en la parte superior del contenedor.
    -- flex-end: Las líneas se posicionan en la parte inferior del contenedor.
    -- center: las líneas se posicionan en el centro (verticalmente hablando) del contenedor.
    -- Space-between: Las líneas se muestran con la misma distancia entre ellas.
    -- space-around: las líneas de muestran con la misma separación alrededor de ellas.
    -- stretch: Las líneas se estiran para ajustarse al contenedor.
