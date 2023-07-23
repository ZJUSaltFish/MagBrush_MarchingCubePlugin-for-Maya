# encoding: utf-8
# module PySide2.QtSensors
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSensors.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSensorGestureManager(__PySide2_QtCore.QObject):
    """ QSensorGestureManager(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def gestureIds(self): # real signature unknown; restored from __doc__
        """ gestureIds(self) -> typing.List[str] """
        pass

    def newSensorGestureAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def recognizerSignals(self, recognizerId): # real signature unknown; restored from __doc__
        """ recognizerSignals(self, recognizerId: str) -> typing.List[str] """
        pass

    def registerSensorGestureRecognizer(self, recognizer): # real signature unknown; restored from __doc__
        """ registerSensorGestureRecognizer(self, recognizer: PySide2.QtSensors.QSensorGestureRecognizer) -> bool """
        return False

    def sensorGestureRecognizer(self, id): # real signature unknown; restored from __doc__
        """ sensorGestureRecognizer(id: str) -> PySide2.QtSensors.QSensorGestureRecognizer """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000206286B2E40>'


