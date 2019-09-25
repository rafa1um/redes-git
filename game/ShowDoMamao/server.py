import question
import socket
import sys
import pickle
import select


def send_question(questao, connp1, connp2):

    connp1.sendall(pickle.dumps(questao))
    connp2.sendall(pickle.dumps(questao))
    print("Questão", questao.questionText, " Enviada")

    #espera resposta

def set_questions():

    question_list = []

    question1 = question.Question(
        1,
        "Qual a cor da semente do mamão?",
        "Azul",
        "Cor de rosa",
        "Cor de mamão",
        "Preta",
        4
    )
    question_list.append(question1)
    
    question2 = question.Question(
        2,
        "Qual desses não é um tipo de mamão?",
        "Mamão da Baía",
        "Mamão da Índia",
        "Mamão Maçã",
        "Mamão Corda",
        3
    )
    question_list.append(question2)

    question3 = question.Question(
        3,
        "Qual o nome do pé de mamão?",
        "Marmoraria",
        "Mamoeiro",
        "Marceneiro",
        "Mamona",
        2
    )
    question_list.append(question3)

    question4 = question.Question(
        4,
        "Quanto tempo um mamoeiro demora para florescer?",
        "1 dia após o plantio",
        "10 dias após o plantio",
        "100 anos após o plantio",
        "4 meses após o plantio",
        4
    )
    question_list.append(question4)

    question5 = question.Question(
        5,
        "Qual a melhor época do ano para o plantio do mamão?",
        "Qualquer época do ano",
        "Verão",
        "Outono",
        "Primavera",
        1
    )
    question_list.append(question5)

    question6 = question.Question(
        6,
        "Qual o estado brasileiro que mais produz mamão?",
        "Rio Grande do Sul",
        "Rio Grande do Norte",
        "Bahia",
        "Paraná",
        3
    )
    question_list.append(question6)

    question7 = question.Question(
        7,
        "Qual foi o maior exportador de mamão do mundo em 2016?",
        "Brasil",
        "Inglaterra",
        "Iraque",
        "México",
        4
    )
    question_list.append(question7)
    
    question8 = question.Question(
        8,
        "Qual dessas cidades teve a maior colheita de mamão do brasil em 2017?",
        "Prado - BA",
        "Londrina - PR",
        "Cambé - PR",
        "Paulo Afonso - BA",
        1
    )
    question_list.append(question8)

    question9 = question.Question(
        9,
        "Qual o país que mais importou mamão em 2016?",
        "Trinidad e Tobago",
        "Alemanha",
        "Índia",
        "Estados Unidos",
        4
    )
    question_list.append(question9)

    question10 = question.Question(
        10,
        "Quantas toneladas de mamão a cidade de londrina produziu em 2017?",
        "90 Toneladas",
        "1000 Toneladas",
        "82 Toneladas",
        "8 Toneladas",
        1
    )
    question_list.append(question10)

    return question_list

def main():

    score1 = 0
    score2 = 0
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    BUFSIZ = 2000

    udp_ip = sys.argv[1]    # ip para autenticacao
    udp_port = sys.argv[2]    # porta usada na trasnferencia
    server.bind((udp_ip, int(udp_port)))

    questions = set_questions()

    print("Aguardando jogadores...")

    server.listen()

    connp1, addr1 = server.accept()
    datap1 = connp1.recv(BUFSIZ)
    p1name = datap1.decode()

    print("Primeiro jogador,", p1name, 'conectado.')

    server.listen()

    connp2, addr2 = server.accept()
    datap2 = connp2.recv(BUFSIZ)
    p2name = datap2.decode()

    print("Segundo jogador,", p2name, 'conectado.')

    connp1.sendall("STARTGAME".encode())

    connp2.sendall("STARTGAME".encode())

    msg1 = connp1.recv(BUFSIZ)
    msg2 = connp2.recv(BUFSIZ)
    
    scorep1 = 0
    scorep2 = 0

    if msg1.decode() == "OK" and msg1 == msg2:
        for questao in questions:
            send_question(questao, connp1, connp2)
            ans1 = 10
            ans2 = 10
            
            socks = [connp1, connp2]
            
            av_sock, o, e = select.select(socks, [], [])
            
            ans1 = pickle.loads(av_sock[0].recv(2000))
            print("RESPOSTA", ans1[0] , "RECEBIDA DE", ans1[1], "EM", ans1[2])
            
            if ans1[1] == p1name:
                resp1 = ans1[0]
                tempop1 = ans1[2]
            else:
                resp2 = ans1[0]
                tempop2 = ans1[2]
            
            av_sock, o, e = select.select(socks, [], [])
            
            ans2 = pickle.loads(av_sock[0].recv(2000))
            print("RESPOSTA", ans2[0] , "RECEBIDA DE", ans2[1], "EM", ans2[2])
            
            if ans2[1] == p1name:
                resp1 = ans2[0]
                tempop1 = ans2[2]
            else:
                resp2 = ans2[0]
                tempop2 = ans2[2]
            
            if int(resp1) == int(questao.rightAns):
                print(p1name, "acertou")
                scorep1 += 10000 - tempop1 * 1000
            else:
                print(p1name, "errou")
 
            if int(resp2) == int(questao.rightAns):
                print(p2name, "acertou")
                scorep1 += 10000 - tempop2 * 1000
            else:
                print(p2name, "errou")
    
    stringfim = "FIM DE JOGO!\n O Vencedor foi "
    
    if scorep1 > scorep2:
        stringfim += p1name + " com " + str(scorep1) + " pontos!"
    if scorep2 > scorep1:
        stringfim += p2name + " com " + str(scorep2) + " pontos!"
    if scorep2 == scorep1:
        stringfim += "NINGUEM!!! houve um empate!"
    
    connp1.sendall("FIM".encode())
    connp2.sendall("FIM".encode())
    
    msg1 = connp1.recv(2000)
    msg2 = connp2.recv(2000)
    
    if msg1 == msg2 and msg1.decode() == "FIMRECEBIDO":
        connp1.sendall(stringfim.encode())
        connp2.sendall(stringfim.encode())
        
    
    
    
    # Envia aos dois que o jogo vai começar, espera a resposta dos dois.
    # Enquanto houver perguntas, continua as enviando e contabilizando pontuação.
    # Senão, apresenta aos dois a tela de fim de jogo.


main()
