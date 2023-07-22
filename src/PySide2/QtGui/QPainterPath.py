# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPainterPath(__Shiboken.Object):
    """
    QPainterPath(self) -> None
    QPainterPath(self, other: PySide2.QtGui.QPainterPath) -> None
    QPainterPath(self, startPoint: PySide2.QtCore.QPointF) -> None
    """
    def addEllipse(self, center, rx, ry): # real signature unknown; restored from __doc__
        """
        addEllipse(self, center: PySide2.QtCore.QPointF, rx: float, ry: float) -> None
        addEllipse(self, rect: PySide2.QtCore.QRectF) -> None
        addEllipse(self, x: float, y: float, w: float, h: float) -> None
        """
        pass

    def addPath(self, path): # real signature unknown; restored from __doc__
        """ addPath(self, path: PySide2.QtGui.QPainterPath) -> None """
        pass

    def addPolygon(self, polygon): # real signature unknown; restored from __doc__
        """ addPolygon(self, polygon: PySide2.QtGui.QPolygonF) -> None """
        pass

    def addRect(self, rect): # real signature unknown; restored from __doc__
        """
        addRect(self, rect: PySide2.QtCore.QRectF) -> None
        addRect(self, x: float, y: float, w: float, h: float) -> None
        """
        pass

    def addRegion(self, region): # real signature unknown; restored from __doc__
        """ addRegion(self, region: PySide2.QtGui.QRegion) -> None """
        pass

    def addRoundedRect(self, rect, xRadius, yRadius, mode=None): # real signature unknown; restored from __doc__
        """
        addRoundedRect(self, rect: PySide2.QtCore.QRectF, xRadius: float, yRadius: float, mode: PySide2.QtCore.Qt.SizeMode = PySide2.QtCore.Qt.SizeMode.AbsoluteSize) -> None
        addRoundedRect(self, x: float, y: float, w: float, h: float, xRadius: float, yRadius: float, mode: PySide2.QtCore.Qt.SizeMode = PySide2.QtCore.Qt.SizeMode.AbsoluteSize) -> None
        """
        pass

    def addRoundRect(self, rect, roundness): # real signature unknown; restored from __doc__
        """
        addRoundRect(self, rect: PySide2.QtCore.QRectF, roundness: int) -> None
        addRoundRect(self, rect: PySide2.QtCore.QRectF, xRnd: int, yRnd: int) -> None
        addRoundRect(self, x: float, y: float, w: float, h: float, roundness: int) -> None
        addRoundRect(self, x: float, y: float, w: float, h: float, xRnd: int, yRnd: int) -> None
        """
        pass

    def addText(self, point, f, text): # real signature unknown; restored from __doc__
        """
        addText(self, point: PySide2.QtCore.QPointF, f: PySide2.QtGui.QFont, text: str) -> None
        addText(self, x: float, y: float, f: PySide2.QtGui.QFont, text: str) -> None
        """
        pass

    def angleAtPercent(self, t): # real signature unknown; restored from __doc__
        """ angleAtPercent(self, t: float) -> float """
        return 0.0

    def arcMoveTo(self, rect, angle): # real signature unknown; restored from __doc__
        """
        arcMoveTo(self, rect: PySide2.QtCore.QRectF, angle: float) -> None
        arcMoveTo(self, x: float, y: float, w: float, h: float, angle: float) -> None
        """
        pass

    def arcTo(self, rect, startAngle, arcLength): # real signature unknown; restored from __doc__
        """
        arcTo(self, rect: PySide2.QtCore.QRectF, startAngle: float, arcLength: float) -> None
        arcTo(self, x: float, y: float, w: float, h: float, startAngle: float, arcLength: float) -> None
        """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def capacity(self): # real signature unknown; restored from __doc__
        """ capacity(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def closeSubpath(self): # real signature unknown; restored from __doc__
        """ closeSubpath(self) -> None """
        pass

    def connectPath(self, path): # real signature unknown; restored from __doc__
        """ connectPath(self, path: PySide2.QtGui.QPainterPath) -> None """
        pass

    def contains(self, p): # real signature unknown; restored from __doc__
        """
        contains(self, p: PySide2.QtGui.QPainterPath) -> bool
        contains(self, pt: PySide2.QtCore.QPointF) -> bool
        contains(self, rect: PySide2.QtCore.QRectF) -> bool
        """
        return False

    def controlPointRect(self): # real signature unknown; restored from __doc__
        """ controlPointRect(self) -> PySide2.QtCore.QRectF """
        pass

    def cubicTo(self, ctrlPt1, ctrlPt2, endPt): # real signature unknown; restored from __doc__
        """
        cubicTo(self, ctrlPt1: PySide2.QtCore.QPointF, ctrlPt2: PySide2.QtCore.QPointF, endPt: PySide2.QtCore.QPointF) -> None
        cubicTo(self, ctrlPt1x: float, ctrlPt1y: float, ctrlPt2x: float, ctrlPt2y: float, endPtx: float, endPty: float) -> None
        """
        pass

    def currentPosition(self): # real signature unknown; restored from __doc__
        """ currentPosition(self) -> PySide2.QtCore.QPointF """
        pass

    def elementAt(self, i): # real signature unknown; restored from __doc__
        """ elementAt(self, i: int) -> PySide2.QtGui.QPainterPath.Element """
        pass

    def elementCount(self): # real signature unknown; restored from __doc__
        """ elementCount(self) -> int """
        return 0

    def fillRule(self): # real signature unknown; restored from __doc__
        """ fillRule(self) -> PySide2.QtCore.Qt.FillRule """
        pass

    def intersected(self, r): # real signature unknown; restored from __doc__
        """ intersected(self, r: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath """
        pass

    def intersects(self, p): # real signature unknown; restored from __doc__
        """
        intersects(self, p: PySide2.QtGui.QPainterPath) -> bool
        intersects(self, rect: PySide2.QtCore.QRectF) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def lineTo(self, p): # real signature unknown; restored from __doc__
        """
        lineTo(self, p: PySide2.QtCore.QPointF) -> None
        lineTo(self, x: float, y: float) -> None
        """
        pass

    def moveTo(self, p): # real signature unknown; restored from __doc__
        """
        moveTo(self, p: PySide2.QtCore.QPointF) -> None
        moveTo(self, x: float, y: float) -> None
        """
        pass

    def percentAtLength(self, t): # real signature unknown; restored from __doc__
        """ percentAtLength(self, t: float) -> float """
        return 0.0

    def pointAtPercent(self, t): # real signature unknown; restored from __doc__
        """ pointAtPercent(self, t: float) -> PySide2.QtCore.QPointF """
        pass

    def quadTo(self, ctrlPt, endPt): # real signature unknown; restored from __doc__
        """
        quadTo(self, ctrlPt: PySide2.QtCore.QPointF, endPt: PySide2.QtCore.QPointF) -> None
        quadTo(self, ctrlPtx: float, ctrlPty: float, endPtx: float, endPty: float) -> None
        """
        pass

    def reserve(self, size): # real signature unknown; restored from __doc__
        """ reserve(self, size: int) -> None """
        pass

    def setElementPositionAt(self, i, x, y): # real signature unknown; restored from __doc__
        """ setElementPositionAt(self, i: int, x: float, y: float) -> None """
        pass

    def setFillRule(self, fillRule): # real signature unknown; restored from __doc__
        """ setFillRule(self, fillRule: PySide2.QtCore.Qt.FillRule) -> None """
        pass

    def simplified(self): # real signature unknown; restored from __doc__
        """ simplified(self) -> PySide2.QtGui.QPainterPath """
        pass

    def slopeAtPercent(self, t): # real signature unknown; restored from __doc__
        """ slopeAtPercent(self, t: float) -> float """
        return 0.0

    def subtracted(self, r): # real signature unknown; restored from __doc__
        """ subtracted(self, r: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath """
        pass

    def subtractedInverted(self, r): # real signature unknown; restored from __doc__
        """ subtractedInverted(self, r: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QPainterPath) -> None """
        pass

    def toFillPolygon(self, matrix): # real signature unknown; restored from __doc__
        """
        toFillPolygon(self, matrix: PySide2.QtGui.QMatrix) -> PySide2.QtGui.QPolygonF
        toFillPolygon(self, matrix: PySide2.QtGui.QTransform = Default(QTransform)) -> PySide2.QtGui.QPolygonF
        """
        pass

    def toFillPolygons(self, matrix): # real signature unknown; restored from __doc__
        """
        toFillPolygons(self, matrix: PySide2.QtGui.QMatrix) -> typing.List[PySide2.QtGui.QPolygonF]
        toFillPolygons(self, matrix: PySide2.QtGui.QTransform = Default(QTransform)) -> typing.List[PySide2.QtGui.QPolygonF]
        """
        pass

    def toReversed(self): # real signature unknown; restored from __doc__
        """ toReversed(self) -> PySide2.QtGui.QPainterPath """
        pass

    def toSubpathPolygons(self, matrix): # real signature unknown; restored from __doc__
        """
        toSubpathPolygons(self, matrix: PySide2.QtGui.QMatrix) -> typing.List[PySide2.QtGui.QPolygonF]
        toSubpathPolygons(self, matrix: PySide2.QtGui.QTransform = Default(QTransform)) -> typing.List[PySide2.QtGui.QPolygonF]
        """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translate(self, dx: float, dy: float) -> None
        translate(self, offset: PySide2.QtCore.QPointF) -> None
        """
        pass

    def translated(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translated(self, dx: float, dy: float) -> PySide2.QtGui.QPainterPath
        translated(self, offset: PySide2.QtCore.QPointF) -> PySide2.QtGui.QPainterPath
        """
        pass

    def united(self, r): # real signature unknown; restored from __doc__
        """ united(self, r: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath """
        pass

    def __add__(self, other): # real signature unknown; restored from __doc__
        """
        __add__(self, other: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        
        Return self+value.
        """
        pass

    def __and__(self, other): # real signature unknown; restored from __doc__
        """
        __and__(self, other: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        
        Return self&value.
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

    def __iadd__(self, other): # real signature unknown; restored from __doc__
        """
        __iadd__(self, other: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        
        Return self+=value.
        """
        pass

    def __iand__(self, other): # real signature unknown; restored from __doc__
        """
        __iand__(self, other: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        
        Return self&=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __ior__(self, other): # real signature unknown; restored from __doc__
        """
        __ior__(self, other: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        
        Return self|=value.
        """
        pass

    def __isub__(self, other): # real signature unknown; restored from __doc__
        """
        __isub__(self, other: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        
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

    def __mul__(self, m): # real signature unknown; restored from __doc__
        """
        __mul__(self, m: PySide2.QtGui.QMatrix) -> PySide2.QtGui.QPainterPath
        __mul__(self, m: PySide2.QtGui.QTransform) -> PySide2.QtGui.QPainterPath
        
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

    def __or__(self, other): # real signature unknown; restored from __doc__
        """
        __or__(self, other: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        
        Return self|value.
        """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
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

    def __sub__(self, other): # real signature unknown; restored from __doc__
        """
        __sub__(self, other: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        
        Return self-value.
        """
        pass

    CurveToDataElement = PySide2.QtGui.QPainterPath.ElementType.CurveToDataElement
    CurveToElement = PySide2.QtGui.QPainterPath.ElementType.CurveToElement
    Element = None # (!) real value is "<class 'PySide2.QtGui.QPainterPath.Element'>"
    ElementType = None # (!) real value is "<class 'PySide2.QtGui.QPainterPath.ElementType'>"
    LineToElement = PySide2.QtGui.QPainterPath.ElementType.LineToElement
    MoveToElement = PySide2.QtGui.QPainterPath.ElementType.MoveToElement
    __hash__ = None


