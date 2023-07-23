# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QInputEvent import QInputEvent

class QContextMenuEvent(QInputEvent):
    """
    QContextMenuEvent(self, reason: PySide2.QtGui.QContextMenuEvent.Reason, pos: PySide2.QtCore.QPoint) -> None
    QContextMenuEvent(self, reason: PySide2.QtGui.QContextMenuEvent.Reason, pos: PySide2.QtCore.QPoint, globalPos: PySide2.QtCore.QPoint) -> None
    QContextMenuEvent(self, reason: PySide2.QtGui.QContextMenuEvent.Reason, pos: PySide2.QtCore.QPoint, globalPos: PySide2.QtCore.QPoint, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> None
    """
    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> PySide2.QtCore.QPoint """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ globalX(self) -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ globalY(self) -> int """
        return 0

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> PySide2.QtCore.QPoint """
        pass

    def reason(self): # real signature unknown; restored from __doc__
        """ reason(self) -> PySide2.QtGui.QContextMenuEvent.Reason """
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

    def __init__(self, reason, pos): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Keyboard = PySide2.QtGui.QContextMenuEvent.Reason.Keyboard
    Mouse = PySide2.QtGui.QContextMenuEvent.Reason.Mouse
    Other = PySide2.QtGui.QContextMenuEvent.Reason.Other
    Reason = None # (!) real value is "<class 'PySide2.QtGui.QContextMenuEvent.Reason'>"


