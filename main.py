#! python3, PyQt6
#! main.py -- Main applicaiton window


import os, sys

from scripts.login import Login
from scripts.databaseQueries import DatabaseQueries
from PyQt6.QtWidgets import (
    QApplication, QMainWindow
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.dataBass: DatabaseQueries = DatabaseQueries()
        self.login = Login(self.dataBass)
        self.setCentralWidget(self.login)


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    mainWindow: MainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())