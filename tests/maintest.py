from perguntas import Ui_Jogo
from utils import load_json
from variables import dicas_path
from PyQt5.QtWidgets import *
from random import randint
from ui_final import FinalWindow
from ui_inicio import InicialWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dicas = load_json(dicas_path)
        self.respostas = []
        self.dicas_respondidas = []
        self.dica_index = 0
        self.initUI()
        
    def initUI(self):
        self.stackedWidget = QStackedWidget(self)
        
        self.inicialWindow = InicialWindow()
        self.dica_index += 1
        self.inicialWindow.button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.dica_index))
        self.stackedWidget.addWidget(self.inicialWindow)
        
        for i in range(len(self.dicas)):
            ui_pergunta = self.createWindow()
            self.stackedWidget.addWidget(ui_pergunta.centralwidget)
            
        self.finalWindow = FinalWindow()
        self.stackedWidget.addWidget(self.finalWindow)
            
        self.setCentralWidget(self.stackedWidget)
        
    def createWindow(self) -> Ui_Jogo():
        ui_pergunta = Ui_Jogo()
        ui_pergunta.setupUi(self)
        
        dicas = self.takeHint()
        dica1, dica2, dica3 = dicas
        
        ui_pergunta.dica1_label.setText(dica1)
        ui_pergunta.dica2_label.setText(dica2)
        ui_pergunta.dica3_label.setText(dica3)
        
        ui_pergunta.titulo.setText('3 Pistas - Filosofia')
        ui_pergunta.dica2.setHidden(True)
        ui_pergunta.dica3.setHidden(True)

        ui_pergunta.reveladas = 0

        ui_pergunta.pushButton.clicked.connect(lambda: self.exibirDica(ui_pergunta))
        ui_pergunta.sendButton.clicked.connect(lambda: self.sendAnswer(ui_pergunta))
        ui_pergunta.input_resposta.returnPressed.connect(lambda: self.sendAnswer(ui_pergunta))
        
        return ui_pergunta
        
    def takeHint(self) -> dict:
        while True:
            pergunta = self.dicas[str(randint(1, len(self.dicas)))]
            if pergunta not in self.dicas_respondidas:
                self.dicas_respondidas.append(pergunta)
                return pergunta['dicas']

    def exibirDica(self, ui_pergunta: Ui_Jogo):
        ui_pergunta.reveladas += 1
        if ui_pergunta.reveladas == 1:
            ui_pergunta.dica2.setVisible(True)
        
        elif ui_pergunta.reveladas == 2:
            ui_pergunta.dica3.setVisible(True)
            ui_pergunta.pushButton.setText('Próxima')
        elif ui_pergunta.reveladas == 3:
            self.dica_index += 1
            self.stackedWidget.setCurrentIndex(self.dica_index)
 
    def sendAnswer(self, ui_pergunta):
        text = str(ui_pergunta.input_resposta.text())
        print(text)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())