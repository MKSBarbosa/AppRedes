#Hands on 2: Web Server based on HTTP

from socket import socket, AF_INET, SOCK_STREAM

with open('./index.html', 'r') as f:
    index_html = f.read()
with open('./style.css', 'r') as f:
    style_css = f.read()

ss = socket(AF_INET, SOCK_STREAM)
ss.bind(('192.168.70.131', 9999))
ss.listen()

while True:
    sc, addr = ss.accept()
    request = sc.recv(1024).decode()
    print(f'O endereço {addr} fez a requisição = {request}')
    if request.startswith('GET / HTTP/1.1'):
        reply = 'HTTP/1.1 200 OK\n\n' + index_html
    elif request.startswith('GET /style.css HTTP/1.1'):
        reply = 'HTTP/1.1 200 OK\nContent-Type: text/css\n\n' + style_css
    else:
        reply = 'HTTP/1.1 404 Not Found\n\nPage not found.'

    sc.send(reply.encode())
    sc.close()

ss.close()