#! python3, PyQt6
#! formsAndDialogues -- Application storing the classes for all forms for the application and message Dialogues

import os, sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QHBoxLayout, QFileDialog
)

class CreateAnAccount(QWidget):
    def __init__(self) -> None:                                     # -- Initiates Class Variables and functionality
        super().__init__()

        self.initWidgets()
        self.initEditWidgets()
        self.initApplyLayout()

    def initWidgets(self) -> None:                                  # -- Initiates all child widgets of the overall Widgets
        self.welcomeLabel: QLabel = QLabel("WELCOME COLLECTORS")    # -- Labels
        self.nameLabel: QLabel = QLabel("Name")
        self.dobLabel: QLabel = QLabel("DOB")
        self.usernameLabel: QLabel = QLabel("Username")
        self.passwordLabel: QLabel = QLabel("Password")
        self.emailLabel: QLabel = QLabel("Email")
        self.profilePicLabel: QLabel = QLabel("Profile Picture")

        self.nameLineEdit: QLineEdit = QLineEdit()                  # -- Line Edits
        self.dobLineEdit: QLineEdit = QLineEdit()
        self.usernameLineEdit: QLineEdit = QLineEdit()
        self.passwordLineEdit: QLineEdit = QLineEdit()
        self.emailLineEdit: QLineEdit = QLineEdit()

        self.profilePicBtn: QPushButton = QPushButton('Open')       # -- Buttons
        self.cancelBtn: QPushButton = QPushButton("Cancel")
        self.submitBtn: QPushButton = QPushButton("Submit")

    def initEditWidgets(self) -> None:                              # -- Initiates and applies all layouts to the main widget      
        self.nameLineEdit.setPlaceholderText("Name")                # -- Placeholder Text 
        self.dobLineEdit.setPlaceholderText("Date Of Birth")
        self.usernameLineEdit.setPlaceholderText("Username")
        self.passwordLineEdit.setPlaceholderText("Password")
        self.emailLineEdit.setPlaceholderText("Email")

        self.welcomeLabel.toolTip("Welcome")                        # -- Tool Tips
        self.nameLabel.toolTip("Name")
        self.dobLabel.toolTip("Date of Birth")
        self.usernameLabel.toolTip("Username")
        self.passwordLabel.toolTip("Password")
        self.emailLabel.toolTip("Email")
        self.profilePicLabel.toolTip("Profile Picture")
        self.nameLineEdit.toolTip("Name")
        self.dobLineEdit.toolTip("Date of Birth")
        self.usernameLineEdit.toolTip("Username")
        self.passwordLineEdit.toolTip("Password")
        self.emailLineEdit.toolTip("Email")
        self.profilePicBtn.toolTip("Profile Picture")
        self.cancelBtn.toolTip("Cancel Account Creation")
        self.submitBtn.toolTip("Submit")

        self.profilePicBtn.clicked.connect(self.openImage)          # -- Button Connections
        self.cancelBtn.clicked.connect(self.cancelSubmission)
        self.submitBtn.clicked.connect(self.submitNewUser)

    def initApplyLayout(self) -> None:                              # -- Initiates and applies all layouts to the main widget
        self.mainLayout: QVBoxLayout = QVBoxLayout()                # -- Layouts
        self.nameLayout: QHBoxLayout = QHBoxLayout()
        self.dobLayout: QHBoxLayout = QHBoxLayout()
        self.usernameLayout: QHBoxLayout = QHBoxLayout()
        self.passwordLayout: QHBoxLayout = QHBoxLayout()
        self.emailLayout: QHBoxLayout = QHBoxLayout()
        self.profilePicLayout: QHBoxLayout = QHBoxLayout()
        self.buttonLayout: QHBoxLayout = QHBoxLayout()

        self.nameLayout.addWidget(self.nameLabel)                   # -- Adding Widgets to Layouts
        self.nameLayout.addWidget(self.nameLineEdit)
        self.dobLayout.addWidget(self.dobLabel)
        self.dobLayout.addWidget(self.dobLineEdit)
        self.usernameLayout.addWidget(self.usernameLabel)
        self.usernameLayout.addWidget(self.usernameLineEdit)
        self.passwordLayout.addWidget(self.passwordLabel)
        self.passwordLayout.addWidget(self.passwordLineEdit)
        self.emailLayout.addWidget(self.emailLabel)
        self.emailLayout.addWidget(self.emailLineEdit)
        self.profilePicLayout.addWidget(self.profilePicLabel)
        self.profilePicLayout.addWidget(self.profilePicBtn)
        self.buttonLayout.addWidget(self.cancelBtn)
        self.buttonLayout.addWidget(self.submitBtn)

        self.mainLayout.addWidget(self.welcomeLabel)                # -- Establish layouts/widgets in the main layout
        self.mainLayout.addLayout(self.nameLayout)
        self.mainLayout.addLayout(self.dobLayout)
        self.mainLayout.addLayout(self.usernameLayout)
        self.mainLayout.addLayout(self.passwordLayout)
        self.mainLayout.addLayout(self.emailLayout)
        self.mainLayout.addLayout(self.profilePicLayout)
        self.mainLayout.addLayout(self.buttonLayout)

        self.setLayout(self.mainLayout)                             # -- Sets the main layout

    def cancelSubmission(self) -> None:                             # -- Cancels the form and closes the form window
        pass

    def submitNewUser(self) -> None:                                # -- Submits New User informaiton to the database
        pass

    def openImage(self) -> None:                                    # -- Opens the image Dialogue to open a photo
        openImg: QFileDialog = QFileDialog()
        filePath = openImg.getOpenFileName()[0]
        self.profilePicLabel.setText(filePath)

if __name__ ==  "__main__":
    app = QApplication(sys.argv)
    createAnAccount: CreateAnAccount = CreateAnAccount()
    createAnAccount.show()
    sys.exit(app.exec())