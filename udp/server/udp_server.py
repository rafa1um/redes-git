import socket
import os
import datetime
import sys
import select

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_ip = sys.argv[1]    # ip para autenticacao
udp_port = sys.argv[2]    # porta usada na trasnferencia
BUFSIZ = 100
server.bind((udp_ip, int(udp_port)))
# cria um arquivo que sera escrito com os dados do arquivo recebido
i = 1
timeout = 3

while True:     # loop infinito
    data, addr = server.recvfrom(BUFSIZ)    # estabelece conexao com o client
    if data:
        file_name = data.strip()
    start = datetime.datetime.now()
    f = open(file_name, 'wb')
    print("Recebendo...")
    # recebe os primeiros BUFSIZ bytes enviados pelo client
    while True:
        ready = select.select([server], [], [], timeout)
        if ready[0]:
            print("Recebido o pacote", i)
            data, addr = server.recvfrom(BUFSIZ)
            f.write(data)  
            i += 1
        else:
            print("Recebido!")
            f.close()
            break
        # recebe os proximos BUFSIZ bytes enviados pelo client

#   ---------------non-relevant area (closes and prints) ----------------------

    end = datetime.datetime.now()
    td = end - start
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    seconds += td.microseconds / 1e6

    size = os.path.getsize(file_name)
    print("Quantidade de bytes recebidos:",  size, 'em ', hours,
          'horas, ', minutes, 'minutos e', seconds, "segundos!")
    print("A taxa de recebimento foi de ", (size/td.total_seconds()) * 8, "bits/s")
    break   # quebra o loop
