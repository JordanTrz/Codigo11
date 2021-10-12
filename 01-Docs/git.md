# Configurar github

## Git init
Se inicializa el git local de la carpeta donde nos encontramos

## git config --global user.email <email>
Es para agregar el email a git

## git config --global user.name <nombre>
Para colocar nombre

## git config --global core.editor vim
Esto es paradefinir como editor predeterminado al vim

## ssh-keygen
Esto es para generar una clave ssh publica y privada (en caso no se tenga) para que se pueda enlazar con la cuenta del github

## ssh-agent sh -c 'ssh-add; ssh-add -L'
Esto es para visualizar tu ssh key. Con esto se configura el github. 
    - Se ingresa en la página de github
    - se entra a settings en la cuenta principal
    - nos dirigimos a la opción SSH and GPG keys
    - damos click en el boton "New SSH key"
    - le coloco un nombre a mi key y pego todo el código que obtengo en el terminal luego de colocar el comando

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

## git log
Es para visualizar todos los commit que se hicieron en el tiempo

## git show
This property helps you to see the details of the commit

git show <SHA-1 CODE>

## git diff
This helps you to see de difference between to commits

git diff <SHA OLDER> <SHA NEW>

## git commit --ammend -m "comment"
this ussefull if you did a commit and you realize something was wrong and you want to change it.

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

## git checkout -b
se utiliza un nuevo branch:

git checkout -b <nombre rama>

con esa línea de código lo que se hace es crear la nueva rama y ponerla como principal para que se guarde todo ahí

## git branch <nombre>
Si se quiere crear una rama pero sin ponerla como principal

## git branch -a
Esto se utiliza para visualizar las ramas que se tienen de forma local y remota.

## git branch -D <branch>
Se elimina un branch. Se coloca el nombre del branch que se desea eliminar del repo local

## git fetch --prune
limpiar tags locales que no se encuentran en el remoto y eliminar tags cambiados
Actualiza y limpia el repo remoto   

## git pull origin <branch>
Esto se utiliza para descargar las actualizaciones que se tiene en el repo remoto

## git push origin --delete <branch remoto>
Esto es para poder eliminar un branch en el repo remoto

## Tags
Tag is like a branch but immutable. it will not be udated even if you create a new commit. usallu, developers create tags for product releases.

# git tag <nombre>
git push nombre

"buscar versionado semántico"

# reglas github
Se puede definir reglas en el github para que las personas no hagan un pull request directamente. También se puede definir si alguien tiene que definir.

https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule

## HEAD

head is a pointer, which always points to the latest commit in the branch.

## lo que se encuentra al momento de crear un nuevo repo:

…or create a new repository on the command line
echo "# clase-2" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:JordanTrz/clase-2.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin git@github.com:JordanTrz/clase-2.git
git branch -M main
git push -u origin main

# token
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
