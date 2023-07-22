# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QGeoCodeReply(__PySide2_QtCore.QObject):
    """
    QGeoCodeReply(self, error: PySide2.QtLocation.QGeoCodeReply.Error, errorString: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QGeoCodeReply(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> None """
        pass

    def aborted(self, *args, **kwargs): # real signature unknown
        pass

    def addLocation(self, location): # real signature unknown; restored from __doc__
        """ addLocation(self, location: PySide2.QtPositioning.QGeoLocation) -> None """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtLocation.QGeoCodeReply.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def limit(self): # real signature unknown; restored from __doc__
        """ limit(self) -> int """
        return 0

    def locations(self): # real signature unknown; restored from __doc__
        """ locations(self) -> typing.List[PySide2.QtPositioning.QGeoLocation] """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> int """
        return 0

    def setError(self, error, errorString): # real signature unknown; restored from __doc__
        """ setError(self, error: PySide2.QtLocation.QGeoCodeReply.Error, errorString: str) -> None """
        pass

    def setFinished(self, finished): # real signature unknown; restored from __doc__
        """ setFinished(self, finished: bool) -> None """
        pass

    def setLimit(self, limit): # real signature unknown; restored from __doc__
        """ setLimit(self, limit: int) -> None """
        pass

    def setLocations(self, locations, PySide2_QtPositioning_QGeoLocation=None): # real signature unknown; restored from __doc__
        """ setLocations(self, locations: typing.Sequence[PySide2.QtPositioning.QGeoLocation]) -> None """
        pass

    def setOffset(self, offset): # real signature unknown; restored from __doc__
        """ setOffset(self, offset: int) -> None """
        pass

    def setViewport(self, viewport): # real signature unknown; restored from __doc__
        """ setViewport(self, viewport: PySide2.QtPositioning.QGeoShape) -> None """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> PySide2.QtPositioning.QGeoShape """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, error, errorString, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    CombinationError = PySide2.QtLocation.QGeoCodeReply.Error.CombinationError
    CommunicationError = PySide2.QtLocation.QGeoCodeReply.Error.CommunicationError
    EngineNotSetError = PySide2.QtLocation.QGeoCodeReply.Error.EngineNotSetError
    Error = None # (!) real value is "<class 'PySide2.QtLocation.QGeoCodeReply.Error'>"
    NoError = PySide2.QtLocation.QGeoCodeReply.Error.NoError
    ParseError = PySide2.QtLocation.QGeoCodeReply.Error.ParseError
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000013BA752E0C0>'
    UnknownError = PySide2.QtLocation.QGeoCodeReply.Error.UnknownError
    UnsupportedOptionError = PySide2.QtLocation.QGeoCodeReply.Error.UnsupportedOptionError


