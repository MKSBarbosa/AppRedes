# TCP

Exemplo de comunicação cliente-servidor usando sockets TCP (`SOCK_STREAM`), no qual o servidor atende múltiplos clientes simultaneamente por meio de threads, mantendo uma conexão persistente com cada um.

## Arquivos

### `servidor-thread.py`
Servidor TCP que:
1. Cria um socket (`socket(AF_INET, SOCK_STREAM)`).
2. Faz o *bind* na porta `1235` de `127.0.0.1`.
3. Entra em `listen()` aguardando conexões.
4. A cada conexão aceita (`accept()`), inicia uma nova `Thread` executando `HandleRequest`, permitindo atender vários clientes ao mesmo tempo.
5. Dentro de `HandleRequest`, fica em loop recebendo (`recv`) e respondendo (`send`) mensagens do mesmo cliente, sem precisar criar uma nova conexão a cada mensagem.

### `cliente.py`
Cliente TCP que:
1. Cria um socket e se conecta (`connect`) ao servidor em `localhost:1235`.
2. Em loop, lê uma mensagem digitada pelo usuário (`input`), envia para o servidor e imprime a resposta recebida.

## Como executar

Em dois terminais separados, dentro desta pasta:

```bash
# Terminal 1 — inicia o servidor
python3 servidor-thread.py

# Terminal 2 — inicia o cliente
python3 cliente.py
```

Digite mensagens no terminal do cliente; o servidor sempre responderá `Hey cliente!`. Você pode abrir vários terminais de cliente para testar o atendimento simultâneo do servidor.
