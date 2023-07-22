# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QInputEvent import QInputEvent

class QNativeGestureEvent(QInputEvent):
    """
    QNativeGestureEvent(self, type: PySide2.QtCore.Qt.NativeGestureType, dev: PySide2.QtGui.QTouchDevice, localPos: PySide2.QtCore.QPointF, windowPos: PySide2.QtCore.QPointF, screenPos: PySide2.QtCore.QPointF, value: float, sequenceId: int, intArgument: int) -> None
    QNativeGestureEvent(self, type: PySide2.QtCore.Qt.NativeGestureType, localPos: PySide2.QtCore.QPointF, windowPos: PySide2.QtCore.QPointF, screenPos: PySide2.QtCore.QPointF, value: float, sequenceId: int, intArgument: int) -> None
    """
    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtGui.QTouchDevice """
        pass

    def gestureType(self): # real signature unknown; restored from __doc__
        """ gestureType(self) -> PySide2.QtCore.Qt.NativeGestureType """
        pass

    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> PySide2.QtCore.QPoint """
        pass

    def localPos(self): # real signature unknown; restored from __doc__
        """ localPos(self) -> PySide2.QtCore.QPointF """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> PySide2.QtCore.QPoint """
        pass

    def screenPos(self): # real signature unknown; restored from __doc__
        """ screenPos(self) -> PySide2.QtCore.QPointF """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> float """
        return 0.0

    def windowPos(self): # real signature unknown; restored from __doc__
        """ windowPos(self) -> PySide2.QtCore.QPointF """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type, dev, localPos, windowPos, screenPos, value, sequenceId, intArgument): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


