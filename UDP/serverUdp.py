
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def HandleRequestUdp(serverSocket):
    for j in range(3):
        message, clientaddress = serverSocket.recvfrom(2048)
        req = message.decode()
        print(f'Requisicao recebida de {clientaddress}')
        print(f'A requisicao foi: {req}')

        # Identificando o cliente e a solicitação recebida
        info = f'Cliente: {clientaddress}, Solicitação: {req}\n'

        # Salvando as informações em um arquivo
        with open('registro_solicitacoes.txt', 'a') as file:
            file.write(info)

        rep = 'Hey cliente!'
        serverSocket.sendto(rep.encode(), clientaddress)

serverPort = int('10305')
serverName = 'localhost'

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print(f'O servidor está pronto para receber na porta {serverPort}')

for i in range(2):  # Atendendo pelo menos dois clientes simultaneamente
    Thread(target=HandleRequestUdp, args=(serverSocket,)).start()
