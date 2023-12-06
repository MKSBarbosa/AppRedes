# Hands on 5: HTTPS + Certificados (Asymmetric Key)

import http.server
import ssl

httpd = http.server.HTTPServer(('localhost', 443),
                               http.server.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               certfile='certificate.pem',
                               keyfile= "key.pem",
                               server_side=True,
                               ssl_version=ssl.PROTOCOL_TLS)

httpd.serve_forever()
