# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTextLine(__Shiboken.Object):
    """ QTextLine(self) -> None """
    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> float """
        return 0.0

    def cursorToX(self, cursorPos, edge=None): # real signature unknown; restored from __doc__
        """ cursorToX(self, cursorPos: int, edge: PySide2.QtGui.QTextLine.Edge = PySide2.QtGui.QTextLine.Edge.Leading) -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> float """
        return 0.0

    def draw(self, p, point, selection, PySide2_QtGui_QTextLayout_FormatRange=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw(self, p: PySide2.QtGui.QPainter, point: PySide2.QtCore.QPointF, selection: typing.Optional[PySide2.QtGui.QTextLayout.FormatRange] = None) -> None """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def horizontalAdvance(self): # real signature unknown; restored from __doc__
        """ horizontalAdvance(self) -> float """
        return 0.0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ leading(self) -> float """
        return 0.0

    def leadingIncluded(self): # real signature unknown; restored from __doc__
        """ leadingIncluded(self) -> bool """
        return False

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def naturalTextRect(self): # real signature unknown; restored from __doc__
        """ naturalTextRect(self) -> PySide2.QtCore.QRectF """
        pass

    def naturalTextWidth(self): # real signature unknown; restored from __doc__
        """ naturalTextWidth(self) -> float """
        return 0.0

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> PySide2.QtCore.QPointF """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> PySide2.QtCore.QRectF """
        pass

    def setLeadingIncluded(self, included): # real signature unknown; restored from __doc__
        """ setLeadingIncluded(self, included: bool) -> None """
        pass

    def setLineWidth(self, width): # real signature unknown; restored from __doc__
        """ setLineWidth(self, width: float) -> None """
        pass

    def setNumColumns(self, columns): # real signature unknown; restored from __doc__
        """
        setNumColumns(self, columns: int) -> None
        setNumColumns(self, columns: int, alignmentWidth: float) -> None
        """
        pass

    def setPosition(self, pos): # real signature unknown; restored from __doc__
        """ setPosition(self, pos: PySide2.QtCore.QPointF) -> None """
        pass

    def textLength(self): # real signature unknown; restored from __doc__
        """ textLength(self) -> int """
        return 0

    def textStart(self): # real signature unknown; restored from __doc__
        """ textStart(self) -> int """
        return 0

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def xToCursor(self, x, edge=None): # real signature unknown; restored from __doc__
        """ xToCursor(self, x: float, edge: PySide2.QtGui.QTextLine.CursorPosition = PySide2.QtGui.QTextLine.CursorPosition.CursorBetweenCharacters) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CursorBetweenCharacters = PySide2.QtGui.QTextLine.CursorPosition.CursorBetweenCharacters
    CursorOnCharacter = PySide2.QtGui.QTextLine.CursorPosition.CursorOnCharacter
    CursorPosition = None # (!) real value is "<class 'PySide2.QtGui.QTextLine.CursorPosition'>"
    Edge = None # (!) real value is "<class 'PySide2.QtGui.QTextLine.Edge'>"
    Leading = PySide2.QtGui.QTextLine.Edge.Leading
    Trailing = PySide2.QtGui.QTextLine.Edge.Trailing


