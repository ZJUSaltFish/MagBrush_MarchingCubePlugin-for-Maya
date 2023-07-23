# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QAccessibleTextCursorEvent import QAccessibleTextCursorEvent

class QAccessibleTextInsertEvent(QAccessibleTextCursorEvent):
    """
    QAccessibleTextInsertEvent(self, iface: PySide2.QtGui.QAccessibleInterface, position: int, text: str) -> None
    QAccessibleTextInsertEvent(self, obj: PySide2.QtCore.QObject, position: int, text: str) -> None
    """
    def changePosition(self): # real signature unknown; restored from __doc__
        """ changePosition(self) -> int """
        return 0

    def textInserted(self): # real signature unknown; restored from __doc__
        """ textInserted(self) -> str """
        return ""

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, iface, position, text): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


