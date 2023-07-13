from socket import socket, AF_INET, SOCK_DGRAM
#Passo 1: Criando o socket.
mClientSocket = socket(AF_INET, SOCK_DGRAM)

serverPort = 1234
serverName = 'localhost'

serverAddress = (serverName, serverPort)

for i in range(3):
    # Este loop foi criado apenas para que o cliente conseguisse enviar múltiplas solicitações
    message = input('>>')
    #Enviando a mensagem pelo socket criado.
    mClientSocket.sendto(message.encode(), serverAddress)
    #Recebendo as respostas do servidor.
    data, sAddress = mClientSocket.recvfrom(2048)
    reply = data.decode()
    print(f'Resposta recebida:{reply}')

mClientSocket.close()