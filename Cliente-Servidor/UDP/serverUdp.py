from socket import socket, AF_INET, SOCK_DGRAM

serverPort = 1234
serverName = 'localhost'

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print('The server is ready to receive')

for i in range(6):
    message, clientAddress = serverSocket.recvfrom(2048)
    req = message.decode()
    print(f'A requisicao foi:{req}')
    rep = 'Hey cliente!'
    serverSocket.sendto(rep.encode(),clientAddress)

serverSocket.close()