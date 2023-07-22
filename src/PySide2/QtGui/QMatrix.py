# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QMatrix(__Shiboken.Object):
    """
    QMatrix(self) -> None
    QMatrix(self, m11: float, m12: float, m21: float, m22: float, dx: float, dy: float) -> None
    QMatrix(self, other: PySide2.QtGui.QMatrix) -> None
    """
    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def dx(self): # real signature unknown; restored from __doc__
        """ dx(self) -> float """
        return 0.0

    def dy(self): # real signature unknown; restored from __doc__
        """ dy(self) -> float """
        return 0.0

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> typing.Tuple[PySide2.QtGui.QMatrix, bool] """
        pass

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def isInvertible(self): # real signature unknown; restored from __doc__
        """ isInvertible(self) -> bool """
        return False

    def m11(self): # real signature unknown; restored from __doc__
        """ m11(self) -> float """
        return 0.0

    def m12(self): # real signature unknown; restored from __doc__
        """ m12(self) -> float """
        return 0.0

    def m21(self): # real signature unknown; restored from __doc__
        """ m21(self) -> float """
        return 0.0

    def m22(self): # real signature unknown; restored from __doc__
        """ m22(self) -> float """
        return 0.0

    def map(self, a): # real signature unknown; restored from __doc__
        """
        map(self, a: PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygon
        map(self, a: PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF
        map(self, l: PySide2.QtCore.QLine) -> PySide2.QtCore.QLine
        map(self, l: PySide2.QtCore.QLineF) -> PySide2.QtCore.QLineF
        map(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint
        map(self, p: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        map(self, p: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        map(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        map(self, x: int, y: int) -> typing.Tuple[int, int]
        map(self, x: float, y: float) -> typing.Tuple[float, float]
        """
        pass

    def mapRect(self, arg__1): # real signature unknown; restored from __doc__
        """
        mapRect(self, arg__1: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect
        mapRect(self, arg__1: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        """
        pass

    def mapToPolygon(self, r): # real signature unknown; restored from __doc__
        """ mapToPolygon(self, r: PySide2.QtCore.QRect) -> PySide2.QtGui.QPolygon """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def rotate(self, a): # real signature unknown; restored from __doc__
        """ rotate(self, a: float) -> PySide2.QtGui.QMatrix """
        pass

    def scale(self, sx, sy): # real signature unknown; restored from __doc__
        """ scale(self, sx: float, sy: float) -> PySide2.QtGui.QMatrix """
        pass

    def setMatrix(self, m11, m12, m21, m22, dx, dy): # real signature unknown; restored from __doc__
        """ setMatrix(self, m11: float, m12: float, m21: float, m22: float, dx: float, dy: float) -> None """
        pass

    def shear(self, sh, sv): # real signature unknown; restored from __doc__
        """ shear(self, sh: float, sv: float) -> PySide2.QtGui.QMatrix """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """ translate(self, dx: float, dy: float) -> PySide2.QtGui.QMatrix """
        pass

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

    def __imul__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __imul__(self, arg__1: PySide2.QtGui.QMatrix) -> PySide2.QtGui.QMatrix
        
        Return self*=value.
        """
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

    def __mul__(self, l): # real signature unknown; restored from __doc__
        """
        __mul__(self, l: PySide2.QtCore.QLine) -> PySide2.QtCore.QLine
        __mul__(self, l: PySide2.QtCore.QLineF) -> PySide2.QtCore.QLineF
        __mul__(self, o: PySide2.QtGui.QMatrix) -> PySide2.QtGui.QMatrix
        __mul__(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint
        __mul__(self, p: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        
        Return self*value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__(self) -> object """
        return object()

    def __repr__(self): # real signature unknown; restored from __doc__
        """
        __repr__(self) -> object
        
        Return repr(self).
        """
        return object()

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
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


