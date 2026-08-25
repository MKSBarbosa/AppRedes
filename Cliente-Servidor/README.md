# Cliente-Servidor

Exemplos básicos de comunicação em rede usando a API de sockets do Python, comparando os dois principais protocolos de transporte: **TCP** (orientado a conexão) e **UDP** (sem conexão).

## Estrutura

- [`TCP/`](./TCP) — cliente e servidor usando sockets `SOCK_STREAM`, com o servidor tratando múltiplos clientes simultaneamente via threads.
- [`UDP/`](./UDP) — cliente e servidor usando sockets `SOCK_DGRAM`, incluindo uma versão do servidor com threads.

## TCP x UDP

| | TCP | UDP |
|---|---|---|
| Conexão | Orientado a conexão (`connect` / `accept`) | Sem conexão (envia direto para o endereço) |
| Confiabilidade | Garante entrega e ordem das mensagens | Não garante entrega nem ordem |
| Chamadas usadas | `listen()`, `accept()`, `send()`, `recv()` | `sendto()`, `recvfrom()` |

Veja o `README.md` de cada subpasta para detalhes de cada script e como executá-los.
