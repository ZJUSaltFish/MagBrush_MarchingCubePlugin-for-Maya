# encoding: utf-8
# module PySide2.QtSensors
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSensors.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QSensor import QSensor

class QAccelerometer(QSensor):
    """ QAccelerometer(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def accelerationMode(self): # real signature unknown; restored from __doc__
        """ accelerationMode(self) -> PySide2.QtSensors.QAccelerometer.AccelerationMode """
        pass

    def accelerationModeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> PySide2.QtSensors.QAccelerometerReading """
        pass

    def setAccelerationMode(self, accelerationMode): # real signature unknown; restored from __doc__
        """ setAccelerationMode(self, accelerationMode: PySide2.QtSensors.QAccelerometer.AccelerationMode) -> None """
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

    AccelerationMode = None # (!) real value is "<class 'PySide2.QtSensors.QAccelerometer.AccelerationMode'>"
    Combined = PySide2.QtSensors.QAccelerometer.AccelerationMode.Combined
    Gravity = PySide2.QtSensors.QAccelerometer.AccelerationMode.Gravity
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000206286C4480>'
    type = 'QAccelerometer'
    User = PySide2.QtSensors.QAccelerometer.AccelerationMode.User


