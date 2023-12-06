# Hands on 4: Key Generator (Asymmetric Key)
# Este script demonstra como gerar uma chave aleatória, criptografar e descriptografar dados usando o algoritmo RSA.

# Caso o seu computador não tenha a biblioteca Crypto
# pip install rsa
import rsa

# Geraçaõ das chaves públicas e privadas
pubkey, privkey = rsa.newkeys(512)

# Dados a serem criptografados
data = b'hello world'

# Criptografa os dados com a chave pública
ciphertext = rsa.encrypt(data, pubkey)
print(f'Ciphertext: {ciphertext.hex()}')

# Descriptografa os dados com a chave privada
plaintext = rsa.decrypt(ciphertext, privkey)

print(f'Plaintext: {plaintext.decode("utf-8")}')