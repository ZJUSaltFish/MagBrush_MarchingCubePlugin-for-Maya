# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDateTime(__Shiboken.Object):
    """
    QDateTime(self) -> None
    QDateTime(self, arg__1: PySide2.QtCore.QDate) -> None
    QDateTime(self, arg__1: PySide2.QtCore.QDate, arg__2: PySide2.QtCore.QTime, spec: PySide2.QtCore.Qt.TimeSpec = PySide2.QtCore.Qt.TimeSpec.LocalTime) -> None
    QDateTime(self, arg__1: int, arg__2: int, arg__3: int, arg__4: int, arg__5: int, arg__6: int) -> None
    QDateTime(self, arg__1: int, arg__2: int, arg__3: int, arg__4: int, arg__5: int, arg__6: int, arg__7: int, arg__8: int = PySide2.QtCore.Qt.TimeSpec.LocalTime) -> None
    QDateTime(self, date: PySide2.QtCore.QDate, time: PySide2.QtCore.QTime, spec: PySide2.QtCore.Qt.TimeSpec, offsetSeconds: int) -> None
    QDateTime(self, date: PySide2.QtCore.QDate, time: PySide2.QtCore.QTime, timeZone: PySide2.QtCore.QTimeZone) -> None
    QDateTime(self, other: PySide2.QtCore.QDateTime) -> None
    """
    def addDays(self, days): # real signature unknown; restored from __doc__
        """ addDays(self, days: int) -> PySide2.QtCore.QDateTime """
        pass

    def addMonths(self, months): # real signature unknown; restored from __doc__
        """ addMonths(self, months: int) -> PySide2.QtCore.QDateTime """
        pass

    def addMSecs(self, msecs): # real signature unknown; restored from __doc__
        """ addMSecs(self, msecs: int) -> PySide2.QtCore.QDateTime """
        pass

    def addSecs(self, secs): # real signature unknown; restored from __doc__
        """ addSecs(self, secs: int) -> PySide2.QtCore.QDateTime """
        pass

    def addYears(self, years): # real signature unknown; restored from __doc__
        """ addYears(self, years: int) -> PySide2.QtCore.QDateTime """
        pass

    def currentDateTime(self): # real signature unknown; restored from __doc__
        """ currentDateTime() -> PySide2.QtCore.QDateTime """
        pass

    def currentDateTimeUtc(self): # real signature unknown; restored from __doc__
        """ currentDateTimeUtc() -> PySide2.QtCore.QDateTime """
        pass

    def currentMSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ currentMSecsSinceEpoch() -> int """
        return 0

    def currentSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ currentSecsSinceEpoch() -> int """
        return 0

    def date(self): # real signature unknown; restored from __doc__
        """ date(self) -> PySide2.QtCore.QDate """
        pass

    def daysTo(self, arg__1): # real signature unknown; restored from __doc__
        """ daysTo(self, arg__1: PySide2.QtCore.QDateTime) -> int """
        return 0

    def fromMSecsSinceEpoch(self, msecs): # real signature unknown; restored from __doc__
        """
        fromMSecsSinceEpoch(msecs: int) -> PySide2.QtCore.QDateTime
        fromMSecsSinceEpoch(msecs: int, spec: PySide2.QtCore.Qt.TimeSpec, offsetFromUtc: int = 0) -> PySide2.QtCore.QDateTime
        fromMSecsSinceEpoch(msecs: int, timeZone: PySide2.QtCore.QTimeZone) -> PySide2.QtCore.QDateTime
        """
        pass

    def fromSecsSinceEpoch(self, secs, spe=None, offsetFromUtc=0): # real signature unknown; restored from __doc__
        """
        fromSecsSinceEpoch(secs: int, spe: PySide2.QtCore.Qt.TimeSpec = PySide2.QtCore.Qt.TimeSpec.LocalTime, offsetFromUtc: int = 0) -> PySide2.QtCore.QDateTime
        fromSecsSinceEpoch(secs: int, timeZone: PySide2.QtCore.QTimeZone) -> PySide2.QtCore.QDateTime
        """
        pass

    def fromString(self, s, f=None): # real signature unknown; restored from __doc__
        """
        fromString(s: str, f: PySide2.QtCore.Qt.DateFormat = PySide2.QtCore.Qt.DateFormat.TextDate) -> PySide2.QtCore.QDateTime
        fromString(s: str, format: str) -> PySide2.QtCore.QDateTime
        fromString(s: str, format: str, cal: PySide2.QtCore.QCalendar) -> PySide2.QtCore.QDateTime
        """
        pass

    def fromTime_t(self, secsSince1Jan1970UTC): # real signature unknown; restored from __doc__
        """
        fromTime_t(secsSince1Jan1970UTC: int) -> PySide2.QtCore.QDateTime
        fromTime_t(secsSince1Jan1970UTC: int, spec: PySide2.QtCore.Qt.TimeSpec, offsetFromUtc: int = 0) -> PySide2.QtCore.QDateTime
        fromTime_t(secsSince1Jan1970UTC: int, timeZone: PySide2.QtCore.QTimeZone) -> PySide2.QtCore.QDateTime
        """
        pass

    def isDaylightTime(self): # real signature unknown; restored from __doc__
        """ isDaylightTime(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def msecsTo(self, arg__1): # real signature unknown; restored from __doc__
        """ msecsTo(self, arg__1: PySide2.QtCore.QDateTime) -> int """
        return 0

    def offsetFromUtc(self): # real signature unknown; restored from __doc__
        """ offsetFromUtc(self) -> int """
        return 0

    def secsTo(self, arg__1): # real signature unknown; restored from __doc__
        """ secsTo(self, arg__1: PySide2.QtCore.QDateTime) -> int """
        return 0

    def setDate(self, date): # real signature unknown; restored from __doc__
        """ setDate(self, date: PySide2.QtCore.QDate) -> None """
        pass

    def setMSecsSinceEpoch(self, msecs): # real signature unknown; restored from __doc__
        """ setMSecsSinceEpoch(self, msecs: int) -> None """
        pass

    def setOffsetFromUtc(self, offsetSeconds): # real signature unknown; restored from __doc__
        """ setOffsetFromUtc(self, offsetSeconds: int) -> None """
        pass

    def setSecsSinceEpoch(self, secs): # real signature unknown; restored from __doc__
        """ setSecsSinceEpoch(self, secs: int) -> None """
        pass

    def setTime(self, time): # real signature unknown; restored from __doc__
        """ setTime(self, time: PySide2.QtCore.QTime) -> None """
        pass

    def setTimeSpec(self, spec): # real signature unknown; restored from __doc__
        """ setTimeSpec(self, spec: PySide2.QtCore.Qt.TimeSpec) -> None """
        pass

    def setTimeZone(self, toZone): # real signature unknown; restored from __doc__
        """ setTimeZone(self, toZone: PySide2.QtCore.QTimeZone) -> None """
        pass

    def setTime_t(self, secsSince1Jan1970UTC): # real signature unknown; restored from __doc__
        """ setTime_t(self, secsSince1Jan1970UTC: int) -> None """
        pass

    def setUtcOffset(self, seconds): # real signature unknown; restored from __doc__
        """ setUtcOffset(self, seconds: int) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QDateTime) -> None """
        pass

    def time(self): # real signature unknown; restored from __doc__
        """ time(self) -> PySide2.QtCore.QTime """
        pass

    def timeSpec(self): # real signature unknown; restored from __doc__
        """ timeSpec(self) -> PySide2.QtCore.Qt.TimeSpec """
        pass

    def timeZone(self): # real signature unknown; restored from __doc__
        """ timeZone(self) -> PySide2.QtCore.QTimeZone """
        pass

    def timeZoneAbbreviation(self): # real signature unknown; restored from __doc__
        """ timeZoneAbbreviation(self) -> str """
        return ""

    def toLocalTime(self): # real signature unknown; restored from __doc__
        """ toLocalTime(self) -> PySide2.QtCore.QDateTime """
        pass

    def toMSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ toMSecsSinceEpoch(self) -> int """
        return 0

    def toOffsetFromUtc(self, offsetSeconds): # real signature unknown; restored from __doc__
        """ toOffsetFromUtc(self, offsetSeconds: int) -> PySide2.QtCore.QDateTime """
        pass

    def toPython(self): # real signature unknown; restored from __doc__
        """ toPython(self) -> object """
        return object()

    def toSecsSinceEpoch(self): # real signature unknown; restored from __doc__
        """ toSecsSinceEpoch(self) -> int """
        return 0

    def toString(self, format=None): # real signature unknown; restored from __doc__
        """
        toString(self, format: PySide2.QtCore.Qt.DateFormat = PySide2.QtCore.Qt.DateFormat.TextDate) -> str
        toString(self, format: str) -> str
        toString(self, format: str, cal: PySide2.QtCore.QCalendar) -> str
        """
        return ""

    def toTimeSpec(self, spec): # real signature unknown; restored from __doc__
        """ toTimeSpec(self, spec: PySide2.QtCore.Qt.TimeSpec) -> PySide2.QtCore.QDateTime """
        pass

    def toTimeZone(self, toZone): # real signature unknown; restored from __doc__
        """ toTimeZone(self, toZone: PySide2.QtCore.QTimeZone) -> PySide2.QtCore.QDateTime """
        pass

    def toTime_t(self): # real signature unknown; restored from __doc__
        """ toTime_t(self) -> int """
        return 0

    def toUTC(self): # real signature unknown; restored from __doc__
        """ toUTC(self) -> PySide2.QtCore.QDateTime """
        pass

    def utcOffset(self): # real signature unknown; restored from __doc__
        """ utcOffset(self) -> int """
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

    YearRange = None # (!) real value is "<class 'PySide2.QtCore.QDateTime.YearRange'>"


