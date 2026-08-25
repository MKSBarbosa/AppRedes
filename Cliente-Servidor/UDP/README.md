# UDP

Exemplo de comunicação cliente-servidor usando sockets UDP (`SOCK_DGRAM`), um protocolo sem conexão: cada mensagem é enviada de forma independente, sem garantia de entrega ou ordem.

## Arquivos

### `serverUdp.py`
Servidor UDP simples que:
1. Cria o socket e faz o *bind* na porta `1234` de `localhost`.
2. Recebe até 6 mensagens (`recvfrom`), imprimindo cada requisição e respondendo `Hey cliente!` (`sendto`) a cada uma.
3. Fecha o socket ao final do loop.

### `serverUdpThreads.py`
Versão do servidor que atende requisições em paralelo:
1. Cria e faz o *bind* do socket na porta `1234`.
2. Dispara 2 threads executando `HandleRequestUdp`, cada uma recebendo e respondendo até 3 mensagens no mesmo socket compartilhado.

### `clienteUdp.py`
Cliente UDP que:
1. Cria o socket e define o endereço do servidor (`localhost:1234`).
2. Em um loop de 3 iterações, lê uma mensagem do usuário, envia via `sendto` e imprime a resposta recebida via `recvfrom`.
3. Fecha o socket ao final.

## Como executar

Em dois terminais separados, dentro desta pasta:

```bash
# Terminal 1 — inicia o servidor (escolha um dos dois)
python3 serverUdp.py
# ou
python3 serverUdpThreads.py

# Terminal 2 — inicia o cliente
python3 clienteUdp.py
```

O cliente envia 3 mensagens; o `serverUdp.py` aceita até 6 no total (dá para rodar o cliente duas vezes) e o `serverUdpThreads.py` atende até 3 mensagens por thread (2 threads no total).
