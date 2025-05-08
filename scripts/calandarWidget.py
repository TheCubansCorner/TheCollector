#! python3, PyQt6
#! calandarWidget.py -- main calandar widget

import os, sys, datetime, calendar

from datetime import timedelta
from formsAndDialogues import CreateNewEvent
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import (
    QWidget, QApplication, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QFrame, QScrollArea, QScrollBar
)

"""
Calculating if it is a leap year 101: 
#####################################
- Rule 1: Divisible by 4: If a year is evenly divisible by 4, it's generally considered a leap year.
- Rule 2: Divisible by 100: If a year is evenly divisible by 100 (a century year), it's not a leap year unless it also meets the next condition.
- Rule 3: Divisible by 400: If a century year is also evenly divisible by 400, it is considered a leap year.
"""

#TODO -- Create a module that shows the individual day selected within the month CurrentDaysSchedule(year, month, day)
#TODO -- add button connections to open the scheduled day
#TODO -- Make the Calendar highlight the current day when opened
#TODO -- Find a way to make days that have passed. 
#TODO -- Find a way to format the calendar in Sunday to Saturday fashion

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button().__str__() == "MouseButton.LeftButton":  # Left mouse button
            self.clicked.emit()
        QLabel.mousePressEvent(self, event)


class CurrentDaysSchedule(QWidget):
    def __init__(self, date: tuple, userId: int) -> None:
        super().__init__()
        self.active: bool = True
        self.userId: int = userId
        self.widgetList: list = []
        self.date: tuple = date
        self.hoursList: list = self.generateTime(30)
        self.initApplication()
        
    def initApplication(self) -> None:
        self.initLayouts()
        self.initMainWidgets()
        self.initConnections()
        self.initApplyLayouts()
    
    def initMainWidgets(self) -> None:
        ###TEST###
        self.scrollArea: QScrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        ###TEST###

        self.backBtn: QPushButton = QPushButton("<-")
        self.dateLabel: QLabel = QLabel(f"{self.date[0]}/{self.date[1]}/{self.date[2]}")
        self.previousDayBtn: QPushButton = QPushButton("<<")
        self.nextDayBtn: QPushButton = QPushButton(">>")
        self.timeLabelList: list = self.generateTimeLabelsList()
        self.widgetList = [self.backBtn, self.dateLabel, self.previousDayBtn, self.nextDayBtn] + self.timeLabelList

    def initTooltips(self) -> None:
        self.backBtn.setToolTip("Return to main Calendar")
        self.dateLabel.setToolTip("Current Date")
        self.previousDayBtn.setToolTip("Go to previous Day")
        self.nextDayBtn.setToolTip("Go to next Day")

    def initConnections(self) -> None:
        self.backBtn.clicked.connect(self.closeApplication)

    def initLayouts(self) -> None:
        self.mainLayout: QVBoxLayout = QVBoxLayout()
        self.taskBarLayout: QHBoxLayout = QHBoxLayout()
        self.timesLayout: QVBoxLayout = QVBoxLayout()

    def initApplyLayouts(self) -> None:
        self.taskBarLayout.addWidget(self.backBtn)
        self.taskBarLayout.addWidget(self.dateLabel)
        self.taskBarLayout.addWidget(self.previousDayBtn)
        self.taskBarLayout.addWidget(self.nextDayBtn)

        self.mainLayout.addLayout(self.taskBarLayout)
        self.mainLayout.addLayout(self.timesLayout)

        ###TEST###
        self.mainLayout.addWidget(self.scrollArea)

        self.setLayout(self.mainLayout)

    def closeApplication(self) -> None:
        self.active = False
        self.close()
        
    def generateTime(self, interval_minutes):
        start_time = datetime.datetime.strptime("00:00", "%H:%M")
        end_time = datetime.datetime.strptime("11:30", "%H:%M")
        times = []
        current_time = start_time

        while current_time <= end_time:
            current: str = current_time.strftime("%H:%M")
            if current[:2] != "00":
                times.append(current)
            else:
                times.append(f"12{current[2::]}")

            current_time += timedelta(minutes=interval_minutes)

        times = self.formatTimes(times)

        return times

    def formatTimes(self, timeList: list, count: int = 2, newList: list = []) -> list:
        for time in timeList:
            if count == 2: 
                newList.append(time + " AM")

            if count == 1:
                newList.append(time + " PM")

        count -= 1

        if count > 0:
            self.formatTimes(timeList, count, newList)

        return newList
    
    def generateTimeLabelsList(self) -> list:
        widgList: list = []
        contentWidget: QWidget = QWidget()
        contentLayout: QVBoxLayout = QVBoxLayout()
        contentWidget.setLayout(contentLayout)

        for time in self.hoursList:
            label: ClickableLabel = ClickableLabel(time)
            label.clicked.connect(lambda text = time: self.timeClicked(text))
            line = QFrame()
            line.setFrameShape(QFrame.Shape.HLine)
            line.setFrameShadow(QFrame.Shadow.Sunken)
            contentLayout.addWidget(label)
            contentLayout.addWidget(line)
            widgList.append(label)
            widgList.append(line)
        
        self.scrollArea.setWidget(contentWidget)

        return widgList
    
    def timeClicked(self, time) -> None:
        print(time)


class Schedule(QWidget):
    def __init__(self, userID: int) -> None:
        super().__init__()
        self.fullWidgetList: list = []
        self.dayWidgetList: list = []
        self.weekdays: list = ["Sunday", "Monday", " Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
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
        self.userId: int = userID
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

        self.fullWidgetList = self.fullWidgetList + [self.monthYearLabel, self.previousMonthBtn, self.forwardMonthBtn]

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
        self.individualDayLayout: QVBoxLayout = QVBoxLayout()
        
    def initApplyLayout(self) -> None:
        self.mainLayout.addLayout(self.calandarMonthLayout)
        self.mainLayout.addLayout(self.weekdayLayout)
        self.mainLayout.addLayout(self.daysLayout)
        self.mainLayout.addLayout(self.individualDayLayout)

        for day in self.weekdays:
            label: QLabel = QLabel(day)
            self.weekdayLayout.addWidget(label)
            self.fullWidgetList.append(label)
            
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
        previousMonthEndInfo: int = self.dayCount[self.monthList[self.currentMonthSelection - 1]]
        weekdayCounter: int = 0
        tempPreviousMonthList: list = []

        if startDay == 6:
            startDay = 0
        else:
            startDay += 1
   
        if self.currentMonthSelection == 1:
            numberOfDays: int = self.isLeapYear(self.currentYearSelection)
        else:
            numberOfDays: int = self.dayCount[self.monthList[self.currentMonthSelection]]

        if startDay != 0:
            for _ in range(startDay):
                tempPreviousMonthList.append(previousMonthEndInfo)
                previousMonthEndInfo -= 1

            for day in tempPreviousMonthList[::-1]:
                blankBox: QPushButton = QPushButton(str(day))
                blankBox.setEnabled(False)
                tempDayLayout.addWidget(blankBox)
                self.daysWidgets.append(blankBox)
                
                weekdayCounter += 1

        for day in range(1, numberOfDays + 1):
            if weekdayCounter > 6:
                weekdayCounter = 0
                self.daysLayout.addLayout(tempDayLayout)
                tempDayLayout = QHBoxLayout()
           
            dayBtn: QPushButton = QPushButton(f"{day}")
            dayBtn.clicked.connect((lambda checked, text = day: self.currentDaySelection(text)))
            tempDayLayout.addWidget(dayBtn)
            self.daysWidgets.append(dayBtn)
            weekdayCounter += 1
        
        endDays: int = 1
        while weekdayCounter <= 6:
            blankBox: QPushButton = QPushButton(f"{endDays}")
            blankBox.setEnabled(False)
            tempDayLayout.addWidget(blankBox)
            self.daysWidgets.append(blankBox)
            endDays += 1
            weekdayCounter += 1
        
        self.fullWidgetList = self.fullWidgetList + self.daysWidgets

        self.daysLayout.addLayout(tempDayLayout)

    def hideShowWidgets(self, hideShow: str) -> None:
        for widg in self.fullWidgetList:
            if hideShow == "hide":
                widg.hide()
            else:
                widg.show()
        
    def currentDaySelection(self, day: int) -> None:
        yearMonthDay: tuple = (self.currentMonthSelection + 1, day, self.currentYearSelection) 
        self.selectedDay: CurrentDaysSchedule = CurrentDaysSchedule(yearMonthDay, self.userId)

        self.hideShowWidgets("hide")
        self.individualDayLayout.addWidget(self.selectedDay)

        self.currentDayChecker: QTimer = QTimer()
        self.currentDayChecker.timeout.connect(self.currentDayActive)
        self.currentDayChecker.start(250)
    
    def currentDayActive(self) -> None:
        if self.selectedDay.active == False:
            self.hideShowWidgets("show")
            self.currentDayChecker.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    schedule: Schedule = Schedule(1)
    schedule.show()
    sys.exit(app.exec())
