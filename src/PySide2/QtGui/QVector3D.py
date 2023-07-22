# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QVector3D(__Shiboken.Object):
    """
    QVector3D(self) -> None
    QVector3D(self, point: PySide2.QtCore.QPoint) -> None
    QVector3D(self, point: PySide2.QtCore.QPointF) -> None
    QVector3D(self, vector: PySide2.QtGui.QVector2D) -> None
    QVector3D(self, vector: PySide2.QtGui.QVector2D, zpos: float) -> None
    QVector3D(self, vector: PySide2.QtGui.QVector4D) -> None
    QVector3D(self, xpos: float, ypos: float, zpos: float) -> None
    """
    def crossProduct(self, v1, v2): # real signature unknown; restored from __doc__
        """ crossProduct(v1: PySide2.QtGui.QVector3D, v2: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D """
        pass

    def distanceToLine(self, point, direction): # real signature unknown; restored from __doc__
        """ distanceToLine(self, point: PySide2.QtGui.QVector3D, direction: PySide2.QtGui.QVector3D) -> float """
        return 0.0

    def distanceToPlane(self, plane1, plane2, plane3): # real signature unknown; restored from __doc__
        """
        distanceToPlane(self, plane1: PySide2.QtGui.QVector3D, plane2: PySide2.QtGui.QVector3D, plane3: PySide2.QtGui.QVector3D) -> float
        distanceToPlane(self, plane: PySide2.QtGui.QVector3D, normal: PySide2.QtGui.QVector3D) -> float
        """
        return 0.0

    def distanceToPoint(self, point): # real signature unknown; restored from __doc__
        """ distanceToPoint(self, point: PySide2.QtGui.QVector3D) -> float """
        return 0.0

    def dotProduct(self, v1, v2): # real signature unknown; restored from __doc__
        """ dotProduct(v1: PySide2.QtGui.QVector3D, v2: PySide2.QtGui.QVector3D) -> float """
        return 0.0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def lengthSquared(self): # real signature unknown; restored from __doc__
        """ lengthSquared(self) -> float """
        return 0.0

    def normal(self, v1, v2): # real signature unknown; restored from __doc__
        """
        normal(v1: PySide2.QtGui.QVector3D, v2: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D
        normal(v1: PySide2.QtGui.QVector3D, v2: PySide2.QtGui.QVector3D, v3: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D
        """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> None """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> PySide2.QtGui.QVector3D """
        pass

    def project(self, modelView, projection, viewport): # real signature unknown; restored from __doc__
        """ project(self, modelView: PySide2.QtGui.QMatrix4x4, projection: PySide2.QtGui.QMatrix4x4, viewport: PySide2.QtCore.QRect) -> PySide2.QtGui.QVector3D """
        pass

    def setX(self, x): # real signature unknown; restored from __doc__
        """ setX(self, x: float) -> None """
        pass

    def setY(self, y): # real signature unknown; restored from __doc__
        """ setY(self, y: float) -> None """
        pass

    def setZ(self, z): # real signature unknown; restored from __doc__
        """ setZ(self, z: float) -> None """
        pass

    def toPoint(self): # real signature unknown; restored from __doc__
        """ toPoint(self) -> PySide2.QtCore.QPoint """
        pass

    def toPointF(self): # real signature unknown; restored from __doc__
        """ toPointF(self) -> PySide2.QtCore.QPointF """
        pass

    def toTuple(self): # real signature unknown; restored from __doc__
        """ toTuple(self) -> object """
        return object()

    def toVector2D(self): # real signature unknown; restored from __doc__
        """ toVector2D(self) -> PySide2.QtGui.QVector2D """
        pass

    def toVector4D(self): # real signature unknown; restored from __doc__
        """ toVector4D(self) -> PySide2.QtGui.QVector4D """
        pass

    def unproject(self, modelView, projection, viewport): # real signature unknown; restored from __doc__
        """ unproject(self, modelView: PySide2.QtGui.QMatrix4x4, projection: PySide2.QtGui.QMatrix4x4, viewport: PySide2.QtCore.QRect) -> PySide2.QtGui.QVector3D """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def z(self): # real signature unknown; restored from __doc__
        """ z(self) -> float """
        return 0.0

    def __add__(self, v2): # real signature unknown; restored from __doc__
        """
        __add__(self, v2: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D
        
        Return self+value.
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    def __iadd__(self, vector): # real signature unknown; restored from __doc__
        """
        __iadd__(self, vector: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D
        
        Return self+=value.
        """
        pass

    def __imul__(self, factor): # real signature unknown; restored from __doc__
        """
        __imul__(self, factor: float) -> PySide2.QtGui.QVector3D
        __imul__(self, vector: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D
        
        Return self*=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __isub__(self, vector): # real signature unknown; restored from __doc__
        """
        __isub__(self, vector: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D
        
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
        __mul__(self, factor: float) -> PySide2.QtGui.QVector3D
        __mul__(self, matrix: PySide2.QtGui.QMatrix4x4) -> PySide2.QtGui.QVector3D
        __mul__(self, quaternion: PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QVector3D
        __mul__(self, v2: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D
        
        Return self*value.
        """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """
        __neg__(self) -> PySide2.QtGui.QVector3D
        
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

    def __sub__(self, v2): # real signature unknown; restored from __doc__
        """
        __sub__(self, v2: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D
        
        Return self-value.
        """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __hash__ = None


