# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QUndoStack(__PySide2_QtCore.QObject):
    """ QUndoStack(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def beginMacro(self, text): # real signature unknown; restored from __doc__
        """ beginMacro(self, text: str) -> None """
        pass

    def canRedo(self): # real signature unknown; restored from __doc__
        """ canRedo(self) -> bool """
        return False

    def canRedoChanged(self, *args, **kwargs): # real signature unknown
        pass

    def canUndo(self): # real signature unknown; restored from __doc__
        """ canUndo(self) -> bool """
        return False

    def canUndoChanged(self, *args, **kwargs): # real signature unknown
        pass

    def cleanChanged(self, *args, **kwargs): # real signature unknown
        pass

    def cleanIndex(self): # real signature unknown; restored from __doc__
        """ cleanIndex(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def command(self, index): # real signature unknown; restored from __doc__
        """ command(self, index: int) -> PySide2.QtWidgets.QUndoCommand """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def createRedoAction(self, parent, prefix=''): # real signature unknown; restored from __doc__
        """ createRedoAction(self, parent: PySide2.QtCore.QObject, prefix: str = '') -> PySide2.QtWidgets.QAction """
        pass

    def createUndoAction(self, parent, prefix=''): # real signature unknown; restored from __doc__
        """ createUndoAction(self, parent: PySide2.QtCore.QObject, prefix: str = '') -> PySide2.QtWidgets.QAction """
        pass

    def endMacro(self): # real signature unknown; restored from __doc__
        """ endMacro(self) -> None """
        pass

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> int """
        return 0

    def indexChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isClean(self): # real signature unknown; restored from __doc__
        """ isClean(self) -> bool """
        return False

    def push(self, cmd): # real signature unknown; restored from __doc__
        """ push(self, cmd: PySide2.QtWidgets.QUndoCommand) -> None """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) -> None """
        pass

    def redoText(self): # real signature unknown; restored from __doc__
        """ redoText(self) -> str """
        return ""

    def redoTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def resetClean(self): # real signature unknown; restored from __doc__
        """ resetClean(self) -> None """
        pass

    def setActive(self, active=True): # real signature unknown; restored from __doc__
        """ setActive(self, active: bool = True) -> None """
        pass

    def setClean(self): # real signature unknown; restored from __doc__
        """ setClean(self) -> None """
        pass

    def setIndex(self, idx): # real signature unknown; restored from __doc__
        """ setIndex(self, idx: int) -> None """
        pass

    def setUndoLimit(self, limit): # real signature unknown; restored from __doc__
        """ setUndoLimit(self, limit: int) -> None """
        pass

    def text(self, idx): # real signature unknown; restored from __doc__
        """ text(self, idx: int) -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) -> None """
        pass

    def undoLimit(self): # real signature unknown; restored from __doc__
        """ undoLimit(self) -> int """
        return 0

    def undoText(self): # real signature unknown; restored from __doc__
        """ undoText(self) -> str """
        return ""

    def undoTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50858B40>'


