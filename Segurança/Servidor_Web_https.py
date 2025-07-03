# Hands on 5: HTTPS + Certificados (Asymmetric Key)

import http.server
import ssl

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Adiciona um log no terminal mostrando que o usuário realizou uma solicitação
        print(f"Usuário fez uma solicitação: {self.path}")

        # Retorna um texto HTML simples para o cliente
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Hello, World!</h1></body></html>')

# Cria um servidor HTTP com certificados SSL
httpd = http.server.HTTPServer(('localhost', 8119), MyHandler)

# Configuração do SSL
httpd.socket = ssl.wrap_socket(httpd.socket,
                               certfile='certificate.pem',
                               keyfile='key.pem',
                               server_side=True,
                               ssl_version=ssl.PROTOCOL_TLS)

# Inicia o servidor
print("Servidor HTTPS rodando na porta 8119...")
httpd.serve_forever()
