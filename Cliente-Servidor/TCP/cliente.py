from socket import socket, AF_INET, SOCK_STREAM
import time

# Configuração do servidor (ext-dn)
SERVER_IP = "192.168.70.130"  # IP do eth0 do oai-ext-dn
PORT = 1235  # Porta do servidor

# Criando o socket
mClientSocket = socket(AF_INET, SOCK_STREAM)

# Conectando ao servidor
mClientSocket.connect((SERVER_IP, PORT))

# Enviando "Hello World" 15 vezes com intervalo de 5s
for i in range(15):
    message = f"Hello World #{i+1} from UE"
    mClientSocket.send(message.encode())  # Envia a mensagem
    data = mClientSocket.recv(2048)  # Recebe resposta do servidor
    reply = data.decode()
    print(f'Resposta recebida: {reply}')
    time.sleep(5)  # Aguarda 5 segundos

# Fecha o socket após enviar todas as mensagens
mClientSocket.close()
