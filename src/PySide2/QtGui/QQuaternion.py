# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QQuaternion(__Shiboken.Object):
    """
    QQuaternion(self) -> None
    QQuaternion(self, scalar: float, vector: PySide2.QtGui.QVector3D) -> None
    QQuaternion(self, scalar: float, xpos: float, ypos: float, zpos: float) -> None
    QQuaternion(self, vector: PySide2.QtGui.QVector4D) -> None
    """
    def conjugate(self): # real signature unknown; restored from __doc__
        """ conjugate(self) -> PySide2.QtGui.QQuaternion """
        pass

    def conjugated(self): # real signature unknown; restored from __doc__
        """ conjugated(self) -> PySide2.QtGui.QQuaternion """
        pass

    def dotProduct(self, q1, q2): # real signature unknown; restored from __doc__
        """ dotProduct(q1: PySide2.QtGui.QQuaternion, q2: PySide2.QtGui.QQuaternion) -> float """
        return 0.0

    def fromAxes(self, xAxis, yAxis, zAxis): # real signature unknown; restored from __doc__
        """ fromAxes(xAxis: PySide2.QtGui.QVector3D, yAxis: PySide2.QtGui.QVector3D, zAxis: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion """
        pass

    def fromAxisAndAngle(self, axis, angle): # real signature unknown; restored from __doc__
        """
        fromAxisAndAngle(axis: PySide2.QtGui.QVector3D, angle: float) -> PySide2.QtGui.QQuaternion
        fromAxisAndAngle(x: float, y: float, z: float, angle: float) -> PySide2.QtGui.QQuaternion
        """
        pass

    def fromDirection(self, direction, up): # real signature unknown; restored from __doc__
        """ fromDirection(direction: PySide2.QtGui.QVector3D, up: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion """
        pass

    def fromEulerAngles(self, eulerAngles): # real signature unknown; restored from __doc__
        """
        fromEulerAngles(eulerAngles: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion
        fromEulerAngles(pitch: float, yaw: float, roll: float) -> PySide2.QtGui.QQuaternion
        """
        pass

    def fromRotationMatrix(self, rot3x3): # real signature unknown; restored from __doc__
        """ fromRotationMatrix(rot3x3: PySide2.QtGui.QMatrix3x3) -> PySide2.QtGui.QQuaternion """
        pass

    def getAxes(self, xAxis, yAxis, zAxis): # real signature unknown; restored from __doc__
        """ getAxes(self, xAxis: PySide2.QtGui.QVector3D, yAxis: PySide2.QtGui.QVector3D, zAxis: PySide2.QtGui.QVector3D) -> None """
        pass

    def inverted(self): # real signature unknown; restored from __doc__
        """ inverted(self) -> PySide2.QtGui.QQuaternion """
        pass

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ isIdentity(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def lengthSquared(self): # real signature unknown; restored from __doc__
        """ lengthSquared(self) -> float """
        return 0.0

    def nlerp(self, q1, q2, t): # real signature unknown; restored from __doc__
        """ nlerp(q1: PySide2.QtGui.QQuaternion, q2: PySide2.QtGui.QQuaternion, t: float) -> PySide2.QtGui.QQuaternion """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> None """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> PySide2.QtGui.QQuaternion """
        pass

    def rotatedVector(self, vector): # real signature unknown; restored from __doc__
        """ rotatedVector(self, vector: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QVector3D """
        pass

    def rotationTo(self, from_, to): # real signature unknown; restored from __doc__
        """ rotationTo(from_: PySide2.QtGui.QVector3D, to: PySide2.QtGui.QVector3D) -> PySide2.QtGui.QQuaternion """
        pass

    def scalar(self): # real signature unknown; restored from __doc__
        """ scalar(self) -> float """
        return 0.0

    def setScalar(self, scalar): # real signature unknown; restored from __doc__
        """ setScalar(self, scalar: float) -> None """
        pass

    def setVector(self, vector): # real signature unknown; restored from __doc__
        """
        setVector(self, vector: PySide2.QtGui.QVector3D) -> None
        setVector(self, x: float, y: float, z: float) -> None
        """
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

    def slerp(self, q1, q2, t): # real signature unknown; restored from __doc__
        """ slerp(q1: PySide2.QtGui.QQuaternion, q2: PySide2.QtGui.QQuaternion, t: float) -> PySide2.QtGui.QQuaternion """
        pass

    def toEulerAngles(self): # real signature unknown; restored from __doc__
        """ toEulerAngles(self) -> PySide2.QtGui.QVector3D """
        pass

    def toRotationMatrix(self): # real signature unknown; restored from __doc__
        """ toRotationMatrix(self) -> PySide2.QtGui.QMatrix3x3 """
        pass

    def toVector4D(self): # real signature unknown; restored from __doc__
        """ toVector4D(self) -> PySide2.QtGui.QVector4D """
        pass

    def vector(self): # real signature unknown; restored from __doc__
        """ vector(self) -> PySide2.QtGui.QVector3D """
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

    def __add__(self, q2): # real signature unknown; restored from __doc__
        """
        __add__(self, q2: PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion
        
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

    def __iadd__(self, quaternion): # real signature unknown; restored from __doc__
        """
        __iadd__(self, quaternion: PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion
        
        Return self+=value.
        """
        pass

    def __imul__(self, factor): # real signature unknown; restored from __doc__
        """
        __imul__(self, factor: float) -> PySide2.QtGui.QQuaternion
        __imul__(self, quaternion: PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion
        
        Return self*=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __isub__(self, quaternion): # real signature unknown; restored from __doc__
        """
        __isub__(self, quaternion: PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion
        
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
        __mul__(self, factor: float) -> PySide2.QtGui.QQuaternion
        __mul__(self, q2: PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion
        
        Return self*value.
        """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """
        __neg__(self) -> PySide2.QtGui.QQuaternion
        
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

    def __sub__(self, q2): # real signature unknown; restored from __doc__
        """
        __sub__(self, q2: PySide2.QtGui.QQuaternion) -> PySide2.QtGui.QQuaternion
        
        Return self-value.
        """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __hash__ = None


