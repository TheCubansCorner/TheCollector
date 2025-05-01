#! python3, PyQt6
#! formsAndDialogues -- Application storing the classes for all forms for the application and message Dialogues

import os, sys, sqlite3

from databaseQueries import DatabaseQueries
from PyQt6.QtCore import QTimer, QDate, QTime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QHBoxLayout, QFileDialog,
    QComboBox, QLineEdit, QTimeEdit, QDateEdit,
    QTextEdit, QListWidget
)

"""
TODO: There are several minor and major updates we should make to the different widgets to add more adjustability and alarms.
- WHen an event submission already exists it should give the option to replace the existing submission.
- submissions should check for conflicting times for events and todos.
- notes should not need to be checked for duplicate times or dates. Those bits of informaiton are strictly referencial for notes.
- Should be an option for setting alarms for events
"""

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
        self.currentTime: QTime.currentTime = QTime.currentTime()
        self.currentDate: QDate.currentDate = QDate.currentDate()
        self.todoString: str = ""
        self.todoList: list = []
        self.errorMessage: str = ""
        self.errorCode: str = ""
        self.initApplication()
        
    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.setWidgetToolTips()
        self.initConnections()
        self.initLayouts()
        self.ApplyLayouts()

    def initWidgets(self) -> None:
        self.timeLabel: QLabel = QLabel("Time:")
        self.dateLabel: QLabel = QLabel("Date:")
        self.titleLabel: QLabel = QLabel("Title:")
        self.errorLabel: QLabel = QLabel()
        
        self.timeEntry: QTimeEdit = QTimeEdit()
        self.dateEntry: QDateEdit = QDateEdit()
        self.titleEntry: QLineEdit = QLineEdit()
        self.toDoEntry: QLineEdit = QLineEdit()

        self.toDoListWidg: QListWidget = QListWidget()

        self.toDoBtn: QPushButton = QPushButton("+")

    def initEditWidgets(self) -> None:
        self.dateEntry.setDate(self.currentDate)
        self.timeEntry.setTime(self.currentTime)

    def setWidgetToolTips(self) -> None:
        self.timeLabel.setToolTip("Time")
        self.dateLabel.setToolTip("Date")
        self.titleLabel.setToolTip("Title")
        self.toDoListWidg.setToolTip("To Do List")
        self.timeEntry.setToolTip("Time Format HH:MM AM/PM")
        self.dateEntry.setToolTip("Date Format DD/MM/YYYY")
        self.titleEntry.setToolTip("Title of the to do list")
        self.toDoEntry.setToolTip("To Do to be added to the list.")
        self.toDoBtn.setToolTip("Add To Do to")

    def initConnections(self) -> None:
        self.toDoBtn.clicked.connect(self.addTodoTask)
        self.toDoListWidg.doubleClicked.connect(self.selectItem)
    
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
        self.mainLayout.addWidget(self.toDoListWidg)
        self.mainLayout.addWidget(self.errorLabel)

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
        if self.toDoEntry.text() == "":
            self.errorMessage = "You cannot add a blank task."
            self.errorCode = " 005,"
            self.errorLabel.setText(self.errorMessage)
            return
        
        self.todoString = f"- {self.toDoEntry.text()}"
        self.toDoListWidg.addItem(self.todoString)
        self.toDoEntry.clear()

    def checkEntries(self) -> list:
        self.errorMessage = ""
        self.errorCode = ""
        error: bool = False

        if self.dateEntry.text() == "":
            self.errorMessage += "*You must choose a valid date*\n"
            self.errorCode += " 001,"
            error = True
        
        if self.titleEntry.text() == "":
            self.errorMessage += "*You must provide a title*\n"
            self.errorCode += " 002,"
            error = True
        
        if self.toDoListWidg.count() == 0:
            self.errorMessage += "*You must have at least one thing to do.*\n"
            self.errorCode += " 003,"
            error = True

        if error:
            self.errorLabel.setText(self.errorMessage)
            return []
        
        toDoString: str = ""

        return [self.timeEntry.text(), self.dateEntry.text(), self.titleEntry.text(), self.getListItems()]

    def getListItems(self) -> str:
        toDoString: str = ""

        for inx in range(self.toDoListWidg.count()):
            toDoString += f"{self.toDoListWidg.item(inx).text()}\n"
        
        return toDoString

    def selectItem(self) -> None:
        currentItem = self.toDoListWidg.currentItem().text()
        self.selectItemWIndow: QWidget = QWidget()
        self.taskLabel: QLabel = QLabel()
        self.editBtn: QPushButton = QPushButton("Edit")
        self.deleteBtn: QPushButton = QPushButton("Delete")
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.labelLayout: QHBoxLayout = QVBoxLayout()
        self.btnLayout: QHBoxLayout = QHBoxLayout()
        self.deleteBtn.clicked.connect(self.deleteTask)
        self.editBtn.clicked.connect(self.editTask)
        self.taskLabel.setText(currentItem)
        self.mainLayout.addLayout(self.labelLayout)
        self.mainLayout.addLayout(self.btnLayout)
        
        self.btnLayout.addWidget(self.editBtn)
        self.btnLayout.addWidget(self.deleteBtn)
        self.labelLayout.addWidget(self.taskLabel)
        self.selectItemWIndow.setLayout(self.mainLayout)
        self.selectItemWIndow.show()
        self.setEnabled(False)

    def deleteTask(self) -> None:
        self.toDoListWidg.takeItem(self.toDoListWidg.currentRow())
        self.selectItemWIndow.close()
        self.setEnabled(True)

    def editTask(self) -> None:
        taskText: str = self.taskLabel.text().strip("-")

        self.editBtn.hide()
        self.deleteBtn.hide()
        self.taskLabel.hide()

        self.taskEntry: QTextEdit = QTextEdit()
        self.cancelBtn: QPushButton = QPushButton("Cancel")
        self.submitBtn: QPushButton = QPushButton("Submit")

        self.taskEntry.setText(taskText)

        self.cancelBtn.clicked.connect(self.cancelEdit)
        self.submitBtn.clicked.connect(self.submitEdit)

        self.labelLayout.addWidget(self.taskEntry)
        self.btnLayout.addWidget(self.submitBtn)
        self.btnLayout.addWidget(self.cancelBtn)

    def cancelEdit(self) -> None:
        self.taskEntry.hide()
        self.cancelBtn.hide()
        self.submitBtn.hide()
        self.editBtn.show()
        self.deleteBtn.show()
        self.taskLabel.show()

    def submitEdit(self) -> None:
        self.toDoListWidg.insertItem(self.toDoListWidg.currentRow(), f"-{self.taskEntry.toPlainText()}")
        self.toDoListWidg.takeItem(self.toDoListWidg.currentRow())
        self.selectItemWIndow.close()
        self.setEnabled(True)
        

class DailyEvent(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Time, Date, Title, event description
        self.initApplication()
        self.errorMessage: str = "Unknown"
        self.errorCode: str = "Unknown"
        #TODO: Add start and end time for events

    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.initConnections()
        self.initLayouts()
        self.ApplyLayouts()

    def initWidgets(self) -> None:
        self.startTimeLabel: QLabel = QLabel("Start Time:")
        self.endTimeLabel: QLabel = QLabel("End Time:")
        self.dateLabel: QLabel = QLabel("Date: ")
        self.titleLabel: QLabel = QLabel("Title")
        self.descriptionLabel: QLabel = QLabel("Description")
        self.errorLabel: QLabel = QLabel()

        self.starttimeEntry: QTimeEdit = QTimeEdit()
        self.endTimeEntry: QTimeEdit = QTimeEdit()
        self.dateEntry: QDateEdit = QDateEdit()
        self.titleEntry: QLineEdit = QLineEdit()
        self.descriptionEntry: QTextEdit = QTextEdit()

    def initEditWidgets(self) -> None:
        pass

    def setWidgetToolTips(self) -> None:
        self.startTimeLabel.setToolTip("Event Start Time")
        self.endTimeLabel.setToolTip("Event End Time")
        self.dateLabel.setToolTip("Date of the Event")
        self.titleLabel.setToolTip("Title")
        self.descriptionLabel.setToolTip("Description")
        self.errorLabel.setToolTip(f"Error Code: {self.errorCode} -- {self.errorMessage}")

    def initConnections(self) -> None:
        pass
    
    def initLayouts(self) -> None:
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.startLayout: QHBoxLayout = QHBoxLayout()
        self.endLayout: QHBoxLayout = QHBoxLayout()
        self.dateLayout: QHBoxLayout = QHBoxLayout()
        self.descriptionLayout: QVBoxLayout = QVBoxLayout()
        self.titleLayout: QHBoxLayout = QHBoxLayout()

    def ApplyLayouts(self) -> None:
        self.mainLayout.addLayout(self.startLayout)
        self.mainLayout.addLayout(self.endLayout)
        self.mainLayout.addLayout(self.dateLayout)
        self.mainLayout.addLayout(self.titleLayout)
        self.mainLayout.addLayout(self.descriptionLayout)
        self.mainLayout.addWidget(self.errorLabel)
        
        self.mainLayout.addWidget(self.errorLabel)

        self.startLayout.addWidget(self.startTimeLabel)
        self.startLayout.addWidget(self.starttimeEntry)

        self.endLayout.addWidget(self.endTimeLabel)
        self.endLayout.addWidget(self.endTimeEntry)

        self.dateLayout.addWidget(self.dateLabel)
        self.dateLayout.addWidget(self.dateEntry)

        self.titleLayout.addWidget(self.titleLabel)
        self.titleLayout.addWidget(self.titleEntry)

        self.descriptionLayout.addWidget(self.descriptionLabel)
        self.descriptionLayout.addWidget(self.descriptionEntry)

        self.setLayout(self.mainLayout)

    def checkEntries(self) -> list:
        self.errorMessage = ""
        self.errorCode = ""
        error: bool = False

        self.errorLabel.clear()

        if self.titleEntry.text() == "":
            self.errorMessage += "*You must provide a title.*\n"
            self.errorCode += " 002,"
            error = True

        if self.descriptionEntry.toPlainText() == "":
            self.errorMessage += "*You must provide a description.*\n"
            self.errorCode += " 004,"
            error = True
        
        if error:
            self.errorLabel.setText(self.errorMessage)
            return []
        
        return [self.starttimeEntry.text(), self.endTimeEntry.text(), self.dateEntry.text(),
                self.titleEntry.text(), self.descriptionEntry.toPlainText()
                ]


class Note(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Time, Date, Title, Body
        self.errorMessage: str = ""
        self.errorCode: str = ""
        self.initApplication()

    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.initConnections()
        self.initLayouts()
        self.ApplyLayouts()

    def initWidgets(self) -> None:
        self.timeLabel: QLabel = QLabel("Time")
        self.dateLabel: QLabel = QLabel("Date")
        self.titleLabel: QLabel = QLabel("Title")
        self.descriptionLabel: QLabel = QLabel("Description")
        self.errorLabel: QLabel = QLabel()
        
        self.timeEntry: QTimeEdit = QTimeEdit()
        self.dateEntry: QDateEdit = QDateEdit()
        self.titleEntry: QLineEdit = QLineEdit()
        self.descriptionEntry: QTextEdit = QTextEdit()

    def initEditWidgets(self) -> None:
        pass

    def setWidgetToolTips(self) -> None:
        pass

    def initConnections(self) -> None:
        pass
    
    def initLayouts(self) -> None:
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.timeLayout: QHBoxLayout = QHBoxLayout()
        self.dateLayout: QHBoxLayout = QHBoxLayout()
        self.titleLayout: QHBoxLayout = QHBoxLayout()
        self.desciptionLayout: QVBoxLayout = QVBoxLayout()

    def ApplyLayouts(self) -> None:
        self.mainLayout.addLayout(self.timeLayout)
        self.mainLayout.addLayout(self.dateLayout)
        self.mainLayout.addLayout(self.titleLayout)
        self.mainLayout.addLayout(self.desciptionLayout)
        self.mainLayout.addWidget(self.errorLabel)

        self.timeLayout.addWidget(self.timeLabel)
        self.timeLayout.addWidget(self.timeEntry)

        self.dateLayout.addWidget(self.dateLabel)
        self.dateLayout.addWidget(self.dateEntry)

        self.titleLayout.addWidget(self.titleLabel)
        self.titleLayout.addWidget(self.titleEntry)

        self.desciptionLayout.addWidget(self.descriptionLabel)
        self.desciptionLayout.addWidget(self.descriptionEntry)

        self.setLayout(self.mainLayout)

    def checkEntries(self) -> list:
        self.errorMessage = ""
        error: bool = False
        if self.titleEntry.text() == "":
            self.errorMessage += "*You must provide a Title*\n"
            self.errorCode += " 002,"
            error = True

        if self.descriptionEntry.toPlainText() == "":
            self.errorMessage += "*You must provide a Description*\n"
            self.errorCode += " 004,"
            error = True

        if error:
            self.errorLabel.setText(self.errorMessage)
            return []
        
        return [self.timeEntry.text(), self.dateEntry.text(), self.titleEntry.text(), self.descriptionEntry.toPlainText()]


class CreateNewEvent(QWidget):
    def __init__(self, userID: int) -> None:
        super().__init__()
        self.dataBass = DatabaseQueries()
        self.userID = userID
        self.currentSelection: str = "no selection"
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
        self.errorLabel: QLabel = QLabel()
        self.eventTypeCombo: QComboBox = QComboBox()

        self.submitBtn: QPushButton = QPushButton("Submit")

    def initEditWidgets(self) -> None:                  # -- Edits widgets before applying them
        self.eventTypeCombo.addItem("No Selection")
        self.eventTypeCombo.addItem("To Do List")
        self.eventTypeCombo.addItem("Event")
        self.eventTypeCombo.addItem("Note")

        for app in self.applicaitonDict.values():
            app.hide()

    def initConnections(self) -> None:                  # -- Initiates connections between widgets and functions
        self.eventTypeCombo.currentIndexChanged.connect(self.changeActiveEvent)
        self.submitBtn.clicked.connect(self.submitInformation)

    def initLayouts(self) -> None:                      # -- Initiates the layouts
        self.mainLayout: QVBoxLayout = QVBoxLayout()

    def ApplyLayouts(self) -> None:                     # -- Applies widgets to the layouts/applies the main layout
        self.mainLayout.addWidget(self.eventTypeCombo)
        self.mainLayout.addWidget(self.applicaitonDict["to do list"])
        self.mainLayout.addWidget(self.applicaitonDict["event"])
        self.mainLayout.addWidget(self.applicaitonDict["note"])
        self.mainLayout.addWidget(self.submitBtn)

        self.setLayout(self.mainLayout)

    def changeActiveEvent(self) -> None:                # -- Triggers when the event type is changed in the combo box
        currentIndex: int = self.eventTypeCombo.currentIndex()
        currentSelection: str = self.eventTypeCombo.itemText(currentIndex)

        for app in self.applicaitonDict.values():
            app.hide()

        if currentSelection.lower() != "no selection":
            self.currentSelection = currentSelection.lower()
            self.applicaitonDict[self.currentSelection].show()
        else:
            self.currentSelection = "no selection"
        
        self.applicaitonDict[self.currentSelection].errorLabel.clear()      # Clears Error Messages

    def submitInformation(self) -> None:                # -- 
        if self.currentSelection == "no selection":
            return
        
        currentSubmittionInformation: list = self.applicaitonDict[self.currentSelection].checkEntries()
        if len(currentSubmittionInformation) > 0:    
            if self.currentSelection == "to do list":
                # Time, Date, Title, To Do (str)
                success: bool = self.dataBass.submitEventInformation((self.userID,) + tuple(currentSubmittionInformation), "to do list")
            elif self.currentSelection == "event":
                # Start Time, End Time, date, title, description
                success: bool = self.dataBass.submitEventInformation((self.userID,) + tuple(currentSubmittionInformation), "event")
            elif self.currentSelection == "note":
                # Time, Date, Title Description
                success: bool = self.dataBass.submitEventInformation((self.userID,) + tuple(currentSubmittionInformation), "note")
            else:
                self.applicaitonDict[self.currentSelection].errorLabel.setText("You have to submit at least one input")
                return

            if success:
                pass
                #self.close()
            else:
                self.applicaitonDict[self.currentSelection].errorLabel.setText("This submission conflicts with a previous submission")
        

if __name__ ==  "__main__":
    #Test
    db = DatabaseQueries()
    app = QApplication(sys.argv)
    createAnAccount: CreateAnAccount = CreateNewEvent(1) #CreateAnAccount()
    createAnAccount.show()
    sys.exit(app.exec())