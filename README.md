# AppRedes

Repositório de apoio ao estágio docência da disciplina de Redes de Computadores (CIn/UFPE). Reúne exemplos práticos ("hands-on") em Python que ilustram, de forma incremental, os principais conceitos de programação de redes: sockets TCP e UDP, servidores Web (HTTP e HTTPS), criptografia simétrica/assimétrica e uma arquitetura cliente-servidor em containers Docker.

## Estrutura do repositório

| Pasta | Conteúdo |
|---|---|
| [`Cliente-Servidor/`](./Cliente-Servidor) | Exemplos de sockets TCP e UDP básicos, com e sem threads. |
| [`Web/`](./Web) | Servidores Web feitos "na mão" com sockets e com a biblioteca `http.server`. |
| [`Segurança/`](./Segurança) | Criptografia simétrica (AES), assimétrica (RSA) e um servidor HTTPS. |
| [`Docker/`](./Docker) | A mesma arquitetura cliente-servidor rodando em containers Docker, em rede isolada. |
| [`Apresentações/`](./Apresentações) | Slides usados nas aulas/apresentações. |

Cada pasta possui seu próprio `README.md` detalhando os arquivos que contém, o que fazem e como executá-los.

## Pré-requisitos

- Python 3
- Bibliotecas extras usadas em alguns exemplos (ver README de cada pasta): `pycryptodome`, `rsa`, `pandas`, `numpy`
- Docker e Docker Compose (apenas para os exemplos em `Docker/`)

## Como executar

```bash
git clone <url-do-repositório>
```

Abra o terminal, entre na pasta do exemplo desejado e rode o script com Python 3:

```bash
python3 arquivo.py
```

> Para os exemplos cliente-servidor (`Cliente-Servidor/`, `Web/`), é necessário abrir dois terminais: um para o servidor e outro para o cliente. Inicie sempre o servidor primeiro.

Consulte o `README.md` de cada pasta para instruções específicas (portas usadas, dependências extras, arquivos necessários etc).
