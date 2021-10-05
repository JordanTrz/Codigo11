# Los métodos GET y POST

## GET:
- Es un método que se usa para obtener un resultado
- ejemplo: cuando usar get
[1] cuando tengamos un filtro
[2] Cuando uso un buscador

ojo: La información de GET viaja por la URL

## POST:
- Es un método pero que se usa para enviar información sensible (password, numero de telefono, DNI, ...)
- Ejemplo:
[1] Iniciar Sesión => Email, Password
[2] Crear cuenta
[3] Solicitudes de cuenta bancaria

## readonly vs disabled

### readonly

- Se usa cuando queremos hacer que un input no sea editable, pero queremos mantener su valor al momento de enviar la información

### diabled
- Se usa cuando queremos hacer que un input no sea editable, pero esto no conserva el valor

* porque al momento de enviar la información, sabemos que enviamos el valor de cada input, pero si el input tiene la propiedad *disabled* este valor sera nulo, sin emvargo, si se usa *readonly el valor será enviado.