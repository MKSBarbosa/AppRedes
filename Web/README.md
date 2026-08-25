# Web

Evolução de um servidor Web simples, do socket "cru" até o uso da biblioteca padrão `http.server`. Os arquivos seguem a numeração dos "Hands on" das aulas.

## Arquivos

### `ServidorWeb.py` (Hands on 1)
Servidor Web mínimo construído diretamente sobre sockets TCP:
1. Cria o socket, faz *bind* em `localhost:9595` e entra em `listen()`.
2. Aceita 2 conexões (`accept`), lê a requisição do cliente e sempre responde com o mesmo cabeçalho/HTML `200 OK` (montado manualmente na variável `msgHtml`).
3. Pode, alternativamente, montar a resposta usando as funções do módulo `htmlMessage.py` (linhas comentadas no arquivo).

### `htmlMessage.py`
Módulo auxiliar com funções que montam respostas HTTP completas (cabeçalho + HTML) como string:
- `sucesso()` — resposta `200 OK` com uma página "Hello World".
- `NaoEncontrado()` — resposta `404 Not Found`.

### `web_client.py`
Cliente que se conecta a `ServidorWeb.py` (`localhost:9595`), envia uma requisição `GET /favicon.ico HTTP/1.1` e imprime a resposta recebida.

### `serverweb-multiplas-solicitacoes.py` (Hands on 2)
Servidor Web sobre sockets que serve arquivos estáticos reais:
1. Faz *bind* em `localhost:9999`.
2. Para cada conexão aceita, lê a requisição e, dependendo do caminho pedido, devolve o conteúdo de `index.html` ou `style.css` (lidos do disco na inicialização); qualquer outro caminho recebe `404 Not Found`.
3. Atende um cliente por vez (loop infinito sem threads).

> Este script espera encontrar `index.html` e `style.css` na mesma pasta — eles não estão versionados no repositório, então é necessário criá-los antes de rodar.

### `httpServer.py` (Hands on 3)
Servidor Web usando a classe pronta `http.server.HTTPServer` / `BaseHTTPRequestHandler` da biblioteca padrão, escutando em `localhost:9090` e respondendo qualquer `GET` com o próprio caminho requisitado.

## Como executar

```bash
# Hands on 1
python3 ServidorWeb.py      # terminal 1
python3 web_client.py       # terminal 2 (ou acesse http://localhost:9595 no navegador)

# Hands on 2 (crie antes index.html e style.css)
python3 serverweb-multiplas-solicitacoes.py
# acesse http://localhost:9999 no navegador

# Hands on 3
python3 httpServer.py
# acesse http://localhost:9090 no navegador
```
