from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Midterm in OOP"
        self.x = 750
        self.y = 200
        self.width = 500
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.textboxbl2 = QLabel("Enter your Full name: ", self)
        self.textboxbl2.move(25, 60)
        self.textboxbl2.setStyleSheet("color: red")
        self.FullNameInput = QLineEdit(self)
        self.FullNameInput.move(200, 50)
        self.FullNameInput.resize(200, 30)

        self.button = QPushButton("Click to Display your Full name: ", self)
        self.button.setStyleSheet("color: red")
        self.button.move(20, 100)
        self.button.clicked.connect(self.DisplayName)


        self.FullNameInput2 = QLineEdit(self)
        self.FullNameInput2.move(200, 100)
        self.FullNameInput2.resize(200, 30)

        self.show()
    def DisplayName(self):
        full_name = self.FullNameInput.text()
        self.FullNameInput2.setText(full_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
