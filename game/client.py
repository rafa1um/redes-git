import sys


def main():

    if len(sys.argv) != 4:
        print("Uso: python client.py nome ip porta")
        quit()

    playerName = sys.argv[1]
    ipAddr = sys.argv[2]
    portConnect = sys.argv[3]

    # Conecta ao servidor
    # Quando receber a mensagem de que o jogo vai começar, começa a ouvir as perguntas
    #   Contabiliza tempo
    #   Envia resposta com tempo - tempo de recebimento da pergunta
    # Caso receba outra pergunta, continua o jogo. Senão, finaliza

main()
