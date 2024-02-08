# Introdução a docker

### Utilizando Docker Run

docker build -t server:latest -f Dockerfile.server .
docker build -t cliente:latest -f Dockerfile.client .
docker network create --subnet=192.168.70.128/26 reder-docker-exemplo
docker run -it --name servidor --net reder-docker-exemplo --ip 192.168.70.131 server:latest 
docker run --name cliente --net reder-docker-exemplo --ip 192.168.70.135 cliente:latest


### Utilizando o Docker Compose

docker-compose -f aplication.yaml up server
docker-compose -f aplication.yaml up