from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class InicialWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Jogo")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.move(1055, 90)
        self.button = QPushButton("Iniciar")
        self.button.setFont(font)
        self.button.move(255, 90)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)