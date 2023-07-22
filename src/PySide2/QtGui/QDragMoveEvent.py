# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QDropEvent import QDropEvent

class QDragMoveEvent(QDropEvent):
    """ QDragMoveEvent(self, pos: PySide2.QtCore.QPoint, actions: PySide2.QtCore.Qt.DropActions, data: PySide2.QtCore.QMimeData, buttons: PySide2.QtCore.Qt.MouseButtons, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, type: PySide2.QtCore.QEvent.Type = PySide2.QtCore.QEvent.Type.DragMove) -> None """
    def accept(self): # real signature unknown; restored from __doc__
        """
        accept(self) -> None
        accept(self, r: PySide2.QtCore.QRect) -> None
        """
        pass

    def answerRect(self): # real signature unknown; restored from __doc__
        """ answerRect(self) -> PySide2.QtCore.QRect """
        pass

    def ignore(self): # real signature unknown; restored from __doc__
        """
        ignore(self) -> None
        ignore(self, r: PySide2.QtCore.QRect) -> None
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, pos, actions, data, buttons, modifiers, type=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


