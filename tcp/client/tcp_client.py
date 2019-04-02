import socket
import time


def send_packets(l, size):
        for i in range(0,size-1):
                server.sendall(l)
                packet_count += 1
                l = f.read(BUFSIZ)
                if not l:
                        break
                i += 1
        print(i)

server = socket.socket()    # cria um socket
print("HOST: ", end='')
tcp_ip = input()    # ip para autenticacao
print("PORT: ", end='')
tcp_port = input()    # porta usada na trasnferencia
BUFSIZ = 100   # quantidade de bytes que será enviado por vez
count_loop = 0
packet_count = 0
server.connect((tcp_ip, int(tcp_port)))  # faz a conexao com ip e porta


print("Informe o nome do arquivo a ser enviado: ", end='')
file = input()  # entrada do nome do arquivo
print("Enviando o arquivo", file, "...")
f = open(file, 'rb')   # abre arquivo que sera enviado
l = f.read(BUFSIZ)  # le os primeiros BUFSIZ bytes do arquivo (1024 bytes)
count_loop += 1

while(l):   # enquanto nao for final do arquivo, continua o loop
        print("Enviando...")
        send_packets(l, 6)  # enviando 6 pacotes
        count_loop += 1  # quantidade de tempo
        time.sleep(0.02)  # tempo de espera
f.close()   # fecha o arquivo
print("Enviado!")
server.shutdown(socket.SHUT_RDWR)
# envia uma notificacao de desligament para o servidor
server.close()  # fecha a conexao
