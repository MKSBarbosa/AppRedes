# Hands on 1: Web Server based on HTTP initial

from socket import socket, AF_INET, SOCK_STREAM
import htmlMessage

#1)Criar o socket servidor:
webServerSocket = socket(AF_INET, SOCK_STREAM)
webServerSocket.bind(('localhost', 9595))
webServerSocket.listen()

#2)Aceitar as solicitações dos clientes:
for i in range(2):
    print('Esperando Solicitações ....')
    clientSocket, clientAddress = webServerSocket.accept()
    #Recebendo dados do cliente
    data = clientSocket.recv(2048)
    print(f'{data.decode()}')
    #Respondendo a solicitação
    msgHeader = 'HTTP/1.1 200 OK \r\n' \
                'Date: Tue, 09 Aug 2022 13:23:35 GMT\r\n' \
                'Server: MyServer/0.0.1 (Ubuntu)\r\n' \
                'Content-Type: text/html\r\n' \
                '\r\n'
    msgBody = '<html>' \
              '<head><title>Hello, World</title></head>' \
              '<body><h1> Your first web server!</h1>' \
              '<h3>Congratulation!!</h3>' \
              '</body>' \
              '</html>'

    msgHtml = msgHeader + msgBody
    #msgHtml = htmlMessage.sucesso()
    #msgHtml = htmlMessage.NaoEncontrado()

    clientSocket.send(msgHtml.encode())
    clientSocket.close()

webServerSocket.close()