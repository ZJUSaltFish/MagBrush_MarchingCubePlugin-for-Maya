# encoding: utf-8
# module PySide2.QtSensors
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSensors.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSensorBackend(__PySide2_QtCore.QObject):
    """ QSensorBackend(self, sensor: PySide2.QtSensors.QSensor, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addDataRate(self, min, max): # real signature unknown; restored from __doc__
        """ addDataRate(self, min: float, max: float) -> None """
        pass

    def addOutputRange(self, min, max, accuracy): # real signature unknown; restored from __doc__
        """ addOutputRange(self, min: float, max: float, accuracy: float) -> None """
        pass

    def isFeatureSupported(self, feature): # real signature unknown; restored from __doc__
        """ isFeatureSupported(self, feature: PySide2.QtSensors.QSensor.Feature) -> bool """
        return False

    def newReadingAvailable(self): # real signature unknown; restored from __doc__
        """ newReadingAvailable(self) -> None """
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> PySide2.QtSensors.QSensorReading """
        pass

    def sensor(self): # real signature unknown; restored from __doc__
        """ sensor(self) -> PySide2.QtSensors.QSensor """
        pass

    def sensorBusy(self): # real signature unknown; restored from __doc__
        """ sensorBusy(self) -> None """
        pass

    def sensorError(self, error): # real signature unknown; restored from __doc__
        """ sensorError(self, error: int) -> None """
        pass

    def sensorStopped(self): # real signature unknown; restored from __doc__
        """ sensorStopped(self) -> None """
        pass

    def setDataRates(self, otherSensor): # real signature unknown; restored from __doc__
        """ setDataRates(self, otherSensor: PySide2.QtSensors.QSensor) -> None """
        pass

    def setDescription(self, description): # real signature unknown; restored from __doc__
        """ setDescription(self, description: str) -> None """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> None """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, sensor, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000206286B3180>'


