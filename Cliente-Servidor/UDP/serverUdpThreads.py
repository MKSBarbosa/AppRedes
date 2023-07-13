from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def HandleRequestUdp(mserverSocket):
    for j in range(3):
        message, clientaddress = serverSocket.recvfrom(2048)
        req = message.decode()
        print(f'Requisicao recebida de {clientaddress}')
        print(f'A requisicao foi:{req}')
        rep = 'Hey cliente!'
        mserverSocket.sendto(rep.encode(), clientaddress)

serverPort = 1234
serverName = 'localhost'

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print('The server is ready to receive')

for i in range(2):
    Thread(target=HandleRequestUdp, args=(serverSocket,)).start()

