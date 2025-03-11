#! python, PyQt6
#! collectionPage.py -- Widget that displays various collection lists for the user

import os, sys

from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout, QVBoxLayout, QWidget,
    QPushButton, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QListWidget
)

class CollectionPage(QWidget):
    def __init__(self) -> None:                                         # -- Initiates Class Variables and functionality
        super().__init__()
        self.collectionComboInfo: list = [
            "Movies", " Video Games", "Records", "Cassettes",
            "CD", "Toys", "Manga", "Comics"
        ]
        
        self.testGenreList: list = [
            "Alphabetical", "Horror", "Comedy", "Suspence",
            "Romance", "Musical"
        ]

        self.initWidgets()
        self.initEditWidgets()
        self.initApplyLayout()

    def initWidgets(self) -> None:                                      # -- Initiates all child widgets of the overall Widgets
        self.currentGenreCombo: QComboBox = QComboBox()                 # -- QCombobox
        self.currentCollectionCombo: QComboBox = QComboBox()

        self.currentCollectioniList: QListWidget = QListWidget()        # -- QListWidget

        self.activeSelectionLabel: QLabel = QLabel("Under Construction")                    # -- Qlabel

        self.backBtn: QPushButton = QPushButton("<<<")                  # -- QPushbuttons
        self.logOutBtn: QPushButton = QPushButton("Log Out")
        self.addBtn: QPushButton = QPushButton("Add")  

    def initEditWidgets(self) -> None:                                  # -- Initiates and applies all layouts to the main widget
        for collection in self.collectionComboInfo:
            self.currentCollectionCombo.addItem(collection)

        for genre in self.testGenreList:
            self.currentGenreCombo.addItem(genre)

    def initApplyLayout(self) -> None:                                  # -- Initiates and applies all layouts to the main widget
        self.mainLayout: QHBoxLayout = QHBoxLayout()
        self.leftLayout: QVBoxLayout = QVBoxLayout()

        self.leftLayout.addWidget(self.currentCollectionCombo)
        self.leftLayout.addWidget(self.currentGenreCombo)
        self.leftLayout.addWidget(self.currentCollectioniList)
        self.leftLayout.addWidget(self.addBtn)
        self.leftLayout.addWidget(self.backBtn)
        self.leftLayout.addWidget(self.logOutBtn)

        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addWidget(self.activeSelectionLabel)

        self.setLayout(self.mainLayout)      

    def addCollectable(self) -> None:
        pass


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    collectionPage: CollectionPage = CollectionPage()
    collectionPage.show()
    sys.exit(app.exec())