import question
import socket
import sys
import pickle


def send_question(questao, addr1, addr2, server):

    server.sendto(pickle.dumps(questao), addr1)
    server.sendto(pickle.dumps(questao), addr2)

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

    question11 = question.Question(
        11,
        "FIM",
        "-",
        "-",
        "-",
        "-",
        0
    )
    question_list.append(question11)

    return question_list

def main():

    score1 = 0
    score2 = 0
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    BUFSIZ = 2000

    udp_ip = sys.argv[1]    # ip para autenticacao
    udp_port = sys.argv[2]    # porta usada na trasnferencia
    server.bind((udp_ip, int(udp_port)))

    questions = set_questions()

    print("Aguardando jogadores...")

    datap1, addr1 = server.recvfrom(BUFSIZ)

    print("Primeiro jogador,", datap1.decode(), 'conectado.')

    datap2, addr2 = server.recvfrom(BUFSIZ)

    print("Segundo jogador,", datap2.decode(), 'conectado.')

    server.sendto("STARTGAME".encode(), addr1)

    server.sendto("STARTGAME".encode(), addr2)

    msg1 = server.recv(BUFSIZ)
    msg2 = server.recv(BUFSIZ)

    if msg1.decode() == "OK" and msg1 == msg2:
        for questao in questions:
            send_question(questao, addr1, addr2, server)
            dataAns1, addrAns1 = server.recvfrom(BUFSIZ)
            dataAns2, addrAns2 = server.recvfrom(BUFSIZ)

            if addrAns1 == addr1:
                respostap1 = pickle.loads(dataAns1)
                respostap2 = pickle.loads(dataAns2)
            else:
                respostap1 = pickle.loads(dataAns2)
                respostap2 = pickle.loads(dataAns1)

            if int(respostap1[1]) == int(questao.rightAns):
                score1 += 10000 - respostap1[0]
                server.sendto("Voce acertou!".encode(), addr1)
            elif int(respostap1[1]) != 0:
                server.sendto("Voce errou ):".encode(), addr1)
                # envia msg pro p1 de q ele errou
            elif int(respostap1[1]) == 0:
                server.sendto("Seu tempo se esgotou ):".encode(), addr1)
            
            if int(respostap2[1]) == int(questao.rightAns):
                score2 += 10000 - respostap2[0]
                server.sendto("Voce acertou".encode(), addr2)
            elif int(respostap2[1]) != 0:
                server.sendto("Voce errou ):".encode(), addr2)
                # envia msg pro p2 q ele errou
            elif int(respostap2[1]) == 0:
                server.sendto("Seu tempo se esgotou ):".encode(), addr2)
    # Envia aos dois que o jogo vai começar, espera a resposta dos dois.
    # Enquanto houver perguntas, continua as enviando e contabilizando pontuação.
    # Senão, apresenta aos dois a tela de fim de jogo.


main()
