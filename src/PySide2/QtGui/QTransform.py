# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTransform(__Shiboken.Object):
    """
    QTransform(self) -> None
    QTransform(self, h11: float, h12: float, h13: float, h21: float, h22: float, h23: float, h31: float, h32: float, h33: float = 1.0) -> None
    QTransform(self, h11: float, h12: float, h21: float, h22: float, dx: float, dy: float) -> None
    QTransform(self, mtx: PySide2.QtGui.QMatrix) -> None
    QTransform(self, other: PySide2.QtGui.QTransform) -> None
    """
    def adjoint(self): # real signature unknown; restored from __doc__
        """ adjoint(self) -> PySide2.QtGui.QTransform """
        pass

    def det(self): # real signature unknown; restored from __doc__
        """ det(self) -> float """
        return 0.0

    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def dx(self): # real signature unknown; restored from __doc__
        """ dx(self) -> float """
        return 0.0

    def dy(self): # real signature unknown; restored from __doc__
        """ dy(self) -> float """
        return 0.0

    def fromScale(self, dx, dy): # real signature unknown; restored from __doc__
        """ fromScale(dx: float, dy: float) -> PySide2.QtGui.QTransform """
        pass

    def fromTranslate(self, dx, dy): # real signature unknown; restored from __doc__
        """ fromTranslate(dx: float, dy: float) -> PySide2.QtGui.QTransform """
        pass

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> typing.Tuple[PySide2.QtGui.QTransform, bool] """
        pass

    def isAffine(self): # real signature unknown; restored from __doc__
        """ isAffine(self) -> bool """
        return False

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def isInvertible(self): # real signature unknown; restored from __doc__
        """ isInvertible(self) -> bool """
        return False

    def isRotating(self): # real signature unknown; restored from __doc__
        """ isRotating(self) -> bool """
        return False

    def isScaling(self): # real signature unknown; restored from __doc__
        """ isScaling(self) -> bool """
        return False

    def isTranslating(self): # real signature unknown; restored from __doc__
        """ isTranslating(self) -> bool """
        return False

    def m11(self): # real signature unknown; restored from __doc__
        """ m11(self) -> float """
        return 0.0

    def m12(self): # real signature unknown; restored from __doc__
        """ m12(self) -> float """
        return 0.0

    def m13(self): # real signature unknown; restored from __doc__
        """ m13(self) -> float """
        return 0.0

    def m21(self): # real signature unknown; restored from __doc__
        """ m21(self) -> float """
        return 0.0

    def m22(self): # real signature unknown; restored from __doc__
        """ m22(self) -> float """
        return 0.0

    def m23(self): # real signature unknown; restored from __doc__
        """ m23(self) -> float """
        return 0.0

    def m31(self): # real signature unknown; restored from __doc__
        """ m31(self) -> float """
        return 0.0

    def m32(self): # real signature unknown; restored from __doc__
        """ m32(self) -> float """
        return 0.0

    def m33(self): # real signature unknown; restored from __doc__
        """ m33(self) -> float """
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

    def quadToQuad(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        quadToQuad(arg__1: PySide2.QtGui.QPolygonF, arg__2: PySide2.QtGui.QPolygonF) -> object
        quadToQuad(one: PySide2.QtGui.QPolygonF, two: PySide2.QtGui.QPolygonF, result: PySide2.QtGui.QTransform) -> bool
        """
        return object()

    def quadToSquare(self, arg__1): # real signature unknown; restored from __doc__
        """
        quadToSquare(arg__1: PySide2.QtGui.QPolygonF) -> object
        quadToSquare(quad: PySide2.QtGui.QPolygonF, result: PySide2.QtGui.QTransform) -> bool
        """
        return object()

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def rotate(self, a, axis=None): # real signature unknown; restored from __doc__
        """ rotate(self, a: float, axis: PySide2.QtCore.Qt.Axis = PySide2.QtCore.Qt.Axis.ZAxis) -> PySide2.QtGui.QTransform """
        pass

    def rotateRadians(self, a, axis=None): # real signature unknown; restored from __doc__
        """ rotateRadians(self, a: float, axis: PySide2.QtCore.Qt.Axis = PySide2.QtCore.Qt.Axis.ZAxis) -> PySide2.QtGui.QTransform """
        pass

    def scale(self, sx, sy): # real signature unknown; restored from __doc__
        """ scale(self, sx: float, sy: float) -> PySide2.QtGui.QTransform """
        pass

    def setMatrix(self, m11, m12, m13, m21, m22, m23, m31, m32, m33): # real signature unknown; restored from __doc__
        """ setMatrix(self, m11: float, m12: float, m13: float, m21: float, m22: float, m23: float, m31: float, m32: float, m33: float) -> None """
        pass

    def shear(self, sh, sv): # real signature unknown; restored from __doc__
        """ shear(self, sh: float, sv: float) -> PySide2.QtGui.QTransform """
        pass

    def squareToQuad(self, arg__1): # real signature unknown; restored from __doc__
        """
        squareToQuad(arg__1: PySide2.QtGui.QPolygonF) -> object
        squareToQuad(square: PySide2.QtGui.QPolygonF, result: PySide2.QtGui.QTransform) -> bool
        """
        return object()

    def toAffine(self): # real signature unknown; restored from __doc__
        """ toAffine(self) -> PySide2.QtGui.QMatrix """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """ translate(self, dx: float, dy: float) -> PySide2.QtGui.QTransform """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> PySide2.QtGui.QTransform """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtGui.QTransform.TransformationType """
        pass

    def __add__(self, n): # real signature unknown; restored from __doc__
        """
        __add__(self, n: float) -> PySide2.QtGui.QTransform
        
        Return self+value.
        """
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

    def __iadd__(self, div): # real signature unknown; restored from __doc__
        """
        __iadd__(self, div: float) -> PySide2.QtGui.QTransform
        
        Return self+=value.
        """
        pass

    def __imul__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __imul__(self, arg__1: PySide2.QtGui.QTransform) -> PySide2.QtGui.QTransform
        __imul__(self, div: float) -> PySide2.QtGui.QTransform
        
        Return self*=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __isub__(self, div): # real signature unknown; restored from __doc__
        """
        __isub__(self, div: float) -> PySide2.QtGui.QTransform
        
        Return self-=value.
        """
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
        __mul__(self, n: float) -> PySide2.QtGui.QTransform
        __mul__(self, o: PySide2.QtGui.QTransform) -> PySide2.QtGui.QTransform
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
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

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sub__(self, n): # real signature unknown; restored from __doc__
        """
        __sub__(self, n: float) -> PySide2.QtGui.QTransform
        
        Return self-value.
        """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    TransformationType = None # (!) real value is "<class 'PySide2.QtGui.QTransform.TransformationType'>"
    TxNone = PySide2.QtGui.QTransform.TransformationType.TxNone
    TxProject = PySide2.QtGui.QTransform.TransformationType.TxProject
    TxRotate = PySide2.QtGui.QTransform.TransformationType.TxRotate
    TxScale = PySide2.QtGui.QTransform.TransformationType.TxScale
    TxShear = PySide2.QtGui.QTransform.TransformationType.TxShear
    TxTranslate = PySide2.QtGui.QTransform.TransformationType.TxTranslate
    __hash__ = None


