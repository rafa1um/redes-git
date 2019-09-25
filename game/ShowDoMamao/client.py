from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import formPerguntas
import time
import socket
import pickle


class Client(QtWidgets.QMainWindow, formPerguntas.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Client, self).__init__(parent)
        self.setupUi(self)
        self.checkArgs()
        self.playerName = sys.argv[1]
        self.ipAddr = sys.argv[2]
        self.portConnect = int(sys.argv[3])
        self.con = self.connectToServer(self.playerName, self.ipAddr, self.portConnect)
        self.startGame(self.con)

    def enviaResposta(self, con):
        time_start = time.clock()
        if self.buttonResposta1.isChecked():
            resposta = 1
        elif self.buttonResposta2.isChecked():
            resposta = 2
        elif self.buttonResposta3.isChecked():
            resposta = 3
        elif self.buttonResposta4.isChecked():
             resposta = 4
        print("Respondeu", resposta)

    def checkArgs(self):
        if len(sys.argv) != 4:
            print("Uso: python client.py nome ip porta")
            quit()

    def connectToServer(self, playerName, ipAddr, portConnect):
        tcpConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destAddr = (ipAddr, portConnect)
        try:
            tcpConnection.connect(destAddr)
            tcpConnection.sendall(playerName.encode())
        except Exception:
            print("Não foi possível conectar-se ao servidor.")
            quit()

        return tcpConnection

    def startGame(self, con):
        data = con.recv(2000)
        if data.decode() == "STARTGAME":
            con.sendall("OK".encode())
        qst = con.recv(2000)
        self.labelPergunta.setText(pickle.loads(qst).questionText)
        self.buttonResposta1.setText(pickle.loads(qst).ans1)


def main():
    app = QApplication(sys.argv)
    form = Client()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
