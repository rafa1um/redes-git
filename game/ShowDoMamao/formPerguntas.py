# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formPerguntas.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelPergunta = QtWidgets.QLabel(self.centralwidget)
        self.labelPergunta.setGeometry(QtCore.QRect(30, 30, 461, 41))
        self.labelPergunta.setObjectName("labelPergunta")
        self.buttonResposta1 = QtWidgets.QRadioButton(self.centralwidget)
        self.buttonResposta1.setGeometry(QtCore.QRect(30, 100, 341, 17))
        self.buttonResposta1.setObjectName("buttonResposta1")
        self.buttonResposta2 = QtWidgets.QRadioButton(self.centralwidget)
        self.buttonResposta2.setGeometry(QtCore.QRect(30, 160, 401, 17))
        self.buttonResposta2.setObjectName("buttonResposta2")
        self.buttonResposta3 = QtWidgets.QRadioButton(self.centralwidget)
        self.buttonResposta3.setGeometry(QtCore.QRect(30, 220, 431, 17))
        self.buttonResposta3.setObjectName("buttonResposta3")
        self.buttonResposta4 = QtWidgets.QRadioButton(self.centralwidget)
        self.buttonResposta4.setGeometry(QtCore.QRect(30, 280, 451, 17))
        self.buttonResposta4.setObjectName("buttonResposta4")
        self.botaoEnviar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEnviar.setGeometry(QtCore.QRect(420, 330, 75, 23))
        self.botaoEnviar.setObjectName("botaoEnviar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show do Mamao"))
        self.labelPergunta.setText(_translate("MainWindow", "Pergunta"))
        self.buttonResposta1.setText(_translate("MainWindow", "Resposta 1"))
        self.buttonResposta2.setText(_translate("MainWindow", "Respsta 2"))
        self.buttonResposta3.setText(_translate("MainWindow", "Resposta 3"))
        self.buttonResposta4.setText(_translate("MainWindow", "Resposta 4"))
        self.botaoEnviar.setText(_translate("MainWindow", "Enviar"))
