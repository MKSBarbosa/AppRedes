from socket import socket, AF_INET, SOCK_STREAM
#Passo 1: Criando o socket.
mClientSocket = socket(AF_INET, SOCK_STREAM)
#Passo 2: Transformando o socket criado num socket de um cliente,
#ou seja, colacando para realizar solicitações.
mClientSocket.connect(('localhost', 1235))

while True:
    # Este loop foi criado apenas para que o cliente conseguisse enviar múltiplas solicitações
    message = input('>>')
    #Enviando a mensagem pelo socket criado.
    mClientSocket.send(message.encode())
    #Recebendo as respostas do servidor.
    data = mClientSocket.recv(2048)
    reply = data.decode()
    print(f'Resposta recebida:{reply}')
