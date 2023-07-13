from socket import socket, AF_INET, SOCK_STREAM
mClientSocket = socket(AF_INET, SOCK_STREAM)
mClientSocket.connect(('localhost', 9595))

# Este loop foi criado apenas para que o cliente conseguisse enviar múltiplas solicitações
message = 'GET /favicon.ico HTTP/1.1\r\n'
message += 'Host: localhost:9595\r\n'
message += 'Connection: keep-alive\r\n'

#Enviando a mensagem pelo socket criado.
mClientSocket.send(message.encode())
#Recebendo as respostas do servidor.
data = mClientSocket.recv(2048)
reply = data.decode()
print(f'Resposta recebida:{reply}')
