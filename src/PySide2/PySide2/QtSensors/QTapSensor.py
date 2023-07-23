# encoding: utf-8
# module PySide2.QtSensors
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSensors.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QSensor import QSensor

class QTapSensor(QSensor):
    """ QTapSensor(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> PySide2.QtSensors.QTapReading """
        pass

    def returnDoubleTapEvents(self): # real signature unknown; restored from __doc__
        """ returnDoubleTapEvents(self) -> bool """
        return False

    def returnDoubleTapEventsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setReturnDoubleTapEvents(self, returnDoubleTapEvents): # real signature unknown; restored from __doc__
        """ setReturnDoubleTapEvents(self, returnDoubleTapEvents: bool) -> None """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000206286C4F00>'
    type = 'QTapSensor'


