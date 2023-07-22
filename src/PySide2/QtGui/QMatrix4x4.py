# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QMatrix4x4(__Shiboken.Object):
    """
    QMatrix4x4(self) -> None
    QMatrix4x4(self, m11: float, m12: float, m13: float, m14: float, m21: float, m22: float, m23: float, m24: float, m31: float, m32: float, m33: float, m34: float, m41: float, m42: float, m43: float, m44: float) -> None
    QMatrix4x4(self, matrix: PySide2.QtGui.QMatrix) -> None
    QMatrix4x4(self, transform: PySide2.QtGui.QTransform) -> None
    QMatrix4x4(self, values: typing.Sequence[float]) -> None
    """
    def column(self, index): # real signature unknown; restored from __doc__
        """ column(self, index: int) -> PySide2.QtGui.QVector4D """
        pass

    def constData(self): # reliably restored by inspect
        # no doc
        pass

    def copyDataTo(self): # real signature unknown; restored from __doc__
        """ copyDataTo(self) -> float """
        return 0.0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> typing.List[float] """
        pass

    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def fill(self, value): # real signature unknown; restored from __doc__
        """ fill(self, value: float) -> None """
        pass

    def flipCoordinates(self): # real signature unknown; restored from __doc__
        """ flipCoordinates(self) -> None """
        pass

    def frustum(self, left, right, bottom, top, nearPlane, farPlane): # real signature unknown; restored from __doc__
        """ frustum(self, left: float, right: float, bottom: float, top: float, nearPlane: float, farPlane: float) -> None """
        pass

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> typing.Tuple[PySide2.QtGui.QMatrix4x4, bool] """
        pass

    def isAffine(self): # real signature unknown; restored from __doc__
        """ isAffine(self) -> bool """
        return False

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def lookAt(self, eye, center, up): # real signature unknown; restored from __doc__
        """ lookAt(self, eye: PySide2.QtGui.QVector3D, center: PySide2.QtGui.QVector3D, up: PySide2.QtGui.QVector3D) -> None """
        pass

    def map(self, point): # real signature unknown; restored from __doc__
        """
        map(self, point: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint
        map(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        map(self, point: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D
        map(self, point: PySide2.QtGui.QVector4D) -> PySide2.QtGui.QVector4D
        """
        pass

    def mapRect(self, rect): # real signature unknown; restored from __doc__
        """
        mapRect(self, rect: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect
        mapRect(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        """
        pass

    def mapVector(self, vector): # real signature unknown; restored from __doc__
        """ mapVector(self, vector: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D """
        pass

    def normalMatrix(self): # real signature unknown; restored from __doc__
        """ normalMatrix(self) -> PySide2.QtGui.QMatrix3x3 """
        pass

    def optimize(self): # real signature unknown; restored from __doc__
        """ optimize(self) -> None """
        pass

    def ortho(self, left, right, bottom, top, nearPlane, farPlane): # real signature unknown; restored from __doc__
        """
        ortho(self, left: float, right: float, bottom: float, top: float, nearPlane: float, farPlane: float) -> None
        ortho(self, rect: PySide2.QtCore.QRect) -> None
        ortho(self, rect: PySide2.QtCore.QRectF) -> None
        """
        pass

    def perspective(self, verticalAngle, aspectRatio, nearPlane, farPlane): # real signature unknown; restored from __doc__
        """ perspective(self, verticalAngle: float, aspectRatio: float, nearPlane: float, farPlane: float) -> None """
        pass

    def rotate(self, angle, vector): # real signature unknown; restored from __doc__
        """
        rotate(self, angle: float, vector: PySide2.QtGui.QVector3D) -> None
        rotate(self, angle: float, x: float, y: float, z: float = 0.0) -> None
        rotate(self, quaternion: PySide2.QtGui.QQuaternion) -> None
        """
        pass

    def row(self, index): # real signature unknown; restored from __doc__
        """ row(self, index: int) -> PySide2.QtGui.QVector4D """
        pass

    def scale(self, factor): # real signature unknown; restored from __doc__
        """
        scale(self, factor: float) -> None
        scale(self, vector: PySide2.QtGui.QVector3D) -> None
        scale(self, x: float, y: float) -> None
        scale(self, x: float, y: float, z: float) -> None
        """
        pass

    def setColumn(self, index, value): # real signature unknown; restored from __doc__
        """ setColumn(self, index: int, value: PySide2.QtGui.QVector4D) -> None """
        pass

    def setRow(self, index, value): # real signature unknown; restored from __doc__
        """ setRow(self, index: int, value: PySide2.QtGui.QVector4D) -> None """
        pass

    def setToIdentity(self): # real signature unknown; restored from __doc__
        """ setToIdentity(self) -> None """
        pass

    def toAffine(self): # real signature unknown; restored from __doc__
        """ toAffine(self) -> PySide2.QtGui.QMatrix """
        pass

    def toTransform(self): # real signature unknown; restored from __doc__
        """
        toTransform(self) -> PySide2.QtGui.QTransform
        toTransform(self, distanceToPlane: float) -> PySide2.QtGui.QTransform
        """
        pass

    def translate(self, vector): # real signature unknown; restored from __doc__
        """
        translate(self, vector: PySide2.QtGui.QVector3D) -> None
        translate(self, x: float, y: float) -> None
        translate(self, x: float, y: float, z: float) -> None
        """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> PySide2.QtGui.QMatrix4x4 """
        pass

    def viewport(self, left, bottom, width, height, nearPlane=0.0, farPlane=1.0): # real signature unknown; restored from __doc__
        """
        viewport(self, left: float, bottom: float, width: float, height: float, nearPlane: float = 0.0, farPlane: float = 1.0) -> None
        viewport(self, rect: PySide2.QtCore.QRectF) -> None
        """
        pass

    def __add__(self, m2): # real signature unknown; restored from __doc__
        """
        __add__(self, m2: PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4
        
        Return self+value.
        """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __dummy(self, arg__1, p_float=None): # real signature unknown; restored from __doc__
        """ __dummy(self, arg__1: typing.Sequence[float]) -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, other): # real signature unknown; restored from __doc__
        """
        __iadd__(self, other: PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4
        
        Return self+=value.
        """
        pass

    def __imul__(self, factor): # real signature unknown; restored from __doc__
        """
        __imul__(self, factor: float) -> PySide2.QtGui.QMatrix4x4
        __imul__(self, other: PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4
        
        Return self*=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __isub__(self, other): # real signature unknown; restored from __doc__
        """
        __isub__(self, other: PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4
        
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

    def __mul__(self, factor): # real signature unknown; restored from __doc__
        """
        __mul__(self, factor: float) -> PySide2.QtGui.QMatrix4x4
        __mul__(self, m2: PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4
        __mul__(self, point: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint
        __mul__(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        
        Return self*value.
        """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """
        __neg__(self) -> PySide2.QtGui.QMatrix4x4
        
        -self
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

    def __sub__(self, m2): # real signature unknown; restored from __doc__
        """
        __sub__(self, m2: PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QMatrix4x4
        
        Return self-value.
        """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __hash__ = None


