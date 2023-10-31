import sys
import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, QEvent
from PyQt5.QtGui import QKeyEvent

from variables import (dicas_path)
from uigame import Ui_Jogo
from utils import (load_json)

class MainWindow(QMainWindow, Ui_Jogo):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # neymar
        self.dicas = load_json(dicas_path)
    	
        self.titulo.setText('3 Pistas - Filosofia')
        self.dica2.setHidden(True)
        self.dica3.setHidden(True)

        self.reveladas = 0

        self.pushButton.clicked.connect(self.exibirDica)
        self.sendButton.clicked.connect(self.sendAnswer)
        self.input_resposta.returnPressed.connect(self.sendAnswer)

    def exibirDica(self):
        self.reveladas += 1
        if self.reveladas == 1:
            self.dica2.setVisible(True)
        
        elif self.reveladas == 2:
            self.dica3.setVisible(True)
            self.pushButton.setText('Próxima')
 
    def sendAnswer(self):
        text = str(self.input_resposta.text())
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    jogo = MainWindow()
    jogo.show()
    app.exec()