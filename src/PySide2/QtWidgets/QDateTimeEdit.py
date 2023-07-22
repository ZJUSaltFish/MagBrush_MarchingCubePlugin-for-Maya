# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractSpinBox import QAbstractSpinBox

class QDateTimeEdit(QAbstractSpinBox):
    """
    QDateTimeEdit(self, d: PySide2.QtCore.QDate, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QDateTimeEdit(self, dt: PySide2.QtCore.QDateTime, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QDateTimeEdit(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QDateTimeEdit(self, t: PySide2.QtCore.QTime, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QDateTimeEdit(self, val: typing.Any, parserType: type, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def calendar(self): # real signature unknown; restored from __doc__
        """ calendar(self) -> PySide2.QtCore.QCalendar """
        pass

    def calendarPopup(self): # real signature unknown; restored from __doc__
        """ calendarPopup(self) -> bool """
        return False

    def calendarWidget(self): # real signature unknown; restored from __doc__
        """ calendarWidget(self) -> PySide2.QtWidgets.QCalendarWidget """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clearMaximumDate(self): # real signature unknown; restored from __doc__
        """ clearMaximumDate(self) -> None """
        pass

    def clearMaximumDateTime(self): # real signature unknown; restored from __doc__
        """ clearMaximumDateTime(self) -> None """
        pass

    def clearMaximumTime(self): # real signature unknown; restored from __doc__
        """ clearMaximumTime(self) -> None """
        pass

    def clearMinimumDate(self): # real signature unknown; restored from __doc__
        """ clearMinimumDate(self) -> None """
        pass

    def clearMinimumDateTime(self): # real signature unknown; restored from __doc__
        """ clearMinimumDateTime(self) -> None """
        pass

    def clearMinimumTime(self): # real signature unknown; restored from __doc__
        """ clearMinimumTime(self) -> None """
        pass

    def currentSection(self): # real signature unknown; restored from __doc__
        """ currentSection(self) -> PySide2.QtWidgets.QDateTimeEdit.Section """
        pass

    def currentSectionIndex(self): # real signature unknown; restored from __doc__
        """ currentSectionIndex(self) -> int """
        return 0

    def date(self): # real signature unknown; restored from __doc__
        """ date(self) -> PySide2.QtCore.QDate """
        pass

    def dateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def dateTime(self): # real signature unknown; restored from __doc__
        """ dateTime(self) -> PySide2.QtCore.QDateTime """
        pass

    def dateTimeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def dateTimeFromText(self, text): # real signature unknown; restored from __doc__
        """ dateTimeFromText(self, text: str) -> PySide2.QtCore.QDateTime """
        pass

    def displayedSections(self): # real signature unknown; restored from __doc__
        """ displayedSections(self) -> PySide2.QtWidgets.QDateTimeEdit.Sections """
        pass

    def displayFormat(self): # real signature unknown; restored from __doc__
        """ displayFormat(self) -> str """
        return ""

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def fixup(self, input): # real signature unknown; restored from __doc__
        """ fixup(self, input: str) -> None """
        pass

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionSpinBox) -> None """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def maximumDate(self): # real signature unknown; restored from __doc__
        """ maximumDate(self) -> PySide2.QtCore.QDate """
        pass

    def maximumDateTime(self): # real signature unknown; restored from __doc__
        """ maximumDateTime(self) -> PySide2.QtCore.QDateTime """
        pass

    def maximumTime(self): # real signature unknown; restored from __doc__
        """ maximumTime(self) -> PySide2.QtCore.QTime """
        pass

    def minimumDate(self): # real signature unknown; restored from __doc__
        """ minimumDate(self) -> PySide2.QtCore.QDate """
        pass

    def minimumDateTime(self): # real signature unknown; restored from __doc__
        """ minimumDateTime(self) -> PySide2.QtCore.QDateTime """
        pass

    def minimumTime(self): # real signature unknown; restored from __doc__
        """ minimumTime(self) -> PySide2.QtCore.QTime """
        pass

    def mousePressEvent(self, event): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def sectionAt(self, index): # real signature unknown; restored from __doc__
        """ sectionAt(self, index: int) -> PySide2.QtWidgets.QDateTimeEdit.Section """
        pass

    def sectionCount(self): # real signature unknown; restored from __doc__
        """ sectionCount(self) -> int """
        return 0

    def sectionText(self, section): # real signature unknown; restored from __doc__
        """ sectionText(self, section: PySide2.QtWidgets.QDateTimeEdit.Section) -> str """
        return ""

    def setCalendar(self, calendar): # real signature unknown; restored from __doc__
        """ setCalendar(self, calendar: PySide2.QtCore.QCalendar) -> None """
        pass

    def setCalendarPopup(self, enable): # real signature unknown; restored from __doc__
        """ setCalendarPopup(self, enable: bool) -> None """
        pass

    def setCalendarWidget(self, calendarWidget): # real signature unknown; restored from __doc__
        """ setCalendarWidget(self, calendarWidget: PySide2.QtWidgets.QCalendarWidget) -> None """
        pass

    def setCurrentSection(self, section): # real signature unknown; restored from __doc__
        """ setCurrentSection(self, section: PySide2.QtWidgets.QDateTimeEdit.Section) -> None """
        pass

    def setCurrentSectionIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentSectionIndex(self, index: int) -> None """
        pass

    def setDate(self, date): # real signature unknown; restored from __doc__
        """ setDate(self, date: PySide2.QtCore.QDate) -> None """
        pass

    def setDateRange(self, min, max): # real signature unknown; restored from __doc__
        """ setDateRange(self, min: PySide2.QtCore.QDate, max: PySide2.QtCore.QDate) -> None """
        pass

    def setDateTime(self, dateTime): # real signature unknown; restored from __doc__
        """ setDateTime(self, dateTime: PySide2.QtCore.QDateTime) -> None """
        pass

    def setDateTimeRange(self, min, max): # real signature unknown; restored from __doc__
        """ setDateTimeRange(self, min: PySide2.QtCore.QDateTime, max: PySide2.QtCore.QDateTime) -> None """
        pass

    def setDisplayFormat(self, format): # real signature unknown; restored from __doc__
        """ setDisplayFormat(self, format: str) -> None """
        pass

    def setMaximumDate(self, max): # real signature unknown; restored from __doc__
        """ setMaximumDate(self, max: PySide2.QtCore.QDate) -> None """
        pass

    def setMaximumDateTime(self, dt): # real signature unknown; restored from __doc__
        """ setMaximumDateTime(self, dt: PySide2.QtCore.QDateTime) -> None """
        pass

    def setMaximumTime(self, max): # real signature unknown; restored from __doc__
        """ setMaximumTime(self, max: PySide2.QtCore.QTime) -> None """
        pass

    def setMinimumDate(self, min): # real signature unknown; restored from __doc__
        """ setMinimumDate(self, min: PySide2.QtCore.QDate) -> None """
        pass

    def setMinimumDateTime(self, dt): # real signature unknown; restored from __doc__
        """ setMinimumDateTime(self, dt: PySide2.QtCore.QDateTime) -> None """
        pass

    def setMinimumTime(self, min): # real signature unknown; restored from __doc__
        """ setMinimumTime(self, min: PySide2.QtCore.QTime) -> None """
        pass

    def setSelectedSection(self, section): # real signature unknown; restored from __doc__
        """ setSelectedSection(self, section: PySide2.QtWidgets.QDateTimeEdit.Section) -> None """
        pass

    def setTime(self, time): # real signature unknown; restored from __doc__
        """ setTime(self, time: PySide2.QtCore.QTime) -> None """
        pass

    def setTimeRange(self, min, max): # real signature unknown; restored from __doc__
        """ setTimeRange(self, min: PySide2.QtCore.QTime, max: PySide2.QtCore.QTime) -> None """
        pass

    def setTimeSpec(self, spec): # real signature unknown; restored from __doc__
        """ setTimeSpec(self, spec: PySide2.QtCore.Qt.TimeSpec) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def stepBy(self, steps): # real signature unknown; restored from __doc__
        """ stepBy(self, steps: int) -> None """
        pass

    def stepEnabled(self): # real signature unknown; restored from __doc__
        """ stepEnabled(self) -> PySide2.QtWidgets.QAbstractSpinBox.StepEnabled """
        pass

    def textFromDateTime(self, dt): # real signature unknown; restored from __doc__
        """ textFromDateTime(self, dt: PySide2.QtCore.QDateTime) -> str """
        return ""

    def time(self): # real signature unknown; restored from __doc__
        """ time(self) -> PySide2.QtCore.QTime """
        pass

    def timeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def timeSpec(self): # real signature unknown; restored from __doc__
        """ timeSpec(self) -> PySide2.QtCore.Qt.TimeSpec """
        pass

    def validate(self, input, pos): # real signature unknown; restored from __doc__
        """ validate(self, input: str, pos: int) -> PySide2.QtGui.QValidator.State """
        pass

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, d, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AmPmSection = PySide2.QtWidgets.QDateTimeEdit.Section.AmPmSection
    DateSections_Mask = PySide2.QtWidgets.QDateTimeEdit.Section.DateSections_Mask
    DaySection = PySide2.QtWidgets.QDateTimeEdit.Section.DaySection
    HourSection = PySide2.QtWidgets.QDateTimeEdit.Section.HourSection
    MinuteSection = PySide2.QtWidgets.QDateTimeEdit.Section.MinuteSection
    MonthSection = PySide2.QtWidgets.QDateTimeEdit.Section.MonthSection
    MSecSection = PySide2.QtWidgets.QDateTimeEdit.Section.MSecSection
    NoSection = PySide2.QtWidgets.QDateTimeEdit.Section.NoSection
    SecondSection = PySide2.QtWidgets.QDateTimeEdit.Section.SecondSection
    Section = None # (!) real value is "<class 'PySide2.QtWidgets.QDateTimeEdit.Section'>"
    Sections = None # (!) real value is "<class 'PySide2.QtWidgets.QDateTimeEdit.Sections'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507D5B00>'
    TimeSections_Mask = PySide2.QtWidgets.QDateTimeEdit.Section.TimeSections_Mask
    YearSection = PySide2.QtWidgets.QDateTimeEdit.Section.YearSection


