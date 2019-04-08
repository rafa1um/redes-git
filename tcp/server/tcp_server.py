import socket


server = socket.socket()

print("HOST: ", end='')
tcp_ip = input()    # ip para autenticacao
print("PORT: ", end='')
tcp_port = input()    # porta usada na trasnferencia
BUFSIZ = 100
server.bind((tcp_ip, int(tcp_port)))
f = open('transferred-file.jpeg', 'wb')
# cria um arquivo que sera escrito com os dados do arquivo recebido
server.listen(5)    # servidor aguarda uma conexao
i = 1

while True:     # loop infinito
    conn, addr = server.accept()    # estabelece conexao com o client
    print(addr, "Conectou-se")
    print("Recebendo...")
    l = conn.recv(BUFSIZ)
    # recebe os primeiros BUFSIZ bytes enviados pelo client
    while(l):
        print("Recebido o pacote", i)
        f.write(l)
        l = conn.recv(BUFSIZ)
        i += 1
        # recebe os proximos BUFSIZ bytes enviados pelo client
    f.close()   # fecha o arquivo
    print("Recebido!")
    print("Quantidade de bytes recebidos:", BUFSIZ * (i - 1))
    print("Taxa de transferencia:", ((BUFSIZ * (i - 1) * 8) / 60), "bits/s")

    conn.close()    # fecha a conexao
    break   # quebra o loop
