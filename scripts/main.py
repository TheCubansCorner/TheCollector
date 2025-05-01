#! python3, PyQt6
#! main.py -- Main applicaiton window


import os, sys, threading, time

from login import Login
from splashPage import SplashPage
from calandarWidget import Schedule

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QTabWidget, QPushButton,

)
from PyQt6.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.applications: dict = {
            "login" : Login,
            "splash page": SplashPage
        }
        self.login = self.applications["login"]()
        self.activeUser: int = None
        self.currentApp: int = "login"

        self.setWindowTitle("Some Sort Of App that does stuff and things for me")
        self.setCentralWidget(self.login)
        #self.showFullScreen()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loginListener)
        self.timer.start(200)

    def loginListener(self) -> None:
        if self.login.userId != None:
            self.activeUser = self.login.userId
            self.initWidgets()
            self.timer.stop()
        return

    def initWidgets(self) -> None:
        self.applicationTabs: QTabWidget = QTabWidget()
        self.initLayouts()

    def initLayouts(self) -> None:
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.applicationTabs)
        self.schedule: Schedule = Schedule()
        self.applicationTabs.addTab(self.schedule, "Home")
        
        self.setCentralWidget(self.applicationTabs)



if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    mainWindow: MainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())