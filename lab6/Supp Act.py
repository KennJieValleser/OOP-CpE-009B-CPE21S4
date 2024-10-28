import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class SciCal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loadmenu()
        self.loadwidget()
        self.initUI()

    def loadmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')

        editButton = QAction('Clear', self)
        editButton.setShortcut("Ctrl+M")
        editButton.triggered.connect(self.cleartext)
        editMenu.addAction(editButton)

        saveButton = QAction('Save', self)
        saveButton.setShortcut("Ctrl+S")
        saveButton.triggered.connect(self.saveFileDialog)
        fileMenu.addAction(saveButton)

        openButton = QAction('Open', self)
        openButton.setShortcut("Ctrl+O")
        openButton.triggered.connect(self.openFileNameDialog)
        fileMenu.addAction(openButton)

        exitButton = QAction('Exit', self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save calculator file", "",
                                                  "Text Files (*.txt);;Python Files (*.py);;All files (*)",
                                                  options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.calculator.toPlainText())

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open calculator file", "",
                                                  "Text Files (*.txt);;Python Files (*.py);;All files (*)",
                                                  options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.calculator.setPlainText(data)

    def cleartext(self):
        self.calculator.clear()

    def loadwidget(self):
        self.calculator = QTextEdit()
        self.setCentralWidget(self.calculator)

    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        grid = QGridLayout()
        centralWidget.setLayout(grid)

        names = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'exp',
            '0', '.', '=', '+', 'Clear'
        ]

        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 0, 1, 5)

        # Using a loop to generate positions
        positions = [(i, j) for i in range(1, 5) for j in range(5)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Scientific Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SciCal()
    sys.exit(app.exec())
