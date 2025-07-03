from socket import socket, AF_INET, SOCK_STREAM
import ssl

# Carrega os arquivos HTML e CSS
with open('./index.html', 'r') as f:
    index_html = f.read()
with open('./style.css', 'r') as f:
    style_css = f.read()

# Cria o socket base
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen()

# Configura o contexto SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='certificate.pem', keyfile='key.pem')

print("Servidor HTTPS rodando em https://localhost:9999")

while True:
    client_socket, addr = server_socket.accept()
    
    # Envolve o socket com SSL
    try:
        ssl_socket = context.wrap_socket(client_socket, server_side=True)
    except ssl.SSLError as e:
        print(f"Erro SSL com {addr}: {e}")
        client_socket.close()
        continue

    try:
        request = ssl_socket.recv(1024).decode()
        print(f"Requisição recebida: {request.splitlines()[0]}")

        if request.startswith('GET / HTTP/1.1'):
            reply = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + index_html
        elif request.startswith('GET /style.css HTTP/1.1'):
            reply = 'HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n' + style_css
        else:
            reply = 'HTTP/1.1 404 Not Found\r\n\r\nPage not found.'

        ssl_socket.sendall(reply.encode())
    except Exception as e:
        print(f"Erro ao lidar com a requisição: {e}")
    finally:
        ssl_socket.close()

server_socket.close()
