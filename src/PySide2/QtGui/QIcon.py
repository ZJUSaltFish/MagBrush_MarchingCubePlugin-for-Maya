# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QIcon(__Shiboken.Object):
    """
    QIcon(self) -> None
    QIcon(self, engine: PySide2.QtGui.QIconEngine) -> None
    QIcon(self, fileName: str) -> None
    QIcon(self, other: PySide2.QtGui.QIcon) -> None
    QIcon(self, pixmap: PySide2.QtGui.QPixmap) -> None
    """
    def actualSize(self, size, mode=None, state=None): # real signature unknown; restored from __doc__
        """
        actualSize(self, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> PySide2.QtCore.QSize
        actualSize(self, window: PySide2.QtGui.QWindow, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> PySide2.QtCore.QSize
        """
        pass

    def addFile(self, fileName, size=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addFile(self, fileName: str, size: PySide2.QtCore.QSize = Default(QSize), mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> None """
        pass

    def addPixmap(self, pixmap, mode=None, state=None): # real signature unknown; restored from __doc__
        """ addPixmap(self, pixmap: PySide2.QtGui.QPixmap, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> None """
        pass

    def availableSizes(self, mode=None, state=None): # real signature unknown; restored from __doc__
        """ availableSizes(self, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> typing.List[PySide2.QtCore.QSize] """
        pass

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def fallbackSearchPaths(self): # real signature unknown; restored from __doc__
        """ fallbackSearchPaths() -> typing.List[str] """
        pass

    def fallbackThemeName(self): # real signature unknown; restored from __doc__
        """ fallbackThemeName() -> str """
        return ""

    def fromTheme(self, name): # real signature unknown; restored from __doc__
        """
        fromTheme(name: str) -> PySide2.QtGui.QIcon
        fromTheme(name: str, fallback: PySide2.QtGui.QIcon) -> PySide2.QtGui.QIcon
        """
        pass

    def hasThemeIcon(self, name): # real signature unknown; restored from __doc__
        """ hasThemeIcon(name: str) -> bool """
        return False

    def isMask(self): # real signature unknown; restored from __doc__
        """ isMask(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def paint(self, painter, rect, alignment=None, mode=None, state=None): # real signature unknown; restored from __doc__
        """
        paint(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, alignment: PySide2.QtCore.Qt.Alignment = PySide2.QtCore.Qt.AlignmentFlag.AlignCenter, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> None
        paint(self, painter: PySide2.QtGui.QPainter, x: int, y: int, w: int, h: int, alignment: PySide2.QtCore.Qt.Alignment = PySide2.QtCore.Qt.AlignmentFlag.AlignCenter, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> None
        """
        pass

    def pixmap(self, extent, mode=None, state=None): # real signature unknown; restored from __doc__
        """
        pixmap(self, extent: int, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> PySide2.QtGui.QPixmap
        pixmap(self, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> PySide2.QtGui.QPixmap
        pixmap(self, w: int, h: int, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> PySide2.QtGui.QPixmap
        pixmap(self, window: PySide2.QtGui.QWindow, size: PySide2.QtCore.QSize, mode: PySide2.QtGui.QIcon.Mode = PySide2.QtGui.QIcon.Mode.Normal, state: PySide2.QtGui.QIcon.State = PySide2.QtGui.QIcon.State.Off) -> PySide2.QtGui.QPixmap
        """
        pass

    def setFallbackSearchPaths(self, paths, p_str=None): # real signature unknown; restored from __doc__
        """ setFallbackSearchPaths(paths: typing.Sequence[str]) -> None """
        pass

    def setFallbackThemeName(self, name): # real signature unknown; restored from __doc__
        """ setFallbackThemeName(name: str) -> None """
        pass

    def setIsMask(self, isMask): # real signature unknown; restored from __doc__
        """ setIsMask(self, isMask: bool) -> None """
        pass

    def setThemeName(self, path): # real signature unknown; restored from __doc__
        """ setThemeName(path: str) -> None """
        pass

    def setThemeSearchPaths(self, searchpath, p_str=None): # real signature unknown; restored from __doc__
        """ setThemeSearchPaths(searchpath: typing.Sequence[str]) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QIcon) -> None """
        pass

    def themeName(self): # real signature unknown; restored from __doc__
        """ themeName() -> str """
        return ""

    def themeSearchPaths(self): # real signature unknown; restored from __doc__
        """ themeSearchPaths() -> typing.List[str] """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
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

    def __rshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __rshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    Active = PySide2.QtGui.QIcon.Mode.Active
    Disabled = PySide2.QtGui.QIcon.Mode.Disabled
    Mode = None # (!) real value is "<class 'PySide2.QtGui.QIcon.Mode'>"
    Normal = PySide2.QtGui.QIcon.Mode.Normal
    Off = PySide2.QtGui.QIcon.State.Off
    On = PySide2.QtGui.QIcon.State.On
    Selected = PySide2.QtGui.QIcon.Mode.Selected
    State = None # (!) real value is "<class 'PySide2.QtGui.QIcon.State'>"


