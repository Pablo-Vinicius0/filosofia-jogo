# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_final.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)

class Ui_FinalWindow(object):
    def setupUi(self, FinalWindow):
        if not FinalWindow.objectName():
            FinalWindow.setObjectName(u"FinalWindow")
        FinalWindow.resize(1366, 768)
        FinalWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(FinalWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel {color: #fff;}\n"
"\n"
"#player1Widget  {\n"
"	border: 2px solid #fff;	\n"
"	background: qlineargradient(spread:pad, x1:0.523, y1:0, x2:0.625, y2:1, stop:0.5 rgba(9, 36, 126, 176), stop:1 rgba(0, 0, 0, 189));\n"
"}\n"
"\n"
"#player2Widget  {\n"
"	border: 2px solid #fff;	\n"
"	background: qlineargradient(spread:pad, x1:0.523, y1:0, x2:0.625, y2:1, stop:0.5 rgba(9, 36, 126, 176), stop:1 rgba(0, 0, 0, 189));\n"
"}\n"
"\n"
"\n"
"#tituloLabel {\n"
"	background: qlineargradient(spread:pad, x1:0.591273, y1:1, x2:0.511363, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"	border-radius: 30px;\n"
"	border: 4px solid #fff;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background: qlineargradient(spread:pad, x1:0.591273, y1:1, x2:0.511363, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"}")
        self.tituloLabel = QLabel(self.centralwidget)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setGeometry(QRect(293, 50, 780, 90))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(40)
        font.setBold(True)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setStyleSheet(u"")
        self.tituloLabel.setAlignment(Qt.AlignCenter)
        self.campeaoLabel = QLabel(self.centralwidget)
        self.campeaoLabel.setObjectName(u"campeaoLabel")
        self.campeaoLabel.setGeometry(QRect(466, 172, 434, 60))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(28)
        self.campeaoLabel.setFont(font1)
        self.campeaoLabel.setAlignment(Qt.AlignCenter)
        self.player1Widget = QWidget(self.centralwidget)
        self.player1Widget.setObjectName(u"player1Widget")
        self.player1Widget.setGeometry(QRect(228, 250, 420, 440))
        self.player1Widget.setStyleSheet(u"#playerNomeLabel {\n"
"	background: qlineargradient(spread:pad, x1:0.552, y1:0, x2:0.557, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"	border: 2px solid #fff;\n"
"}")
        self.playerNomeLabel = QLabel(self.player1Widget)
        self.playerNomeLabel.setObjectName(u"playerNomeLabel")
        self.playerNomeLabel.setGeometry(QRect(0, 0, 420, 100))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(36)
        self.playerNomeLabel.setFont(font2)
        self.playerNomeLabel.setAlignment(Qt.AlignCenter)
        self.pontosLabel = QLabel(self.player1Widget)
        self.pontosLabel.setObjectName(u"pontosLabel")
        self.pontosLabel.setGeometry(QRect(85, 142, 250, 211))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(114)
        self.pontosLabel.setFont(font3)
        self.pontosLabel.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.player1Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(72, 376, 276, 49))
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.player2Widget = QWidget(self.centralwidget)
        self.player2Widget.setObjectName(u"player2Widget")
        self.player2Widget.setGeometry(QRect(718, 250, 420, 440))
        self.player2Widget.setStyleSheet(u"#playerNomeLabel_2 {\n"
"	background: qlineargradient(spread:pad, x1:0.552, y1:0, x2:0.557, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"	border: 2px solid #fff;\n"
"}")
        self.playerNomeLabel_2 = QLabel(self.player2Widget)
        self.playerNomeLabel_2.setObjectName(u"playerNomeLabel_2")
        self.playerNomeLabel_2.setGeometry(QRect(0, 0, 420, 100))
        self.playerNomeLabel_2.setFont(font2)
        self.playerNomeLabel_2.setAlignment(Qt.AlignCenter)
        self.pontosLabel_2 = QLabel(self.player2Widget)
        self.pontosLabel_2.setObjectName(u"pontosLabel_2")
        self.pontosLabel_2.setGeometry(QRect(85, 142, 250, 211))
        self.pontosLabel_2.setFont(font3)
        self.pontosLabel_2.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.player2Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(72, 376, 276, 49))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        FinalWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FinalWindow)

        QMetaObject.connectSlotsByName(FinalWindow)
    # setupUi

    def retranslateUi(self, FinalWindow):
        FinalWindow.setWindowTitle(QCoreApplication.translate("FinalWindow", u"MainWindow", None))
        self.tituloLabel.setText(QCoreApplication.translate("FinalWindow", u"Resultado", None))
        self.campeaoLabel.setText(QCoreApplication.translate("FinalWindow", u"Player1 ganhou", None))
        self.playerNomeLabel.setText(QCoreApplication.translate("FinalWindow", u"Player1", None))
        self.pontosLabel.setText(QCoreApplication.translate("FinalWindow", u"80", None))
        self.label.setText(QCoreApplication.translate("FinalWindow", u"Pontos", None))
        self.playerNomeLabel_2.setText(QCoreApplication.translate("FinalWindow", u"Player2", None))
        self.pontosLabel_2.setText(QCoreApplication.translate("FinalWindow", u"48", None))
        self.label_2.setText(QCoreApplication.translate("FinalWindow", u"Pontos", None))
    # retranslateUi

