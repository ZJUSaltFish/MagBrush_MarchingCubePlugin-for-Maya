# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QInputEvent import QInputEvent

class QWheelEvent(QInputEvent):
    """
    QWheelEvent(self, pos: PySide2.QtCore.QPointF, delta: int, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, orient: PySide2.QtCore.Qt.Orientation = PySide2.QtCore.Qt.Orientation.Vertical) -> None
    QWheelEvent(self, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, delta: int, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, orient: PySide2.QtCore.Qt.Orientation = PySide2.QtCore.Qt.Orientation.Vertical) -> None
    QWheelEvent(self, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, pixelDelta: PySide2.QtCore.QPoint, angleDelta: PySide2.QtCore.QPoint, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, phase: PySide2.QtCore.Qt.ScrollPhase, inverted: bool, source: PySide2.QtCore.Qt.MouseEventSource = PySide2.QtCore.Qt.MouseEventSource.MouseEventNotSynthesized) -> None
    QWheelEvent(self, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, pixelDelta: PySide2.QtCore.QPoint, angleDelta: PySide2.QtCore.QPoint, qt4Delta: int, qt4Orientation: PySide2.QtCore.Qt.Orientation, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> None
    QWheelEvent(self, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, pixelDelta: PySide2.QtCore.QPoint, angleDelta: PySide2.QtCore.QPoint, qt4Delta: int, qt4Orientation: PySide2.QtCore.Qt.Orientation, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, phase: PySide2.QtCore.Qt.ScrollPhase) -> None
    QWheelEvent(self, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, pixelDelta: PySide2.QtCore.QPoint, angleDelta: PySide2.QtCore.QPoint, qt4Delta: int, qt4Orientation: PySide2.QtCore.Qt.Orientation, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, phase: PySide2.QtCore.Qt.ScrollPhase, source: PySide2.QtCore.Qt.MouseEventSource) -> None
    QWheelEvent(self, pos: PySide2.QtCore.QPointF, globalPos: PySide2.QtCore.QPointF, pixelDelta: PySide2.QtCore.QPoint, angleDelta: PySide2.QtCore.QPoint, qt4Delta: int, qt4Orientation: PySide2.QtCore.Qt.Orientation, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, phase: PySide2.QtCore.Qt.ScrollPhase, source: PySide2.QtCore.Qt.MouseEventSource, inverted: bool) -> None
    """
    def angleDelta(self): # real signature unknown; restored from __doc__
        """ angleDelta(self) -> PySide2.QtCore.QPoint """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> PySide2.QtCore.Qt.MouseButtons """
        pass

    def delta(self): # real signature unknown; restored from __doc__
        """ delta(self) -> int """
        return 0

    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> PySide2.QtCore.QPoint """
        pass

    def globalPosF(self): # real signature unknown; restored from __doc__
        """ globalPosF(self) -> PySide2.QtCore.QPointF """
        pass

    def globalPosition(self): # real signature unknown; restored from __doc__
        """ globalPosition(self) -> PySide2.QtCore.QPointF """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ globalX(self) -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ globalY(self) -> int """
        return 0

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> bool """
        return False

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.Orientation """
        pass

    def phase(self): # real signature unknown; restored from __doc__
        """ phase(self) -> PySide2.QtCore.Qt.ScrollPhase """
        pass

    def pixelDelta(self): # real signature unknown; restored from __doc__
        """ pixelDelta(self) -> PySide2.QtCore.QPoint """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> PySide2.QtCore.QPoint """
        pass

    def posF(self): # real signature unknown; restored from __doc__
        """ posF(self) -> PySide2.QtCore.QPointF """
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> PySide2.QtCore.QPointF """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> PySide2.QtCore.Qt.MouseEventSource """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, pos, delta, buttons, modifiers, orient=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    angleD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    invertedScrolling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixelD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qt4D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qt4O = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _unused_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



