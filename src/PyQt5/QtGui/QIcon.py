# encoding: utf-8
# module PyQt5.QtGui
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QIcon(__sip.wrapper):
    """
    QIcon()
    QIcon(pixmap: QPixmap)
    QIcon(other: QIcon)
    QIcon(fileName: str)
    QIcon(engine: QIconEngine)
    QIcon(variant: Any)
    """
    def actualSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        actualSize(self, size: QSize, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QSize
        actualSize(self, window: QWindow, size: QSize, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QSize
        """
        pass

    def addFile(self, fileName, size=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addFile(self, fileName: str, size: QSize = QSize(), mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) """
        pass

    def addPixmap(self, pixmap, mode=None, state=None): # real signature unknown; restored from __doc__
        """ addPixmap(self, pixmap: QPixmap, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) """
        pass

    def availableSizes(self, mode=None, state=None): # real signature unknown; restored from __doc__
        """ availableSizes(self, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> List[QSize] """
        return []

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def fallbackSearchPaths(self): # real signature unknown; restored from __doc__
        """ fallbackSearchPaths() -> List[str] """
        return []

    def fallbackThemeName(self): # real signature unknown; restored from __doc__
        """ fallbackThemeName() -> str """
        return ""

    def fromTheme(self, name, fallback=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromTheme(name: str) -> QIcon
        fromTheme(name: str, fallback: QIcon) -> QIcon
        """
        return QIcon

    def hasThemeIcon(self, name): # real signature unknown; restored from __doc__
        """ hasThemeIcon(name: str) -> bool """
        return False

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
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

    def paint(self, painter, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        paint(self, painter: QPainter, rect: QRect, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.AlignCenter, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off)
        paint(self, painter: QPainter, x: int, y: int, w: int, h: int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.AlignCenter, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off)
        """
        pass

    def pixmap(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pixmap(self, size: QSize, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QPixmap
        pixmap(self, w: int, h: int, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QPixmap
        pixmap(self, extent: int, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QPixmap
        pixmap(self, window: QWindow, size: QSize, mode: QIcon.Mode = QIcon.Normal, state: QIcon.State = QIcon.Off) -> QPixmap
        """
        return QPixmap

    def setFallbackSearchPaths(self, paths, p_str=None): # real signature unknown; restored from __doc__
        """ setFallbackSearchPaths(paths: Iterable[str]) """
        pass

    def setFallbackThemeName(self, name): # real signature unknown; restored from __doc__
        """ setFallbackThemeName(name: str) """
        pass

    def setIsMask(self, isMask): # real signature unknown; restored from __doc__
        """ setIsMask(self, isMask: bool) """
        pass

    def setThemeName(self, path): # real signature unknown; restored from __doc__
        """ setThemeName(path: str) """
        pass

    def setThemeSearchPaths(self, searchpath, p_str=None): # real signature unknown; restored from __doc__
        """ setThemeSearchPaths(searchpath: Iterable[str]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QIcon) """
        pass

    def themeName(self): # real signature unknown; restored from __doc__
        """ themeName() -> str """
        return ""

    def themeSearchPaths(self): # real signature unknown; restored from __doc__
        """ themeSearchPaths() -> List[str] """
        return []

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Active = 2
    Disabled = 1
    Normal = 0
    Off = 1
    On = 0
    Selected = 3


