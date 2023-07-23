# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaControl import QMediaControl

class QVideoDeviceSelectorControl(QMediaControl):
    """ QVideoDeviceSelectorControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def defaultDevice(self): # real signature unknown; restored from __doc__
        """ defaultDevice(self) -> int """
        return 0

    def deviceCount(self): # real signature unknown; restored from __doc__
        """ deviceCount(self) -> int """
        return 0

    def deviceDescription(self, index): # real signature unknown; restored from __doc__
        """ deviceDescription(self, index: int) -> str """
        return ""

    def deviceName(self, index): # real signature unknown; restored from __doc__
        """ deviceName(self, index: int) -> str """
        return ""

    def devicesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectedDevice(self): # real signature unknown; restored from __doc__
        """ selectedDevice(self) -> int """
        return 0

    def selectedDeviceChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setSelectedDevice(self, index): # real signature unknown; restored from __doc__
        """ setSelectedDevice(self, index: int) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000018874679D80>'


