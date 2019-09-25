from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import formPerguntas
import time



class Client(QtWidgets.QMainWindow, formPerguntas.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Client, self).__init__(parent)
        self.setupUi(self)
        self.botaoEnviar.clicked.connect(self.enviaResposta)

    def enviaResposta(self):
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


def main():
    app = QApplication(sys.argv)
    form = Client()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
