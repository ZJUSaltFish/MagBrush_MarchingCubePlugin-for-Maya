# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QGeoRouteReply(__PySide2_QtCore.QObject):
    """
    QGeoRouteReply(self, error: PySide2.QtLocation.QGeoRouteReply.Error, errorString: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QGeoRouteReply(self, request: PySide2.QtLocation.QGeoRouteRequest, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> None """
        pass

    def aborted(self, *args, **kwargs): # real signature unknown
        pass

    def addRoutes(self, routes, PySide2_QtLocation_QGeoRoute=None): # real signature unknown; restored from __doc__
        """ addRoutes(self, routes: typing.Sequence[PySide2.QtLocation.QGeoRoute]) -> None """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtLocation.QGeoRouteReply.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> PySide2.QtLocation.QGeoRouteRequest """
        pass

    def routes(self): # real signature unknown; restored from __doc__
        """ routes(self) -> typing.List[PySide2.QtLocation.QGeoRoute] """
        pass

    def setError(self, error, errorString): # real signature unknown; restored from __doc__
        """ setError(self, error: PySide2.QtLocation.QGeoRouteReply.Error, errorString: str) -> None """
        pass

    def setFinished(self, finished): # real signature unknown; restored from __doc__
        """ setFinished(self, finished: bool) -> None """
        pass

    def setRoutes(self, routes, PySide2_QtLocation_QGeoRoute=None): # real signature unknown; restored from __doc__
        """ setRoutes(self, routes: typing.Sequence[PySide2.QtLocation.QGeoRoute]) -> None """
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

    CommunicationError = PySide2.QtLocation.QGeoRouteReply.Error.CommunicationError
    EngineNotSetError = PySide2.QtLocation.QGeoRouteReply.Error.EngineNotSetError
    Error = None # (!) real value is "<class 'PySide2.QtLocation.QGeoRouteReply.Error'>"
    NoError = PySide2.QtLocation.QGeoRouteReply.Error.NoError
    ParseError = PySide2.QtLocation.QGeoRouteReply.Error.ParseError
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000013BA752D900>'
    UnknownError = PySide2.QtLocation.QGeoRouteReply.Error.UnknownError
    UnsupportedOptionError = PySide2.QtLocation.QGeoRouteReply.Error.UnsupportedOptionError


