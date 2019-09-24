import sys
import time
import socket

def main():

    BUFSIZ = 2000

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if len(sys.argv) != 4:
        print("Uso: python client.py nome ip porta")
        quit()

    playerName = sys.argv[1]
    ipAddr = sys.argv[2]
    portConnect = sys.argv[3]

    server.connect((ipAddr, int(portConnect)))
    server.sendto((playerName).encode(), (ipAddr.encode(), int(portConnect)))

    msg = server.recv(BUFSIZ)

    print(msg.decode())

    # Conecta ao servidor
    # Quando receber a mensagem de que o jogo vai começar, começa a ouvir as perguntas
    #   Contabiliza tempo
    #   Envia resposta com tempo - tempo de recebimento da pergunta
    # Caso receba outra pergunta, continua o jogo. Senão, finaliza

main()
