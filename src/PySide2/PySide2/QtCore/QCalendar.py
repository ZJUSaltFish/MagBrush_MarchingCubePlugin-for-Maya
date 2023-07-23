# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QCalendar(__Shiboken.Object):
    """
    QCalendar(self) -> None
    QCalendar(self, system: PySide2.QtCore.QCalendar.System) -> None
    """
    def availableCalendars(self): # real signature unknown; restored from __doc__
        """ availableCalendars() -> typing.List[str] """
        pass

    def dateFromParts(self, parts): # real signature unknown; restored from __doc__
        """
        dateFromParts(self, parts: PySide2.QtCore.QCalendar.YearMonthDay) -> PySide2.QtCore.QDate
        dateFromParts(self, year: int, month: int, day: int) -> PySide2.QtCore.QDate
        """
        pass

    def dayOfWeek(self, date): # real signature unknown; restored from __doc__
        """ dayOfWeek(self, date: PySide2.QtCore.QDate) -> int """
        return 0

    def daysInMonth(self, month, year, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ daysInMonth(self, month: int, year: typing.Optional[int] = None) -> int """
        pass

    def daysInYear(self, year): # real signature unknown; restored from __doc__
        """ daysInYear(self, year: int) -> int """
        return 0

    def hasYearZero(self): # real signature unknown; restored from __doc__
        """ hasYearZero(self) -> bool """
        return False

    def isDateValid(self, year, month, day): # real signature unknown; restored from __doc__
        """ isDateValid(self, year: int, month: int, day: int) -> bool """
        return False

    def isGregorian(self): # real signature unknown; restored from __doc__
        """ isGregorian(self) -> bool """
        return False

    def isLeapYear(self, year): # real signature unknown; restored from __doc__
        """ isLeapYear(self, year: int) -> bool """
        return False

    def isLunar(self): # real signature unknown; restored from __doc__
        """ isLunar(self) -> bool """
        return False

    def isLuniSolar(self): # real signature unknown; restored from __doc__
        """ isLuniSolar(self) -> bool """
        return False

    def isProleptic(self): # real signature unknown; restored from __doc__
        """ isProleptic(self) -> bool """
        return False

    def isSolar(self): # real signature unknown; restored from __doc__
        """ isSolar(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def maximumDaysInMonth(self): # real signature unknown; restored from __doc__
        """ maximumDaysInMonth(self) -> int """
        return 0

    def maximumMonthsInYear(self): # real signature unknown; restored from __doc__
        """ maximumMonthsInYear(self) -> int """
        return 0

    def minimumDaysInMonth(self): # real signature unknown; restored from __doc__
        """ minimumDaysInMonth(self) -> int """
        return 0

    def monthName(self, locale, month, year, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ monthName(self, locale: PySide2.QtCore.QLocale, month: int, year: typing.Optional[int] = None, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        pass

    def monthsInYear(self, year): # real signature unknown; restored from __doc__
        """ monthsInYear(self, year: int) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def partsFromDate(self, date): # real signature unknown; restored from __doc__
        """ partsFromDate(self, date: PySide2.QtCore.QDate) -> PySide2.QtCore.QCalendar.YearMonthDay """
        pass

    def standaloneMonthName(self, locale, month, year, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standaloneMonthName(self, locale: PySide2.QtCore.QLocale, month: int, year: typing.Optional[int] = None, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        pass

    def standaloneWeekDayName(self, locale, day, format=None): # real signature unknown; restored from __doc__
        """ standaloneWeekDayName(self, locale: PySide2.QtCore.QLocale, day: int, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        return ""

    def weekDayName(self, locale, day, format=None): # real signature unknown; restored from __doc__
        """ weekDayName(self, locale: PySide2.QtCore.QLocale, day: int, format: PySide2.QtCore.QLocale.FormatType = PySide2.QtCore.QLocale.FormatType.LongFormat) -> str """
        return ""

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    System = None # (!) real value is "<class 'PySide2.QtCore.QCalendar.System'>"
    YearMonthDay = None # (!) real value is "<class 'PySide2.QtCore.QCalendar.YearMonthDay'>"


