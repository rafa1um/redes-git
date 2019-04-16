import socket
import time
import os
import datetime
import sys

BUFSIZ = 100   # quantidade de bytes que será enviado por vez
packet_count = 1  # contador de pacotes
server = socket.socket()    # cria um socket


def send_packets(f, l, size):
        global packet_count
        global server
        for i in range(0, size):
                print("Enviando pacote ", packet_count, "...")
                server.sendall(l)
                l = f.read(BUFSIZ)
                if not l:
                        break
                else:  
                        packet_count += 1
                        
        return l


def main():
        global count_loop
        count_loop = 0  # contador de loops
        tcp_ip = sys.argv[1]    # ip para autenticacao
        tcp_port = sys.argv[2]    # porta usada na trasnferencia
        server.connect((tcp_ip, int(tcp_port)))  # faz a conexao com ip e porta
        print("Informe o nome do arquivo a ser enviado: ", end='')
        file = input()  # entrada do nome do arquivo   
        server.sendall(file.encode())
        print("Enviando o arquivo", file, "...")
        f = open(file, 'rb')   # abre arquivo que sera enviado
        l = f.read(BUFSIZ)  # le os primeiros BUFSIZ bytes do arquivo (100 bytes)
        start = datetime.datetime.now()
        while(l):   # enquanto nao for final do arquivo, continua o loop
                l = send_packets(f, l, 2)  # enviando 6 pacotes
        f.close()   # fecha o arquivo
        # envia uma notificacao de desligamento para o servidor
        server.shutdown(socket.SHUT_RDWR)
        server.close()  # fecha a conexao
        end = datetime.datetime.now()
        td = end - start
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        seconds += td.microseconds / 1e6
        print("Enviados", packet_count, "pacotes em", hours, 'horas, ', minutes, 'minutos e' ,seconds, "segundos!")
        size = os.path.getsize('../client/%s'% file)
        print("Quantidade de bytes enviados:", size, 'ou ',
              (size * 8), 'bits')
        print("Taxa de transferencia:",
              (size / td.total_seconds()) * 8, "bits/s")


if __name__ == "__main__":
    main()
