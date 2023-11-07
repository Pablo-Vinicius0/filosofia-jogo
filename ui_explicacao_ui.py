# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_explicacao.ui'
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

class Ui_Explicacao(object):
    def setupUi(self, Explicacao):
        if not Explicacao.objectName():
            Explicacao.setObjectName(u"Explicacao")
        Explicacao.setEnabled(True)
        Explicacao.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Explicacao.sizePolicy().hasHeightForWidth())
        Explicacao.setSizePolicy(sizePolicy)
        Explicacao.setMinimumSize(QSize(1366, 768))
        Explicacao.setMaximumSize(QSize(1366, 768))
        Explicacao.setStyleSheet(u"QWidget #Explicacao {\n"
"	background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"	color: #fff;\n"
"}")
        self.resposta_label = QLabel(Explicacao)
        self.resposta_label.setObjectName(u"resposta_label")
        self.resposta_label.setGeometry(QRect(258, 10, 850, 130))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(32)
        self.resposta_label.setFont(font)
        self.resposta_label.setLayoutDirection(Qt.LeftToRight)
        self.resposta_label.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"border-radius: 45px;\n"
"border: 2px solid #fff;\n"
"color: #fff;")
        self.resposta_label.setAlignment(Qt.AlignCenter)
        self.explicacao_label = QLabel(Explicacao)
        self.explicacao_label.setObjectName(u"explicacao_label")
        self.explicacao_label.setGeometry(QRect(60, 60, 1246, 648))
        self.explicacao_label.setFont(font)
        self.explicacao_label.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"border-radius: 45px;\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding-top: 30px;")
        self.explicacao_label.setTextFormat(Qt.RichText)
        self.explicacao_label.setScaledContents(False)
        self.explicacao_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.explicacao_label.setWordWrap(True)
        self.explicacao_label.setMargin(80)
        self.explicacao_label.setIndent(10)
        self.proxima_btn = QPushButton(Explicacao)
        self.proxima_btn.setObjectName(u"proxima_btn")
        self.proxima_btn.setGeometry(QRect(1091, 658, 255, 90))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(24)
        self.proxima_btn.setFont(font1)
        self.proxima_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.proxima_btn.setStyleSheet(u"QPushButton {\n"
"      background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"       border: 2px solid #fff;\n"
"	   border-radius: 30px;\n"
"	   color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: qlineargradient(spread:pad, x1:0.494, y1:0.5, x2:0.5, y2:1, stop:0.335227 rgba(9, 34, 126, 228), stop:1 rgba(0, 0, 0, 0));\n"
"}")
        self.explicacao_label.raise_()
        self.proxima_btn.raise_()
        self.resposta_label.raise_()

        self.retranslateUi(Explicacao)

        QMetaObject.connectSlotsByName(Explicacao)
    # setupUi

    def retranslateUi(self, Explicacao):
        Explicacao.setWindowTitle(QCoreApplication.translate("Explicacao", u"Window", None))
        self.resposta_label.setText(QCoreApplication.translate("Explicacao", u"Resposta Ultra Massa", None))
        self.explicacao_label.setText(QCoreApplication.translate("Explicacao", u"Para Arist\u00f3teles, a \u00e9tica opera no campo do poss\u00edvel, tudo aquilo que depende das delibera\u00e7\u00f5es, escolhas e da a\u00e7\u00e3o humana. Ele prop\u00f5e a ideia da a\u00e7\u00e3o guiada pela raz\u00e3o como um princ\u00edpio fundamental da exist\u00eancia \u00e9tica.", None))
        self.proxima_btn.setText(QCoreApplication.translate("Explicacao", u"Pr\u00f3xima", None))
    # retranslateUi

