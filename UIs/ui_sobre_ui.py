# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_sobre.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QWidget #centralwidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528409, y1:0.454, x2:1, y2:1, stop:0.0511364 rgba(0, 0, 107, 255), stop:1 rgba(0, 0, 255, 255));\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #FFF;\n"
"	background: transparent;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_sobre = QLabel(self.centralwidget)
        self.label_sobre.setObjectName(u"label_sobre")
        self.label_sobre.setGeometry(QRect(116, 60, 1135, 90))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(48)
        self.label_sobre.setFont(font1)
        self.label_sobre.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;")
        self.label_sobre.setAlignment(Qt.AlignCenter)
        self.label_tema = QLabel(self.centralwidget)
        self.label_tema.setObjectName(u"label_tema")
        self.label_tema.setGeometry(QRect(143, 250, 1101, 68))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(30)
        self.label_tema.setFont(font2)
        self.label_tema.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_tema.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(178, 473, 1011, 121))
        font3 = QFont()
        font3.setPointSize(22)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(448, 380, 471, 41))
        font4 = QFont()
        font4.setPointSize(23)
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"")
        self.label_11.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_tema.setText(QCoreApplication.translate("MainWindow", u"A virtude e a felicidade para Arist\u00f3teles e S\u00eaneca", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Alunos: Caio Cabral,  Gloria Maria,  Gabriel Santos,  Italo Gabriel,  Marcelo Esa\u00fa,\n"
"Pablo Vin\u00edcius, Samuel L\u00e1zaro", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Professora: Euza Raquel de Sousa", None))
    # retranslateUi

