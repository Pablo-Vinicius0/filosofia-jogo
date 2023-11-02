from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5 import QtGui

class FinalWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        self.label = QLabel("Página final.")
        self.label.setFont(font)
        self.label.setObjectName("label")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)