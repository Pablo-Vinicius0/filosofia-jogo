# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_inicial.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_InicialWindow(object):
    def setupUi(self, InicialWindow):
        if not InicialWindow.objectName():
            InicialWindow.setObjectName(u"InicialWindow")
        InicialWindow.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InicialWindow.sizePolicy().hasHeightForWidth())
        InicialWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Consolas"])
        InicialWindow.setFont(font)
        InicialWindow.setStyleSheet(u"\n"
"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"	border: 2px solid #FFF;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: qlineargradient(spread:pad, x1:0.494, y1:0.5, x2:0.5, y2:1, stop:0.335227 rgba(9, 34, 126, 228), stop:1 rgba(0, 0, 0, 0));\n"
"}")
        self.titulo = QLabel(InicialWindow)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(183, 95, 1000, 270))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(84)
        font1.setBold(True)
        self.titulo.setFont(font1)
        self.titulo.setStyleSheet(u"QLabel {\n"
"	background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"	border-radius: 30px;\n"
"	border: 4px solid #FFF;\n"
"}")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.iniciar_btn = QPushButton(InicialWindow)
        self.iniciar_btn.setObjectName(u"iniciar_btn")
        self.iniciar_btn.setGeometry(QRect(463, 427, 440, 110))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(36)
        font2.setBold(False)
        self.iniciar_btn.setFont(font2)
        self.iniciar_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sobre_btn = QPushButton(InicialWindow)
        self.sobre_btn.setObjectName(u"sobre_btn")
        self.sobre_btn.setGeometry(QRect(470, 587, 440, 110))
        self.sobre_btn.setFont(font2)
        self.sobre_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.retranslateUi(InicialWindow)

        QMetaObject.connectSlotsByName(InicialWindow)
    # setupUi

    def retranslateUi(self, InicialWindow):
        InicialWindow.setWindowTitle(QCoreApplication.translate("InicialWindow", u"Filosofia", None))
        self.titulo.setText(QCoreApplication.translate("InicialWindow", u"Filosofia", None))
        self.iniciar_btn.setText(QCoreApplication.translate("InicialWindow", u"Iniciar", None))
        self.sobre_btn.setText(QCoreApplication.translate("InicialWindow", u"Sobre", None))
    # retranslateUi

