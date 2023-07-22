# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QUndoGroup(__PySide2_QtCore.QObject):
    """ QUndoGroup(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def activeStack(self): # real signature unknown; restored from __doc__
        """ activeStack(self) -> PySide2.QtWidgets.QUndoStack """
        pass

    def activeStackChanged(self, *args, **kwargs): # real signature unknown
        pass

    def addStack(self, stack): # real signature unknown; restored from __doc__
        """ addStack(self, stack: PySide2.QtWidgets.QUndoStack) -> None """
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

    def createRedoAction(self, parent, prefix=''): # real signature unknown; restored from __doc__
        """ createRedoAction(self, parent: PySide2.QtCore.QObject, prefix: str = '') -> PySide2.QtWidgets.QAction """
        pass

    def createUndoAction(self, parent, prefix=''): # real signature unknown; restored from __doc__
        """ createUndoAction(self, parent: PySide2.QtCore.QObject, prefix: str = '') -> PySide2.QtWidgets.QAction """
        pass

    def indexChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isClean(self): # real signature unknown; restored from __doc__
        """ isClean(self) -> bool """
        return False

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) -> None """
        pass

    def redoText(self): # real signature unknown; restored from __doc__
        """ redoText(self) -> str """
        return ""

    def redoTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def removeStack(self, stack): # real signature unknown; restored from __doc__
        """ removeStack(self, stack: PySide2.QtWidgets.QUndoStack) -> None """
        pass

    def setActiveStack(self, stack): # real signature unknown; restored from __doc__
        """ setActiveStack(self, stack: PySide2.QtWidgets.QUndoStack) -> None """
        pass

    def stacks(self): # real signature unknown; restored from __doc__
        """ stacks(self) -> typing.List[PySide2.QtWidgets.QUndoStack] """
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) -> None """
        pass

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50859640>'


