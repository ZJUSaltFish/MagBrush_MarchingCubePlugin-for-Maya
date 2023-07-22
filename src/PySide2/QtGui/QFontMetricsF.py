# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QFontMetricsF(__Shiboken.Object):
    """
    QFontMetricsF(self, arg__1: PySide2.QtGui.QFontMetrics) -> None
    QFontMetricsF(self, arg__1: PySide2.QtGui.QFontMetricsF) -> None
    QFontMetricsF(self, font: PySide2.QtGui.QFont) -> None
    QFontMetricsF(self, font: PySide2.QtGui.QFont, pd: PySide2.QtGui.QPaintDevice) -> None
    """
    def ascent(self): # real signature unknown; restored from __doc__
        """ ascent(self) -> float """
        return 0.0

    def averageCharWidth(self): # real signature unknown; restored from __doc__
        """ averageCharWidth(self) -> float """
        return 0.0

    def boundingRect(self, r, flags, string, tabstops=0, tabarray, typing_Sequence=None, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        boundingRect(self, r: PySide2.QtCore.QRectF, flags: int, string: str, tabstops: int = 0, tabarray: typing.Optional[typing.Sequence[int]] = None) -> PySide2.QtCore.QRectF
        boundingRect(self, string: str) -> PySide2.QtCore.QRectF
        """
        pass

    def boundingRectChar(self, arg__1): # real signature unknown; restored from __doc__
        """ boundingRectChar(self, arg__1: str) -> PySide2.QtCore.QRectF """
        pass

    def capHeight(self): # real signature unknown; restored from __doc__
        """ capHeight(self) -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ descent(self) -> float """
        return 0.0

    def elidedText(self, text, mode, width, flags=0): # real signature unknown; restored from __doc__
        """ elidedText(self, text: str, mode: PySide2.QtCore.Qt.TextElideMode, width: float, flags: int = 0) -> str """
        return ""

    def fontDpi(self): # real signature unknown; restored from __doc__
        """ fontDpi(self) -> float """
        return 0.0

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def horizontalAdvance(self, arg__1): # real signature unknown; restored from __doc__
        """
        horizontalAdvance(self, arg__1: str) -> float
        horizontalAdvance(self, string: str, length: int = -1) -> float
        """
        return 0.0

    def inFont(self, arg__1): # real signature unknown; restored from __doc__
        """ inFont(self, arg__1: str) -> bool """
        return False

    def inFontUcs4(self, ucs4): # real signature unknown; restored from __doc__
        """ inFontUcs4(self, ucs4: int) -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ leading(self) -> float """
        return 0.0

    def leftBearing(self, arg__1): # real signature unknown; restored from __doc__
        """ leftBearing(self, arg__1: str) -> float """
        return 0.0

    def lineSpacing(self): # real signature unknown; restored from __doc__
        """ lineSpacing(self) -> float """
        return 0.0

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> float """
        return 0.0

    def maxWidth(self): # real signature unknown; restored from __doc__
        """ maxWidth(self) -> float """
        return 0.0

    def minLeftBearing(self): # real signature unknown; restored from __doc__
        """ minLeftBearing(self) -> float """
        return 0.0

    def minRightBearing(self): # real signature unknown; restored from __doc__
        """ minRightBearing(self) -> float """
        return 0.0

    def overlinePos(self): # real signature unknown; restored from __doc__
        """ overlinePos(self) -> float """
        return 0.0

    def rightBearing(self, arg__1): # real signature unknown; restored from __doc__
        """ rightBearing(self, arg__1: str) -> float """
        return 0.0

    def size(self, flags, p_str, tabstops=0, tabarray, typing_Sequence=None, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ size(self, flags: int, str: str, tabstops: int = 0, tabarray: typing.Optional[typing.Sequence[int]] = None) -> PySide2.QtCore.QSizeF """
        pass

    def strikeOutPos(self): # real signature unknown; restored from __doc__
        """ strikeOutPos(self) -> float """
        return 0.0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QFontMetricsF) -> None """
        pass

    def tightBoundingRect(self, text): # real signature unknown; restored from __doc__
        """ tightBoundingRect(self, text: str) -> PySide2.QtCore.QRectF """
        pass

    def underlinePos(self): # real signature unknown; restored from __doc__
        """ underlinePos(self) -> float """
        return 0.0

    def width(self, string): # real signature unknown; restored from __doc__
        """ width(self, string: str) -> float """
        return 0.0

    def widthChar(self, arg__1): # real signature unknown; restored from __doc__
        """ widthChar(self, arg__1: str) -> float """
        return 0.0

    def xHeight(self): # real signature unknown; restored from __doc__
        """ xHeight(self) -> float """
        return 0.0

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, arg__1): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __hash__ = None


