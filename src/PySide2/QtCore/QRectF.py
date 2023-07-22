# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QRectF(__Shiboken.Object):
    """
    QRectF(self) -> None
    QRectF(self, QRectF: PySide2.QtCore.QRectF) -> None
    QRectF(self, left: float, top: float, width: float, height: float) -> None
    QRectF(self, rect: PySide2.QtCore.QRect) -> None
    QRectF(self, topleft: PySide2.QtCore.QPointF, bottomRight: PySide2.QtCore.QPointF) -> None
    QRectF(self, topleft: PySide2.QtCore.QPointF, size: PySide2.QtCore.QSizeF) -> None
    """
    def adjust(self, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ adjust(self, x1: float, y1: float, x2: float, y2: float) -> None """
        pass

    def adjusted(self, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ adjusted(self, x1: float, y1: float, x2: float, y2: float) -> PySide2.QtCore.QRectF """
        pass

    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> float """
        return 0.0

    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ bottomLeft(self) -> PySide2.QtCore.QPointF """
        pass

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> PySide2.QtCore.QPointF """
        pass

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> PySide2.QtCore.QPointF """
        pass

    def contains(self, p): # real signature unknown; restored from __doc__
        """
        contains(self, p: PySide2.QtCore.QPointF) -> bool
        contains(self, r: PySide2.QtCore.QRectF) -> bool
        contains(self, x: float, y: float) -> bool
        """
        return False

    def getCoords(self): # real signature unknown; restored from __doc__
        """ getCoords(self) -> typing.Tuple[float, float, float, float] """
        pass

    def getRect(self): # real signature unknown; restored from __doc__
        """ getRect(self) -> typing.Tuple[float, float, float, float] """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def intersected(self, other): # real signature unknown; restored from __doc__
        """ intersected(self, other: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF """
        pass

    def intersects(self, r): # real signature unknown; restored from __doc__
        """ intersects(self, r: PySide2.QtCore.QRectF) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def left(self): # real signature unknown; restored from __doc__
        """ left(self) -> float """
        return 0.0

    def marginsAdded(self, margins): # real signature unknown; restored from __doc__
        """ marginsAdded(self, margins: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF """
        pass

    def marginsRemoved(self, margins): # real signature unknown; restored from __doc__
        """ marginsRemoved(self, margins: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF """
        pass

    def moveBottom(self, pos): # real signature unknown; restored from __doc__
        """ moveBottom(self, pos: float) -> None """
        pass

    def moveBottomLeft(self, p): # real signature unknown; restored from __doc__
        """ moveBottomLeft(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def moveBottomRight(self, p): # real signature unknown; restored from __doc__
        """ moveBottomRight(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def moveCenter(self, p): # real signature unknown; restored from __doc__
        """ moveCenter(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def moveLeft(self, pos): # real signature unknown; restored from __doc__
        """ moveLeft(self, pos: float) -> None """
        pass

    def moveRight(self, pos): # real signature unknown; restored from __doc__
        """ moveRight(self, pos: float) -> None """
        pass

    def moveTo(self, p): # real signature unknown; restored from __doc__
        """
        moveTo(self, p: PySide2.QtCore.QPointF) -> None
        moveTo(self, x: float, y: float) -> None
        """
        pass

    def moveTop(self, pos): # real signature unknown; restored from __doc__
        """ moveTop(self, pos: float) -> None """
        pass

    def moveTopLeft(self, p): # real signature unknown; restored from __doc__
        """ moveTopLeft(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def moveTopRight(self, p): # real signature unknown; restored from __doc__
        """ moveTopRight(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> PySide2.QtCore.QRectF """
        pass

    def right(self): # real signature unknown; restored from __doc__
        """ right(self) -> float """
        return 0.0

    def setBottom(self, pos): # real signature unknown; restored from __doc__
        """ setBottom(self, pos: float) -> None """
        pass

    def setBottomLeft(self, p): # real signature unknown; restored from __doc__
        """ setBottomLeft(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def setBottomRight(self, p): # real signature unknown; restored from __doc__
        """ setBottomRight(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def setCoords(self, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ setCoords(self, x1: float, y1: float, x2: float, y2: float) -> None """
        pass

    def setHeight(self, h): # real signature unknown; restored from __doc__
        """ setHeight(self, h: float) -> None """
        pass

    def setLeft(self, pos): # real signature unknown; restored from __doc__
        """ setLeft(self, pos: float) -> None """
        pass

    def setRect(self, x, y, w, h): # real signature unknown; restored from __doc__
        """ setRect(self, x: float, y: float, w: float, h: float) -> None """
        pass

    def setRight(self, pos): # real signature unknown; restored from __doc__
        """ setRight(self, pos: float) -> None """
        pass

    def setSize(self, s): # real signature unknown; restored from __doc__
        """ setSize(self, s: PySide2.QtCore.QSizeF) -> None """
        pass

    def setTop(self, pos): # real signature unknown; restored from __doc__
        """ setTop(self, pos: float) -> None """
        pass

    def setTopLeft(self, p): # real signature unknown; restored from __doc__
        """ setTopLeft(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def setTopRight(self, p): # real signature unknown; restored from __doc__
        """ setTopRight(self, p: PySide2.QtCore.QPointF) -> None """
        pass

    def setWidth(self, w): # real signature unknown; restored from __doc__
        """ setWidth(self, w: float) -> None """
        pass

    def setX(self, pos): # real signature unknown; restored from __doc__
        """ setX(self, pos: float) -> None """
        pass

    def setY(self, pos): # real signature unknown; restored from __doc__
        """ setY(self, pos: float) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSizeF """
        pass

    def toAlignedRect(self): # real signature unknown; restored from __doc__
        """ toAlignedRect(self) -> PySide2.QtCore.QRect """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> float """
        return 0.0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> PySide2.QtCore.QPointF """
        pass

    def topRight(self): # real signature unknown; restored from __doc__
        """ topRight(self) -> PySide2.QtCore.QPointF """
        pass

    def toRect(self): # real signature unknown; restored from __doc__
        """ toRect(self) -> PySide2.QtCore.QRect """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translate(self, dx: float, dy: float) -> None
        translate(self, p: PySide2.QtCore.QPointF) -> None
        """
        pass

    def translated(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translated(self, dx: float, dy: float) -> PySide2.QtCore.QRectF
        translated(self, p: PySide2.QtCore.QPointF) -> PySide2.QtCore.QRectF
        """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> PySide2.QtCore.QRectF """
        pass

    def united(self, other): # real signature unknown; restored from __doc__
        """ united(self, other: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def __add__(self, lhs): # real signature unknown; restored from __doc__
        """
        __add__(self, lhs: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF
        __add__(self, rhs: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF
        
        Return self+value.
        """
        pass

    def __and__(self, r): # real signature unknown; restored from __doc__
        """
        __and__(self, r: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        
        Return self&value.
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

    def __iadd__(self, margins): # real signature unknown; restored from __doc__
        """
        __iadd__(self, margins: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF
        
        Return self+=value.
        """
        pass

    def __iand__(self, r): # real signature unknown; restored from __doc__
        """
        __iand__(self, r: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        
        Return self&=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __ior__(self, r): # real signature unknown; restored from __doc__
        """
        __ior__(self, r: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        
        Return self|=value.
        """
        pass

    def __isub__(self, margins): # real signature unknown; restored from __doc__
        """
        __isub__(self, margins: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF
        
        Return self-=value.
        """
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

    def __or__(self, r): # real signature unknown; restored from __doc__
        """
        __or__(self, r: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        
        Return self|value.
        """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
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

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, rhs): # real signature unknown; restored from __doc__
        """
        __sub__(self, rhs: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF
        
        Return self-value.
        """
        pass

    __hash__ = None


