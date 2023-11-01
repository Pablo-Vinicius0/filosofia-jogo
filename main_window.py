import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from ui_mainwindow import Ui_Jogo
from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
from typing import cast

class MainWindow(QMainWindow, Ui_Jogo):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.titulo.setText('3 Pistas - Filosofia')
        self.dica2.setHidden(True)
        self.dica3.setHidden(True)
        self.c = 0

        self.pushButton.clicked.connect(lambda: self.button(self.c+1))


    
    def button(self, n : int):
        self.c += 1
        if n == 1:
            self.dica2.setVisible(True)
        
        if n == 2:
            self.dica3.setVisible(True)
            self.pushButton.setText('Próxima')

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    jogo = MainWindow()
    jogo.show()
    app.exec()