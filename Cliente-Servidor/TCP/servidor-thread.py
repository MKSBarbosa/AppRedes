from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def HandleRequest(mClientSocket, mClientAddr):
    while True:
        # Este loop foi criado para que o servidor conseguisse receber diversas requisições de
        # um mesmo cliente, usando a mesma conexão, ou seja, sem que fosse necessária a
        # criação de uma nova conexão.
        print('Esperando o próximo pacote ...')
        # Recebendo os dados do Cliente:
        # o Servidor irá receber bytes do cliente, sendo necessária a conversão de bytes
        # para string ou para o tipo desejado.
        data = mClientSocket.recv(2048)
        print(f'Requisição recebida de {mClientAddr}')
        req = data.decode()
        print(f'A requisição foi:{req}')
        # Após receber e processar a requisição o servidor está apto para enviar uma resposta.
        rep = 'Hey cliente!'
        mClientSocket.send(rep.encode())

#Passo 1: Criação do socket
mSocketServer = socket(AF_INET, SOCK_STREAM)
print(f'Socket criado ...')
#Passo 2: Transformando o socket em um socket servidor.
#Dar Bind significa vincular um socket a um endereço
mSocketServer.bind(('127.0.0.1',1235))

#Colocar o servidor para escutar as solicitações de conexão
mSocketServer.listen()
while True:
    # Este loop foi colocado para que o servidor conseguisse se conectar com vários cliente;
    # Passo 3: Colocar o servidor para aceitar as solicitações de conexão:
    clientSocket, clientAddr =  mSocketServer.accept()
    print(f'O servidor aceitou a conexão do Cliente: {clientAddr}')
    # Passo 4: Criação de múltiplas threads para que o servidor consiga responder mais de
    # um cliente por vez.
    Thread(target=HandleRequest, args=(clientSocket, clientAddr)).start()
