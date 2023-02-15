import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 8080  # Porta para conexão

# Cria o socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Conecta ao servidor
    print("Conectado ao servidor")
    while True:
        msg = input("Cliente: ")  # Digita a mensagem
        s.sendall(msg.encode('utf-8'))  # Envia a mensagem para o servidor
        data = s.recv(1024)  # Recebe a resposta do servidor
        print(f"Servidor: {data.decode('utf-8')}")
