import question

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

    
    questions = set_questions()
    # Aguarda as duas conexões.
    # Envia aos dois que o jogo vai começar, espera a resposta dos dois.
    # Enquanto houver perguntas, continua as enviando e contabilizando pontuação.
    # Senão, apresenta aos dois a tela de fim de jogo.


main()
