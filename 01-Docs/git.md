# Configurar github

## Git init
Se inicializa el git local de la carpeta donde nos encontramos

## git config --global user.email <email>
Es para agregar el email a git

## git config --glocal user.name <nombre>
Para colocar nombre

## git config --list
Esto es para visualizar las configuraciones que se tienen guardadas

## git add .
pone en tracking los archivos que se tienen

## git commit -m "comentario"
Guarda los archivos que se hicieron tracking

## git remote add origin url-repo
Se tiene que configurar la URL a la que se va a realizar el push.

## git push origin main
Hace el push del repositorio local al repo en la nube (una vez creado el url en github)

## git status
Es para verificar el estatus de si hay archivos modificados y que no se han guardado

## Git log
Es para visualizar todos los commit que se hicieron en el tiempo

## git remote add origin <url>
Si no se tiene una url, se utiliza este comando


## git remote set-url origin <url>
Si ya secuenta con un url y se desea cambiar, se debe utilizar este comando

## git restore
Retaura en base al última versión que se tenía registrado en el staging area

Si se quiere restaurar solo un archivo de todos los que se modificaron, se puede realizar:

- git restore <nombre archivo>

## git reset
Es para restaurar a una versión anterior del commit. Esto cuando los cambios ya se necuentran en el repo

git reset --hard <se pone el head del git log>

"Cuando se pone el --hard elimina los archivos

Para volver a la versión anterior pero sin eliminar los archivos el comando sería:

git reset <se pone el head del git log>