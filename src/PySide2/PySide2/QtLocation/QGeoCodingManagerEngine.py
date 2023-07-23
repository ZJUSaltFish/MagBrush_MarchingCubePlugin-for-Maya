# encoding: utf-8
# module PySide2.QtLocation
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtLocation.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QGeoCodingManagerEngine(__PySide2_QtCore.QObject):
    """ QGeoCodingManagerEngine(self, parameters: typing.Dict[str, typing.Any], parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def error(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def geocode(self, address, bounds): # real signature unknown; restored from __doc__
        """
        geocode(self, address: PySide2.QtPositioning.QGeoAddress, bounds: PySide2.QtPositioning.QGeoShape) -> PySide2.QtLocation.QGeoCodeReply
        geocode(self, address: str, limit: int, offset: int, bounds: PySide2.QtPositioning.QGeoShape) -> PySide2.QtLocation.QGeoCodeReply
        """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> PySide2.QtCore.QLocale """
        pass

    def managerName(self): # real signature unknown; restored from __doc__
        """ managerName(self) -> str """
        return ""

    def managerVersion(self): # real signature unknown; restored from __doc__
        """ managerVersion(self) -> int """
        return 0

    def reverseGeocode(self, coordinate, bounds): # real signature unknown; restored from __doc__
        """ reverseGeocode(self, coordinate: PySide2.QtPositioning.QGeoCoordinate, bounds: PySide2.QtPositioning.QGeoShape) -> PySide2.QtLocation.QGeoCodeReply """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: PySide2.QtCore.QLocale) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parameters, p_str=None, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000013BA752DAC0>'


