import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QAction, QFileDialog

class SciCal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loadmenu()
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
                                                  "Text Files (*.txt);;All files (*)",
                                                  options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textLine.text())

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open calculator file", "",
                                                  "Text Files (*.txt);;All files (*)",
                                                  options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.textLine.setText(data)

    def cleartext(self):
        self.textLine.clear()

    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        grid = QGridLayout()
        centralWidget.setLayout(grid)

        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 0, 1, 5)

        names = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'exp',
            '0', '.', '=', '+', 'Clear'
        ]

        # Create buttons and add to layout
        positions = [(i, j) for i in range(1, 5) for j in range(5)]
        for position, name in zip(positions, names):
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(lambda _, b=name: self.buttonClicked(b))

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Scientific Calculator')
        self.show()

    def buttonClicked(self, text):
        if text == 'Clear':
            self.cleartext()
        elif text == '=':
            self.calculate_result()
        elif text == 'sin':
            self.calculate_trig(math.sin)
        elif text == 'cos':
            self.calculate_trig(math.cos)
        elif text == 'exp':
            self.calculate_exp()
        else:
            self.textLine.setText(self.textLine.text() + text)

    def calculate_result(self):
        try:
            result = str(eval(self.textLine.text()))
            self.textLine.setText(result)
        except Exception:
            self.textLine.setText("Error")

    def calculate_trig(self, func):
        try:
            value = float(self.textLine.text())
            result = str(func(math.radians(value)))  # Convert to radians
            self.textLine.setText(result)
        except Exception:
            self.textLine.setText("Error")

    def calculate_exp(self):
        try:
            value = float(self.textLine.text())
            result = str(math.exp(value))
            self.textLine.setText(result)
        except Exception:
            self.textLine.setText("Error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SciCal()
    sys.exit(app.exec())
