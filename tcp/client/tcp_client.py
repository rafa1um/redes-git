import socket
import time

BUFSIZ = 100   # quantidade de bytes que será enviado por vez
packet_count = 0  # contador de pacotes
server = socket.socket()    # cria um socket


def send_packets(f, l, size):
        global packet_count
        global server
        for i in range(0,size):
                print("Enviando pacote ", packet_count, "...")
                server.sendall(l)
                packet_count += 1
                l = f.read(BUFSIZ)
                if not l:
                        break
        return l


def main(): 
        global count_loop
        count_loop = 0  # contador de loops
        print("HOST: ", end='')
        tcp_ip = input()    # ip para autenticacao
        print("PORT: ", end='')
        tcp_port = input()    # porta usada na trasnferencia
        server.connect((tcp_ip, int(tcp_port)))  # faz a conexao com ip e porta
        print("Informe o nome do arquivo a ser enviado: ", end='')
        file = input()  # entrada do nome do arquivo
        print("Enviando o arquivo", file, "...")
        f = open(file, 'rb')   # abre arquivo que sera enviado
        l = f.read(BUFSIZ)  # le os primeiros BUFSIZ bytes do arquivo (1024 bytes)
        count_loop += 1
        while(l):   # enquanto nao for final do arquivo, continua o loop
                l = send_packets(f, l, 6)  # enviando 6 pacotes
                count_loop += 1  # quantidade de tempo
                time.sleep(0.02)  # tempo de espera
        f.close()   # fecha o arquivo
        print("Enviados", packet_count, "pacotes em", count_loop*0.02, "segundos!")
        server.shutdown(socket.SHUT_RDWR)
        # envia uma notificacao de desligament para o servidor
        server.close()  # fecha a conexao


if __name__ == "__main__":
    main()
