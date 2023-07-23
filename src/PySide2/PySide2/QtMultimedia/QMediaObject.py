# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QMediaObject(__PySide2_QtCore.QObject):
    """ QMediaObject(self, parent: PySide2.QtCore.QObject, service: PySide2.QtMultimedia.QMediaService) -> None """
    def addPropertyWatch(self, name): # real signature unknown; restored from __doc__
        """ addPropertyWatch(self, name: PySide2.QtCore.QByteArray) -> None """
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> PySide2.QtMultimedia.QMultimedia.AvailabilityStatus """
        pass

    def availabilityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def availableMetaData(self): # real signature unknown; restored from __doc__
        """ availableMetaData(self) -> typing.List[str] """
        pass

    def bind(self, arg__1): # real signature unknown; restored from __doc__
        """ bind(self, arg__1: PySide2.QtCore.QObject) -> bool """
        return False

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isMetaDataAvailable(self): # real signature unknown; restored from __doc__
        """ isMetaDataAvailable(self) -> bool """
        return False

    def metaData(self, key): # real signature unknown; restored from __doc__
        """ metaData(self, key: str) -> typing.Any """
        pass

    def metaDataAvailableChanged(self, *args, **kwargs): # real signature unknown
        pass

    def metaDataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def notifyInterval(self): # real signature unknown; restored from __doc__
        """ notifyInterval(self) -> int """
        return 0

    def notifyIntervalChanged(self, *args, **kwargs): # real signature unknown
        pass

    def removePropertyWatch(self, name): # real signature unknown; restored from __doc__
        """ removePropertyWatch(self, name: PySide2.QtCore.QByteArray) -> None """
        pass

    def service(self): # real signature unknown; restored from __doc__
        """ service(self) -> PySide2.QtMultimedia.QMediaService """
        pass

    def setNotifyInterval(self, milliSeconds): # real signature unknown; restored from __doc__
        """ setNotifyInterval(self, milliSeconds: int) -> None """
        pass

    def unbind(self, arg__1): # real signature unknown; restored from __doc__
        """ unbind(self, arg__1: PySide2.QtCore.QObject) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, service): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887465D600>'


