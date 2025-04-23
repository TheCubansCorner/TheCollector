#! python3, PyQt6
#! login.py -- a basic login application

import sys


from formsAndDialogues import CreateAnAccount
from PyQt6.QtWidgets import (
    QApplication, QPushButton, 
    QLabel, QLineEdit, QWidget,
    QHBoxLayout, QVBoxLayout
                             )

class Login(QWidget):
    def __init__(self, db):                                                           # -- Initiates Class Variables and functionality
        super().__init__()
        self.dataBass = db
        self.loginSuccessful: bool = None
        self.userId: int = None

        self.setWindowTitle("WELCOME!")  
        self.initWidgets()
        self.initEditWidgets()
        self.initApplyLayout()
        self.buttonConnections()

    def initWidgets(self) -> None:                                                          # -- Initiates all child widgets of the overall Widget
        self.loginLabel: QLabel = QLabel("LOGIN")
        self.usernameLabel: QLabel = QLabel("Username: ")
        self.passwordLabel: QLabel = QLabel("Password: ")
        self.messageLabel: QLabel = QLabel()
        self.errorLabel: QLabel = QLabel()
        
        self.usernameLineEdit: QLineEdit = QLineEdit()
        self.passwordLineEdit: QLineEdit = QLineEdit()

        self.cancelBtn: QPushButton = QPushButton("Cancel")
        self.loginBtn: QPushButton =  QPushButton("Login") 
        self.createAccountBtn: QPushButton = QPushButton("Create an Account")

    def initEditWidgets(self) -> None:                                                      # -- Initiates widget connections to functions/inputs dummy data/edit widgit behaviour
        self.usernameLineEdit.setPlaceholderText("Username")
        self.passwordLineEdit.setPlaceholderText("Password")

        self.usernameLabel.setToolTip("Username")
        self.passwordLabel.setToolTip("Password")
        self.usernameLineEdit.setToolTip("Username")
        self.passwordLineEdit.setToolTip("Password")
        self.cancelBtn.setToolTip("Cancel")
        self.loginBtn.setToolTip("Submit Information")

        self.cancelBtn.clicked.connect(self.cancelLogin)
        self.loginBtn.clicked.connect(self.signIN)
        self.createAccountBtn.clicked.connect(self.createAccount)

    def initApplyLayout(self) -> None:                                                # -- Initiates and applies all layouts to the main widget                                          
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.usernameLayout: QHBoxLayout = QHBoxLayout()
        self.passwordLayout: QHBoxLayout = QHBoxLayout()
        self.buttonLayout: QHBoxLayout = QHBoxLayout()

        self.usernameLayout.addWidget(self.usernameLabel)
        self.usernameLayout.addWidget(self.usernameLineEdit)

        self.passwordLayout.addWidget(self.passwordLabel)
        self.passwordLayout.addWidget(self.passwordLineEdit)

        self.buttonLayout.addWidget(self.cancelBtn)
        self.buttonLayout.addWidget(self.loginBtn)

        self.mainLayout.addWidget(self.loginLabel)
        self.mainLayout.addLayout(self.usernameLayout)
        self.mainLayout.addLayout(self.passwordLayout)
        self.mainLayout.addWidget(self.messageLabel)
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addWidget(self.createAccountBtn)
        self.mainLayout.addWidget(self.errorLabel)

        self.setLayout(self.mainLayout)

    def buttonConnections(self) -> None:
        self.createAccountBtn.clicked.connect(self.createAccount)
        self.loginBtn.clicked.connect(self.signIN)

    def signIN(self) -> None:                                                               # -- Sends credentials to be checked and if confirmed sends info to main application
        username: str = self.usernameLineEdit.text()
        password: str = self.passwordLineEdit.text()
        confirm: bool = self.dataBass.checkLogin(username, password)

        if confirm:
            self.userId = self.dataBass.fetchUserID(username, password)[0][0]
            self.errorLabel.setText("Login Successful!")
            self.close()
        else:
            self.errorLabel.setText(self.dataBass.errorMessage)

    def createAccount(self) -> None:                                                        # -- Opens up a form to create an account
        self.createAnAccount: CreateAnAccount = CreateAnAccount(self.dataBass)
        self.createAnAccount.show()

    def cancelLogin(self) -> None:                                                          # -- Cancels login and shuts down the application
        sys.exit()

if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    login: Login = Login()
    login.show()
    sys.exit(app.exec())