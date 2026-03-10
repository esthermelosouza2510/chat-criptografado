from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

KEY = b'chave_secreta123'

def criptografar(mensagem):
    cipher = AES.new(KEY, AES.MODE_ECB)
    mensagem_bytes = mensagem.encode()
    mensagem_padded = pad(mensagem_bytes, AES.block_size)
    criptografado = cipher.encrypt(mensagem_padded)
    
    return base64.b64encode(criptografado).decode()

def descriptografar(mensagem):
    cipher = AES.new(KEY, AES.MODE_ECB)
    mensagem_bytes = base64.b64decode(mensagem)
    descriptografado = cipher.decrypt(mensagem_bytes)
    mensagem_final = unpad(descriptografado, AES.block_size)
    
    return mensagem_final.decode()