# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QUndoCommand(__sip.wrapper):
    """
    QUndoCommand(parent: typing.Optional[QUndoCommand] = None)
    QUndoCommand(text: str, parent: typing.Optional[QUndoCommand] = None)
    """
    def actionText(self): # real signature unknown; restored from __doc__
        """ actionText(self) -> str """
        return ""

    def child(self, index): # real signature unknown; restored from __doc__
        """ child(self, index: int) -> QUndoCommand """
        return QUndoCommand

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
        """ mergeWith(self, other: QUndoCommand) -> bool """
        return False

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def setObsolete(self, obsolete): # real signature unknown; restored from __doc__
        """ setObsolete(self, obsolete: bool) """
        pass

    def setText(self, text): # real signature unknown; restored from __doc__
        """ setText(self, text: str) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


