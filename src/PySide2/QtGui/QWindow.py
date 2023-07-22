# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QSurface import QSurface

class QWindow(__PySide2_QtCore.QObject, QSurface):
    """
    QWindow(self, parent: PySide2.QtGui.QWindow) -> None
    QWindow(self, screen: typing.Optional[PySide2.QtGui.QScreen] = None) -> None
    """
    def accessibleRoot(self): # real signature unknown; restored from __doc__
        """ accessibleRoot(self) -> PySide2.QtGui.QAccessibleInterface """
        pass

    def activeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def alert(self, msec): # real signature unknown; restored from __doc__
        """ alert(self, msec: int) -> None """
        pass

    def baseSize(self): # real signature unknown; restored from __doc__
        """ baseSize(self) -> PySide2.QtCore.QSize """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def contentOrientation(self): # real signature unknown; restored from __doc__
        """ contentOrientation(self) -> PySide2.QtCore.Qt.ScreenOrientation """
        pass

    def contentOrientationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> None """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> PySide2.QtGui.QCursor """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) -> None """
        pass

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def exposeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ exposeEvent(self, arg__1: PySide2.QtGui.QExposeEvent) -> None """
        pass

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtCore.Qt.WindowFlags """
        pass

    def focusInEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusInEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusObject(self): # real signature unknown; restored from __doc__
        """ focusObject(self) -> PySide2.QtCore.QObject """
        pass

    def focusObjectChanged(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QSurfaceFormat """
        pass

    def frameGeometry(self): # real signature unknown; restored from __doc__
        """ frameGeometry(self) -> PySide2.QtCore.QRect """
        pass

    def frameMargins(self): # real signature unknown; restored from __doc__
        """ frameMargins(self) -> PySide2.QtCore.QMargins """
        pass

    def framePosition(self): # real signature unknown; restored from __doc__
        """ framePosition(self) -> PySide2.QtCore.QPoint """
        pass

    def fromWinId(self, id): # real signature unknown; restored from __doc__
        """ fromWinId(id: int) -> PySide2.QtGui.QWindow """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> PySide2.QtCore.QRect """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def heightChanged(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) -> None """
        pass

    def hideEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ hideEvent(self, arg__1: PySide2.QtGui.QHideEvent) -> None """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isAncestorOf(self, child, mode=None): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, child: PySide2.QtGui.QWindow, mode: PySide2.QtGui.QWindow.AncestorMode = PySide2.QtGui.QWindow.AncestorMode.IncludeTransients) -> bool """
        return False

    def isExposed(self): # real signature unknown; restored from __doc__
        """ isExposed(self) -> bool """
        return False

    def isModal(self): # real signature unknown; restored from __doc__
        """ isModal(self) -> bool """
        return False

    def isTopLevel(self): # real signature unknown; restored from __doc__
        """ isTopLevel(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """ lower(self) -> None """
        pass

    def mapFromGlobal(self, pos): # real signature unknown; restored from __doc__
        """ mapFromGlobal(self, pos: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint """
        pass

    def mapToGlobal(self, pos): # real signature unknown; restored from __doc__
        """ mapToGlobal(self, pos: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> PySide2.QtGui.QRegion """
        pass

    def maximumHeight(self): # real signature unknown; restored from __doc__
        """ maximumHeight(self) -> int """
        return 0

    def maximumHeightChanged(self, *args, **kwargs): # real signature unknown
        pass

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> PySide2.QtCore.QSize """
        pass

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ maximumWidth(self) -> int """
        return 0

    def maximumWidthChanged(self, *args, **kwargs): # real signature unknown
        pass

    def minimumHeight(self): # real signature unknown; restored from __doc__
        """ minimumHeight(self) -> int """
        return 0

    def minimumHeightChanged(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> PySide2.QtCore.QSize """
        pass

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ minimumWidth(self) -> int """
        return 0

    def minimumWidthChanged(self, *args, **kwargs): # real signature unknown
        pass

    def modality(self): # real signature unknown; restored from __doc__
        """ modality(self) -> PySide2.QtCore.Qt.WindowModality """
        pass

    def modalityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseMoveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def moveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ moveEvent(self, arg__1: PySide2.QtGui.QMoveEvent) -> None """
        pass

    def nativeEvent(self, eventType, message): # real signature unknown; restored from __doc__
        """ nativeEvent(self, eventType: PySide2.QtCore.QByteArray, message: int) -> typing.Tuple[bool, int] """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def opacityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """
        parent(self) -> PySide2.QtGui.QWindow
        parent(self, mode: PySide2.QtGui.QWindow.AncestorMode) -> PySide2.QtGui.QWindow
        """
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> PySide2.QtCore.QPoint """
        pass

    def raise_(self): # real signature unknown; restored from __doc__
        """ raise_(self) -> None """
        pass

    def reportContentOrientationChange(self, orientation): # real signature unknown; restored from __doc__
        """ reportContentOrientationChange(self, orientation: PySide2.QtCore.Qt.ScreenOrientation) -> None """
        pass

    def requestActivate(self): # real signature unknown; restored from __doc__
        """ requestActivate(self) -> None """
        pass

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ requestedFormat(self) -> PySide2.QtGui.QSurfaceFormat """
        pass

    def requestUpdate(self): # real signature unknown; restored from __doc__
        """ requestUpdate(self) -> None """
        pass

    def resize(self, newSize): # real signature unknown; restored from __doc__
        """
        resize(self, newSize: PySide2.QtCore.QSize) -> None
        resize(self, w: int, h: int) -> None
        """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> PySide2.QtGui.QScreen """
        pass

    def screenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseSize(self, size): # real signature unknown; restored from __doc__
        """ setBaseSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setCursor(self, arg__1): # real signature unknown; restored from __doc__
        """ setCursor(self, arg__1: PySide2.QtGui.QCursor) -> None """
        pass

    def setFilePath(self, filePath): # real signature unknown; restored from __doc__
        """ setFilePath(self, filePath: str) -> None """
        pass

    def setFlag(self, arg__1, on=True): # real signature unknown; restored from __doc__
        """ setFlag(self, arg__1: PySide2.QtCore.Qt.WindowType, on: bool = True) -> None """
        pass

    def setFlags(self, flags): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: PySide2.QtCore.Qt.WindowFlags) -> None """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: PySide2.QtGui.QSurfaceFormat) -> None """
        pass

    def setFramePosition(self, point): # real signature unknown; restored from __doc__
        """ setFramePosition(self, point: PySide2.QtCore.QPoint) -> None """
        pass

    def setGeometry(self, posx, posy, w, h): # real signature unknown; restored from __doc__
        """
        setGeometry(self, posx: int, posy: int, w: int, h: int) -> None
        setGeometry(self, rect: PySide2.QtCore.QRect) -> None
        """
        pass

    def setHeight(self, arg): # real signature unknown; restored from __doc__
        """ setHeight(self, arg: int) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setKeyboardGrabEnabled(self, grab): # real signature unknown; restored from __doc__
        """ setKeyboardGrabEnabled(self, grab: bool) -> bool """
        return False

    def setMask(self, region): # real signature unknown; restored from __doc__
        """ setMask(self, region: PySide2.QtGui.QRegion) -> None """
        pass

    def setMaximumHeight(self, h): # real signature unknown; restored from __doc__
        """ setMaximumHeight(self, h: int) -> None """
        pass

    def setMaximumSize(self, size): # real signature unknown; restored from __doc__
        """ setMaximumSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setMaximumWidth(self, w): # real signature unknown; restored from __doc__
        """ setMaximumWidth(self, w: int) -> None """
        pass

    def setMinimumHeight(self, h): # real signature unknown; restored from __doc__
        """ setMinimumHeight(self, h: int) -> None """
        pass

    def setMinimumSize(self, size): # real signature unknown; restored from __doc__
        """ setMinimumSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setMinimumWidth(self, w): # real signature unknown; restored from __doc__
        """ setMinimumWidth(self, w: int) -> None """
        pass

    def setModality(self, modality): # real signature unknown; restored from __doc__
        """ setModality(self, modality: PySide2.QtCore.Qt.WindowModality) -> None """
        pass

    def setMouseGrabEnabled(self, grab): # real signature unknown; restored from __doc__
        """ setMouseGrabEnabled(self, grab: bool) -> bool """
        return False

    def setOpacity(self, level): # real signature unknown; restored from __doc__
        """ setOpacity(self, level: float) -> None """
        pass

    def setParent(self, parent): # real signature unknown; restored from __doc__
        """
        setParent(self, parent: PySide2.QtCore.QObject) -> None
        setParent(self, parent: PySide2.QtGui.QWindow) -> None
        """
        pass

    def setPosition(self, posx, posy): # real signature unknown; restored from __doc__
        """
        setPosition(self, posx: int, posy: int) -> None
        setPosition(self, pt: PySide2.QtCore.QPoint) -> None
        """
        pass

    def setScreen(self, screen): # real signature unknown; restored from __doc__
        """ setScreen(self, screen: PySide2.QtGui.QScreen) -> None """
        pass

    def setSizeIncrement(self, size): # real signature unknown; restored from __doc__
        """ setSizeIncrement(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setSurfaceType(self, surfaceType): # real signature unknown; restored from __doc__
        """ setSurfaceType(self, surfaceType: PySide2.QtGui.QSurface.SurfaceType) -> None """
        pass

    def setTitle(self, arg__1): # real signature unknown; restored from __doc__
        """ setTitle(self, arg__1: str) -> None """
        pass

    def setTransientParent(self, parent): # real signature unknown; restored from __doc__
        """ setTransientParent(self, parent: PySide2.QtGui.QWindow) -> None """
        pass

    def setVisibility(self, v): # real signature unknown; restored from __doc__
        """ setVisibility(self, v: PySide2.QtGui.QWindow.Visibility) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def setWidth(self, arg): # real signature unknown; restored from __doc__
        """ setWidth(self, arg: int) -> None """
        pass

    def setWindowState(self, state): # real signature unknown; restored from __doc__
        """ setWindowState(self, state: PySide2.QtCore.Qt.WindowState) -> None """
        pass

    def setWindowStates(self, states): # real signature unknown; restored from __doc__
        """ setWindowStates(self, states: PySide2.QtCore.Qt.WindowStates) -> None """
        pass

    def setX(self, arg): # real signature unknown; restored from __doc__
        """ setX(self, arg: int) -> None """
        pass

    def setY(self, arg): # real signature unknown; restored from __doc__
        """ setY(self, arg: int) -> None """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) -> None """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def showFullScreen(self): # real signature unknown; restored from __doc__
        """ showFullScreen(self) -> None """
        pass

    def showMaximized(self): # real signature unknown; restored from __doc__
        """ showMaximized(self) -> None """
        pass

    def showMinimized(self): # real signature unknown; restored from __doc__
        """ showMinimized(self) -> None """
        pass

    def showNormal(self): # real signature unknown; restored from __doc__
        """ showNormal(self) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def sizeIncrement(self): # real signature unknown; restored from __doc__
        """ sizeIncrement(self) -> PySide2.QtCore.QSize """
        pass

    def startSystemMove(self): # real signature unknown; restored from __doc__
        """ startSystemMove(self) -> bool """
        return False

    def startSystemResize(self, edges): # real signature unknown; restored from __doc__
        """ startSystemResize(self, edges: PySide2.QtCore.Qt.Edges) -> bool """
        return False

    def surfaceHandle(self): # real signature unknown; restored from __doc__
        """ surfaceHandle(self) -> int """
        return 0

    def surfaceType(self): # real signature unknown; restored from __doc__
        """ surfaceType(self) -> PySide2.QtGui.QSurface.SurfaceType """
        pass

    def tabletEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ tabletEvent(self, arg__1: PySide2.QtGui.QTabletEvent) -> None """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def touchEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ touchEvent(self, arg__1: PySide2.QtGui.QTouchEvent) -> None """
        pass

    def transientParent(self): # real signature unknown; restored from __doc__
        """ transientParent(self) -> PySide2.QtGui.QWindow """
        pass

    def transientParentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtCore.Qt.WindowType """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) -> None """
        pass

    def visibility(self): # real signature unknown; restored from __doc__
        """ visibility(self) -> PySide2.QtGui.QWindow.Visibility """
        pass

    def visibilityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def visibleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ wheelEvent(self, arg__1: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def widthChanged(self, *args, **kwargs): # real signature unknown
        pass

    def windowState(self): # real signature unknown; restored from __doc__
        """ windowState(self) -> PySide2.QtCore.Qt.WindowState """
        pass

    def windowStateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def windowStates(self): # real signature unknown; restored from __doc__
        """ windowStates(self) -> PySide2.QtCore.Qt.WindowStates """
        pass

    def windowTitleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def winId(self): # real signature unknown; restored from __doc__
        """ winId(self) -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def xChanged(self, *args, **kwargs): # real signature unknown
        pass

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def yChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AncestorMode = None # (!) real value is "<class 'PySide2.QtGui.QWindow.AncestorMode'>"
    AutomaticVisibility = PySide2.QtGui.QWindow.Visibility.AutomaticVisibility
    ExcludeTransients = PySide2.QtGui.QWindow.AncestorMode.ExcludeTransients
    FullScreen = PySide2.QtGui.QWindow.Visibility.FullScreen
    Hidden = PySide2.QtGui.QWindow.Visibility.Hidden
    IncludeTransients = PySide2.QtGui.QWindow.AncestorMode.IncludeTransients
    Maximized = PySide2.QtGui.QWindow.Visibility.Maximized
    Minimized = PySide2.QtGui.QWindow.Visibility.Minimized
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00844340>'
    Visibility = None # (!) real value is "<class 'PySide2.QtGui.QWindow.Visibility'>"
    Windowed = PySide2.QtGui.QWindow.Visibility.Windowed


