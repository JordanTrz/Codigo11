- Instalación de docker

Se debe realizar en el servidor de linux
página de tutorial:

https://docs.docker.com/engine/install/ubuntu/

códigos de docker:

https://gist.github.com/hansfpc/335159e420bd750c87ac2f2a3d083cdf

-- Pasos con Docker:

1. Instalar un contenedor de prueba

sudo docker pull hello-world
sudo docker run hello-world

2. verificamos que este levantando el contenedor:

sudo docker ps

3. verificamos estado de docker

sudo service docker status

4. instalamos postgres con docker

sudo docker pull postgres
sudo docker run --db1 codigog11 -e POSTGRES_PASSWORD=codigo2022 -d postgres
