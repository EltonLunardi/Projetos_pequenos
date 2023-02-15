import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 8080  # Porta para conexão

# Cria o socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Associa o socket com o endereço e a porta
    s.listen()  # Aguarda conexões
    print(f"Servidor iniciado e aguardando conexões em {HOST}:{PORT}...")
    conn, addr = s.accept()  # Aceita a conexão
    with conn:
        print(f"Conexão estabelecida com {addr}")
        while True:
            data = conn.recv(1024)  # Recebe a mensagem do cliente
            if not data:
                break
            print(f"Cliente: {data.decode('utf-8')}")
            msg = input("Servidor: ")  # Digita a resposta
            # Envia a resposta para o cliente
            conn.sendall(msg.encode('utf-8'))
