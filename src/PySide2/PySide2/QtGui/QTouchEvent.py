# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QInputEvent import QInputEvent

class QTouchEvent(QInputEvent):
    """ QTouchEvent(self, eventType: PySide2.QtCore.QEvent.Type, device: typing.Optional[PySide2.QtGui.QTouchDevice] = None, modifiers: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, touchPointStates: PySide2.QtCore.Qt.TouchPointStates = Default(Qt.TouchPointStates), touchPoints: typing.Sequence[PySide2.QtGui.QTouchEvent.TouchPoint] = Default(QList< QTouchEvent.TouchPoint >)) -> None """
    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtGui.QTouchDevice """
        pass

    def setDevice(self, adevice): # real signature unknown; restored from __doc__
        """ setDevice(self, adevice: PySide2.QtGui.QTouchDevice) -> None """
        pass

    def setTarget(self, atarget): # real signature unknown; restored from __doc__
        """ setTarget(self, atarget: PySide2.QtCore.QObject) -> None """
        pass

    def setTouchPoints(self, atouchPoints, PySide2_QtGui_QTouchEvent_TouchPoint=None): # real signature unknown; restored from __doc__
        """ setTouchPoints(self, atouchPoints: typing.Sequence[PySide2.QtGui.QTouchEvent.TouchPoint]) -> None """
        pass

    def setTouchPointStates(self, aTouchPointStates): # real signature unknown; restored from __doc__
        """ setTouchPointStates(self, aTouchPointStates: PySide2.QtCore.Qt.TouchPointStates) -> None """
        pass

    def setWindow(self, awindow): # real signature unknown; restored from __doc__
        """ setWindow(self, awindow: PySide2.QtGui.QWindow) -> None """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> PySide2.QtCore.QObject """
        pass

    def touchPoints(self): # real signature unknown; restored from __doc__
        """ touchPoints(self) -> typing.List[PySide2.QtGui.QTouchEvent.TouchPoint] """
        pass

    def touchPointStates(self): # real signature unknown; restored from __doc__
        """ touchPointStates(self) -> PySide2.QtCore.Qt.TouchPointStates """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> PySide2.QtGui.QWindow """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, eventType, device, PySide2_QtGui_QTouchDevice=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    _target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    TouchPoint = None # (!) real value is "<class 'PySide2.QtGui.QTouchEvent.TouchPoint'>"


