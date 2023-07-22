# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPolygon(__Shiboken.Object):
    """
    QPolygon(self) -> None
    QPolygon(self, other: PySide2.QtGui.QPolygon) -> None
    QPolygon(self, r: PySide2.QtCore.QRect, closed: bool = False) -> None
    QPolygon(self, size: int) -> None
    QPolygon(self, v: typing.List[PySide2.QtCore.QPoint]) -> None
    """
    def append(self, l, PySide2_QtCore_QPoint=None): # real signature unknown; restored from __doc__
        """
        append(self, l: typing.List[PySide2.QtCore.QPoint]) -> None
        append(self, t: PySide2.QtCore.QPoint) -> None
        """
        pass

    def at(self, i): # real signature unknown; restored from __doc__
        """ at(self, i: int) -> PySide2.QtCore.QPoint """
        pass

    def back(self): # real signature unknown; restored from __doc__
        """ back(self) -> PySide2.QtCore.QPoint """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRect """
        pass

    def capacity(self): # real signature unknown; restored from __doc__
        """ capacity(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def constData(self): # real signature unknown; restored from __doc__
        """ constData(self) -> PySide2.QtCore.QPoint """
        pass

    def constFirst(self): # real signature unknown; restored from __doc__
        """ constFirst(self) -> PySide2.QtCore.QPoint """
        pass

    def constLast(self): # real signature unknown; restored from __doc__
        """ constLast(self) -> PySide2.QtCore.QPoint """
        pass

    def contains(self, t): # real signature unknown; restored from __doc__
        """ contains(self, t: PySide2.QtCore.QPoint) -> bool """
        return False

    def containsPoint(self, pt, fillRule): # real signature unknown; restored from __doc__
        """ containsPoint(self, pt: PySide2.QtCore.QPoint, fillRule: PySide2.QtCore.Qt.FillRule) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """
        count(self) -> int
        count(self, t: PySide2.QtCore.QPoint) -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> PySide2.QtCore.QPoint """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """ empty(self) -> bool """
        return False

    def endsWith(self, t): # real signature unknown; restored from __doc__
        """ endsWith(self, t: PySide2.QtCore.QPoint) -> bool """
        return False

    def fill(self, t, size=-1): # real signature unknown; restored from __doc__
        """ fill(self, t: PySide2.QtCore.QPoint, size: int = -1) -> typing.List[PySide2.QtCore.QPoint] """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> PySide2.QtCore.QPoint """
        pass

    def fromList(self, p_list, PySide2_QtCore_QPoint=None): # real signature unknown; restored from __doc__
        """ fromList(list: typing.Sequence[PySide2.QtCore.QPoint]) -> typing.List[PySide2.QtCore.QPoint] """
        pass

    def front(self): # real signature unknown; restored from __doc__
        """ front(self) -> PySide2.QtCore.QPoint """
        pass

    def indexOf(self, t, from_=0): # real signature unknown; restored from __doc__
        """ indexOf(self, t: PySide2.QtCore.QPoint, from_: int = 0) -> int """
        return 0

    def insert(self, i, n, t): # real signature unknown; restored from __doc__
        """
        insert(self, i: int, n: int, t: PySide2.QtCore.QPoint) -> None
        insert(self, i: int, t: PySide2.QtCore.QPoint) -> None
        """
        pass

    def intersected(self, r): # real signature unknown; restored from __doc__
        """ intersected(self, r: PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygon """
        pass

    def intersects(self, r): # real signature unknown; restored from __doc__
        """ intersects(self, r: PySide2.QtGui.QPolygon) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isSharedWith(self, other, PySide2_QtCore_QPoint=None): # real signature unknown; restored from __doc__
        """ isSharedWith(self, other: typing.List[PySide2.QtCore.QPoint]) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> PySide2.QtCore.QPoint """
        pass

    def lastIndexOf(self, t, from_=-1): # real signature unknown; restored from __doc__
        """ lastIndexOf(self, t: PySide2.QtCore.QPoint, from_: int = -1) -> int """
        return 0

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def mid(self, pos, len=-1): # real signature unknown; restored from __doc__
        """ mid(self, pos: int, len: int = -1) -> typing.List[PySide2.QtCore.QPoint] """
        pass

    def move(self, from_, to): # real signature unknown; restored from __doc__
        """ move(self, from_: int, to: int) -> None """
        pass

    def pop_back(self): # real signature unknown; restored from __doc__
        """ pop_back(self) -> None """
        pass

    def pop_front(self): # real signature unknown; restored from __doc__
        """ pop_front(self) -> None """
        pass

    def prepend(self, t): # real signature unknown; restored from __doc__
        """ prepend(self, t: PySide2.QtCore.QPoint) -> None """
        pass

    def push_back(self, t): # real signature unknown; restored from __doc__
        """ push_back(self, t: PySide2.QtCore.QPoint) -> None """
        pass

    def push_front(self, t): # real signature unknown; restored from __doc__
        """ push_front(self, t: PySide2.QtCore.QPoint) -> None """
        pass

    def remove(self, i): # real signature unknown; restored from __doc__
        """
        remove(self, i: int) -> None
        remove(self, i: int, n: int) -> None
        """
        pass

    def removeAll(self, t): # real signature unknown; restored from __doc__
        """ removeAll(self, t: PySide2.QtCore.QPoint) -> int """
        return 0

    def removeAt(self, i): # real signature unknown; restored from __doc__
        """ removeAt(self, i: int) -> None """
        pass

    def removeFirst(self): # real signature unknown; restored from __doc__
        """ removeFirst(self) -> None """
        pass

    def removeLast(self): # real signature unknown; restored from __doc__
        """ removeLast(self) -> None """
        pass

    def removeOne(self, t): # real signature unknown; restored from __doc__
        """ removeOne(self, t: PySide2.QtCore.QPoint) -> bool """
        return False

    def replace(self, i, t): # real signature unknown; restored from __doc__
        """ replace(self, i: int, t: PySide2.QtCore.QPoint) -> None """
        pass

    def reserve(self, size): # real signature unknown; restored from __doc__
        """ reserve(self, size: int) -> None """
        pass

    def resize(self, size): # real signature unknown; restored from __doc__
        """ resize(self, size: int) -> None """
        pass

    def setSharable(self, sharable): # real signature unknown; restored from __doc__
        """ setSharable(self, sharable: bool) -> None """
        pass

    def shrink_to_fit(self): # real signature unknown; restored from __doc__
        """ shrink_to_fit(self) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def squeeze(self): # real signature unknown; restored from __doc__
        """ squeeze(self) -> None """
        pass

    def startsWith(self, t): # real signature unknown; restored from __doc__
        """ startsWith(self, t: PySide2.QtCore.QPoint) -> bool """
        return False

    def subtracted(self, r): # real signature unknown; restored from __doc__
        """ subtracted(self, r: PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygon """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QPolygon) -> None """
        pass

    def swapItemsAt(self, i, j): # real signature unknown; restored from __doc__
        """ swapItemsAt(self, i: int, j: int) -> None """
        pass

    def takeAt(self, i): # real signature unknown; restored from __doc__
        """ takeAt(self, i: int) -> PySide2.QtCore.QPoint """
        pass

    def takeFirst(self): # real signature unknown; restored from __doc__
        """ takeFirst(self) -> PySide2.QtCore.QPoint """
        pass

    def takeLast(self): # real signature unknown; restored from __doc__
        """ takeLast(self) -> PySide2.QtCore.QPoint """
        pass

    def toList(self): # real signature unknown; restored from __doc__
        """ toList(self) -> typing.List[PySide2.QtCore.QPoint] """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translate(self, dx: int, dy: int) -> None
        translate(self, offset: PySide2.QtCore.QPoint) -> None
        """
        pass

    def translated(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translated(self, dx: int, dy: int) -> PySide2.QtGui.QPolygon
        translated(self, offset: PySide2.QtCore.QPoint) -> PySide2.QtGui.QPolygon
        """
        pass

    def united(self, r): # real signature unknown; restored from __doc__
        """ united(self, r: PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygon """
        pass

    def value(self, i): # real signature unknown; restored from __doc__
        """
        value(self, i: int) -> PySide2.QtCore.QPoint
        value(self, i: int, defaultValue: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint
        """
        pass

    def __add__(self, l, PySide2_QtCore_QPoint=None): # real signature unknown; restored from __doc__
        """
        __add__(self, l: typing.List[PySide2.QtCore.QPoint]) -> typing.List[PySide2.QtCore.QPoint]
        
        Return self+value.
        """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
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

    def __iadd__(self, t): # real signature unknown; restored from __doc__
        """
        __iadd__(self, t: PySide2.QtCore.QPoint) -> typing.List[PySide2.QtCore.QPoint]
        
        Return self+=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, l, PySide2_QtCore_QPoint=None): # real signature unknown; restored from __doc__
        """
        __lshift__(self, l: typing.List[PySide2.QtCore.QPoint]) -> typing.List[PySide2.QtCore.QPoint]
        __lshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        __lshift__(self, t: PySide2.QtCore.QPoint) -> typing.List[PySide2.QtCore.QPoint]
        
        Return self<<value.
        """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, m): # real signature unknown; restored from __doc__
        """
        __mul__(self, m: PySide2.QtGui.QMatrix) -> PySide2.QtGui.QPolygon
        __mul__(self, m: PySide2.QtGui.QTransform) -> PySide2.QtGui.QPolygon
        
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __rshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


