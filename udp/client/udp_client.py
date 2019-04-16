import socket
import time
import os
import datetime
import sys

BUFSIZ = 200   # quantidade de bytes que será enviado por vez
packet_count = 1  # contador de pacotes
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # cria um socket


def send_packets(f, data, size):
        global packet_count
        global server
        for i in range(0, size):
                data = f.read(BUFSIZ)
                if not data:
                        break
                else:  
                        packet_count += 1
                        
        return data


def main():
        global count_loop
        count_loop = 0  # contador de loops
        udp_ip = sys.argv[1]    # ip para autenticacao
        udp_port = sys.argv[2]    # porta usada na trasnferencia
        file_name = sys.argv[3]
        server.sendto((file_name).encode(), (udp_ip.encode(), int(udp_port)))
        print("Enviando o arquivo", file_name, "...")
        f = open(file_name, 'rb')   # abre arquivo que sera enviado
        data = f.read(BUFSIZ)  # le os primeiros BUFSIZ bytes do arquivo (100 bytes)
        start = datetime.datetime.now()
        while(data):   # enquanto nao for final do arquivo, continua o loop
                if(server.sendto(data, (udp_ip.encode(), int(udp_port)))):
                        data = f.read(BUFSIZ)  # enviando 6 pacotes
                        time.sleep(0.02)  # tempo de espera
        f.close()   # fecha o arquivo
        # envia uma notificacao de desligamento para o servidor


        #     -------------  non-relevant area (closes and prints)------------------

        server.close()  # fecha a conexao
        end = datetime.datetime.now()
        td = end - start
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        seconds += td.microseconds / 1e6
        print("Enviados", packet_count, "pacotes em", hours, 'horas, ', minutes, 'minutos e' ,seconds, "segundos!")
        size = os.path.getsize('../client/%s'% file_name)
        print("Quantidade de bytes enviados:", size, 'ou ',
              (size * 8), 'bits')
        print("Taxa de transferencia:",
              (size / td.total_seconds()) * 8, "bits/s")


if __name__ == "__main__":
    main()