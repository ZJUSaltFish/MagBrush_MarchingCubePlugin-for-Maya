# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDate(__Shiboken.Object):
    """
    QDate(self) -> None
    QDate(self, QDate: PySide2.QtCore.QDate) -> None
    QDate(self, y: int, m: int, d: int) -> None
    QDate(self, y: int, m: int, d: int, cal: PySide2.QtCore.QCalendar) -> None
    """
    def addDays(self, days): # real signature unknown; restored from __doc__
        """ addDays(self, days: int) -> PySide2.QtCore.QDate """
        pass

    def addMonths(self, months): # real signature unknown; restored from __doc__
        """
        addMonths(self, months: int) -> PySide2.QtCore.QDate
        addMonths(self, months: int, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QDate
        """
        pass

    def addYears(self, years): # real signature unknown; restored from __doc__
        """
        addYears(self, years: int) -> PySide2.QtCore.QDate
        addYears(self, years: int, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QDate
        """
        pass

    def currentDate(self): # real signature unknown; restored from __doc__
        """ currentDate() -> PySide2.QtCore.QDate """
        pass

    def day(self): # real signature unknown; restored from __doc__
        """
        day(self) -> int
        day(self, cal: PySide2.QtCore.QCalendar) -> int
        """
        return 0

    def dayOfWeek(self): # real signature unknown; restored from __doc__
        """
        dayOfWeek(self) -> int
        dayOfWeek(self, cal: PySide2.QtCore.QCalendar) -> int
        """
        return 0

    def dayOfYear(self): # real signature unknown; restored from __doc__
        """
        dayOfYear(self) -> int
        dayOfYear(self, cal: PySide2.QtCore.QCalendar) -> int
        """
        return 0

    def daysInMonth(self): # real signature unknown; restored from __doc__
        """
        daysInMonth(self) -> int
        daysInMonth(self, cal: PySide2.QtCore.QCalendar) -> int
        """
        return 0

    def daysInYear(self): # real signature unknown; restored from __doc__
        """
        daysInYear(self) -> int
        daysInYear(self, cal: PySide2.QtCore.QCalendar) -> int
        """
        return 0

    def daysTo(self, arg__1): # real signature unknown; restored from __doc__
        """ daysTo(self, arg__1: PySide2.QtCore.QDate) -> int """
        return 0

    def endOfDay(self, spec=None, offsetSeconds=0): # real signature unknown; restored from __doc__
        """
        endOfDay(self, spec: PySide2.QtCore.Qt.TimeSpec = PySide2.QtCore.Qt.TimeSpec.LocalTime, offsetSeconds: int = 0) -> PySide2.QtCore.QDateTime
        endOfDay(self, zone: PySide2.QtCore.QTimeZone) -> PySide2.QtCore.QDateTime
        """
        pass

    def fromJulianDay(self, jd_): # real signature unknown; restored from __doc__
        """ fromJulianDay(jd_: int) -> PySide2.QtCore.QDate """
        pass

    def fromString(self, s, f=None): # real signature unknown; restored from __doc__
        """
        fromString(s: str, f: PySide2.QtCore.Qt.DateFormat = PySide2.QtCore.Qt.DateFormat.TextDate) -> PySide2.QtCore.QDate
        fromString(s: str, format: str) -> PySide2.QtCore.QDate
        fromString(s: str, format: str, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QDate
        """
        pass

    def getDate(self): # real signature unknown; restored from __doc__
        """ getDate(self) -> typing.Tuple[int, int, int] """
        pass

    def isLeapYear(self, year): # real signature unknown; restored from __doc__
        """ isLeapYear(year: int) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """
        isValid(self) -> bool
        isValid(y: int, m: int, d: int) -> bool
        """
        return False

    def longDayName(self, weekday, type=None): # real signature unknown; restored from __doc__
        """ longDayName(weekday: int, type: PySide2.QtCore.QDate.MonthNameType = PySide2.QtCore.QDate.MonthNameType.DateFormat) -> str """
        return ""

    def longMonthName(self, month, type=None): # real signature unknown; restored from __doc__
        """ longMonthName(month: int, type: PySide2.QtCore.QDate.MonthNameType = PySide2.QtCore.QDate.MonthNameType.DateFormat) -> str """
        return ""

    def month(self): # real signature unknown; restored from __doc__
        """
        month(self) -> int
        month(self, cal: PySide2.QtCore.QCalendar) -> int
        """
        return 0

    def setDate(self, year, month, day): # real signature unknown; restored from __doc__
        """
        setDate(self, year: int, month: int, day: int) -> bool
        setDate(self, year: int, month: int, day: int, cal: PySide2.QtCore.QCalendar) -> bool
        """
        return False

    def shortDayName(self, weekday, type=None): # real signature unknown; restored from __doc__
        """ shortDayName(weekday: int, type: PySide2.QtCore.QDate.MonthNameType = PySide2.QtCore.QDate.MonthNameType.DateFormat) -> str """
        return ""

    def shortMonthName(self, month, type=None): # real signature unknown; restored from __doc__
        """ shortMonthName(month: int, type: PySide2.QtCore.QDate.MonthNameType = PySide2.QtCore.QDate.MonthNameType.DateFormat) -> str """
        return ""

    def startOfDay(self, spec=None, offsetSeconds=0): # real signature unknown; restored from __doc__
        """
        startOfDay(self, spec: PySide2.QtCore.Qt.TimeSpec = PySide2.QtCore.Qt.TimeSpec.LocalTime, offsetSeconds: int = 0) -> PySide2.QtCore.QDateTime
        startOfDay(self, zone: PySide2.QtCore.QTimeZone) -> PySide2.QtCore.QDateTime
        """
        pass

    def toJulianDay(self): # real signature unknown; restored from __doc__
        """ toJulianDay(self) -> int """
        return 0

    def toPython(self): # real signature unknown; restored from __doc__
        """ toPython(self) -> object """
        return object()

    def toString(self, format, cal): # real signature unknown; restored from __doc__
        """
        toString(self, format: PySide2.QtCore.Qt.DateFormat, cal: PySide2.QtCore.QCalendar) -> str
        toString(self, format: PySide2.QtCore.Qt.DateFormat = PySide2.QtCore.Qt.DateFormat.TextDate) -> str
        toString(self, format: str) -> str
        toString(self, format: str, cal: PySide2.QtCore.QCalendar) -> str
        """
        return ""

    def weekNumber(self): # real signature unknown; restored from __doc__
        """ weekNumber(self) -> typing.Tuple[int, int] """
        pass

    def year(self): # real signature unknown; restored from __doc__
        """
        year(self) -> int
        year(self, cal: PySide2.QtCore.QCalendar) -> int
        """
        return 0

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__(self) -> object """
        return object()

    def __repr__(self): # real signature unknown; restored from __doc__
        """
        __repr__(self) -> object
        
        Return repr(self).
        """
        return object()

    DateFormat = PySide2.QtCore.QDate.MonthNameType.DateFormat
    MonthNameType = None # (!) real value is "<class 'PySide2.QtCore.QDate.MonthNameType'>"
    StandaloneFormat = PySide2.QtCore.QDate.MonthNameType.StandaloneFormat


