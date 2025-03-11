#! python, PyQt6
#! collectionPage.py -- Widget that displays various collection lists for the user

import os, sys

from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout, QVBoxLayout, QWidget,
    QPushButton, QLabel, QLineEdit, QTextEdit, 
    QComboBox
)

class CollectionPage(QWidget):
    def __init__(self) -> None:                                         # -- Initiates Class Variables and functionality
        super().__init__()

    def initWidgets(self) -> None:                                      # -- Initiates all child widgets of the overall Widgets
        self.currentlistCombo: QComboBox = QComboBox()                  # -- Combo

        self.activeSelectionLabel: QLabel = QLabel()                    # -- Qlabel

        self.backBtn: QPushButton = QPushButton("<<<")                       # -- QPushbuttons
        self.logOut: QPushButton = QPushButton("Log Out")
        self.addBtn: QPushButton = QPushButton("Add")  

    def initEditWidgets(self) -> None:                                  # -- Initiates and applies all layouts to the main widget
        pass

    def initApplyLayout(self) -> None:                                  # -- Initiates and applies all layouts to the main widget
        pass


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    collectionPage: CollectionPage = CollectionPage()
    collectionPage.show()
    sys.exit(app.exec())