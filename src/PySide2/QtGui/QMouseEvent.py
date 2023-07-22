# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QInputEvent import QInputEvent

class QMouseEvent(QInputEvent):
    """
    QMouseEvent(self, type: PySide2.QtCore.QEvent.Type, localPos: PySide2.QtCore.QPointF, button: PySide2.QtCore.Qt.MouseButton, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> None
    QMouseEvent(self, type: PySide2.QtCore.QEvent.Type, localPos: PySide2.QtCore.QPointF, screenPos: PySide2.QtCore.QPointF, button: PySide2.QtCore.Qt.MouseButton, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> None
    QMouseEvent(self, type: PySide2.QtCore.QEvent.Type, localPos: PySide2.QtCore.QPointF, windowPos: PySide2.QtCore.QPointF, screenPos: PySide2.QtCore.QPointF, button: PySide2.QtCore.Qt.MouseButton, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> None
    QMouseEvent(self, type: PySide2.QtCore.QEvent.Type, localPos: PySide2.QtCore.QPointF, windowPos: PySide2.QtCore.QPointF, screenPos: PySide2.QtCore.QPointF, button: PySide2.QtCore.Qt.MouseButton, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, source: PySide2.QtCore.Qt.MouseEventSource) -> None
    """
    def button(self): # real signature unknown; restored from __doc__
        """ button(self) -> PySide2.QtCore.Qt.MouseButton """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> PySide2.QtCore.Qt.MouseButtons """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtCore.Qt.MouseEventFlags """
        pass

    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> PySide2.QtCore.QPoint """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ globalX(self) -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ globalY(self) -> int """
        return 0

    def localPos(self): # real signature unknown; restored from __doc__
        """ localPos(self) -> PySide2.QtCore.QPointF """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> PySide2.QtCore.QPoint """
        pass

    def screenPos(self): # real signature unknown; restored from __doc__
        """ screenPos(self) -> PySide2.QtCore.QPointF """
        pass

    def setLocalPos(self, localPosition): # real signature unknown; restored from __doc__
        """ setLocalPos(self, localPosition: PySide2.QtCore.QPointF) -> None """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> PySide2.QtCore.Qt.MouseEventSource """
        pass

    def windowPos(self): # real signature unknown; restored from __doc__
        """ windowPos(self) -> PySide2.QtCore.QPointF """
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

    def __init__(self, type, localPos, button, buttons, modifiers): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    l = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    s = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    velocity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



