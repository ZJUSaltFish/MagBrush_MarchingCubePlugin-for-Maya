# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QUndoCommand(__Shiboken.Object):
    """
    QUndoCommand(self, parent: typing.Optional[PySide2.QtWidgets.QUndoCommand] = None) -> None
    QUndoCommand(self, text: str, parent: typing.Optional[PySide2.QtWidgets.QUndoCommand] = None) -> None
    """
    def actionText(self): # real signature unknown; restored from __doc__
        """ actionText(self) -> str """
        return ""

    def child(self, index): # real signature unknown; restored from __doc__
        """ child(self, index: int) -> PySide2.QtWidgets.QUndoCommand """
        pass

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def isObsolete(self): # real signature unknown; restored from __doc__
        """ isObsolete(self) -> bool """
        return False

    def mergeWith(self, other): # real signature unknown; restored from __doc__
        """ mergeWith(self, other: PySide2.QtWidgets.QUndoCommand) -> bool """
        return False

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) -> None """
        pass

    def setObsolete(self, obsolete): # real signature unknown; restored from __doc__
        """ setObsolete(self, obsolete: bool) -> None """
        pass

    def setText(self, text): # real signature unknown; restored from __doc__
        """ setText(self, text: str) -> None """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QUndoCommand=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


