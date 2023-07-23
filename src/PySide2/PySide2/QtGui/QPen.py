# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPen(__Shiboken.Object):
    """
    QPen(self) -> None
    QPen(self, arg__1: PySide2.QtCore.Qt.PenStyle) -> None
    QPen(self, brush: PySide2.QtGui.QBrush, width: float, s: PySide2.QtCore.Qt.PenStyle = PySide2.QtCore.Qt.PenStyle.SolidLine, c: PySide2.QtCore.Qt.PenCapStyle = PySide2.QtCore.Qt.PenCapStyle.SquareCap, j: PySide2.QtCore.Qt.PenJoinStyle = PySide2.QtCore.Qt.PenJoinStyle.BevelJoin) -> None
    QPen(self, color: PySide2.QtGui.QColor) -> None
    QPen(self, pen: PySide2.QtGui.QPen) -> None
    """
    def brush(self): # real signature unknown; restored from __doc__
        """ brush(self) -> PySide2.QtGui.QBrush """
        pass

    def capStyle(self): # real signature unknown; restored from __doc__
        """ capStyle(self) -> PySide2.QtCore.Qt.PenCapStyle """
        pass

    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> PySide2.QtGui.QColor """
        pass

    def dashOffset(self): # real signature unknown; restored from __doc__
        """ dashOffset(self) -> float """
        return 0.0

    def dashPattern(self): # real signature unknown; restored from __doc__
        """ dashPattern(self) -> typing.List[float] """
        pass

    def isCosmetic(self): # real signature unknown; restored from __doc__
        """ isCosmetic(self) -> bool """
        return False

    def isSolid(self): # real signature unknown; restored from __doc__
        """ isSolid(self) -> bool """
        return False

    def joinStyle(self): # real signature unknown; restored from __doc__
        """ joinStyle(self) -> PySide2.QtCore.Qt.PenJoinStyle """
        pass

    def miterLimit(self): # real signature unknown; restored from __doc__
        """ miterLimit(self) -> float """
        return 0.0

    def setBrush(self, brush): # real signature unknown; restored from __doc__
        """ setBrush(self, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setCapStyle(self, pcs): # real signature unknown; restored from __doc__
        """ setCapStyle(self, pcs: PySide2.QtCore.Qt.PenCapStyle) -> None """
        pass

    def setColor(self, color): # real signature unknown; restored from __doc__
        """ setColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setCosmetic(self, cosmetic): # real signature unknown; restored from __doc__
        """ setCosmetic(self, cosmetic: bool) -> None """
        pass

    def setDashOffset(self, doffset): # real signature unknown; restored from __doc__
        """ setDashOffset(self, doffset: float) -> None """
        pass

    def setDashPattern(self, pattern, p_float=None): # real signature unknown; restored from __doc__
        """ setDashPattern(self, pattern: typing.List[float]) -> None """
        pass

    def setJoinStyle(self, pcs): # real signature unknown; restored from __doc__
        """ setJoinStyle(self, pcs: PySide2.QtCore.Qt.PenJoinStyle) -> None """
        pass

    def setMiterLimit(self, limit): # real signature unknown; restored from __doc__
        """ setMiterLimit(self, limit: float) -> None """
        pass

    def setStyle(self, arg__1): # real signature unknown; restored from __doc__
        """ setStyle(self, arg__1: PySide2.QtCore.Qt.PenStyle) -> None """
        pass

    def setWidth(self, width): # real signature unknown; restored from __doc__
        """ setWidth(self, width: int) -> None """
        pass

    def setWidthF(self, width): # real signature unknown; restored from __doc__
        """ setWidthF(self, width: float) -> None """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> PySide2.QtCore.Qt.PenStyle """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QPen) -> None """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def widthF(self): # real signature unknown; restored from __doc__
        """ widthF(self) -> float """
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

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __rshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    __hash__ = None


