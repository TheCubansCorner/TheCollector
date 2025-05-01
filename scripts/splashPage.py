#! Python3, PyQt6
#! splashPage.py -- Home Page for when you log in. 


import os, sys

#from databaseQueries import DatabaseQueries
from formsAndDialogues import CreateNewEvent
from calandarWidget import Schedule
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTabWidget
)


class SplashPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initApplication()

    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.initLayouts()
        self.initBtnConnections()
        self.initApplyLayouts()

    def initWidgets(self) -> None:
        self.homeBtn: QPushButton = QPushButton("Home")                         # -- Buttons
        self.addNewEventBtn: QPushButton = QPushButton("+")
        self.collectionAppBtn: QPushButton = QPushButton("Collection")

        self.mainWindowTabWidget: QTabWidget = QTabWidget()

    def initEditWidgets(self) -> None:
        self.schedule: Schedule = Schedule()
        self.mainWindowTabWidget.addTab(self.schedule, "Home")

    def initBtnConnections(self) -> None: 
        self.addNewEventBtn.clicked.connect(self.addNewEvent)

    def initLayouts(self) -> None:
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.btnLayout: QHBoxLayout = QHBoxLayout()
        self.tabLayout: QHBoxLayout = QHBoxLayout()

    def initApplyLayouts(self) -> None:
        self.mainLayout.addLayout(self.btnLayout)
        self.mainLayout.addLayout(self.tabLayout)
        
        self.btnLayout.addWidget(self.homeBtn)
        self.btnLayout.addWidget(self.addNewEventBtn)
        self.btnLayout.addWidget(self.collectionAppBtn)

        self.tabLayout.addWidget(self.mainWindowTabWidget)

        self.setLayout(self.mainLayout)

    def addNewEvent(self) -> None:
        self.newEventDialogue: CreateNewEvent = CreateNewEvent(1)
        self.mainWindowTabWidget.addTab(self.newEventDialogue, "New Task")
        #self.newEventDialogue.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splashPage: SplashPage = SplashPage()
    splashPage.show()
    sys.exit(app.exec())