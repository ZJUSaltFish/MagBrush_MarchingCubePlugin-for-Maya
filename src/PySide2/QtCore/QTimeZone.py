# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QTimeZone(__Shiboken.Object):
    """
    QTimeZone(self) -> None
    QTimeZone(self, ianaId: PySide2.QtCore.QByteArray) -> None
    QTimeZone(self, offsetSeconds: int) -> None
    QTimeZone(self, other: PySide2.QtCore.QTimeZone) -> None
    QTimeZone(self, zoneId: PySide2.QtCore.QByteArray, offsetSeconds: int, name: str, abbreviation: str, country: PySide2.QtCore.QLocale.Country = PySide2.QtCore.QLocale.Country.AnyCountry, comment: str = '') -> None
    """
    def abbreviation(self, atDateTime): # real signature unknown; restored from __doc__
        """ abbreviation(self, atDateTime: PySide2.QtCore.QDateTime) -> str """
        return ""

    def availableTimeZoneIds(self): # real signature unknown; restored from __doc__
        """
        availableTimeZoneIds() -> typing.List[PySide2.QtCore.QByteArray]
        availableTimeZoneIds(country: PySide2.QtCore.QLocale.Country) -> typing.List[PySide2.QtCore.QByteArray]
        availableTimeZoneIds(offsetSeconds: int) -> typing.List[PySide2.QtCore.QByteArray]
        """
        pass

    def comment(self): # real signature unknown; restored from __doc__
        """ comment(self) -> str """
        return ""

    def country(self): # real signature unknown; restored from __doc__
        """ country(self) -> PySide2.QtCore.QLocale.Country """
        pass

    def daylightTimeOffset(self, atDateTime): # real signature unknown; restored from __doc__
        """ daylightTimeOffset(self, atDateTime: PySide2.QtCore.QDateTime) -> int """
        return 0

    def displayName(self, atDateTime, nameType=None, locale=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        displayName(self, atDateTime: PySide2.QtCore.QDateTime, nameType: PySide2.QtCore.QTimeZone.NameType = PySide2.QtCore.QTimeZone.NameType.DefaultName, locale: PySide2.QtCore.QLocale = Default(QLocale)) -> str
        displayName(self, timeType: PySide2.QtCore.QTimeZone.TimeType, nameType: PySide2.QtCore.QTimeZone.NameType = PySide2.QtCore.QTimeZone.NameType.DefaultName, locale: PySide2.QtCore.QLocale = Default(QLocale)) -> str
        """
        pass

    def hasDaylightTime(self): # real signature unknown; restored from __doc__
        """ hasDaylightTime(self) -> bool """
        return False

    def hasTransitions(self): # real signature unknown; restored from __doc__
        """ hasTransitions(self) -> bool """
        return False

    def ianaIdToWindowsId(self, ianaId): # real signature unknown; restored from __doc__
        """ ianaIdToWindowsId(ianaId: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray """
        pass

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> PySide2.QtCore.QByteArray """
        pass

    def isDaylightTime(self, atDateTime): # real signature unknown; restored from __doc__
        """ isDaylightTime(self, atDateTime: PySide2.QtCore.QDateTime) -> bool """
        return False

    def isTimeZoneIdAvailable(self, ianaId): # real signature unknown; restored from __doc__
        """ isTimeZoneIdAvailable(ianaId: PySide2.QtCore.QByteArray) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nextTransition(self, afterDateTime): # real signature unknown; restored from __doc__
        """ nextTransition(self, afterDateTime: PySide2.QtCore.QDateTime) -> PySide2.QtCore.QTimeZone.OffsetData """
        pass

    def offsetData(self, forDateTime): # real signature unknown; restored from __doc__
        """ offsetData(self, forDateTime: PySide2.QtCore.QDateTime) -> PySide2.QtCore.QTimeZone.OffsetData """
        pass

    def offsetFromUtc(self, atDateTime): # real signature unknown; restored from __doc__
        """ offsetFromUtc(self, atDateTime: PySide2.QtCore.QDateTime) -> int """
        return 0

    def previousTransition(self, beforeDateTime): # real signature unknown; restored from __doc__
        """ previousTransition(self, beforeDateTime: PySide2.QtCore.QDateTime) -> PySide2.QtCore.QTimeZone.OffsetData """
        pass

    def standardTimeOffset(self, atDateTime): # real signature unknown; restored from __doc__
        """ standardTimeOffset(self, atDateTime: PySide2.QtCore.QDateTime) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QTimeZone) -> None """
        pass

    def systemTimeZone(self): # real signature unknown; restored from __doc__
        """ systemTimeZone() -> PySide2.QtCore.QTimeZone """
        pass

    def systemTimeZoneId(self): # real signature unknown; restored from __doc__
        """ systemTimeZoneId() -> PySide2.QtCore.QByteArray """
        pass

    def transitions(self, fromDateTime, toDateTime): # real signature unknown; restored from __doc__
        """ transitions(self, fromDateTime: PySide2.QtCore.QDateTime, toDateTime: PySide2.QtCore.QDateTime) -> typing.List[PySide2.QtCore.QTimeZone.OffsetData] """
        pass

    def utc(self): # real signature unknown; restored from __doc__
        """ utc() -> PySide2.QtCore.QTimeZone """
        pass

    def windowsIdToDefaultIanaId(self, windowsId): # real signature unknown; restored from __doc__
        """
        windowsIdToDefaultIanaId(windowsId: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray
        windowsIdToDefaultIanaId(windowsId: PySide2.QtCore.QByteArray, country: PySide2.QtCore.QLocale.Country) -> PySide2.QtCore.QByteArray
        """
        pass

    def windowsIdToIanaIds(self, windowsId): # real signature unknown; restored from __doc__
        """
        windowsIdToIanaIds(windowsId: PySide2.QtCore.QByteArray) -> typing.List[PySide2.QtCore.QByteArray]
        windowsIdToIanaIds(windowsId: PySide2.QtCore.QByteArray, country: PySide2.QtCore.QLocale.Country) -> typing.List[PySide2.QtCore.QByteArray]
        """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    DaylightTime = PySide2.QtCore.QTimeZone.TimeType.DaylightTime
    DefaultName = PySide2.QtCore.QTimeZone.NameType.DefaultName
    GenericTime = PySide2.QtCore.QTimeZone.TimeType.GenericTime
    LongName = PySide2.QtCore.QTimeZone.NameType.LongName
    NameType = None # (!) real value is "<class 'PySide2.QtCore.QTimeZone.NameType'>"
    OffsetData = None # (!) real value is "<class 'PySide2.QtCore.QTimeZone.OffsetData'>"
    OffsetName = PySide2.QtCore.QTimeZone.NameType.OffsetName
    ShortName = PySide2.QtCore.QTimeZone.NameType.ShortName
    StandardTime = PySide2.QtCore.QTimeZone.TimeType.StandardTime
    TimeType = None # (!) real value is "<class 'PySide2.QtCore.QTimeZone.TimeType'>"
    __hash__ = None


