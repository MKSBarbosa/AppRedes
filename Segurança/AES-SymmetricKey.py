# Hands on 4: Key Generator (Symmetric Key)
# Este script demonstra como gerar uma chave aleatória, criptografar e descriptografar dados usando o algoritmo AES.

# Caso o seu computador não tenha a biblioteca Crypto
# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Texto a ser criptografado

#data = b'hello world'
data = input("Digite o texto a ser criptografado: ").encode('utf-8')

# Gera uma sequência de bytes aleatórios de tamanho 16 para ser usada como chave
key = get_random_bytes(16)

print(f'Key: {key}')

# Criptografando os dados usando o modo de operação EAX
# O modo EAX (Encrypt-Then-Authenticate-X) é projetado 
# para fornecer confidencialidade, autenticidade e 
# integridade dos dados. 

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(f'Cipher = {ciphertext} - size is {len(ciphertext)} bytes')

##### Não é necessário #####

# Essa parte do código salva o nonce, a tag e o texto cifrado em um arquivo binário.
file_out = open("encrypted.bin", "wb")
[file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
file_out.close()

# Lê o nonce, a tag e o texto cifrado do arquivo binário
file_in = open("encrypted.bin", "rb")
nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
file_in.close()

#############################

# Descriptografando os dados usando a mesma chave, nonce e tag
cipher = AES.new(key, AES.MODE_EAX, nonce)
new_data = cipher.decrypt_and_verify(ciphertext, tag)

print(f'The initial data is {new_data} and the length is {len(new_data)}')
