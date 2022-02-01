# Transiciones

Se puede realizar transiciones a diferentes box o textos en lo que es el front.

la propiedad como tal es el transition:

div {
  transition-property: width;
  transition-duration: 2s;
  transition-timing-function: linear;
  transition-delay: 1s;
}

Se cuenta con varias propiedades:

transition-delay: Es el tiempo que demora desde que colocas el cursor sobre el elemento (no se suele utilizar)

transition-duration: Es el tiempo que demora en realizar la transición

transition-property: especifica el nombre del efecto CSS que se va a aplicar (ejemplo: ease, ease-in ...)

transition-timing-function: especifica la velocidad con la que se va a ejectuar el efecto (esto se vusializa con el inspector)

TODAS ESTAS PROPIEDADES TIENEN UN SHORT-HAND:

## transition

En las propiedad transition se puede especificar todas las propiedades anteriormente mencionadas.

ejemplo:

div {
  transition: width 2s linear 1s;
}

Esta transición debe estar especificada dentro del elemento y no dentro del hover. Dentro del hover se debe especificar los valores de las imágenes, tamaño que se van  modificar