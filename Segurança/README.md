# Segurança

Exemplos de criptografia aplicada à comunicação em rede: criptografia simétrica, assimétrica e um servidor Web com HTTPS.

## Arquivos

### `AES-SymmetricKey.py` (Hands on 4 — Chave Simétrica)
Demonstra criptografia simétrica com AES (biblioteca `pycryptodome`):
1. Lê um texto digitado pelo usuário e gera uma chave aleatória de 16 bytes.
2. Criptografa o texto no modo `AES.MODE_EAX` (que garante confidencialidade, autenticidade e integridade), obtendo `ciphertext` e uma `tag` de verificação.
3. Salva `nonce`, `tag` e `ciphertext` em `encrypted.bin`, lê o arquivo de volta e descriptografa os dados usando a mesma chave, validando a `tag`.

Requer: `pip install pycryptodome`

### `RSA-Asymmetric Key.py` (Hands on 4 — Chave Assimétrica)
Demonstra criptografia assimétrica com RSA (biblioteca `rsa`):
1. Gera um par de chaves pública/privada de 512 bits (tamanho reduzido apenas para fins didáticos — inseguro para uso real).
2. Criptografa uma mensagem fixa com a chave pública e descriptografa com a chave privada.

Requer: `pip install rsa`

### `Servidor_Web_https.py` (Hands on 5 — HTTPS)
Servidor Web com TLS/SSL, baseado em `http.server` + módulo `ssl`:
1. Sobe um `HTTPServer` em `localhost:443` que responde a qualquer `GET` com um HTML fixo.
2. Envolve o socket do servidor com `ssl.wrap_socket`, usando um certificado (`certificate.pem`) e uma chave privada (`key.pem`).

> A porta 443 exige privilégios de administrador (`sudo`) e é necessário gerar antes o certificado/chave — veja o arquivo `notes`.

### `notes`
Passo a passo (comandos `openssl`) para gerar, no Ubuntu, o certificado e a chave privada usados por `Servidor_Web_https.py`.

### `encrypted.bin`
Arquivo binário gerado por `AES-SymmetricKey.py` (nonce + tag + texto cifrado) — é um artefato de exemplo/saída, não precisa ser editado manualmente.

## Como executar

```bash
python3 AES-SymmetricKey.py
python3 "RSA-Asymmetric Key.py"

# HTTPS (gere antes certificate.pem e key.pem conforme o arquivo `notes`)
sudo python3 Servidor_Web_https.py
# acesse https://localhost no navegador (aceite o certificado autoassinado)
```
