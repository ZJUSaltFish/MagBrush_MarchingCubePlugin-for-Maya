# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAccessibleTextInterface(__Shiboken.Object):
    """ QAccessibleTextInterface(self) -> None """
    def addSelection(self, startOffset, endOffset): # real signature unknown; restored from __doc__
        """ addSelection(self, startOffset: int, endOffset: int) -> None """
        pass

    def attributes(self, offset): # real signature unknown; restored from __doc__
        """ attributes(self, offset: int) -> typing.Tuple[str, int, int] """
        pass

    def characterCount(self): # real signature unknown; restored from __doc__
        """ characterCount(self) -> int """
        return 0

    def characterRect(self, offset): # real signature unknown; restored from __doc__
        """ characterRect(self, offset: int) -> PySide2.QtCore.QRect """
        pass

    def cursorPosition(self): # real signature unknown; restored from __doc__
        """ cursorPosition(self) -> int """
        return 0

    def offsetAtPoint(self, point): # real signature unknown; restored from __doc__
        """ offsetAtPoint(self, point: PySide2.QtCore.QPoint) -> int """
        return 0

    def removeSelection(self, selectionIndex): # real signature unknown; restored from __doc__
        """ removeSelection(self, selectionIndex: int) -> None """
        pass

    def scrollToSubstring(self, startIndex, endIndex): # real signature unknown; restored from __doc__
        """ scrollToSubstring(self, startIndex: int, endIndex: int) -> None """
        pass

    def selection(self, selectionIndex): # real signature unknown; restored from __doc__
        """ selection(self, selectionIndex: int) -> typing.Tuple[int, int] """
        pass

    def selectionCount(self): # real signature unknown; restored from __doc__
        """ selectionCount(self) -> int """
        return 0

    def setCursorPosition(self, position): # real signature unknown; restored from __doc__
        """ setCursorPosition(self, position: int) -> None """
        pass

    def setSelection(self, selectionIndex, startOffset, endOffset): # real signature unknown; restored from __doc__
        """ setSelection(self, selectionIndex: int, startOffset: int, endOffset: int) -> None """
        pass

    def text(self, startOffset, endOffset): # real signature unknown; restored from __doc__
        """ text(self, startOffset: int, endOffset: int) -> str """
        return ""

    def textAfterOffset(self, offset, boundaryType): # real signature unknown; restored from __doc__
        """ textAfterOffset(self, offset: int, boundaryType: PySide2.QtGui.QAccessible.TextBoundaryType) -> typing.Tuple[str, int, int] """
        pass

    def textAtOffset(self, offset, boundaryType): # real signature unknown; restored from __doc__
        """ textAtOffset(self, offset: int, boundaryType: PySide2.QtGui.QAccessible.TextBoundaryType) -> typing.Tuple[str, int, int] """
        pass

    def textBeforeOffset(self, offset, boundaryType): # real signature unknown; restored from __doc__
        """ textBeforeOffset(self, offset: int, boundaryType: PySide2.QtGui.QAccessible.TextBoundaryType) -> typing.Tuple[str, int, int] """
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


