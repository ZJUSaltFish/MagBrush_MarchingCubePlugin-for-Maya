# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QInputMethodEvent(__PySide2_QtCore.QEvent):
    """
    QInputMethodEvent(self) -> None
    QInputMethodEvent(self, other: PySide2.QtGui.QInputMethodEvent) -> None
    QInputMethodEvent(self, preeditText: str, attributes: typing.Sequence[PySide2.QtGui.QInputMethodEvent.Attribute]) -> None
    """
    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> typing.List[PySide2.QtGui.QInputMethodEvent.Attribute] """
        pass

    def commitString(self): # real signature unknown; restored from __doc__
        """ commitString(self) -> str """
        return ""

    def preeditString(self): # real signature unknown; restored from __doc__
        """ preeditString(self) -> str """
        return ""

    def replacementLength(self): # real signature unknown; restored from __doc__
        """ replacementLength(self) -> int """
        return 0

    def replacementStart(self): # real signature unknown; restored from __doc__
        """ replacementStart(self) -> int """
        return 0

    def setCommitString(self, commitString, replaceFrom=0, replaceLength=0): # real signature unknown; restored from __doc__
        """ setCommitString(self, commitString: str, replaceFrom: int = 0, replaceLength: int = 0) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Attribute = None # (!) real value is "<class 'PySide2.QtGui.QInputMethodEvent.Attribute'>"
    AttributeType = None # (!) real value is "<class 'PySide2.QtGui.QInputMethodEvent.AttributeType'>"
    Cursor = PySide2.QtGui.QInputMethodEvent.AttributeType.Cursor
    Language = PySide2.QtGui.QInputMethodEvent.AttributeType.Language
    Ruby = PySide2.QtGui.QInputMethodEvent.AttributeType.Ruby
    Selection = PySide2.QtGui.QInputMethodEvent.AttributeType.Selection
    TextFormat = PySide2.QtGui.QInputMethodEvent.AttributeType.TextFormat


