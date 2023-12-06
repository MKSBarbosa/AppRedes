# Hands on 3: Web Server based on HTTP simple

from http.server import HTTPServer, BaseHTTPRequestHandler

class handleRequest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.path.encode())

httpServer = HTTPServer(('localhost',9090), handleRequest)
print('O servidor está ativo!')
httpServer.serve_forever()

