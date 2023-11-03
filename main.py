import sys
import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import QObject, QEvent
from PyQt5.QtGui import QKeyEvent
from random import randint

from variables import (dicas_path)
from ui_dicas import Ui_Jogo
from utils import (load_json)

from ui_inicial import InicialWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dicas = load_json(dicas_path)
        self.dica_atual = None
        self.respondidas = []
        self.pag_index = 1
        
        self.initUI()
        self.showMaximized()
        
    def initUI(self) -> None:
        self.stackedWidget = QStackedWidget(self)
        self.inicialWindow = InicialWindow()
        self.inicialWindow.iniciar_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.pag_index))
        self.stackedWidget.addWidget(self.inicialWindow)
        
        for i in range(len(self.dicas)):
            ui_dica = self.createWindow()
            self.stackedWidget.addWidget(ui_dica.centralwidget)
        
        self.setCentralWidget(self.stackedWidget)
        
    def createWindow(self) -> Ui_Jogo():
        ui_dica = Ui_Jogo()
        ui_dica.setupUi(self)
        
        self.dica_atual = self.takeHint()
        ui_dica.dica = self.dica_atual
        dica1, dica2, dica3 = self.dica_atual['dicas']
        
        ui_dica.dica1_label.setText(dica1)
        ui_dica.dica2_label.setText(dica2)
        ui_dica.dica3_label.setText(dica3)

        ui_dica.titulo.setText('3 Pistas - Filosofia')
        ui_dica.dica2.setHidden(True)
        ui_dica.dica3.setHidden(True)
        
        ui_dica.reveladas = 0
        
        ui_dica.pushButton.clicked.connect(lambda: self.exibirDica(ui_dica))
        ui_dica.sendButton.clicked.connect(lambda: self.sendAnswer(ui_dica))
        ui_dica.input_resposta.returnPressed.connect(lambda: self.sendAnswer(ui_dica))

        return ui_dica
        
    def takeHint(self) -> dict:
        while True:
            dica = self.dicas[str(randint(1, len(self.dicas)))]
            if dica not in self.respondidas:
                self.respondidas.append(dica)
                return dica

    def exibirDica(self, ui_dica: Ui_Jogo) -> None:
        ui_dica.reveladas += 1
        
        if ui_dica.reveladas == 1:
            ui_dica.dica2.setVisible(True)
        elif ui_dica.reveladas == 2:
            ui_dica.dica3.setVisible(True)
            ui_dica.pushButton.setText('Próxima')
        elif ui_dica.reveladas == 3:
            self.pag_index += 1
            self.stackedWidget.setCurrentIndex(self.pag_index)
            
    def sendAnswer(self, ui_dica: Ui_Jogo) -> None:
        text = str(ui_dica.input_resposta.text())

        if text.lower() in ui_dica.dica['resposta']:
            print("Resposta correta!")
        else:
            print("Resposta errada!")
            print(ui_dica.dica['resposta'])

'''
class MainWindow(QMainWindow, Ui_Jogo):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
 
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
            makeMsgBox(self)           
 
    def sendAnswer(self):
        text = str(self.input_resposta.text())
        print(text)
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    jogo = MainWindow()
    jogo.show()
    app.exec()