# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(910, 600)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.528409, y1:0.454, x2:1, y2:1, stop:0.0511364 rgba(0, 0, 107, 255), stop:1 rgba(0, 0, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(83, 30, 1200, 90))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 220, 750, 90))
        font1 = QFont()
        font1.setPointSize(14)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;\n"
"padding: 10px;")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(310, 380, 750, 90))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;\n"
"padding: 10px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(590, 540, 250, 90))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #fff;\n"
"border-radius: 20px;")
        self.pushButton.setIconSize(QSize(24, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Jogador", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Jogador 1", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Jogador 2", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Jogar", None))
    # retranslateUi

