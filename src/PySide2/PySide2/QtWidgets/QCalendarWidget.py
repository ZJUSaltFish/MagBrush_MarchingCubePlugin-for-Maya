# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QWidget import QWidget

class QCalendarWidget(QWidget):
    """ QCalendarWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def activated(self, *args, **kwargs): # real signature unknown
        pass

    def calendar(self): # real signature unknown; restored from __doc__
        """ calendar(self) -> PySide2.QtCore.QCalendar """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        pass

    def currentPageChanged(self, *args, **kwargs): # real signature unknown
        pass

    def dateEditAcceptDelay(self): # real signature unknown; restored from __doc__
        """ dateEditAcceptDelay(self) -> int """
        return 0

    def dateTextFormat(self): # real signature unknown; restored from __doc__
        """
        dateTextFormat(self) -> typing.Dict[PySide2.QtCore.QDate, PySide2.QtGui.QTextCharFormat]
        dateTextFormat(self, date: PySide2.QtCore.QDate) -> PySide2.QtGui.QTextCharFormat
        """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, watched, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, watched: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def firstDayOfWeek(self): # real signature unknown; restored from __doc__
        """ firstDayOfWeek(self) -> PySide2.QtCore.Qt.DayOfWeek """
        pass

    def headerTextFormat(self): # real signature unknown; restored from __doc__
        """ headerTextFormat(self) -> PySide2.QtGui.QTextCharFormat """
        pass

    def horizontalHeaderFormat(self): # real signature unknown; restored from __doc__
        """ horizontalHeaderFormat(self) -> PySide2.QtWidgets.QCalendarWidget.HorizontalHeaderFormat """
        pass

    def isDateEditEnabled(self): # real signature unknown; restored from __doc__
        """ isDateEditEnabled(self) -> bool """
        return False

    def isGridVisible(self): # real signature unknown; restored from __doc__
        """ isGridVisible(self) -> bool """
        return False

    def isNavigationBarVisible(self): # real signature unknown; restored from __doc__
        """ isNavigationBarVisible(self) -> bool """
        return False

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def maximumDate(self): # real signature unknown; restored from __doc__
        """ maximumDate(self) -> PySide2.QtCore.QDate """
        pass

    def minimumDate(self): # real signature unknown; restored from __doc__
        """ minimumDate(self) -> PySide2.QtCore.QDate """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def monthShown(self): # real signature unknown; restored from __doc__
        """ monthShown(self) -> int """
        return 0

    def mousePressEvent(self, event): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def paintCell(self, painter, rect, date): # real signature unknown; restored from __doc__
        """ paintCell(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, date: PySide2.QtCore.QDate) -> None """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def selectedDate(self): # real signature unknown; restored from __doc__
        """ selectedDate(self) -> PySide2.QtCore.QDate """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectionMode(self): # real signature unknown; restored from __doc__
        """ selectionMode(self) -> PySide2.QtWidgets.QCalendarWidget.SelectionMode """
        pass

    def setCalendar(self, calendar): # real signature unknown; restored from __doc__
        """ setCalendar(self, calendar: PySide2.QtCore.QCalendar) -> None """
        pass

    def setCurrentPage(self, year, month): # real signature unknown; restored from __doc__
        """ setCurrentPage(self, year: int, month: int) -> None """
        pass

    def setDateEditAcceptDelay(self, delay): # real signature unknown; restored from __doc__
        """ setDateEditAcceptDelay(self, delay: int) -> None """
        pass

    def setDateEditEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setDateEditEnabled(self, enable: bool) -> None """
        pass

    def setDateRange(self, min, max): # real signature unknown; restored from __doc__
        """ setDateRange(self, min: PySide2.QtCore.QDate, max: PySide2.QtCore.QDate) -> None """
        pass

    def setDateTextFormat(self, date, format): # real signature unknown; restored from __doc__
        """ setDateTextFormat(self, date: PySide2.QtCore.QDate, format: PySide2.QtGui.QTextCharFormat) -> None """
        pass

    def setFirstDayOfWeek(self, dayOfWeek): # real signature unknown; restored from __doc__
        """ setFirstDayOfWeek(self, dayOfWeek: PySide2.QtCore.Qt.DayOfWeek) -> None """
        pass

    def setGridVisible(self, show): # real signature unknown; restored from __doc__
        """ setGridVisible(self, show: bool) -> None """
        pass

    def setHeaderTextFormat(self, format): # real signature unknown; restored from __doc__
        """ setHeaderTextFormat(self, format: PySide2.QtGui.QTextCharFormat) -> None """
        pass

    def setHorizontalHeaderFormat(self, format): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderFormat(self, format: PySide2.QtWidgets.QCalendarWidget.HorizontalHeaderFormat) -> None """
        pass

    def setMaximumDate(self, date): # real signature unknown; restored from __doc__
        """ setMaximumDate(self, date: PySide2.QtCore.QDate) -> None """
        pass

    def setMinimumDate(self, date): # real signature unknown; restored from __doc__
        """ setMinimumDate(self, date: PySide2.QtCore.QDate) -> None """
        pass

    def setNavigationBarVisible(self, visible): # real signature unknown; restored from __doc__
        """ setNavigationBarVisible(self, visible: bool) -> None """
        pass

    def setSelectedDate(self, date): # real signature unknown; restored from __doc__
        """ setSelectedDate(self, date: PySide2.QtCore.QDate) -> None """
        pass

    def setSelectionMode(self, mode): # real signature unknown; restored from __doc__
        """ setSelectionMode(self, mode: PySide2.QtWidgets.QCalendarWidget.SelectionMode) -> None """
        pass

    def setVerticalHeaderFormat(self, format): # real signature unknown; restored from __doc__
        """ setVerticalHeaderFormat(self, format: PySide2.QtWidgets.QCalendarWidget.VerticalHeaderFormat) -> None """
        pass

    def setWeekdayTextFormat(self, dayOfWeek, format): # real signature unknown; restored from __doc__
        """ setWeekdayTextFormat(self, dayOfWeek: PySide2.QtCore.Qt.DayOfWeek, format: PySide2.QtGui.QTextCharFormat) -> None """
        pass

    def showNextMonth(self): # real signature unknown; restored from __doc__
        """ showNextMonth(self) -> None """
        pass

    def showNextYear(self): # real signature unknown; restored from __doc__
        """ showNextYear(self) -> None """
        pass

    def showPreviousMonth(self): # real signature unknown; restored from __doc__
        """ showPreviousMonth(self) -> None """
        pass

    def showPreviousYear(self): # real signature unknown; restored from __doc__
        """ showPreviousYear(self) -> None """
        pass

    def showSelectedDate(self): # real signature unknown; restored from __doc__
        """ showSelectedDate(self) -> None """
        pass

    def showToday(self): # real signature unknown; restored from __doc__
        """ showToday(self) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def updateCell(self, date): # real signature unknown; restored from __doc__
        """ updateCell(self, date: PySide2.QtCore.QDate) -> None """
        pass

    def updateCells(self): # real signature unknown; restored from __doc__
        """ updateCells(self) -> None """
        pass

    def verticalHeaderFormat(self): # real signature unknown; restored from __doc__
        """ verticalHeaderFormat(self) -> PySide2.QtWidgets.QCalendarWidget.VerticalHeaderFormat """
        pass

    def weekdayTextFormat(self, dayOfWeek): # real signature unknown; restored from __doc__
        """ weekdayTextFormat(self, dayOfWeek: PySide2.QtCore.Qt.DayOfWeek) -> PySide2.QtGui.QTextCharFormat """
        pass

    def yearShown(self): # real signature unknown; restored from __doc__
        """ yearShown(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    HorizontalHeaderFormat = None # (!) real value is "<class 'PySide2.QtWidgets.QCalendarWidget.HorizontalHeaderFormat'>"
    ISOWeekNumbers = PySide2.QtWidgets.QCalendarWidget.VerticalHeaderFormat.ISOWeekNumbers
    LongDayNames = PySide2.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.LongDayNames
    NoHorizontalHeader = PySide2.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader
    NoSelection = PySide2.QtWidgets.QCalendarWidget.SelectionMode.NoSelection
    NoVerticalHeader = PySide2.QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader
    SelectionMode = None # (!) real value is "<class 'PySide2.QtWidgets.QCalendarWidget.SelectionMode'>"
    ShortDayNames = PySide2.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames
    SingleLetterDayNames = PySide2.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.SingleLetterDayNames
    SingleSelection = PySide2.QtWidgets.QCalendarWidget.SelectionMode.SingleSelection
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507BFC80>'
    VerticalHeaderFormat = None # (!) real value is "<class 'PySide2.QtWidgets.QCalendarWidget.VerticalHeaderFormat'>"


