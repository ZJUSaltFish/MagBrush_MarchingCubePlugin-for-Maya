# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QLineF(__Shiboken.Object):
    """
    QLineF(self) -> None
    QLineF(self, QLineF: PySide2.QtCore.QLineF) -> None
    QLineF(self, line: PySide2.QtCore.QLine) -> None
    QLineF(self, pt1: PySide2.QtCore.QPointF, pt2: PySide2.QtCore.QPointF) -> None
    QLineF(self, x1: float, y1: float, x2: float, y2: float) -> None
    """
    def angle(self): # real signature unknown; restored from __doc__
        """
        angle(self) -> float
        angle(self, l: PySide2.QtCore.QLineF) -> float
        """
        return 0.0

    def angleTo(self, l): # real signature unknown; restored from __doc__
        """ angleTo(self, l: PySide2.QtCore.QLineF) -> float """
        return 0.0

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> PySide2.QtCore.QPointF """
        pass

    def dx(self): # real signature unknown; restored from __doc__
        """ dx(self) -> float """
        return 0.0

    def dy(self): # real signature unknown; restored from __doc__
        """ dy(self) -> float """
        return 0.0

    def fromPolar(self, length, angle): # real signature unknown; restored from __doc__
        """ fromPolar(length: float, angle: float) -> PySide2.QtCore.QLineF """
        pass

    def intersect(self, l, intersectionPoint): # real signature unknown; restored from __doc__
        """ intersect(self, l: PySide2.QtCore.QLineF, intersectionPoint: PySide2.QtCore.QPointF) -> PySide2.QtCore.QLineF.IntersectType """
        pass

    def intersects(self, l, intersectionPoint): # real signature unknown; restored from __doc__
        """ intersects(self, l: PySide2.QtCore.QLineF, intersectionPoint: PySide2.QtCore.QPointF) -> PySide2.QtCore.QLineF.IntersectType """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def normalVector(self): # real signature unknown; restored from __doc__
        """ normalVector(self) -> PySide2.QtCore.QLineF """
        pass

    def p1(self): # real signature unknown; restored from __doc__
        """ p1(self) -> PySide2.QtCore.QPointF """
        pass

    def p2(self): # real signature unknown; restored from __doc__
        """ p2(self) -> PySide2.QtCore.QPointF """
        pass

    def pointAt(self, t): # real signature unknown; restored from __doc__
        """ pointAt(self, t: float) -> PySide2.QtCore.QPointF """
        pass

    def setAngle(self, angle): # real signature unknown; restored from __doc__
        """ setAngle(self, angle: float) -> None """
        pass

    def setLength(self, len): # real signature unknown; restored from __doc__
        """ setLength(self, len: float) -> None """
        pass

    def setLine(self, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ setLine(self, x1: float, y1: float, x2: float, y2: float) -> None """
        pass

    def setP1(self, p1): # real signature unknown; restored from __doc__
        """ setP1(self, p1: PySide2.QtCore.QPointF) -> None """
        pass

    def setP2(self, p2): # real signature unknown; restored from __doc__
        """ setP2(self, p2: PySide2.QtCore.QPointF) -> None """
        pass

    def setPoints(self, p1, p2): # real signature unknown; restored from __doc__
        """ setPoints(self, p1: PySide2.QtCore.QPointF, p2: PySide2.QtCore.QPointF) -> None """
        pass

    def toLine(self): # real signature unknown; restored from __doc__
        """ toLine(self) -> PySide2.QtCore.QLine """
        pass

    def toTuple(self): # real signature unknown; restored from __doc__
        """ toTuple(self) -> object """
        return object()

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translate(self, dx: float, dy: float) -> None
        translate(self, p: PySide2.QtCore.QPointF) -> None
        """
        pass

    def translated(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translated(self, dx: float, dy: float) -> PySide2.QtCore.QLineF
        translated(self, p: PySide2.QtCore.QPointF) -> PySide2.QtCore.QLineF
        """
        pass

    def unitVector(self): # real signature unknown; restored from __doc__
        """ unitVector(self) -> PySide2.QtCore.QLineF """
        pass

    def x1(self): # real signature unknown; restored from __doc__
        """ x1(self) -> float """
        return 0.0

    def x2(self): # real signature unknown; restored from __doc__
        """ x2(self) -> float """
        return 0.0

    def y1(self): # real signature unknown; restored from __doc__
        """ y1(self) -> float """
        return 0.0

    def y2(self): # real signature unknown; restored from __doc__
        """ y2(self) -> float """
        return 0.0

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

    def __init__(self): # real signature unknown; restored from __doc__
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

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__(self) -> object """
        return object()

    def __repr__(self): # real signature unknown; restored from __doc__
        """
        __repr__(self) -> object
        
        Return repr(self).
        """
        return object()

    BoundedIntersection = PySide2.QtCore.QLineF.IntersectType.BoundedIntersection
    IntersectType = None # (!) real value is "<class 'PySide2.QtCore.QLineF.IntersectType'>"
    NoIntersection = PySide2.QtCore.QLineF.IntersectType.NoIntersection
    UnboundedIntersection = PySide2.QtCore.QLineF.IntersectType.UnboundedIntersection
    __hash__ = None


