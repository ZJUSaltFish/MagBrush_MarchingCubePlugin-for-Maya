# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QRegion(__Shiboken.Object):
    """
    QRegion(self) -> None
    QRegion(self, bitmap: PySide2.QtGui.QBitmap) -> None
    QRegion(self, pa: PySide2.QtGui.QPolygon, fillRule: PySide2.QtCore.Qt.FillRule = PySide2.QtCore.Qt.FillRule.OddEvenFill) -> None
    QRegion(self, r: PySide2.QtCore.QRect, t: PySide2.QtGui.QRegion.RegionType = PySide2.QtGui.QRegion.RegionType.Rectangle) -> None
    QRegion(self, region: PySide2.QtGui.QRegion) -> None
    QRegion(self, x: int, y: int, w: int, h: int, t: PySide2.QtGui.QRegion.RegionType = PySide2.QtGui.QRegion.RegionType.Rectangle) -> None
    """
    def begin(self): # real signature unknown; restored from __doc__
        """ begin(self) -> PySide2.QtCore.QRect """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRect """
        pass

    def cbegin(self): # real signature unknown; restored from __doc__
        """ cbegin(self) -> PySide2.QtCore.QRect """
        pass

    def cend(self): # real signature unknown; restored from __doc__
        """ cend(self) -> PySide2.QtCore.QRect """
        pass

    def contains(self, p): # real signature unknown; restored from __doc__
        """
        contains(self, p: PySide2.QtCore.QPoint) -> bool
        contains(self, r: PySide2.QtCore.QRect) -> bool
        """
        return False

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> PySide2.QtCore.QRect """
        pass

    def intersected(self, r): # real signature unknown; restored from __doc__
        """
        intersected(self, r: PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion
        intersected(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        """
        pass

    def intersects(self, r): # real signature unknown; restored from __doc__
        """
        intersects(self, r: PySide2.QtCore.QRect) -> bool
        intersects(self, r: PySide2.QtGui.QRegion) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def rectCount(self): # real signature unknown; restored from __doc__
        """ rectCount(self) -> int """
        return 0

    def rects(self): # real signature unknown; restored from __doc__
        """ rects(self) -> typing.List[PySide2.QtCore.QRect] """
        pass

    def setRects(self, rect, num): # real signature unknown; restored from __doc__
        """ setRects(self, rect: PySide2.QtCore.QRect, num: int) -> None """
        pass

    def subtracted(self, r): # real signature unknown; restored from __doc__
        """ subtracted(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QRegion) -> None """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translate(self, dx: int, dy: int) -> None
        translate(self, p: PySide2.QtCore.QPoint) -> None
        """
        pass

    def translated(self, dx, dy): # real signature unknown; restored from __doc__
        """
        translated(self, dx: int, dy: int) -> PySide2.QtGui.QRegion
        translated(self, p: PySide2.QtCore.QPoint) -> PySide2.QtGui.QRegion
        """
        pass

    def united(self, r): # real signature unknown; restored from __doc__
        """
        united(self, r: PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion
        united(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        """
        pass

    def xored(self, r): # real signature unknown; restored from __doc__
        """ xored(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion """
        pass

    def __add__(self, r): # real signature unknown; restored from __doc__
        """
        __add__(self, r: PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion
        __add__(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        
        Return self+value.
        """
        pass

    def __and__(self, r): # real signature unknown; restored from __doc__
        """
        __and__(self, r: PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion
        __and__(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        
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

    def __iadd__(self, r): # real signature unknown; restored from __doc__
        """
        __iadd__(self, r: PySide2.QtCore.QRect) -> PySide2.QtGui.QRegion
        __iadd__(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        
        Return self+=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __ior__(self, r): # real signature unknown; restored from __doc__
        """
        __ior__(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        
        Return self|=value.
        """
        pass

    def __isub__(self, r): # real signature unknown; restored from __doc__
        """
        __isub__(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        
        Return self-=value.
        """
        pass

    def __ixor__(self, r): # real signature unknown; restored from __doc__
        """
        __ixor__(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        
        Return self^=value.
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
        __mul__(self, m: PySide2.QtGui.QMatrix) -> PySide2.QtGui.QRegion
        __mul__(self, m: PySide2.QtGui.QTransform) -> PySide2.QtGui.QRegion
        
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

    def __or__(self, r): # real signature unknown; restored from __doc__
        """
        __or__(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        
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

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __sub__(self, r): # real signature unknown; restored from __doc__
        """
        __sub__(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        
        Return self-value.
        """
        pass

    def __xor__(self, r): # real signature unknown; restored from __doc__
        """
        __xor__(self, r: PySide2.QtGui.QRegion) -> PySide2.QtGui.QRegion
        
        Return self^value.
        """
        pass

    Ellipse = PySide2.QtGui.QRegion.RegionType.Ellipse
    Rectangle = PySide2.QtGui.QRegion.RegionType.Rectangle
    RegionType = None # (!) real value is "<class 'PySide2.QtGui.QRegion.RegionType'>"
    __hash__ = None


