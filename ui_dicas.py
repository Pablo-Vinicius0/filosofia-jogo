# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\jogoeuzawow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from variables import window_icon_path
from PyQt5.QtWidgets import QMessageBox


class Ui_Jogo(object):
    def setupUi(self, Jogo):
        Jogo.setObjectName("Jogo")
        Jogo.setFixedSize(1366, 768)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        Jogo.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Jogo)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(150, 20, 1055, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("border-radius: 20px;\n"
"background: #D9D9D9;")
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.turno = QtWidgets.QLabel(self.centralwidget)
        self.turno.setGeometry(QtCore.QRect(499, 132, 368, 40))
        font.setPointSize(24)
        self.turno.setFont(font)
        self.turno.setAlignment(QtCore.Qt.AlignCenter)
        self.turno.setObjectName("turno")
        self.dica1 = QtWidgets.QWidget(self.centralwidget)
        self.dica1.setEnabled(True)
        self.dica1.setGeometry(QtCore.QRect(30, 206, 1135, 90))
        self.dica1.setObjectName("dica1")
        self.dica1_pontos = QtWidgets.QLabel(self.dica1)
        self.dica1_pontos.setGeometry(QtCore.QRect(0, 0, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        self.dica1_pontos.setFont(font)
        self.dica1_pontos.setStyleSheet("border-radius: 20px;\n"
"background: #d9d9d9;")
        self.dica1_pontos.setAlignment(QtCore.Qt.AlignCenter)
        self.dica1_pontos.setObjectName("dica1_pontos")
        self.dica1_label = QtWidgets.QLabel(self.dica1)
        self.dica1_label.setGeometry(QtCore.QRect(110, 0, 1025, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.dica1_label.setFont(font)
        self.dica1_label.setStyleSheet("border-radius: 20px;\n"
"background: #d9d9d9; padding-left: 15px")
        self.dica1_label.setObjectName("dica1_label")
        self.pontuacao_p1 = QtWidgets.QLabel(self.centralwidget)
        self.pontuacao_p1.setGeometry(QtCore.QRect(30, 20, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        self.pontuacao_p1.setFont(font)
        self.pontuacao_p1.setStyleSheet("border-radius: 20px;\n"
"background: #D9D9D9;")
        self.pontuacao_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.pontuacao_p1.setObjectName("pontuacao_p1")
        self.pontuacao_p1_label = QtWidgets.QLabel(self.centralwidget)
        self.pontuacao_p1_label.setGeometry(QtCore.QRect(30, 119, 90, 20))
        font.setPointSize(16)
        self.pontuacao_p1_label.setFont(font)
        self.pontuacao_p1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pontuacao_p1_label.setObjectName("pontuacao_p1_label")
        self.pontuacao_p2 = QtWidgets.QLabel(self.centralwidget)
        self.pontuacao_p2.setGeometry(QtCore.QRect(1235, 20, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        self.pontuacao_p2.setFont(font)
        self.pontuacao_p2.setStyleSheet("border-radius: 20px;\n"
"background: #D9D9D9;")
        self.pontuacao_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.pontuacao_p2.setObjectName("pontuacao_p2")
        self.pontuacao_p2_label = QtWidgets.QLabel(self.centralwidget)
        self.pontuacao_p2_label.setGeometry(QtCore.QRect(1235, 119, 90, 20))
        font.setPointSize(16)
        self.pontuacao_p2_label.setFont(font)
        self.pontuacao_p2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pontuacao_p2_label.setObjectName("pontuacao_p2_label")
        self.dica2 = QtWidgets.QWidget(self.centralwidget)
        self.dica2.setEnabled(True)
        self.dica2.setGeometry(QtCore.QRect(110, 325, 1135, 90))
        self.dica2.setObjectName("dica2")
        self.dica2_pontos = QtWidgets.QLabel(self.dica2)
        self.dica2_pontos.setGeometry(QtCore.QRect(0, 0, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        self.dica2_pontos.setFont(font)
        self.dica2_pontos.setStyleSheet("border-radius: 20px;\n"
"background: #d9d9d9;")
        self.dica2_pontos.setAlignment(QtCore.Qt.AlignCenter)
        self.dica2_pontos.setObjectName("dica2_pontos")
        self.dica2_label = QtWidgets.QLabel(self.dica2)
        self.dica2_label.setGeometry(QtCore.QRect(110, 0, 1025, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.dica2_label.setFont(font)
        self.dica2_label.setStyleSheet("border-radius: 20px;\n"
"background: #d9d9d9; padding-left: 15px")
        self.dica2_label.setObjectName("dica2_label")
        self.dica3 = QtWidgets.QWidget(self.centralwidget)
        self.dica3.setEnabled(True)
        self.dica3.setGeometry(QtCore.QRect(190, 441, 1135, 90))
        self.dica3.setObjectName("dica3")
        self.dica3_pontos = QtWidgets.QLabel(self.dica3)
        self.dica3_pontos.setGeometry(QtCore.QRect(0, 0, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        self.dica3_pontos.setFont(font)
        self.dica3_pontos.setStyleSheet("border-radius: 20px;\n"
"background: #d9d9d9;")
        self.dica3_pontos.setAlignment(QtCore.Qt.AlignCenter)
        self.dica3_pontos.setObjectName("dica3_pontos")
        self.dica3_label = QtWidgets.QLabel(self.dica3)
        self.dica3_label.setGeometry(QtCore.QRect(110, 0, 1025, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.dica3_label.setFont(font)
        self.dica3_label.setStyleSheet("border-radius: 20px;\n"
"background: #d9d9d9; padding-left: 15px")
        self.dica3_label.setObjectName("dica3_label")
        self.input_resposta = QtWidgets.QLineEdit(self.centralwidget)
        self.input_resposta.setGeometry(QtCore.QRect(30, 628, 1020, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_resposta.sizePolicy().hasHeightForWidth())
        self.input_resposta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.input_resposta.setFont(font)
        self.input_resposta.setStyleSheet("border-radius: 20px;\n"
"background: #d9d9d9; padding-left: 30px")
        self.input_resposta.setMaxLength(100)
        self.input_resposta.setPlaceholderText("Resposta")
        self.input_resposta.setObjectName("input_resposta")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1070, 628, 255, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background: #d9d9d9;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #d6d6d6;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(977, 648, 50, 50))
        ico = QIcon(str(window_icon_path))
        font = QtGui.QFont()
        self.sendButton.setIcon(ico)
        size = QtCore.QSize(50, 50)
        self.sendButton.setIconSize(size)
        font.setFamily("Consolas")
        font.setPointSize(28)
        self.sendButton.setStyleSheet('background: transparent;')
        self.sendButton.setFont(font)
        self.sendButton.setObjectName('sendButton')
        self.input_resposta.setPlaceholderText('Resposta')
                
        Jogo.setCentralWidget(self.centralwidget)

        self.retranslateUi(Jogo)
        QtCore.QMetaObject.connectSlotsByName(Jogo)

    def retranslateUi(self, Jogo):
        _translate = QtCore.QCoreApplication.translate
        Jogo.setWindowTitle(_translate("Jogo", "MainWindow"))
        self.titulo.setText(_translate("Jogo", "Titulo Massa Wow"))
        self.turno.setText(_translate("Jogo", "Vez de Mario")) # Pôr as variáveis dos jogadores
        self.dica1_pontos.setText(_translate("Jogo", "10"))
        self.dica1_label.setText(_translate("Jogo", "Pergunta 1"))
        self.pontuacao_p1.setText(_translate("Jogo", "0"))
        self.pontuacao_p1_label.setText(_translate("Jogo", "Mario"))
        self.pontuacao_p2.setText(_translate("Jogo", "0"))
        self.pontuacao_p2_label.setText(_translate("Jogo", "Junior"))
        self.dica2_pontos.setText(_translate("Jogo", "9"))
        self.dica2_label.setText(_translate("Jogo", "Pergunta 2"))
        self.dica3_pontos.setText(_translate("Jogo", "8"))
        self.dica3_label.setText(_translate("Jogo", "Pergunta 3"))
        self.pushButton.setText(_translate("Jogo", "Não Sei"))

def makeMsgBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Explicação')
        msgBox.setText('Explicação de que a mulher de Edgol vai sofrer, de acordo com Guigui. Ele também fala que a dedada de Durex é perigosa')
        msgBox.textFormat()
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()