import socket


server = socket.socket()

tcp_ip = 'localhost'
tcp_port = 33000
BUFSIZ = 1024
server.bind((tcp_ip, tcp_port))
f = open('ince.jpeg', 'wb')
# cria um arquivo que sera escrito com os dados do arquivo recebido
server.listen(5)    # servidor aguarda uma conexao

while True:     # loop infinito
    conn, addr = server.accept()    # estabelece conexao com o client
    print(addr, "Conectou-se")
    print("Recebendo...")
    l = conn.recv(BUFSIZ)
    # recebe os primeiros BUFSIZ bytes enviados pelo client
    while(l):
        print("Recebendo arquivo...")
        f.write(l)
        l = conn.recv(BUFSIZ)
        # recebe os proximos BUFSIZ bytes enviados pelo client
    f.close()   # fecha o arquivo
    print("Recebido!")
    finConn = "Conexão finalizada!"
    conn.sendall(finConn.encode('utf-8'))
    # avisa que a conexao finalizou (nao ta funcionando)
    conn.close()    # fecha a conexao
    break   # quebra o loop
