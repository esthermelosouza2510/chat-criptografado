import socket
from crypto_utils import criptografar, descriptografar

Host = "127.0.0.1"
Port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
   
    while True:
        mensagem = input("Cliente: ")

        if mensagem.lower() == "encerrar":
            print("Conexão encerrada.")
            break

        mensagem_criptografada = criptografar(mensagem)
        s.sendall(mensagem_criptografada.encode())

        data = s.recv(1024)

        resposta_criptografada = data.decode()
        resposta = descriptografar(resposta_criptografada)

        print("Servidor:", resposta)
    