from email.utils import formatdate
from datetime import datetime
from time import mktime

def sucesso():

    now = datetime.now()
    mStamp = mktime(now.timetuple())

    #header
    resposta = ''
    resposta += 'HTTP/1.1 200 OK\r\n'
    resposta += f'Date: {formatdate(timeval=mStamp, localtime=False, usegmt=True)}\r\n'
    resposta += 'Server: CIn UFPE/0.0.0.1 (Ubuntu)\r\n'
    # resposta += f'Content-Length: '
    resposta += 'Content-Type: text/html\r\n'
    resposta += '\r\n'

    #mensagem
    html = ''
    html += '<html>'
    html += '<head>'
    html += '<title>Redes de Computadores - CIn/UFPE</title>'
    html += '<meta charset="UTF-8">'
    html += '</head>'
    html += '<body>'
    html += '<h1>Hello World</h1>'
    html += '<h2>Hello World</h2>'
    html += '<h3>Hello World</h3>'
    html += '</body>'
    html += '</html>'

    resposta += html
    return resposta

def NaoEncontrado():
    now = datetime.now()
    mStamp = mktime(now.timetuple())

    resposta = ''
    resposta += 'HTTP/1.1 404 Not Found\r\n'
    resposta += f'Date: {formatdate(timeval=mStamp, localtime=False, usegmt=True)}\r\n'
    resposta += 'Server: CIn UFPE/0.0.0.1 (Ubuntu)\r\n'
    # resposta += f'Content-Length: '
    resposta += 'Content-Type: text/html\r\n'
    resposta += '\r\n'

    html = ''
    html += '<html>'
    html += '<head>'
    html += '<title>Not Found - CIn/UFPE</title>'
    html += '<meta charset="UTF-8">'
    html += '</head>'
    html += '<body>'
    html += '<h1>Essa requisição não foi encontrada no servidor</h1>'
    html += '</body>'
    html += '</html>'

    resposta += html
    return resposta