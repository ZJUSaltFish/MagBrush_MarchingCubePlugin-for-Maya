# encoding: utf-8
# module PySide2.QtSensors
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSensors.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QSensorReading import QSensorReading

class QTapReading(QSensorReading):
    """ QTapReading(self, parent: PySide2.QtCore.QObject) -> None """
    def copyValuesFrom(self, other): # real signature unknown; restored from __doc__
        """ copyValuesFrom(self, other: PySide2.QtSensors.QSensorReading) -> None """
        pass

    def isDoubleTap(self): # real signature unknown; restored from __doc__
        """ isDoubleTap(self) -> bool """
        return False

    def setDoubleTap(self, doubleTap): # real signature unknown; restored from __doc__
        """ setDoubleTap(self, doubleTap: bool) -> None """
        pass

    def setTapDirection(self, tapDirection): # real signature unknown; restored from __doc__
        """ setTapDirection(self, tapDirection: PySide2.QtSensors.QTapReading.TapDirection) -> None """
        pass

    def tapDirection(self): # real signature unknown; restored from __doc__
        """ tapDirection(self) -> PySide2.QtSensors.QTapReading.TapDirection """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000206286B1E00>'
    TapDirection = None # (!) real value is "<class 'PySide2.QtSensors.QTapReading.TapDirection'>"
    Undefined = PySide2.QtSensors.QTapReading.TapDirection.Undefined
    X = PySide2.QtSensors.QTapReading.TapDirection.X
    X_Both = PySide2.QtSensors.QTapReading.TapDirection.X_Both
    X_Neg = PySide2.QtSensors.QTapReading.TapDirection.X_Neg
    X_Pos = PySide2.QtSensors.QTapReading.TapDirection.X_Pos
    Y = PySide2.QtSensors.QTapReading.TapDirection.Y
    Y_Both = PySide2.QtSensors.QTapReading.TapDirection.Y_Both
    Y_Neg = PySide2.QtSensors.QTapReading.TapDirection.Y_Neg
    Y_Pos = PySide2.QtSensors.QTapReading.TapDirection.Y_Pos
    Z = PySide2.QtSensors.QTapReading.TapDirection.Z
    Z_Both = PySide2.QtSensors.QTapReading.TapDirection.Z_Both
    Z_Neg = PySide2.QtSensors.QTapReading.TapDirection.Z_Neg
    Z_Pos = PySide2.QtSensors.QTapReading.TapDirection.Z_Pos


