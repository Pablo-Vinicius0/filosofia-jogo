# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_explicacao.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ExplicacaoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.setObjectName("Explicacao")
        self.setEnabled(True)
        self.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(1366, 768))
        self.setMaximumSize(QtCore.QSize(1366, 768))
        self.setStyleSheet("QWidget #Explicacao {\n"
"    background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"    color: #fff;\n"
"}")
        self.resposta_label = QtWidgets.QLabel(self)
        self.resposta_label.setGeometry(QtCore.QRect(258, 10, 850, 130))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(32)
        self.resposta_label.setFont(font)
        self.resposta_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resposta_label.setStyleSheet("background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"border-radius: 45px;\n"
"border: 2px solid #fff;\n"
"color: #fff;")
        self.resposta_label.setAlignment(QtCore.Qt.AlignCenter)
        self.resposta_label.setObjectName("resposta_label")
        self.explicacao_label = QtWidgets.QLabel(self)
        self.explicacao_label.setGeometry(QtCore.QRect(60, 60, 1246, 648))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(32)
        self.explicacao_label.setFont(font)
        self.explicacao_label.setStyleSheet("background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"border-radius: 45px;\n"
"border: 2px solid #fff;\n"
"color: #fff;\n"
"padding-top: 30px;")
        self.explicacao_label.setTextFormat(QtCore.Qt.RichText)
        self.explicacao_label.setScaledContents(False)
        self.explicacao_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.explicacao_label.setWordWrap(True)
        self.explicacao_label.setIndent(10)
        self.explicacao_label.setObjectName("explicacao_label")
        self.proxima_btn = QtWidgets.QPushButton(self)
        self.proxima_btn.setGeometry(QtCore.QRect(1091, 658, 255, 90))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.proxima_btn.setFont(font)
        self.proxima_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.proxima_btn.setStyleSheet("QPushButton {\n"
"      background: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.488636, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(9, 36, 126, 255));\n"
"       border: 2px solid #fff;\n"
"       border-radius: 30px;\n"
"       color: #fff;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: qlineargradient(spread:pad, x1:0.494, y1:0.5, x2:0.5, y2:1, stop:0.335227 rgba(9, 34, 126, 228), stop:1 rgba(0, 0, 0, 0));\n"
"}")
        self.proxima_btn.setObjectName("proxima_btn")
        self.explicacao_label.raise_()
        self.proxima_btn.raise_()
        self.resposta_label.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Explicacao", "Window"))
        self.resposta_label.setText(_translate("Explicacao", "Resposta Ultra Massa"))
        self.explicacao_label.setText(_translate("Explicacao", "Para Aristóteles, a ética opera no campo do possível, tudo aquilo que depende das deliberações, escolhas e da ação humana. Ele propõe a ideia da ação guiada pela razão como um princípio fundamental da existência ética."))
        self.proxima_btn.setText(_translate("Explicacao", "Próxima"))