# encoding: utf-8
# module PySide2.QtSensors
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSensors.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QSensorReading import QSensorReading

class QOrientationReading(QSensorReading):
    """ QOrientationReading(self, parent: PySide2.QtCore.QObject) -> None """
    def copyValuesFrom(self, other): # real signature unknown; restored from __doc__
        """ copyValuesFrom(self, other: PySide2.QtSensors.QSensorReading) -> None """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtSensors.QOrientationReading.Orientation """
        pass

    def setOrientation(self, orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, orientation: PySide2.QtSensors.QOrientationReading.Orientation) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    FaceDown = PySide2.QtSensors.QOrientationReading.Orientation.FaceDown
    FaceUp = PySide2.QtSensors.QOrientationReading.Orientation.FaceUp
    LeftUp = PySide2.QtSensors.QOrientationReading.Orientation.LeftUp
    Orientation = None # (!) real value is "<class 'PySide2.QtSensors.QOrientationReading.Orientation'>"
    RightUp = PySide2.QtSensors.QOrientationReading.Orientation.RightUp
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000206286B0E00>'
    TopDown = PySide2.QtSensors.QOrientationReading.Orientation.TopDown
    TopUp = PySide2.QtSensors.QOrientationReading.Orientation.TopUp
    Undefined = PySide2.QtSensors.QOrientationReading.Orientation.Undefined


