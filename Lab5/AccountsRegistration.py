from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Account Registration System"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 350  # Adjusted for better fit
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.textboxbl = QLabel("Sign Up", self)
        self.textboxbl.move(120, 15)

        # First Name
        self.textboxbl2 = QLabel("First Name: ", self)
        self.textboxbl2.move(25, 60)
        self.firstNameInput = QLineEdit(self)
        self.firstNameInput.move(110, 50)
        self.firstNameInput.resize(150, 30)

        # Last Name
        self.textboxbl3 = QLabel("Last Name: ", self)
        self.textboxbl3.move(25, 100)
        self.lastNameInput = QLineEdit(self)
        self.lastNameInput.move(110, 90)
        self.lastNameInput.resize(150, 30)

        # Username
        self.textboxbl4 = QLabel("Username: ", self)
        self.textboxbl4.move(25, 140)
        self.usernameInput = QLineEdit(self)
        self.usernameInput.move(110, 130)
        self.usernameInput.resize(150, 30)

        # Email Address
        self.textboxbl5 = QLabel("Email Address: ", self)
        self.textboxbl5.move(25, 180)
        self.emailInput = QLineEdit(self)
        self.emailInput.move(110, 170)
        self.emailInput.resize(150, 30)

        # Contact Number
        self.textboxbl6 = QLabel("Contact Number: ", self)
        self.textboxbl6.move(25, 220)
        self.contactInput = QLineEdit(self)
        self.contactInput.move(110, 210)
        self.contactInput.resize(150, 30)

        # Buttons
        self.submitButton = QPushButton("Submit", self)
        self.submitButton.move(70, 260)
        self.submitButton.clicked.connect(self.save_account_details)

        self.clearButton = QPushButton("Clear", self)
        self.clearButton.move(160, 260)
        self.clearButton.clicked.connect(self.clear_fields)

        self.center()
        self.show()

    def center(self):
        # Centers the window on the screen
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def save_account_details(self):
        details = [
            self.firstNameInput.text(),
            self.lastNameInput.text(),
            self.usernameInput.text(),
            self.emailInput.text(),
            self.contactInput.text()
        ]

        # Check if all fields are filled
        if any(not detail for detail in details):
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        with open('account_details.txt', 'a') as f:
            f.write(', '.join(details) + '\n')
        QMessageBox.information(self, "Success", "Details Saved Successfully!")

    def clear_fields(self):
        self.firstNameInput.clear()
        self.lastNameInput.clear()
        self.usernameInput.clear()
        self.emailInput.clear()
        self.contactInput.clear()
        QMessageBox.information(self, "Cleared", "Fields Cleared Successfully!")

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())