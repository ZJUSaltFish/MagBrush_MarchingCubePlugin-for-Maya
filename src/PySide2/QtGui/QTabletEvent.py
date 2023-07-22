# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QInputEvent import QInputEvent

class QTabletEvent(QInputEvent):
    """
    QTabletEvent(self, t: PySide2.QtCore.QEvent.Type, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, device: int, pointerType: int, pressure: float, xTilt: int, yTilt: int, tangentialPressure: float, rotation: float, z: int, keyState: PySide2.QtCore.Qt.KeyboardModifiers, uniqueID: int) -> None
    QTabletEvent(self, t: PySide2.QtCore.QEvent.Type, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, device: int, pointerType: int, pressure: float, xTilt: int, yTilt: int, tangentialPressure: float, rotation: float, z: int, keyState: PySide2.QtCore.Qt.KeyboardModifiers, uniqueID: int, button: PySide2.QtCore.Qt.MouseButton, buttons: PySide2.QtCore.Qt.MouseButtons) -> None
    """
    def button(self): # real signature unknown; restored from __doc__
        """ button(self) -> PySide2.QtCore.Qt.MouseButton """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> PySide2.QtCore.Qt.MouseButtons """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtGui.QTabletEvent.TabletDevice """
        pass

    def deviceType(self): # real signature unknown; restored from __doc__
        """ deviceType(self) -> PySide2.QtGui.QTabletEvent.TabletDevice """
        pass

    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> PySide2.QtCore.QPoint """
        pass

    def globalPosF(self): # real signature unknown; restored from __doc__
        """ globalPosF(self) -> PySide2.QtCore.QPointF """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ globalX(self) -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ globalY(self) -> int """
        return 0

    def hiResGlobalX(self): # real signature unknown; restored from __doc__
        """ hiResGlobalX(self) -> float """
        return 0.0

    def hiResGlobalY(self): # real signature unknown; restored from __doc__
        """ hiResGlobalY(self) -> float """
        return 0.0

    def pointerType(self): # real signature unknown; restored from __doc__
        """ pointerType(self) -> PySide2.QtGui.QTabletEvent.PointerType """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> PySide2.QtCore.QPoint """
        pass

    def posF(self): # real signature unknown; restored from __doc__
        """ posF(self) -> PySide2.QtCore.QPointF """
        pass

    def pressure(self): # real signature unknown; restored from __doc__
        """ pressure(self) -> float """
        return 0.0

    def rotation(self): # real signature unknown; restored from __doc__
        """ rotation(self) -> float """
        return 0.0

    def tangentialPressure(self): # real signature unknown; restored from __doc__
        """ tangentialPressure(self) -> float """
        return 0.0

    def uniqueId(self): # real signature unknown; restored from __doc__
        """ uniqueId(self) -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def xTilt(self): # real signature unknown; restored from __doc__
        """ xTilt(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def yTilt(self): # real signature unknown; restored from __doc__
        """ yTilt(self) -> int """
        return 0

    def z(self): # real signature unknown; restored from __doc__
        """ z(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, t, pos, globalPos, device, pointerType, pressure, xTilt, yTilt, tangentialPressure, rotation, z, keyState, uniqueID): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Airbrush = PySide2.QtGui.QTabletEvent.TabletDevice.Airbrush
    Cursor = PySide2.QtGui.QTabletEvent.PointerType.Cursor
    Eraser = PySide2.QtGui.QTabletEvent.PointerType.Eraser
    FourDMouse = PySide2.QtGui.QTabletEvent.TabletDevice.FourDMouse
    NoDevice = PySide2.QtGui.QTabletEvent.TabletDevice.NoDevice
    Pen = PySide2.QtGui.QTabletEvent.PointerType.Pen
    PointerType = None # (!) real value is "<class 'PySide2.QtGui.QTabletEvent.PointerType'>"
    Puck = PySide2.QtGui.QTabletEvent.TabletDevice.Puck
    RotationStylus = PySide2.QtGui.QTabletEvent.TabletDevice.RotationStylus
    Stylus = PySide2.QtGui.QTabletEvent.TabletDevice.Stylus
    TabletDevice = None # (!) real value is "<class 'PySide2.QtGui.QTabletEvent.TabletDevice'>"
    UnknownPointer = PySide2.QtGui.QTabletEvent.PointerType.UnknownPointer
    XFreeEraser = PySide2.QtGui.QTabletEvent.TabletDevice.XFreeEraser


