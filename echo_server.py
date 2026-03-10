import socket
import threading
from crypto_utils import criptografar, descriptografar

Host = "127.0.0.1"
Port = 65432


def lidar_com_cliente(conn, addr):
    print(f"Cliente conectado: {addr}")

    with conn:
        while True:
            data = conn.recv(1024)

            if not data:
                print(f"Cliente desconectado: {addr}")
                break

            mensagem_criptografada = data.decode()
            mensagem = descriptografar(mensagem_criptografada)

            print(f"Cliente {addr}: {mensagem}")

            resposta = input("Servidor: ")
            resposta_criptografada = criptografar(resposta)

            conn.sendall(resposta_criptografada.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host, Port))
    s.listen()

    print(f"Servidor escutando em {Host}:{Port}")

    while True:
        conn, addr = s.accept()

        thread = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
        thread.start()