- Test

Los test sirven para poder encontrar posibles bugs/errores de código

-- Editando tests.py dentro del proyecto

Se tiene que importar el modelo y crear una clase de test.
Al momento de definir el nombre del def dentro de la clase, siempre tiene que comenzar con nombre test:

`def test_create_bookmark(self):`

luego, dentro del def se instancia el modelo creado y se inserta data como si fuera un post. se pone un .save() para guardar y luego

luego se realiza una comparación de lo que se creó está bien:

`self.assertEqual(bk.titulo,"GOOGLE")`

y se corre la línea de código en el terminal:

python3 manage.py test "nombre del app"