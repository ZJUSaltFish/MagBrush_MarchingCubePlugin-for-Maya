# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QRect(__Shiboken.Object):
    """
    QRect(self) -> None
    QRect(self, QRect: PySide2.QtCore.QRect) -> None
    QRect(self, left: int, top: int, width: int, height: int) -> None
    QRect(self, topleft: PySide2.QtCore.QPoint, bottomright: PySide2.QtCore.QPoint) -> None
    QRect(self, topleft: PySide2.QtCore.QPoint, size: PySide2.QtCore.QSize) -> None
    """
    def adjust(self, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ adjust(self, x1: int, y1: int, x2: int, y2: int) -> None """
        pass

    def adjusted(self, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ adjusted(self, x1: int, y1: int, x2: int, y2: int) -> PySide2.QtCore.QRect """
        pass

    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ bottomLeft(self) -> PySide2.QtCore.QPoint """
        pass

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ bottomRight(self) -> PySide2.QtCore.QPoint """
        pass

    def center(self): # real signature unknown; restored from __doc__
        """ center(self) -> PySide2.QtCore.QPoint """
        pass

    def contains(self, p, proper=False): # real signature unknown; restored from __doc__
        """
        contains(self, p: PySide2.QtCore.QPoint, proper: bool = False) -> bool
        contains(self, r: PySide2.QtCore.QRect, proper: bool = False) -> bool
        contains(self, x: int, y: int) -> bool
        contains(self, x: int, y: int, proper: bool) -> bool
        """
        return False

    def getCoords(self): # real signature unknown; restored from __doc__
        """ getCoords(self) -> typing.Tuple[int, int, int, int] """
        pass

    def getRect(self): # real signature unknown; restored from __doc__
        """ getRect(self) -> typing.Tuple[int, int, int, int] """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def intersected(self, other): # real signature unknown; restored from __doc__
        """ intersected(self, other: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect """
        pass

    def intersects(self, r): # real signature unknown; restored from __doc__
        """ intersects(self, r: PySide2.QtCore.QRect) -> bool """
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
        """ left(self) -> int """
        return 0

    def marginsAdded(self, margins): # real signature unknown; restored from __doc__
        """ marginsAdded(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect """
        pass

    def marginsRemoved(self, margins): # real signature unknown; restored from __doc__
        """ marginsRemoved(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect """
        pass

    def moveBottom(self, pos): # real signature unknown; restored from __doc__
        """ moveBottom(self, pos: int) -> None """
        pass

    def moveBottomLeft(self, p): # real signature unknown; restored from __doc__
        """ moveBottomLeft(self, p: PySide2.QtCore.QPoint) -> None """
        pass

    def moveBottomRight(self, p): # real signature unknown; restored from __doc__
        """ moveBottomRight(self, p: PySide2.QtCore.QPoint) -> None """
        pass

    def moveCenter(self, p): # real signature unknown; restored from __doc__
        """ moveCenter(self, p: PySide2.QtCore.QPoint) -> None """
        pass

    def moveLeft(self, pos): # real signature unknown; restored from __doc__
        """ moveLeft(self, pos: int) -> None """
        pass

    def moveRight(self, pos): # real signature unknown; restored from __doc__
        """ moveRight(self, pos: int) -> None """
        pass

    def moveTo(self, p): # real signature unknown; restored from __doc__
        """
        moveTo(self, p: PySide2.QtCore.QPoint) -> None
        moveTo(self, x: int, t: int) -> None
        """
        pass

    def moveTop(self, pos): # real signature unknown; restored from __doc__
        """ moveTop(self, pos: int) -> None """
        pass

    def moveTopLeft(self, p): # real signature unknown; restored from __doc__
        """ moveTopLeft(self, p: PySide2.QtCore.QPoint) -> None """
        pass

    def moveTopRight(self, p): # real signature unknown; restored from __doc__
        """ moveTopRight(self, p: PySide2.QtCore.QPoint) -> None """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> PySide2.QtCore.QRect """
        pass

    def right(self): # real signature unknown; restored from __doc__
        """ right(self) -> int """
        return 0

    def setBottom(self, pos): # real signature unknown; restored from __doc__
        """ setBottom(self, pos: int) -> None """
        pass

    def setBottomLeft(self, p): # real signature unknown; restored from __doc__
        """ setBottomLeft(self, p: PySide2.QtCore.QPoint) -> None """
        pass

    def setBottomRight(self, p): # real signature unknown; restored from __doc__
        """ setBottomRight(self, p: PySide2.QtCore.QPoint) -> None """
        pass

    def setCoords(self, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ setCoords(self, x1: int, y1: int, x2: int, y2: int) -> None """
        pass

    def setHeight(self, h): # real signature unknown; restored from __doc__
        """ setHeight(self, h: int) -> None """
        pass

    def setLeft(self, pos): # real signature unknown; restored from __doc__
        """ setLeft(self, pos: int) -> None """
        pass

    def setRect(self, x, y, w, h): # real signature unknown; restored from __doc__
        """ setRect(self, x: int, y: int, w: int, h: int) -> None """
        pass

    def setRight(self, pos): # real signature unknown; restored from __doc__
        """ setRight(self, pos: int) -> None """
        pass

    def setSize(self, s): # real signature unknown; restored from __doc__
        """ setSize(self, s: PySide2.QtCore.QSize) -> None """
        pass

    def setTop(self, pos): # real signature unknown; restored from __doc__
        """ setTop(self, pos: int) -> None """
        pass

    def setTopLeft(self, p): # real signature unknown; restored from __doc__
        """ setTopLeft(self, p: PySide2.QtCore.QPoint) -> None """
        pass

    def setTopRight(self, p): # real signature unknown; restored from __doc__
        """ setTopRight(self, p: PySide2.QtCore.QPoint) -> None """
        pass

    def setWidth(self, w): # real signature unknown; restored from __doc__
        """ setWidth(self, w: int) -> None """
        pass

    def setX(self, x): # real signature unknown; restored from __doc__
        """ setX(self, x: int) -> None """
        pass

    def setY(self, y): # real signature unknown; restored from __doc__
        """ setY(self, y: int) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ topLeft(self) -> PySide2.QtCore.QPoint """
        pass

    def topRight(self): # real signature unknown; restored from __doc__
        """ topRight(self) -> PySide2.QtCore.QPoint """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translate(self, dx: int, dy: int) -> None
        translate(self, p: PySide2.QtCore.QPoint) -> None
        """
        pass

    def translated(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translated(self, dx: int, dy: int) -> PySide2.QtCore.QRect
        translated(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QRect
        """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> PySide2.QtCore.QRect """
        pass

    def united(self, other): # real signature unknown; restored from __doc__
        """ united(self, other: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def __add__(self, margins): # real signature unknown; restored from __doc__
        """
        __add__(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect
        
        Return self+value.
        """
        pass

    def __and__(self, r): # real signature unknown; restored from __doc__
        """
        __and__(self, r: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect
        
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, margins): # real signature unknown; restored from __doc__
        """
        __iadd__(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect
        
        Return self+=value.
        """
        pass

    def __iand__(self, r): # real signature unknown; restored from __doc__
        """
        __iand__(self, r: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect
        
        Return self&=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __ior__(self, r): # real signature unknown; restored from __doc__
        """
        __ior__(self, r: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect
        
        Return self|=value.
        """
        pass

    def __isub__(self, margins): # real signature unknown; restored from __doc__
        """
        __isub__(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect
        
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
        __or__(self, r: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect
        
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
        __sub__(self, rhs: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect
        
        Return self-value.
        """
        pass


