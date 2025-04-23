#! Python3, PyQt6
#! splashPage.py -- Home Page for when you log in. 


import os, sys

from databaseQueries import DatabaseQueries
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton
)


class SplashPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initApplication()

    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.initLayouts()
        self.initApplyLayouts()

    def initWidgets(self) -> None:
        self.homeBtn: QPushButton = QPushButton("Home")                         # -- Buttons
        self.addNewEventBtn: QPushButton = QPushButton("+")
        self.collectionAppBtn: QPushButton = QPushButton("Collection")

    def initEditWidgets(self) -> None:
        pass

    def initBtnConnections(self) -> None: 
        pass

    def initLayouts(self) -> None:
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.btnLayout: QHBoxLayout = QHBoxLayout()

    def initApplyLayouts(self) -> None:
        self.mainLayout.addLayout(self.btnLayout)
        self.btnLayout.addWidget(self.homeBtn)
        self.btnLayout.addWidget(self.addNewEventBtn)
        self.btnLayout.addWidget(self.collectionAppBtn)

        self.setLayout(self.mainLayout)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splashPage: SplashPage = SplashPage()
    splashPage.show()
    sys.exit(app.exec())