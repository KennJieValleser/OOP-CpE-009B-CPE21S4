import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP"
        self.x = 750
        self.y = 300
        self.width = 400
        self.height = 400
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)

        self.button = QPushButton("Click to Change Color", self)
        self.button.move(150,150)
        self.button.clicked.connect(self.coloryellow)
        self.show()

    def coloryellow(self):
        self.button.setStyleSheet("background-color: yellow")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())
