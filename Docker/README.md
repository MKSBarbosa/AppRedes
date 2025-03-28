# Introdução a docker

Nesta arquitetura cliente-servidor, estamos utilizando Docker para criar e gerenciar contêineres que implementam o papel de servidor e cliente em uma rede virtual. A rede foi configurada com a subnet 192.168.70.128/26.

O servidor Docker é responsável por fornecer serviços ou recursos, enquanto o cliente Docker consome esses serviços ou recursos.

### Descrição da Arquitetura:

#### Servidor Docker (192.168.70.131):

Um contêiner Docker nomeado "servidor" é iniciado a partir da imagem "server:latest", criada a partir do Dockerfile.server.
Este servidor estará disponível na rede definida como "reder-docker-exemplo".
Ele está configurado com o endereço IP 192.168.70.131 dentro dessa rede.

#### Cliente Docker (192.168.70.135):

Um contêiner Docker nomeado "cliente" é iniciado a partir da imagem "cliente:latest", criada a partir do Dockerfile.client.
Este cliente também está na rede "reder-docker-exemplo".
Ele possui o endereço IP 192.168.70.135 na mesma rede.
Essa arquitetura permite a comunicação entre os contêineres do servidor e do cliente dentro da mesma rede Docker.

A imagem abaixo ilustra a disposição da arquitetura cliente-servidor:


![Arquitetura Cliente-Servidor](docs/images/arquitetura.png)


### Utilizando Docker Run

```
docker build -t server:latest -f Dockerfile.server .
docker build -t cliente:latest -f Dockerfile.client .
docker network create --subnet=192.168.70.128/26 reder-docker-exemplo
docker run -it --name servidor --net reder-docker-exemplo --ip 192.168.70.131 server:latest 
docker run --name cliente --net reder-docker-exemplo --ip 192.168.70.135 cliente:latest
```

### Utilizando o Docker Compose

```
docker-compose -f aplication.yaml up server
docker-compose -f aplication.yaml up
```

### Redirecionamento NAT

```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 9999
sudo iptables -t nat -L --line-numbers
sudo iptables -t nat -D PREROUTING 2
```

### DNS
```
sudo vim /etc/hosts
192.34.1.9 mksb.server
nslookup mksb.server
```


### Rota Estatica

```
sudo ip route add <rede_alvo> via <next_hop> dev <interface_local_de_saída>
#comandos aplicados no host de origem e destigo
sudo sysctl net.ipv4.conf.all.forwarding=1
sudo iptables -P FORWARD ACCEPT
```