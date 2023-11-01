# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jogoeuzawow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_Jogo(object):
    def setupUi(self, Jogo):
        if not Jogo.objectName():
            Jogo.setObjectName(u"Jogo")
        Jogo.resize(1366, 768)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(24)
        Jogo.setFont(font)
        self.centralwidget = QWidget(Jogo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(150, 20, 1055, 90))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(36)
        self.titulo.setFont(font1)
        self.titulo.setStyleSheet(u"border-radius: 20px;\n"
"background: #D9D9D9;")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.dica1 = QWidget(self.centralwidget)
        self.dica1.setObjectName(u"dica1")
        self.dica1.setEnabled(True)
        self.dica1.setGeometry(QRect(30, 206, 1135, 90))
        self.dica1_pontos = QLabel(self.dica1)
        self.dica1_pontos.setObjectName(u"dica1_pontos")
        self.dica1_pontos.setGeometry(QRect(0, 0, 90, 90))
        self.dica1_pontos.setFont(font1)
        self.dica1_pontos.setStyleSheet(u"border-radius: 20px;\n"
"background: #d9d9d9;")
        self.dica1_pontos.setAlignment(Qt.AlignCenter)
        self.dica1_label = QLabel(self.dica1)
        self.dica1_label.setObjectName(u"dica1_label")
        self.dica1_label.setGeometry(QRect(110, 0, 1025, 90))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(20)
        self.dica1_label.setFont(font2)
        self.dica1_label.setStyleSheet(u"border-radius: 20px;\n"
"background: #d9d9d9;")
        self.dica1_label.setMargin(20)
        self.pontuacao_p1 = QLabel(self.centralwidget)
        self.pontuacao_p1.setObjectName(u"pontuacao_p1")
        self.pontuacao_p1.setGeometry(QRect(30, 20, 90, 90))
        self.pontuacao_p1.setFont(font1)
        self.pontuacao_p1.setStyleSheet(u"border-radius: 20px;\n"
"background: #D9D9D9;")
        self.pontuacao_p1.setAlignment(Qt.AlignCenter)
        self.pontuacao_p2 = QLabel(self.centralwidget)
        self.pontuacao_p2.setObjectName(u"pontuacao_p2")
        self.pontuacao_p2.setGeometry(QRect(1235, 20, 90, 90))
        self.pontuacao_p2.setFont(font1)
        self.pontuacao_p2.setStyleSheet(u"border-radius: 20px;\n"
"background: #D9D9D9;")
        self.pontuacao_p2.setAlignment(Qt.AlignCenter)
        self.dica2 = QWidget(self.centralwidget)
        self.dica2.setObjectName(u"dica2")
        self.dica2.setEnabled(True)
        self.dica2.setGeometry(QRect(110, 325, 1135, 90))
        self.dica2_pontos = QLabel(self.dica2)
        self.dica2_pontos.setObjectName(u"dica2_pontos")
        self.dica2_pontos.setGeometry(QRect(0, 0, 90, 90))
        self.dica2_pontos.setFont(font1)
        self.dica2_pontos.setStyleSheet(u"border-radius: 20px;\n"
"background: #d9d9d9;")
        self.dica2_pontos.setAlignment(Qt.AlignCenter)
        self.dica2_label = QLabel(self.dica2)
        self.dica2_label.setObjectName(u"dica2_label")
        self.dica2_label.setGeometry(QRect(110, 0, 1025, 90))
        self.dica2_label.setFont(font2)
        self.dica2_label.setStyleSheet(u"border-radius: 20px;\n"
"background: #d9d9d9;")
        self.dica2_label.setMargin(20)
        self.dica3 = QWidget(self.centralwidget)
        self.dica3.setObjectName(u"dica3")
        self.dica3.setEnabled(True)
        self.dica3.setGeometry(QRect(190, 441, 1135, 90))
        self.dica3_pontos = QLabel(self.dica3)
        self.dica3_pontos.setObjectName(u"dica3_pontos")
        self.dica3_pontos.setGeometry(QRect(0, 0, 90, 90))
        self.dica3_pontos.setFont(font1)
        self.dica3_pontos.setStyleSheet(u"border-radius: 20px;\n"
"background: #d9d9d9;")
        self.dica3_pontos.setAlignment(Qt.AlignCenter)
        self.dica3_label = QLabel(self.dica3)
        self.dica3_label.setObjectName(u"dica3_label")
        self.dica3_label.setGeometry(QRect(110, 0, 1025, 90))
        self.dica3_label.setFont(font2)
        self.dica3_label.setStyleSheet(u"border-radius: 20px;\n"
"background: #d9d9d9;")
        self.dica3_label.setMargin(20)
        self.input_resposta = QLineEdit(self.centralwidget)
        self.input_resposta.setObjectName(u"input_resposta")
        self.input_resposta.setGeometry(QRect(30, 628, 1020, 90))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_resposta.sizePolicy().hasHeightForWidth())
        self.input_resposta.setSizePolicy(sizePolicy)
        self.input_resposta.setFont(font2)
        self.input_resposta.setStyleSheet(u"border-radius: 20px;\n"
"background: #d9d9d9;")
        self.input_resposta.setMaxLength(100)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1070, 628, 255, 90))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(28)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background: #d9d9d9;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #d6d6d6;\n"
"}")
        Jogo.setCentralWidget(self.centralwidget)

        self.retranslateUi(Jogo)

        QMetaObject.connectSlotsByName(Jogo)
    # setupUi

    def retranslateUi(self, Jogo):
        Jogo.setWindowTitle(QCoreApplication.translate("Jogo", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("Jogo", u"Titulo Massa Wow", None))
        self.dica1_pontos.setText(QCoreApplication.translate("Jogo", u"10", None))
        self.dica1_label.setText(QCoreApplication.translate("Jogo", u"Lorem Impsum Dolor Dotrume", None))
        self.pontuacao_p1.setText(QCoreApplication.translate("Jogo", u"100", None))
        self.pontuacao_p2.setText(QCoreApplication.translate("Jogo", u"100", None))
        self.dica2_pontos.setText(QCoreApplication.translate("Jogo", u"9", None))
        self.dica2_label.setText(QCoreApplication.translate("Jogo", u"Neymar Messi Cristiano Ronaldo", None))
        self.dica3_pontos.setText(QCoreApplication.translate("Jogo", u"8", None))
        self.dica3_label.setText(QCoreApplication.translate("Jogo", u"Botafogo Palmeiras Santos Corinthians Coritiba", None))
        self.pushButton.setText(QCoreApplication.translate("Jogo", u"N\u00e3o Sei", None))
    # retranslateUi

