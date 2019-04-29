import socket
import os
import datetime
import sys

server = socket.socket()

tcp_ip = sys.argv[1]    # ip para autenticacao
tcp_port = sys.argv[2]    # porta usada na trasnferencia
BUFSIZ = 2000
server.bind((tcp_ip, int(tcp_port)))
# cria um arquivo que sera escrito com os dados do arquivo recebido
server.listen(5)    # servidor aguarda uma conexao
i = 1
file = 0

while True:     # loop infinito
    conn, addr = server.accept()    # estabelece conexao com o client
    print(addr, "Conectou-se")
    file = conn.recv(1024)
    f = open(file, 'wb')
    print("Recebendo...")
    l = conn.recv(BUFSIZ)
    start = datetime.datetime.now()
    conn.settimeout(0.04)
    # recebe os primeiros BUFSIZ bytes enviados pelo client
    while(l):
        print("Recebido o pacote", i)
        f.write(l)
        l = conn.recv(BUFSIZ)
        i += 1
        # recebe os proximos BUFSIZ bytes enviados pelo client
    conn.settimeout(None)
    f.close()   # fecha o arquivo
    print("Recebido!")

    conn.close()    # fecha a conexao
    end = datetime.datetime.now()
    td = end - start
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    seconds += td.microseconds / 1e6

    size = os.path.getsize(file)
    print("Quantidade de bytes recebidos:",  size, 'em ', hours,
          'horas, ', minutes, 'minutos e', seconds, "segundos!")
    print("A taxa de recebimento foi de ", (size/td.total_seconds()) * 8, "bits/s")
    break   # quebra o loop
