
from socket import socket, AF_INET, SOCK_DGRAM


def communicate_with_server():
    mClientSocket = socket(AF_INET, SOCK_DGRAM)
    serverPort = int('10305')
    serverName = 'localhost'
    serverAddress = (serverName, serverPort)

    for i in range(3):
        message = input('>> ')
        mClientSocket.sendto(message.encode(), serverAddress)
        data, _ = mClientSocket.recvfrom(2048)
        reply = data.decode()
        print(f'Resposta recebida: {reply}')

    mClientSocket.close()

# Criando dois clientes
for _ in range(2):
    communicate_with_server()

