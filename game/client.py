import sys
import time
import socket
import pickle
import select


def question_game(question):
    rec_time = time.clock()
    print("Pergunta:", question.questionText)
    print("1 -", question.ans1)
    print("2 -", question.ans2)
    print("3 -", question.ans3)
    print("4 -", question.ans4)
    i, o, e = select.select([sys.stdin], [], [], 10)
    if (i):
        ans = sys.stdin.readline().strip()
        print("Você respondeu:", ans)
        print("Aguarde seu oponente.")
        ans_time = time.clock() - rec_time
    else:
        ans_time = 10
        ans = 0

    return ans_time, ans

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

    if msg.decode() == "STARTGAME":
        server.sendto("OK".encode(), (ipAddr.encode(), int(portConnect)))
    
    qst = server.recv(BUFSIZ)

    while pickle.loads(qst).questionText != "FIM":
        # mostra questao
        tempo_resposta = question_game(pickle.loads(qst))
        server.sendto(pickle.dumps(tempo_resposta), (ipAddr.encode(), int(portConnect)))
        qst = server.recv(BUFSIZ)
        print(qst.decode())
        qst = server.recv(BUFSIZ)


    # Conecta ao servidor
    # Quando receber a mensagem de que o jogo vai começar, começa a ouvir as perguntas
    #   Contabiliza tempo
    #   Envia resposta com tempo - tempo de recebimento da pergunta
    # Caso receba outra pergunta, continua o jogo. Senão, finaliza

main()
