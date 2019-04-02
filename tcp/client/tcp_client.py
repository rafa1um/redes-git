import socket

server = socket.socket()    # cria um socket
tcp_ip = 'localhost'    # ip para autenticacao
tcp_port = 33000    # porta usada na trasnferencia
BUFSIZ = 1024   # quantidade de bytes que será enviado por vez
server.connect((tcp_ip, tcp_port))  # faz a conexao com ip e porta
file = input()
f = open(file, 'rb')   # abre arquivo que sera enviado
l = f.read(BUFSIZ)  # le os primeiros BUFSIZ bytes do arquivo (1024 bytes)

while(l):   # enquanto nao for final do arquivo, continua o loop
        print("Enviando...")
        server.sendall(l)   # envia os bytes lidos para o servidor
        l = f.read(BUFSIZ)  # le os proximos BUFSIZ bytes do arquivo
f.close()   # fecha o arquivo
print("Enviado!")
server.shutdown(socket.SHUT_RDWR)
# envia uma notificacao de desligament para o servidor
server.close()  # fecha a conexao
