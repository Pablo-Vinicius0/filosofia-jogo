import sys
import PyQt5.QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from random import randint

from variables import (dicas_path)
from ui_dicas import Ui_Jogo
from utils import (load_json)

from ui_inicial import InicialWindow
from ui_explicacao import ExplicacaoWindow
from ui_login import LoginWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dicas = load_json(dicas_path)
        self.dica_atual = None
        self.respondidas = []
        self.pag_index = 1
        self.player1 = {"nome": "", "pontos": 0}
        self.player2 = {"nome": "", "pontos": 0}
        self.turno = randint(0, 1)
        
        self.dica_windows = []
        
        self.initUI()
        self.showMaximized()
        
    def initUI(self) -> None:
        self.stackedWidget = QStackedWidget(self)

        self.inicialWindow = InicialWindow()
        self.inicialWindow.iniciar_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.pag_index))
        self.stackedWidget.addWidget(self.inicialWindow)
        
        self.loginWindow = LoginWindow()
        self.loginWindow.pushButton.clicked.connect(self.checkUsernames)
        self.stackedWidget.addWidget(self.loginWindow)
        
        for i in range(len(self.dicas)):
            ui_dica = self.createWindow()
            self.stackedWidget.addWidget(ui_dica.centralwidget)
            self.dica_windows.append(ui_dica)
            ui_explicacao = ExplicacaoWindow()
            ui_explicacao.proxima_btn.clicked.connect(self.passarPag)
            ui_explicacao.resposta_label.setText(ui_dica.dica['resposta_exibir'])
            ui_explicacao.explicacao_label.setText(ui_dica.dica['explicacao'][0])
            self.stackedWidget.addWidget(ui_explicacao)
        
        self.setCentralWidget(self.stackedWidget)
        
    def passarPag(self) -> None:
        self.pag_index += 1
        self.stackedWidget.setCurrentIndex(self.pag_index)
        
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

    def resposta():
        if acertou:
            ui_dica.pushButton.setText("Explicação")

    def exibirDica(self, ui_dica: Ui_Jogo) -> None:
        ui_dica.reveladas += 1

        if ui_dica.pushButton.text() == "Explicação":
            self.passarPag()
        
        self.passarTurno(ui_dica)
        
        if ui_dica.reveladas == 1:
            ui_dica.dica2.setVisible(True)
        elif ui_dica.reveladas == 2:
            ui_dica.dica3.setVisible(True)
            ui_dica.pushButton.setText('Explicação')
            
    def passarTurno(self, ui_dica: Ui_Jogo) -> None:
        if ui_dica.reveladas in (1, 2):
            ui_dica.turno.setText(f"Vez de {self.player1['nome'] if ui_dica.turno_num == 0 else self.player2['nome']}")
            ui_dica.turno_num = (ui_dica.turno_num + 1) % 2
            
    def sendAnswer(self, ui_dica: Ui_Jogo) -> None:
        text = str(ui_dica.input_resposta.text())

        if text.lower() in ui_dica.dica['resposta']: 
            ui_dica.input_resposta.setText("Resposta correta!")
            s = ui_dica.input_resposta.styleSheet()
            ui_dica.input_resposta.setStyleSheet(s + "color:#00F901;")
            ui_dica.input_resposta.setDisabled(True)
            ui_dica.sendButton.setDisabled(True)
            ui_dica.pushButton.setText("Explicação")
            
            pontos = 0
            dicas_reveladas = ui_dica.reveladas 
            if ui_dica.turno == 0:
                if dicas_reveladas == 0:
                    self.player1['pontos'] += 10
                elif dicas_reveladas == 1:
                    self.player1['pontos'] += 9
                elif dicas_reveladas == 2:
                    self.player1['pontos'] += 8
            elif ui_dica.turno == 1:
                if dicas_reveladas == 0:
                    self.player2['pontos'] += 10
                elif dicas_reveladas == 1:
                    self.player2['pontos'] += 9
                elif dicas_reveladas == 2:
                    self.player2['pontos'] += 8
        else:
            print("Resposta errada!")
            print(ui_dica.dica['resposta'])

    def checkUsernames(self) -> None:
        if self.loginWindow.valideUsernames():
            p1_nome, p2_nome = str(self.loginWindow.lineEdit.text()), str(self.loginWindow.lineEdit_2.text())
            self.player1['nome'] = p1_nome
            self.player2['nome'] = p2_nome
            
            for pag in self.dica_windows:
                pag.turno.setText(f"Vez de {self.player1['nome'] if self.turno == 0 else self.player2['nome']}")
                self.turno = (self.turno + 1) % 2
                pag.turno_num = self.turno
                pag.pontuacao_p1_label.setText(p1_nome)
                pag.pontuacao_p2_label.setText(p2_nome)
                pag.pontuacao_p1.setText(str(self.player1['pontos']))
                pag.pontuacao_p2.setText(str(self.player2['pontos']))
            
            self.passarPag()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    jogo = MainWindow()
    jogo.show()
    app.exec()