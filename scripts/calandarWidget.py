#! python3, PyQt6
#! calandarWidget.py -- main calandar widget

import os, sys, datetime, calendar

from PyQt6.QtWidgets import (
    QWidget, QApplication, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel
)

"""
Calculating if it is a leap year 101: 
#####################################
- Rule 1: Divisible by 4: If a year is evenly divisible by 4, it's generally considered a leap year.
- Rule 2: Divisible by 100: If a year is evenly divisible by 100 (a century year), it's not a leap year unless it also meets the next condition.
- Rule 3: Divisible by 400: If a century year is also evenly divisible by 400, it is considered a leap year.
"""

#TODO -- add button connections to open the scheduled day
#TODO -- Make the Calendar highlight the current day when opened
#TODO -- Find a way to make days that have passed. 
#TODO -- Find a way to format the calendar in Sunday to Saturday fashion

class Schedule(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.dayWidgetList: list = []
        self.weekdays: list = ["Monday", " Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.monthList: list = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
            ]
        self.currentMonthSelection: int = datetime.datetime.now().month - 1
        self.currentYearSelection: str = datetime.datetime.now().year
        self.dayCount: dict = {
            "January" : 31, "February" : self.isLeapYear(self.currentYearSelection),
            "March" : 31, "April" : 30, "May" : 31, "June" : 30,
            "July" : 31, "August" : 31, "September" : 30, "October" : 31,
            "November" : 30, "December" : 31
        }
        self.currentDaysInMonth: int = self.dayCount[self.monthList[self.currentMonthSelection]]
        
        self.dataBass: None
        self.userId: int = None
        self.initApplication()

    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.initToolTips()
        self.initConnections()
        self.initLayouts()
        self.drawMonth()
        self.initApplyLayout()

    def initWidgets(self) -> None:
        self.monthYearLabel: QLabel = QLabel()
        self.previousMonthBtn: QPushButton = QPushButton("<<")
        self.forwardMonthBtn: QPushButton = QPushButton(">>")

    def initEditWidgets(self) -> None:
        self.monthYearLabel.setText(self.currentMonthToDisplay())

    def initToolTips(self) -> None:
        pass

    def initConnections(self) -> None:
        self.previousMonthBtn.clicked.connect(lambda: self.changeMonth("<"))
        self.forwardMonthBtn.clicked.connect(lambda: self.changeMonth(">"))

    def initLayouts(self) -> None:
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.weekdayLayout: QHBoxLayout = QHBoxLayout()
        self.daysLayout: QVBoxLayout = QVBoxLayout()
        self.calandarMonthLayout: QHBoxLayout = QHBoxLayout()
        
    def initApplyLayout(self) -> None:
        self.mainLayout.addLayout(self.calandarMonthLayout)
        self.mainLayout.addLayout(self.weekdayLayout)
        self.mainLayout.addLayout(self.daysLayout)

        for day in self.weekdays:
            label: QLabel = QLabel(day)
            self.weekdayLayout.addWidget(label)
            
        self.calandarMonthLayout.addWidget(self.previousMonthBtn)
        self.calandarMonthLayout.addWidget(self.monthYearLabel)
        self.calandarMonthLayout.addWidget(self.forwardMonthBtn)

        self.setLayout(self.mainLayout)

    def isLeapYear(self, year: int) -> int:
        if year % 4 == 0:
            return 29
        
        return 28
    
    def dayOfTheWeek(self, year: int, month: int, day: int) -> int:
        return datetime.datetime(year, month, day).weekday()
    
    def currentMonthToDisplay(self) -> str:
        month: str = self.monthList[self.currentMonthSelection]
        
        return f"{month} {self.currentYearSelection}"

    def changeMonth(self, direction: str) -> None:
        if direction == "<":
            self.currentMonthSelection -= 1
 
            if self.currentMonthSelection < 0:
                self.currentMonthSelection = 11
                self.currentYearSelection = int(self.currentYearSelection) - 1
            
            self.monthYearLabel.setText(f"{self.monthList[self.currentMonthSelection]} {self.currentYearSelection}")

        if direction == ">":
            self.currentMonthSelection += 1
        
            if self.currentMonthSelection > 11:
                self.currentMonthSelection = 0
                self.currentYearSelection = int(self.currentYearSelection) + 1   

            self.monthYearLabel.setText(f"{self.monthList[self.currentMonthSelection]} {self.currentYearSelection}")

        for btn in self.daysWidgets:
            btn.close()

        self.drawMonth()

    def drawMonth(self) -> None:
        self.daysWidgets: list = []
        tempDayLayout: QHBoxLayout = QHBoxLayout()
        startDay: int = calendar.monthrange(self.currentYearSelection, self.currentMonthSelection + 1)[0]
        weekdayCounter: int = 0
        previousMonthEndInfo: int = self.dayCount[self.monthList[self.currentMonthSelection - 1]]
        tempPreviousMonthList: list = []

        if self.currentMonthSelection == 1:
            numberOfDays: int = self.isLeapYear(self.currentYearSelection)
        else:
            numberOfDays: int = self.dayCount[self.monthList[self.currentMonthSelection]]

        for _ in range(startDay):
            tempPreviousMonthList.append(previousMonthEndInfo)
            previousMonthEndInfo -= 1

        for day in tempPreviousMonthList[::-1]:
            blankBox: QPushButton = QPushButton(str(day))
            tempDayLayout.addWidget(blankBox)
            self.daysWidgets.append(blankBox)
            
            weekdayCounter += 1

        for day in range(1, numberOfDays + 1):
            if weekdayCounter > 6:
                weekdayCounter = 0
                self.daysLayout.addLayout(tempDayLayout)
                tempDayLayout = QHBoxLayout()
                

            dayBtn: QPushButton = QPushButton(f"{day}")
            tempDayLayout.addWidget(dayBtn)
            self.daysWidgets.append(dayBtn)
            weekdayCounter += 1
        
        endDays: int = 1
        while weekdayCounter <= 6:
            blankBox: QPushButton = QPushButton(f"{endDays}")
            tempDayLayout.addWidget(blankBox)
            self.daysWidgets.append(blankBox)
            endDays += 1
            weekdayCounter += 1

        
        self.daysLayout.addLayout(tempDayLayout)

    def currentDaySelection(self) -> None:
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    schedule: Schedule = Schedule()
    schedule.show()
    sys.exit(app.exec())