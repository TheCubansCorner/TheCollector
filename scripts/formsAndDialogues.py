#! python3, PyQt6
#! formsAndDialogues -- Application storing the classes for all forms for the application and message Dialogues

import os, sys, sqlite3

from databaseQueries import DatabaseQueries
from PyQt6.QtCore import QTimer, QDate, QTime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QHBoxLayout, QFileDialog,
    QComboBox, QLineEdit, QTimeEdit, QDateEdit
)


class CreateAnAccount(QWidget):
    def __init__(self, db) -> None:                                     # -- Initiates Class Variables and functionality
        super().__init__()
        self.dataBass = db

        self.initWidgets()
        self.initEditWidgets()
        self.initApplyLayout()
        self.initBtnConnections()

    def initWidgets(self) -> None:                                  # -- Initiates all child widgets of the overall Widgets
        self.welcomeLabel: QLabel = QLabel("WELCOME COLLECTORS")    # -- Labels
        self.firstNameLabel: QLabel = QLabel("First")
        self.lastNameLabel: QLabel = QLabel("Last")
        self.dobLabel: QLabel = QLabel("DOB")
        self.usernameLabel: QLabel = QLabel("Username")
        self.passwordLabel: QLabel = QLabel("Password")
        self.emailLabel: QLabel = QLabel("Email")
        self.profilePicLabel: QLabel = QLabel("Profile Picture")
        self.usernameErrorLabel: QLabel = QLabel()
        self.passwordErrorLabel: QLabel = QLabel()
        self.nameErrorLabel: QLabel = QLabel()
        self.dobErrorLabel: QLabel = QLabel()
        self.emailErrorLabel: QLabel = QLabel()
        self.imageErrorLabel: QLabel = QLabel()


        self.firstNameLineEdit: QLineEdit = QLineEdit()                  # -- Line Edits
        self.lastNameLineEdit: QLineEdit = QLineEdit()
        self.dobLineEdit: QLineEdit = QLineEdit()
        self.usernameLineEdit: QLineEdit = QLineEdit()
        self.passwordLineEdit: QLineEdit = QLineEdit()
        self.emailLineEdit: QLineEdit = QLineEdit()

        self.profilePicBtn: QPushButton = QPushButton('Open')       # -- Buttons
        self.cancelBtn: QPushButton = QPushButton("Cancel")
        self.submitBtn: QPushButton = QPushButton("Submit")

        self.mainLayout: QVBoxLayout = QVBoxLayout()                # -- Layouts
        self.nameLayout: QHBoxLayout = QHBoxLayout()
        self.dobLayout: QHBoxLayout = QHBoxLayout()
        self.usernameLayout: QHBoxLayout = QHBoxLayout()
        self.passwordLayout: QHBoxLayout = QHBoxLayout()
        self.emailLayout: QHBoxLayout = QHBoxLayout()
        self.profilePicLayout: QHBoxLayout = QHBoxLayout()
        self.buttonLayout: QHBoxLayout = QHBoxLayout()

    def initEditWidgets(self) -> None:                              # -- Initiates and applies all layouts to the main widget      
        self.firstNameLineEdit.setPlaceholderText("First Name")                # -- Placeholder Text 
        self.lastNameLineEdit.setPlaceholderText("Last Name")
        self.dobLineEdit.setPlaceholderText("Date Of Birth")
        self.usernameLineEdit.setPlaceholderText("Username")
        self.passwordLineEdit.setPlaceholderText("Password")
        self.emailLineEdit.setPlaceholderText("Email")

        self.welcomeLabel.setToolTip("Welcome")                        # -- Tool Tips
        self.firstNameLabel.setToolTip("First Name")
        self.lastNameLabel.setToolTip("Last Name")
        self.dobLabel.setToolTip("Date of Birth")
        self.usernameLabel.setToolTip("Username")
        self.passwordLabel.setToolTip("""
        - At least, one capital letter.
        - At least one lower case letter
        - At least, one number
        - At least one spectial Character (!@#$%^&*_++-?/\\><")
        """)
        self.emailLabel.setToolTip("Email")
        self.profilePicLabel.setToolTip("Profile Picture")
        self.firstNameLineEdit.setToolTip("First Name")
        self.lastNameLineEdit.setToolTip("Last Name")
        self.dobLineEdit.setToolTip("Date of Birth")
        self.usernameLineEdit.setToolTip("Username")
        self.passwordLineEdit.setToolTip("""
        - At least, one capital letter.
        - At least one lower case letter
        - At least, one number
        - At least one spectial Character (!@#$%^&*_++-?/\\><")
        """)
        self.emailLineEdit.setToolTip("Email")
        self.profilePicBtn.setToolTip("Profile Picture")
        self.cancelBtn.setToolTip("Cancel Account Creation")
        self.submitBtn.setToolTip("Submit")

        self.profilePicBtn.clicked.connect(self.openImage)          # -- Button Connections
        self.cancelBtn.clicked.connect(self.cancelSubmission)
        self.submitBtn.clicked.connect(self.submitNewUser)

    def initApplyLayout(self) -> None:                              # -- Initiates and applies all layouts to the main widget
        self.nameLayout.addWidget(self.firstNameLabel)                   # -- Adding Widgets to Layouts
        self.nameLayout.addWidget(self.firstNameLineEdit)
        self.nameLayout.addWidget(self.lastNameLabel)
        self.nameLayout.addWidget(self.lastNameLineEdit)
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
        self.mainLayout.addWidget(self.usernameErrorLabel)
        self.mainLayout.addWidget(self.passwordErrorLabel)
        self.mainLayout.addWidget(self.emailErrorLabel)
        self.mainLayout.addWidget(self.nameErrorLabel)
        self.mainLayout.addWidget(self.dobErrorLabel)
        self.mainLayout.addWidget(self.imageErrorLabel)

        self.setLayout(self.mainLayout)                             # -- Sets the main layout

    def initBtnConnections(self) -> None:                           # -- Establishes conneciton between buttons and functions
        self.submitBtn.clicked.connect(self.submitNewUser)
        self.cancelBtn.clicked.connect(self.cancelSubmission)

    def cancelSubmission(self) -> None:                             # -- Cancels the form and closes the form window
        self.close()

    def submitNewUser(self) -> None:                                # -- Submits New User informaiton to the database
        userToAdd: tuple = (
            self.usernameLineEdit.text(),
            self.passwordLineEdit.text(),
            self.firstNameLineEdit.text(),
            self.lastNameLineEdit.text(),
            self.dobLineEdit.text(),
            self.emailLineEdit.text(),
            self.profilePicLabel.text(),
        )

        if self.validateName(userToAdd[2], userToAdd[3]) == False:
            self.nameErrorLabel.setText("Names should not contain numbers or spectial characters beyond '-'")
            return 
        else:
            self.nameErrorLabel.setText("")

        if self.validateDOB(userToAdd[4]) == False:
            self.dobErrorLabel.setText("Date of Birth should be formatted MM/DD/YYYY")
            return 
        else:
            self.dobErrorLabel.setText("")

        if self.validateUsername(userToAdd[0]) == False:
            self.usernameErrorLabel.setText("This username already exists.")
            return 
        else:
            self.usernameErrorLabel.setText("")

        if self.validatePassword(userToAdd[1]) == False:
            self.passwordErrorLabel.setText("""This is not a valid password. A valid password must contain:
            - At least, one capital letter.
            - At least one lower case letter
            - At least, one number
            - At least one spectial Character (!@#$%^&*_++-?/\\><")
                    """)
            return
        else:
            self.passwordErrorLabel.setText("")

        if self.validateEmail(userToAdd[5]) == False:
            return 
        else:
            self.emailErrorLabel.setText("")
        
        if self.validateImageFile(userToAdd[6]) == False:
            self.imageErrorLabel.setText("Not a valid image file")
            return
        else:
            self.imageErrorLabel.setText("")

        if userToAdd[0] and userToAdd[1]:
            self.dataBass.createUser(userToAdd)
            self.close()

    def validateUsername(self, username: str) -> bool:              # -- Confirms if username exists or not
        exists = self.dataBass.usernameExists(username)

        if exists:
            return False
        else:
            return True

    def validatePassword(self, password: str) -> bool:              # -- Confirms if a password is valid 
        confirmation: list = []
        validators: list = [
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "abcdefghijklmnopqrstuvwxyz",
            "1234567890", "!@#$%^&*_++-?/\\><"
            ]
        
        for validator in validators:
            for item in validator:
                if item in password:
                    confirmation.append(True)
                    break

        if sum(confirmation) < 4:
            return False
        else:
            return True                 

    def validateName(self, first: str, last: str) -> bool:          # -- Confirms the name is not using invalid characters
        alpha: str = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for letter in first:
            if letter not in alpha:
                return False
        
        for letter in last:
            if letter not in alpha:
                return False
            
        return True
    
    def validateEmail(self, email: str) -> bool:                    # -- Confirms the email is formatted correctly and does not exist in the database
        if "@" not in email or "." not in email:
            self.emailErrorLabel.setText("Invalid format for email")
            return False
        
        if self.dataBass.emailExists(email) == False:
            self.emailErrorLabel.setText("This email has already been registered.")
            return False
        
        return True

    def validateDOB(self, dob: str) -> bool:                        # -- Confirms if the email is valid to use
        # -- This could be better i think
        if "/" not in dob:
            return False
        else:
            dobList: list = dob.split("/")

        if int(dobList[0]) > 12:
            return False
        
        if int(dobList[1]) > 31:
            return False
        
        if int(dobList[2]) > 2025:
            return False
        
        return True

    def validateImageFile(self, imgFileName: str) -> bool:          # -- Confirms if is a valid image format
        validFiles: list = ["jpg", "jpeg", "png"]
        
        if "." in imgFileName:
            fileName: list = imgFileName.split(".")
        else:
            return False

        if fileName[1] not in validFiles:
            return False
        
        return True       

    def openImage(self) -> None:                                    # -- Opens the image Dialogue to open a photo
        openImg: QFileDialog = QFileDialog()
        filePath = openImg.getOpenFileName()[0]
        self.profilePicLabel.setText(filePath)


class ToDoList(QWidget):
    def __init__(self) -> None:
        super().__init__()
        #Time, date, title, list
        self.currentDate: QDate.currentDate = QDate.currentDate()
        self.initApplication()
        
    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.initConnections()
        self.initLayouts()
        self.ApplyLayouts()

    def initWidgets(self) -> None:
        self.timeLabel: QLabel = QLabel("Time:")
        self.dateLabel: QLabel = QLabel("Date:")
        self.titleLabel: QLabel = QLabel("Title:")
        
        self.timeEntry: QTimeEdit = QTimeEdit()
        self.dateEntry: QDate = QDateEdit()
        self.titleEntry: QLineEdit = QLineEdit()
        self.toDoEntry: QLineEdit = QLineEdit()

        self.toDoBtn: QPushButton = QPushButton("+")

    def initEditWidgets(self) -> None:
        pass

    def initConnections(self) -> None:
        pass
    
    def initLayouts(self) -> None:
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.timeLayout: QHBoxLayout = QHBoxLayout()
        self.dateLayout: QHBoxLayout = QHBoxLayout()
        self.titleLayout: QHBoxLayout = QHBoxLayout()
        self.addToDoLayout: QHBoxLayout = QHBoxLayout()
        self.tasksLayout: QVBoxLayout = QVBoxLayout()

    def ApplyLayouts(self) -> None:
        self.mainLayout.addLayout(self.timeLayout)
        self.mainLayout.addLayout(self.dateLayout)
        self.mainLayout.addLayout(self.titleLayout)
        self.mainLayout.addLayout(self.addToDoLayout)

        self.timeLayout.addWidget(self.timeLabel)
        self.timeLayout.addWidget(self.timeEntry)

        self.dateLayout.addWidget(self.dateLabel)
        self.dateLayout.addWidget(self.dateEntry)
        
        self.titleLayout.addWidget(self.titleLabel)
        self.titleLayout.addWidget(self.titleEntry)

        self.addToDoLayout.addWidget(self.toDoEntry)
        self.addToDoLayout.addWidget(self.toDoBtn)

        self.setLayout(self.mainLayout)

    def addTodoTask(self) -> None:
        pass

class DailyEvent(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Time, Date, Title, event description
        self.initApplication()

    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.initConnections()
        self.initLayouts()
        self.ApplyLayouts()

    def initWidgets(self) -> None:
        pass

    def initEditWidgets(self) -> None:
        pass

    def initConnections(self) -> None:
        pass
    
    def initLayouts(self) -> None:
        pass

    def ApplyLayouts(self) -> None:
        pass

class Note(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Time, Date, Title, Body
        self.initApplication()

    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.initConnections()
        self.initLayouts()
        self.ApplyLayouts()

    def initWidgets(self) -> None:
        pass

    def initEditWidgets(self) -> None:
        pass

    def initConnections(self) -> None:
        pass
    
    def initLayouts(self) -> None:
        pass

    def ApplyLayouts(self) -> None:
        pass

class CreateNewEvent(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.applicaitonDict: dict = {
            "to do list" : ToDoList(),
            "event" : DailyEvent(),
            "note" : Note()
        }

        self.initApplication()

    def initApplication(self) -> None:              # -- Initiates the application
        self.initWidgets()
        self.initEditWidgets()
        self.initLayouts()
        self.ApplyLayouts()
        self.initConnections()

    def initWidgets(self) -> None:                  # -- Initiates all child widgets
        self.eventTypeCombo: QComboBox = QComboBox()

    def initEditWidgets(self) -> None:              # -- Edits widgets before applying them
        self.eventTypeCombo.addItem("No Selection")
        self.eventTypeCombo.addItem("To Do List")
        self.eventTypeCombo.addItem("Event")
        self.eventTypeCombo.addItem("Note")

        for app in self.applicaitonDict.values():
            app.hide()

    def initConnections(self) -> None:              # -- Initiates connections between widgets and functions
        self.eventTypeCombo.currentIndexChanged.connect(self.changeActiveEvent)

    def initLayouts(self) -> None:                  # -- Initiates the layouts
        self.mainLayout: QVBoxLayout = QVBoxLayout()

    def ApplyLayouts(self) -> None:             # -- Applies widgets to the layouts/applies the main layout
        self.mainLayout.addWidget(self.eventTypeCombo)
        self.mainLayout.addWidget(self.applicaitonDict["to do list"])
        self.mainLayout.addWidget(self.applicaitonDict["event"])
        self.mainLayout.addWidget(self.applicaitonDict["note"])

        self.setLayout(self.mainLayout)

    def changeActiveEvent(self) -> None:            # -- Triggers when the event type is changed in the combo box
        currentIndex: int = self.eventTypeCombo.currentIndex()
        currentSelection: str = self.eventTypeCombo.itemText(currentIndex)

        for app in self.applicaitonDict.values():
            app.hide()

        if currentSelection.lower != "no selection":
            self.applicaitonDict[currentSelection.lower()].show()
        

if __name__ ==  "__main__":
    app = QApplication(sys.argv)
    createAnAccount: CreateAnAccount = CreateNewEvent() #CreateAnAccount()
    createAnAccount.show()
    sys.exit(app.exec())