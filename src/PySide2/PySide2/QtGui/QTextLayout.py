# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTextLayout(__Shiboken.Object):
    """
    QTextLayout(self) -> None
    QTextLayout(self, b: PySide2.QtGui.QTextBlock) -> None
    QTextLayout(self, text: str) -> None
    QTextLayout(self, text: str, font: PySide2.QtGui.QFont, paintdevice: typing.Optional[PySide2.QtGui.QPaintDevice] = None) -> None
    """
    def additionalFormats(self): # real signature unknown; restored from __doc__
        """ additionalFormats(self) -> typing.List[PySide2.QtGui.QTextLayout.FormatRange] """
        pass

    def beginLayout(self): # real signature unknown; restored from __doc__
        """ beginLayout(self) -> None """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def cacheEnabled(self): # real signature unknown; restored from __doc__
        """ cacheEnabled(self) -> bool """
        return False

    def clearAdditionalFormats(self): # real signature unknown; restored from __doc__
        """ clearAdditionalFormats(self) -> None """
        pass

    def clearFormats(self): # real signature unknown; restored from __doc__
        """ clearFormats(self) -> None """
        pass

    def clearLayout(self): # real signature unknown; restored from __doc__
        """ clearLayout(self) -> None """
        pass

    def createLine(self): # real signature unknown; restored from __doc__
        """ createLine(self) -> PySide2.QtGui.QTextLine """
        pass

    def cursorMoveStyle(self): # real signature unknown; restored from __doc__
        """ cursorMoveStyle(self) -> PySide2.QtCore.Qt.CursorMoveStyle """
        pass

    def draw(self, p, pos, selections, PySide2_QtGui_QTextLayout_FormatRange=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw(self, p: PySide2.QtGui.QPainter, pos: PySide2.QtCore.QPointF, selections: typing.List[PySide2.QtGui.QTextLayout.FormatRange] = [], clip: PySide2.QtCore.QRectF = Default(QRectF)) -> None """
        pass

    def drawCursor(self, p, pos, cursorPosition): # real signature unknown; restored from __doc__
        """
        drawCursor(self, p: PySide2.QtGui.QPainter, pos: PySide2.QtCore.QPointF, cursorPosition: int) -> None
        drawCursor(self, p: PySide2.QtGui.QPainter, pos: PySide2.QtCore.QPointF, cursorPosition: int, width: int) -> None
        """
        pass

    def endLayout(self): # real signature unknown; restored from __doc__
        """ endLayout(self) -> None """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def formats(self): # real signature unknown; restored from __doc__
        """ formats(self) -> typing.List[PySide2.QtGui.QTextLayout.FormatRange] """
        pass

    def isValidCursorPosition(self, pos): # real signature unknown; restored from __doc__
        """ isValidCursorPosition(self, pos: int) -> bool """
        return False

    def leftCursorPosition(self, oldPos): # real signature unknown; restored from __doc__
        """ leftCursorPosition(self, oldPos: int) -> int """
        return 0

    def lineAt(self, i): # real signature unknown; restored from __doc__
        """ lineAt(self, i: int) -> PySide2.QtGui.QTextLine """
        pass

    def lineCount(self): # real signature unknown; restored from __doc__
        """ lineCount(self) -> int """
        return 0

    def lineForTextPosition(self, pos): # real signature unknown; restored from __doc__
        """ lineForTextPosition(self, pos: int) -> PySide2.QtGui.QTextLine """
        pass

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ maximumWidth(self) -> float """
        return 0.0

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ minimumWidth(self) -> float """
        return 0.0

    def nextCursorPosition(self, oldPos, mode=None): # real signature unknown; restored from __doc__
        """ nextCursorPosition(self, oldPos: int, mode: PySide2.QtGui.QTextLayout.CursorMode = PySide2.QtGui.QTextLayout.CursorMode.SkipCharacters) -> int """
        return 0

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> PySide2.QtCore.QPointF """
        pass

    def preeditAreaPosition(self): # real signature unknown; restored from __doc__
        """ preeditAreaPosition(self) -> int """
        return 0

    def preeditAreaText(self): # real signature unknown; restored from __doc__
        """ preeditAreaText(self) -> str """
        return ""

    def previousCursorPosition(self, oldPos, mode=None): # real signature unknown; restored from __doc__
        """ previousCursorPosition(self, oldPos: int, mode: PySide2.QtGui.QTextLayout.CursorMode = PySide2.QtGui.QTextLayout.CursorMode.SkipCharacters) -> int """
        return 0

    def rightCursorPosition(self, oldPos): # real signature unknown; restored from __doc__
        """ rightCursorPosition(self, oldPos: int) -> int """
        return 0

    def setAdditionalFormats(self, overrides, PySide2_QtGui_QTextLayout_FormatRange=None): # real signature unknown; restored from __doc__
        """ setAdditionalFormats(self, overrides: typing.Sequence[PySide2.QtGui.QTextLayout.FormatRange]) -> None """
        pass

    def setCacheEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setCacheEnabled(self, enable: bool) -> None """
        pass

    def setCursorMoveStyle(self, style): # real signature unknown; restored from __doc__
        """ setCursorMoveStyle(self, style: PySide2.QtCore.Qt.CursorMoveStyle) -> None """
        pass

    def setFlags(self, flags): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: int) -> None """
        pass

    def setFont(self, f): # real signature unknown; restored from __doc__
        """ setFont(self, f: PySide2.QtGui.QFont) -> None """
        pass

    def setFormats(self, overrides, PySide2_QtGui_QTextLayout_FormatRange=None): # real signature unknown; restored from __doc__
        """ setFormats(self, overrides: typing.List[PySide2.QtGui.QTextLayout.FormatRange]) -> None """
        pass

    def setPosition(self, p): # real signature unknown; restored from __doc__
        """ setPosition(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def setPreeditArea(self, position, text): # real signature unknown; restored from __doc__
        """ setPreeditArea(self, position: int, text: str) -> None """
        pass

    def setRawFont(self, rawFont): # real signature unknown; restored from __doc__
        """ setRawFont(self, rawFont: PySide2.QtGui.QRawFont) -> None """
        pass

    def setText(self, string): # real signature unknown; restored from __doc__
        """ setText(self, string: str) -> None """
        pass

    def setTextOption(self, option): # real signature unknown; restored from __doc__
        """ setTextOption(self, option: PySide2.QtGui.QTextOption) -> None """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textOption(self): # real signature unknown; restored from __doc__
        """ textOption(self) -> PySide2.QtGui.QTextOption """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CursorMode = None # (!) real value is "<class 'PySide2.QtGui.QTextLayout.CursorMode'>"
    FormatRange = None # (!) real value is "<class 'PySide2.QtGui.QTextLayout.FormatRange'>"
    SkipCharacters = PySide2.QtGui.QTextLayout.CursorMode.SkipCharacters
    SkipWords = PySide2.QtGui.QTextLayout.CursorMode.SkipWords


