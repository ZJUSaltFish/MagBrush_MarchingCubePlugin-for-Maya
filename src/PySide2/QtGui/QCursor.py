# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QCursor(__Shiboken.Object):
    """
    QCursor(self) -> None
    QCursor(self, bitmap: PySide2.QtGui.QBitmap, mask: PySide2.QtGui.QBitmap, hotX: int = -1, hotY: int = -1) -> None
    QCursor(self, cursor: PySide2.QtGui.QCursor) -> None
    QCursor(self, pixmap: PySide2.QtGui.QPixmap, hotX: int = -1, hotY: int = -1) -> None
    QCursor(self, shape: PySide2.QtCore.Qt.CursorShape) -> None
    """
    def bitmap(self): # real signature unknown; restored from __doc__
        """ bitmap(self) -> PySide2.QtGui.QBitmap """
        pass

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ hotSpot(self) -> PySide2.QtCore.QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> PySide2.QtGui.QBitmap """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> PySide2.QtGui.QPixmap """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """
        pos() -> PySide2.QtCore.QPoint
        pos(screen: PySide2.QtGui.QScreen) -> PySide2.QtCore.QPoint
        """
        pass

    def setPos(self, p): # real signature unknown; restored from __doc__
        """
        setPos(p: PySide2.QtCore.QPoint) -> None
        setPos(screen: PySide2.QtGui.QScreen, p: PySide2.QtCore.QPoint) -> None
        setPos(screen: PySide2.QtGui.QScreen, x: int, y: int) -> None
        setPos(x: int, y: int) -> None
        """
        pass

    def setShape(self, newShape): # real signature unknown; restored from __doc__
        """ setShape(self, newShape: PySide2.QtCore.Qt.CursorShape) -> None """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> PySide2.QtCore.Qt.CursorShape """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QCursor) -> None """
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

    def __lshift__(self, outS): # real signature unknown; restored from __doc__
        """
        __lshift__(self, outS: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, inS): # real signature unknown; restored from __doc__
        """
        __rshift__(self, inS: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    __hash__ = None


