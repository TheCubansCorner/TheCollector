#! python3, PyQt6
#! homePage.py -- main calandar page

import os, sys, datetime

from PyQt6.QtWidgets import (
    QWidget, QApplication, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel
)

"""
Calculating if it is a leap year
Rule 1: Divisible by 4: If a year is evenly divisible by 4, it's generally considered a leap year.
Rule 2: Divisible by 100: If a year is evenly divisible by 100 (a century year), it's not a leap year unless it also meets the next condition.
Rule 3: Divisible by 400: If a century year is also evenly divisible by 400, it is considered a leap year.
"""

"""
- Needs to determine if it is a leap year (Check)
- Needs to determine how many days in a month (Check)
- Needs to determine what day of the week the months starts on (check)

Process
- Needs to generate the days of the week in labels 
- will need to confirm what the first day of the month fell on
- create buttons for every day in the month with the day of the month inserted 
- need to add buttons to go forward and back on the months
- when a day is clicked it should open up a list with a breakdown of the day starting from 12AM to 12PM

"""

class Schedule(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.currentYear: str = datetime.datetime.now().year
        self.weekdays: list = ["Monday", " Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.monthList: list = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
            ]
        self.dayCount: dict = {
            "January" : 31, "February" : 29 if self.isLeapYear(self.currentYear) else 28,
            "March" : 31, "April" : 30, "May" : 31, "June" : 30,
            "July" : 31, "August" : 31, "September" : 30, "October" : 31,
            "November" : 30, "December" : 31
        }
        self.dataBass: None
        self.userId: int = None
        self.initApplication()

    def initApplication(self) -> None:
        self.initWidgets()
        self.initEditWidgets()
        self.initToolTips()
        self.initLayouts()
        self.initApplyLayout()

    def initWidgets(self) -> None:
        self.monthYearLabel: QLabel = QLabel()

    def initEditWidgets(self) -> None:
        self.monthYearLabel.setText(self.currentMonthToBeDisplayed())

    def initToolTips(self) -> None:
        pass

    def initLayouts(self) -> None:
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.calandarMonthLabel: QVBoxLayout = QVBoxLayout()

        
    def initApplyLayout(self) -> None:
        self.mainLayout.addLayout(self.calandarMonthLabel)

        self.calandarMonthLabel.addWidget(self.monthYearLabel)

        self.setLayout(self.mainLayout)

    def isLeapYear(self, year: int) -> bool:
        return year % 4 == 0
    
    def dayOfTheWeek(self, year: int, month: int, day: int) -> int:
        return datetime.datetime(year, month, day).weekday()
    
    def currentMonthToBeDisplayed(self) -> str:
        month: str = self.monthList[datetime.datetime.now().month - 1]
        year: str = datetime.datetime.now().year
        return f"{month} {year}"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    schedule: Schedule = Schedule()
    schedule.show()
    sys.exit(app.exec())