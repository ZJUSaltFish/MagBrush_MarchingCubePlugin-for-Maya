# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QWidget(__PySide2_QtCore.QObject, __PySide2_QtGui.QPaintDevice):
    """ QWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def acceptDrops(self): # real signature unknown; restored from __doc__
        """ acceptDrops(self) -> bool """
        return False

    def accessibleDescription(self): # real signature unknown; restored from __doc__
        """ accessibleDescription(self) -> str """
        return ""

    def accessibleName(self): # real signature unknown; restored from __doc__
        """ accessibleName(self) -> str """
        return ""

    def actionEvent(self, event): # real signature unknown; restored from __doc__
        """ actionEvent(self, event: PySide2.QtGui.QActionEvent) -> None """
        pass

    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> typing.List[PySide2.QtWidgets.QAction] """
        pass

    def activateWindow(self): # real signature unknown; restored from __doc__
        """ activateWindow(self) -> None """
        pass

    def addAction(self, action): # real signature unknown; restored from __doc__
        """ addAction(self, action: PySide2.QtWidgets.QAction) -> None """
        pass

    def addActions(self, actions, PySide2_QtWidgets_QAction=None): # real signature unknown; restored from __doc__
        """ addActions(self, actions: typing.Sequence[PySide2.QtWidgets.QAction]) -> None """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) -> None """
        pass

    def autoFillBackground(self): # real signature unknown; restored from __doc__
        """ autoFillBackground(self) -> bool """
        return False

    def backgroundRole(self): # real signature unknown; restored from __doc__
        """ backgroundRole(self) -> PySide2.QtGui.QPalette.ColorRole """
        pass

    def backingStore(self): # real signature unknown; restored from __doc__
        """ backingStore(self) -> PySide2.QtGui.QBackingStore """
        pass

    def baseSize(self): # real signature unknown; restored from __doc__
        """ baseSize(self) -> PySide2.QtCore.QSize """
        pass

    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def childAt(self, p): # real signature unknown; restored from __doc__
        """
        childAt(self, p: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QWidget
        childAt(self, x: int, y: int) -> PySide2.QtWidgets.QWidget
        """
        pass

    def childrenRect(self): # real signature unknown; restored from __doc__
        """ childrenRect(self) -> PySide2.QtCore.QRect """
        pass

    def childrenRegion(self): # real signature unknown; restored from __doc__
        """ childrenRegion(self) -> PySide2.QtGui.QRegion """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ clearFocus(self) -> None """
        pass

    def clearMask(self): # real signature unknown; restored from __doc__
        """ clearMask(self) -> None """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def closeEvent(self, event): # real signature unknown; restored from __doc__
        """ closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None """
        pass

    def contentsMargins(self): # real signature unknown; restored from __doc__
        """ contentsMargins(self) -> PySide2.QtCore.QMargins """
        pass

    def contentsRect(self): # real signature unknown; restored from __doc__
        """ contentsRect(self) -> PySide2.QtCore.QRect """
        pass

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def contextMenuPolicy(self): # real signature unknown; restored from __doc__
        """ contextMenuPolicy(self) -> PySide2.QtCore.Qt.ContextMenuPolicy """
        pass

    def create(self, arg__1=0, initializeWindow=True, destroyOldWindow=True): # real signature unknown; restored from __doc__
        """ create(self, arg__1: int = 0, initializeWindow: bool = True, destroyOldWindow: bool = True) -> None """
        pass

    def createWindowContainer(self, window, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createWindowContainer(window: PySide2.QtGui.QWindow, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> PySide2.QtWidgets.QWidget """
        pass

    def createWinId(self): # real signature unknown; restored from __doc__
        """ createWinId(self) -> None """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> PySide2.QtGui.QCursor """
        pass

    def customContextMenuRequested(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, destroyWindow=True, destroySubWindows=True): # real signature unknown; restored from __doc__
        """ destroy(self, destroyWindow: bool = True, destroySubWindows: bool = True) -> None """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def dragEnterEvent(self, event): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None """
        pass

    def dragLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, event: PySide2.QtGui.QDragLeaveEvent) -> None """
        pass

    def dragMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, event: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None """
        pass

    def effectiveWinId(self): # real signature unknown; restored from __doc__
        """ effectiveWinId(self) -> int """
        return 0

    def ensurePolished(self): # real signature unknown; restored from __doc__
        """ ensurePolished(self) -> None """
        pass

    def enterEvent(self, event): # real signature unknown; restored from __doc__
        """ enterEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def find(self, arg__1): # real signature unknown; restored from __doc__
        """ find(arg__1: int) -> PySide2.QtWidgets.QWidget """
        pass

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusNextChild(self): # real signature unknown; restored from __doc__
        """ focusNextChild(self) -> bool """
        return False

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusPolicy(self): # real signature unknown; restored from __doc__
        """ focusPolicy(self) -> PySide2.QtCore.Qt.FocusPolicy """
        pass

    def focusPreviousChild(self): # real signature unknown; restored from __doc__
        """ focusPreviousChild(self) -> bool """
        return False

    def focusProxy(self): # real signature unknown; restored from __doc__
        """ focusProxy(self) -> PySide2.QtWidgets.QWidget """
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def fontInfo(self): # real signature unknown; restored from __doc__
        """ fontInfo(self) -> PySide2.QtGui.QFontInfo """
        pass

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ fontMetrics(self) -> PySide2.QtGui.QFontMetrics """
        pass

    def foregroundRole(self): # real signature unknown; restored from __doc__
        """ foregroundRole(self) -> PySide2.QtGui.QPalette.ColorRole """
        pass

    def frameGeometry(self): # real signature unknown; restored from __doc__
        """ frameGeometry(self) -> PySide2.QtCore.QRect """
        pass

    def frameSize(self): # real signature unknown; restored from __doc__
        """ frameSize(self) -> PySide2.QtCore.QSize """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> PySide2.QtCore.QRect """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> typing.Tuple[int, int, int, int] """
        pass

    def grab(self, rectangle=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grab(self, rectangle: PySide2.QtCore.QRect = PySide2.QtCore.QRect(0, 0, -1, -1)) -> PySide2.QtGui.QPixmap """
        pass

    def grabGesture(self, type, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabGesture(self, type: PySide2.QtCore.Qt.GestureType, flags: PySide2.QtCore.Qt.GestureFlags = Default(Qt.GestureFlags)) -> None """
        pass

    def grabKeyboard(self): # real signature unknown; restored from __doc__
        """ grabKeyboard(self) -> None """
        pass

    def grabMouse(self): # real signature unknown; restored from __doc__
        """
        grabMouse(self) -> None
        grabMouse(self, arg__1: PySide2.QtGui.QCursor) -> None
        """
        pass

    def grabShortcut(self, key, context=None): # real signature unknown; restored from __doc__
        """ grabShortcut(self, key: PySide2.QtGui.QKeySequence, context: PySide2.QtCore.Qt.ShortcutContext = PySide2.QtCore.Qt.ShortcutContext.WindowShortcut) -> int """
        return 0

    def graphicsEffect(self): # real signature unknown; restored from __doc__
        """ graphicsEffect(self) -> PySide2.QtWidgets.QGraphicsEffect """
        pass

    def graphicsProxyWidget(self): # real signature unknown; restored from __doc__
        """ graphicsProxyWidget(self) -> PySide2.QtWidgets.QGraphicsProxyWidget """
        pass

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def hasMouseTracking(self): # real signature unknown; restored from __doc__
        """ hasMouseTracking(self) -> bool """
        return False

    def hasTabletTracking(self): # real signature unknown; restored from __doc__
        """ hasTabletTracking(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def heightForWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ heightForWidth(self, arg__1: int) -> int """
        return 0

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) -> None """
        pass

    def hideEvent(self, event): # real signature unknown; restored from __doc__
        """ hideEvent(self, event: PySide2.QtGui.QHideEvent) -> None """
        pass

    def initPainter(self, painter): # real signature unknown; restored from __doc__
        """ initPainter(self, painter: PySide2.QtGui.QPainter) -> None """
        pass

    def inputMethodEvent(self, event): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: PySide2.QtGui.QInputMethodEvent) -> None """
        pass

    def inputMethodHints(self): # real signature unknown; restored from __doc__
        """ inputMethodHints(self) -> PySide2.QtCore.Qt.InputMethodHints """
        pass

    def inputMethodQuery(self, arg__1): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, arg__1: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any """
        pass

    def insertAction(self, before, action): # real signature unknown; restored from __doc__
        """ insertAction(self, before: PySide2.QtWidgets.QAction, action: PySide2.QtWidgets.QAction) -> None """
        pass

    def insertActions(self, before, actions, PySide2_QtWidgets_QAction=None): # real signature unknown; restored from __doc__
        """ insertActions(self, before: PySide2.QtWidgets.QAction, actions: typing.Sequence[PySide2.QtWidgets.QAction]) -> None """
        pass

    def internalWinId(self): # real signature unknown; restored from __doc__
        """ internalWinId(self) -> int """
        return 0

    def isActiveWindow(self): # real signature unknown; restored from __doc__
        """ isActiveWindow(self) -> bool """
        return False

    def isAncestorOf(self, child): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, child: PySide2.QtWidgets.QWidget) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isEnabledTo(self, arg__1): # real signature unknown; restored from __doc__
        """ isEnabledTo(self, arg__1: PySide2.QtWidgets.QWidget) -> bool """
        return False

    def isEnabledToTLW(self): # real signature unknown; restored from __doc__
        """ isEnabledToTLW(self) -> bool """
        return False

    def isFullScreen(self): # real signature unknown; restored from __doc__
        """ isFullScreen(self) -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def isLeftToRight(self): # real signature unknown; restored from __doc__
        """ isLeftToRight(self) -> bool """
        return False

    def isMaximized(self): # real signature unknown; restored from __doc__
        """ isMaximized(self) -> bool """
        return False

    def isMinimized(self): # real signature unknown; restored from __doc__
        """ isMinimized(self) -> bool """
        return False

    def isModal(self): # real signature unknown; restored from __doc__
        """ isModal(self) -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ isRightToLeft(self) -> bool """
        return False

    def isTopLevel(self): # real signature unknown; restored from __doc__
        """ isTopLevel(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def isVisibleTo(self, arg__1): # real signature unknown; restored from __doc__
        """ isVisibleTo(self, arg__1: PySide2.QtWidgets.QWidget) -> bool """
        return False

    def isWindow(self): # real signature unknown; restored from __doc__
        """ isWindow(self) -> bool """
        return False

    def isWindowModified(self): # real signature unknown; restored from __doc__
        """ isWindowModified(self) -> bool """
        return False

    def keyboardGrabber(self): # real signature unknown; restored from __doc__
        """ keyboardGrabber() -> PySide2.QtWidgets.QWidget """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> PySide2.QtWidgets.QLayout """
        pass

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> PySide2.QtCore.Qt.LayoutDirection """
        pass

    def leaveEvent(self, event): # real signature unknown; restored from __doc__
        """ leaveEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> PySide2.QtCore.QLocale """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """ lower(self) -> None """
        pass

    def mapFrom(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ mapFrom(self, arg__1: PySide2.QtWidgets.QWidget, arg__2: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint """
        pass

    def mapFromGlobal(self, arg__1): # real signature unknown; restored from __doc__
        """ mapFromGlobal(self, arg__1: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint """
        pass

    def mapFromParent(self, arg__1): # real signature unknown; restored from __doc__
        """ mapFromParent(self, arg__1: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint """
        pass

    def mapTo(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ mapTo(self, arg__1: PySide2.QtWidgets.QWidget, arg__2: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint """
        pass

    def mapToGlobal(self, arg__1): # real signature unknown; restored from __doc__
        """ mapToGlobal(self, arg__1: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint """
        pass

    def mapToParent(self, arg__1): # real signature unknown; restored from __doc__
        """ mapToParent(self, arg__1: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> PySide2.QtGui.QRegion """
        pass

    def maximumHeight(self): # real signature unknown; restored from __doc__
        """ maximumHeight(self) -> int """
        return 0

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> PySide2.QtCore.QSize """
        pass

    def maximumWidth(self): # real signature unknown; restored from __doc__
        """ maximumWidth(self) -> int """
        return 0

    def metric(self, arg__1): # real signature unknown; restored from __doc__
        """ metric(self, arg__1: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def minimumHeight(self): # real signature unknown; restored from __doc__
        """ minimumHeight(self) -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> PySide2.QtCore.QSize """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def minimumWidth(self): # real signature unknown; restored from __doc__
        """ minimumWidth(self) -> int """
        return 0

    def mouseDoubleClickEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseGrabber(self): # real signature unknown; restored from __doc__
        """ mouseGrabber() -> PySide2.QtWidgets.QWidget """
        pass

    def mouseMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, event): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def move(self, arg__1): # real signature unknown; restored from __doc__
        """
        move(self, arg__1: PySide2.QtCore.QPoint) -> None
        move(self, x: int, y: int) -> None
        """
        pass

    def moveEvent(self, event): # real signature unknown; restored from __doc__
        """ moveEvent(self, event: PySide2.QtGui.QMoveEvent) -> None """
        pass

    def nativeEvent(self, eventType, message): # real signature unknown; restored from __doc__
        """ nativeEvent(self, eventType: PySide2.QtCore.QByteArray, message: int) -> typing.Tuple[bool, int] """
        pass

    def nativeParentWidget(self): # real signature unknown; restored from __doc__
        """ nativeParentWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def nextInFocusChain(self): # real signature unknown; restored from __doc__
        """ nextInFocusChain(self) -> PySide2.QtWidgets.QWidget """
        pass

    def normalGeometry(self): # real signature unknown; restored from __doc__
        """ normalGeometry(self) -> PySide2.QtCore.QRect """
        pass

    def overrideWindowFlags(self, type): # real signature unknown; restored from __doc__
        """ overrideWindowFlags(self, type: PySide2.QtCore.Qt.WindowFlags) -> None """
        pass

    def overrideWindowState(self, state): # real signature unknown; restored from __doc__
        """ overrideWindowState(self, state: PySide2.QtCore.Qt.WindowStates) -> None """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> PySide2.QtGui.QPalette """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> PySide2.QtCore.QPoint """
        pass

    def previousInFocusChain(self): # real signature unknown; restored from __doc__
        """ previousInFocusChain(self) -> PySide2.QtWidgets.QWidget """
        pass

    def raise_(self): # real signature unknown; restored from __doc__
        """ raise_(self) -> None """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> PySide2.QtCore.QRect """
        pass

    def redirected(self, offset): # real signature unknown; restored from __doc__
        """ redirected(self, offset: PySide2.QtCore.QPoint) -> PySide2.QtGui.QPaintDevice """
        pass

    def releaseKeyboard(self): # real signature unknown; restored from __doc__
        """ releaseKeyboard(self) -> None """
        pass

    def releaseMouse(self): # real signature unknown; restored from __doc__
        """ releaseMouse(self) -> None """
        pass

    def releaseShortcut(self, id): # real signature unknown; restored from __doc__
        """ releaseShortcut(self, id: int) -> None """
        pass

    def removeAction(self, action): # real signature unknown; restored from __doc__
        """ removeAction(self, action: PySide2.QtWidgets.QAction) -> None """
        pass

    def render(self, painter, targetOffset, sourceRegion=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        render(self, painter: PySide2.QtGui.QPainter, targetOffset: PySide2.QtCore.QPoint, sourceRegion: PySide2.QtGui.QRegion = Default(QRegion), renderFlags: PySide2.QtWidgets.QWidget.RenderFlags = Instance(QWidget.RenderFlags(QWidget.DrawWindowBackground | QWidget.DrawChildren))) -> None
        render(self, target: PySide2.QtGui.QPaintDevice, targetOffset: PySide2.QtCore.QPoint = Default(QPoint), sourceRegion: PySide2.QtGui.QRegion = Default(QRegion), renderFlags: PySide2.QtWidgets.QWidget.RenderFlags = Instance(QWidget.RenderFlags(QWidget.DrawWindowBackground | QWidget.DrawChildren))) -> None
        """
        pass

    def repaint(self): # real signature unknown; restored from __doc__
        """
        repaint(self) -> None
        repaint(self, arg__1: PySide2.QtCore.QRect) -> None
        repaint(self, arg__1: PySide2.QtGui.QRegion) -> None
        repaint(self, x: int, y: int, w: int, h: int) -> None
        """
        pass

    def resize(self, arg__1): # real signature unknown; restored from __doc__
        """
        resize(self, arg__1: PySide2.QtCore.QSize) -> None
        resize(self, w: int, h: int) -> None
        """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def restoreGeometry(self, geometry): # real signature unknown; restored from __doc__
        """ restoreGeometry(self, geometry: PySide2.QtCore.QByteArray) -> bool """
        return False

    def saveGeometry(self): # real signature unknown; restored from __doc__
        """ saveGeometry(self) -> PySide2.QtCore.QByteArray """
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """ screen(self) -> PySide2.QtGui.QScreen """
        pass

    def scroll(self, dx, dy): # real signature unknown; restored from __doc__
        """
        scroll(self, dx: int, dy: int) -> None
        scroll(self, dx: int, dy: int, arg__3: PySide2.QtCore.QRect) -> None
        """
        pass

    def setAcceptDrops(self, on): # real signature unknown; restored from __doc__
        """ setAcceptDrops(self, on: bool) -> None """
        pass

    def setAccessibleDescription(self, description): # real signature unknown; restored from __doc__
        """ setAccessibleDescription(self, description: str) -> None """
        pass

    def setAccessibleName(self, name): # real signature unknown; restored from __doc__
        """ setAccessibleName(self, name: str) -> None """
        pass

    def setAttribute(self, arg__1, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(self, arg__1: PySide2.QtCore.Qt.WidgetAttribute, on: bool = True) -> None """
        pass

    def setAutoFillBackground(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoFillBackground(self, enabled: bool) -> None """
        pass

    def setBackgroundRole(self, arg__1): # real signature unknown; restored from __doc__
        """ setBackgroundRole(self, arg__1: PySide2.QtGui.QPalette.ColorRole) -> None """
        pass

    def setBaseSize(self, arg__1): # real signature unknown; restored from __doc__
        """
        setBaseSize(self, arg__1: PySide2.QtCore.QSize) -> None
        setBaseSize(self, basew: int, baseh: int) -> None
        """
        pass

    def setContentsMargins(self, left, top, right, bottom): # real signature unknown; restored from __doc__
        """
        setContentsMargins(self, left: int, top: int, right: int, bottom: int) -> None
        setContentsMargins(self, margins: PySide2.QtCore.QMargins) -> None
        """
        pass

    def setContextMenuPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setContextMenuPolicy(self, policy: PySide2.QtCore.Qt.ContextMenuPolicy) -> None """
        pass

    def setCursor(self, arg__1): # real signature unknown; restored from __doc__
        """ setCursor(self, arg__1: PySide2.QtGui.QCursor) -> None """
        pass

    def setDisabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setDisabled(self, arg__1: bool) -> None """
        pass

    def setEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setEnabled(self, arg__1: bool) -> None """
        pass

    def setFixedHeight(self, h): # real signature unknown; restored from __doc__
        """ setFixedHeight(self, h: int) -> None """
        pass

    def setFixedSize(self, arg__1): # real signature unknown; restored from __doc__
        """
        setFixedSize(self, arg__1: PySide2.QtCore.QSize) -> None
        setFixedSize(self, w: int, h: int) -> None
        """
        pass

    def setFixedWidth(self, w): # real signature unknown; restored from __doc__
        """ setFixedWidth(self, w: int) -> None """
        pass

    def setFocus(self): # real signature unknown; restored from __doc__
        """
        setFocus(self) -> None
        setFocus(self, reason: PySide2.QtCore.Qt.FocusReason) -> None
        """
        pass

    def setFocusPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setFocusPolicy(self, policy: PySide2.QtCore.Qt.FocusPolicy) -> None """
        pass

    def setFocusProxy(self, arg__1): # real signature unknown; restored from __doc__
        """ setFocusProxy(self, arg__1: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setFont(self, arg__1): # real signature unknown; restored from __doc__
        """ setFont(self, arg__1: PySide2.QtGui.QFont) -> None """
        pass

    def setForegroundRole(self, arg__1): # real signature unknown; restored from __doc__
        """ setForegroundRole(self, arg__1: PySide2.QtGui.QPalette.ColorRole) -> None """
        pass

    def setGeometry(self, arg__1): # real signature unknown; restored from __doc__
        """
        setGeometry(self, arg__1: PySide2.QtCore.QRect) -> None
        setGeometry(self, x: int, y: int, w: int, h: int) -> None
        """
        pass

    def setGraphicsEffect(self, effect): # real signature unknown; restored from __doc__
        """ setGraphicsEffect(self, effect: PySide2.QtWidgets.QGraphicsEffect) -> None """
        pass

    def setHidden(self, hidden): # real signature unknown; restored from __doc__
        """ setHidden(self, hidden: bool) -> None """
        pass

    def setInputMethodHints(self, hints): # real signature unknown; restored from __doc__
        """ setInputMethodHints(self, hints: PySide2.QtCore.Qt.InputMethodHints) -> None """
        pass

    def setLayout(self, arg__1): # real signature unknown; restored from __doc__
        """ setLayout(self, arg__1: PySide2.QtWidgets.QLayout) -> None """
        pass

    def setLayoutDirection(self, direction): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, direction: PySide2.QtCore.Qt.LayoutDirection) -> None """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: PySide2.QtCore.QLocale) -> None """
        pass

    def setMask(self, arg__1): # real signature unknown; restored from __doc__
        """
        setMask(self, arg__1: PySide2.QtGui.QBitmap) -> None
        setMask(self, arg__1: PySide2.QtGui.QRegion) -> None
        """
        pass

    def setMaximumHeight(self, maxh): # real signature unknown; restored from __doc__
        """ setMaximumHeight(self, maxh: int) -> None """
        pass

    def setMaximumSize(self, arg__1): # real signature unknown; restored from __doc__
        """
        setMaximumSize(self, arg__1: PySide2.QtCore.QSize) -> None
        setMaximumSize(self, maxw: int, maxh: int) -> None
        """
        pass

    def setMaximumWidth(self, maxw): # real signature unknown; restored from __doc__
        """ setMaximumWidth(self, maxw: int) -> None """
        pass

    def setMinimumHeight(self, minh): # real signature unknown; restored from __doc__
        """ setMinimumHeight(self, minh: int) -> None """
        pass

    def setMinimumSize(self, arg__1): # real signature unknown; restored from __doc__
        """
        setMinimumSize(self, arg__1: PySide2.QtCore.QSize) -> None
        setMinimumSize(self, minw: int, minh: int) -> None
        """
        pass

    def setMinimumWidth(self, minw): # real signature unknown; restored from __doc__
        """ setMinimumWidth(self, minw: int) -> None """
        pass

    def setMouseTracking(self, enable): # real signature unknown; restored from __doc__
        """ setMouseTracking(self, enable: bool) -> None """
        pass

    def setPalette(self, arg__1): # real signature unknown; restored from __doc__
        """ setPalette(self, arg__1: PySide2.QtGui.QPalette) -> None """
        pass

    def setParent(self, parent): # real signature unknown; restored from __doc__
        """
        setParent(self, parent: PySide2.QtCore.QObject) -> None
        setParent(self, parent: PySide2.QtWidgets.QWidget) -> None
        setParent(self, parent: PySide2.QtWidgets.QWidget, f: PySide2.QtCore.Qt.WindowFlags) -> None
        """
        pass

    def setShortcutAutoRepeat(self, id, enable=True): # real signature unknown; restored from __doc__
        """ setShortcutAutoRepeat(self, id: int, enable: bool = True) -> None """
        pass

    def setShortcutEnabled(self, id, enable=True): # real signature unknown; restored from __doc__
        """ setShortcutEnabled(self, id: int, enable: bool = True) -> None """
        pass

    def setSizeIncrement(self, arg__1): # real signature unknown; restored from __doc__
        """
        setSizeIncrement(self, arg__1: PySide2.QtCore.QSize) -> None
        setSizeIncrement(self, w: int, h: int) -> None
        """
        pass

    def setSizePolicy(self, arg__1): # real signature unknown; restored from __doc__
        """
        setSizePolicy(self, arg__1: PySide2.QtWidgets.QSizePolicy) -> None
        setSizePolicy(self, horizontal: PySide2.QtWidgets.QSizePolicy.Policy, vertical: PySide2.QtWidgets.QSizePolicy.Policy) -> None
        """
        pass

    def setStatusTip(self, arg__1): # real signature unknown; restored from __doc__
        """ setStatusTip(self, arg__1: str) -> None """
        pass

    def setStyle(self, arg__1): # real signature unknown; restored from __doc__
        """ setStyle(self, arg__1: PySide2.QtWidgets.QStyle) -> None """
        pass

    def setStyleSheet(self, styleSheet): # real signature unknown; restored from __doc__
        """ setStyleSheet(self, styleSheet: str) -> None """
        pass

    def setTabletTracking(self, enable): # real signature unknown; restored from __doc__
        """ setTabletTracking(self, enable: bool) -> None """
        pass

    def setTabOrder(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ setTabOrder(arg__1: PySide2.QtWidgets.QWidget, arg__2: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setToolTip(self, arg__1): # real signature unknown; restored from __doc__
        """ setToolTip(self, arg__1: str) -> None """
        pass

    def setToolTipDuration(self, msec): # real signature unknown; restored from __doc__
        """ setToolTipDuration(self, msec: int) -> None """
        pass

    def setUpdatesEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setUpdatesEnabled(self, enable: bool) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def setWhatsThis(self, arg__1): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, arg__1: str) -> None """
        pass

    def setWindowFilePath(self, filePath): # real signature unknown; restored from __doc__
        """ setWindowFilePath(self, filePath: str) -> None """
        pass

    def setWindowFlag(self, arg__1, on=True): # real signature unknown; restored from __doc__
        """ setWindowFlag(self, arg__1: PySide2.QtCore.Qt.WindowType, on: bool = True) -> None """
        pass

    def setWindowFlags(self, type): # real signature unknown; restored from __doc__
        """ setWindowFlags(self, type: PySide2.QtCore.Qt.WindowFlags) -> None """
        pass

    def setWindowIcon(self, icon): # real signature unknown; restored from __doc__
        """ setWindowIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setWindowIconText(self, arg__1): # real signature unknown; restored from __doc__
        """ setWindowIconText(self, arg__1: str) -> None """
        pass

    def setWindowModality(self, windowModality): # real signature unknown; restored from __doc__
        """ setWindowModality(self, windowModality: PySide2.QtCore.Qt.WindowModality) -> None """
        pass

    def setWindowModified(self, arg__1): # real signature unknown; restored from __doc__
        """ setWindowModified(self, arg__1: bool) -> None """
        pass

    def setWindowOpacity(self, level): # real signature unknown; restored from __doc__
        """ setWindowOpacity(self, level: float) -> None """
        pass

    def setWindowRole(self, arg__1): # real signature unknown; restored from __doc__
        """ setWindowRole(self, arg__1: str) -> None """
        pass

    def setWindowState(self, state): # real signature unknown; restored from __doc__
        """ setWindowState(self, state: PySide2.QtCore.Qt.WindowStates) -> None """
        pass

    def setWindowTitle(self, arg__1): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, arg__1: str) -> None """
        pass

    def sharedPainter(self): # real signature unknown; restored from __doc__
        """ sharedPainter(self) -> PySide2.QtGui.QPainter """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) -> None """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: PySide2.QtGui.QShowEvent) -> None """
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

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def sizeIncrement(self): # real signature unknown; restored from __doc__
        """ sizeIncrement(self) -> PySide2.QtCore.QSize """
        pass

    def sizePolicy(self): # real signature unknown; restored from __doc__
        """ sizePolicy(self) -> PySide2.QtWidgets.QSizePolicy """
        pass

    def stackUnder(self, arg__1): # real signature unknown; restored from __doc__
        """ stackUnder(self, arg__1: PySide2.QtWidgets.QWidget) -> None """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ statusTip(self) -> str """
        return ""

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> PySide2.QtWidgets.QStyle """
        pass

    def styleSheet(self): # real signature unknown; restored from __doc__
        """ styleSheet(self) -> str """
        return ""

    def tabletEvent(self, event): # real signature unknown; restored from __doc__
        """ tabletEvent(self, event: PySide2.QtGui.QTabletEvent) -> None """
        pass

    def testAttribute(self, arg__1): # real signature unknown; restored from __doc__
        """ testAttribute(self, arg__1: PySide2.QtCore.Qt.WidgetAttribute) -> bool """
        return False

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def toolTipDuration(self): # real signature unknown; restored from __doc__
        """ toolTipDuration(self) -> int """
        return 0

    def topLevelWidget(self): # real signature unknown; restored from __doc__
        """ topLevelWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def underMouse(self): # real signature unknown; restored from __doc__
        """ underMouse(self) -> bool """
        return False

    def ungrabGesture(self, type): # real signature unknown; restored from __doc__
        """ ungrabGesture(self, type: PySide2.QtCore.Qt.GestureType) -> None """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) -> None """
        pass

    def unsetLayoutDirection(self): # real signature unknown; restored from __doc__
        """ unsetLayoutDirection(self) -> None """
        pass

    def unsetLocale(self): # real signature unknown; restored from __doc__
        """ unsetLocale(self) -> None """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """
        update(self) -> None
        update(self, arg__1: PySide2.QtCore.QRect) -> None
        update(self, arg__1: PySide2.QtGui.QRegion) -> None
        update(self, x: int, y: int, w: int, h: int) -> None
        """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ updateGeometry(self) -> None """
        pass

    def updateMicroFocus(self): # real signature unknown; restored from __doc__
        """ updateMicroFocus(self) -> None """
        pass

    def updatesEnabled(self): # real signature unknown; restored from __doc__
        """ updatesEnabled(self) -> bool """
        return False

    def visibleRegion(self): # real signature unknown; restored from __doc__
        """ visibleRegion(self) -> PySide2.QtGui.QRegion """
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> PySide2.QtWidgets.QWidget """
        pass

    def windowFilePath(self): # real signature unknown; restored from __doc__
        """ windowFilePath(self) -> str """
        return ""

    def windowFlags(self): # real signature unknown; restored from __doc__
        """ windowFlags(self) -> PySide2.QtCore.Qt.WindowFlags """
        pass

    def windowHandle(self): # real signature unknown; restored from __doc__
        """ windowHandle(self) -> PySide2.QtGui.QWindow """
        pass

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ windowIcon(self) -> PySide2.QtGui.QIcon """
        pass

    def windowIconChanged(self, *args, **kwargs): # real signature unknown
        pass

    def windowIconText(self): # real signature unknown; restored from __doc__
        """ windowIconText(self) -> str """
        return ""

    def windowIconTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def windowModality(self): # real signature unknown; restored from __doc__
        """ windowModality(self) -> PySide2.QtCore.Qt.WindowModality """
        pass

    def windowOpacity(self): # real signature unknown; restored from __doc__
        """ windowOpacity(self) -> float """
        return 0.0

    def windowRole(self): # real signature unknown; restored from __doc__
        """ windowRole(self) -> str """
        return ""

    def windowState(self): # real signature unknown; restored from __doc__
        """ windowState(self) -> PySide2.QtCore.Qt.WindowStates """
        pass

    def windowTitle(self): # real signature unknown; restored from __doc__
        """ windowTitle(self) -> str """
        return ""

    def windowTitleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def windowType(self): # real signature unknown; restored from __doc__
        """ windowType(self) -> PySide2.QtCore.Qt.WindowType """
        pass

    def winId(self): # real signature unknown; restored from __doc__
        """ winId(self) -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    DrawChildren = PySide2.QtWidgets.QWidget.RenderFlag.DrawChildren
    DrawWindowBackground = PySide2.QtWidgets.QWidget.RenderFlag.DrawWindowBackground
    IgnoreMask = PySide2.QtWidgets.QWidget.RenderFlag.IgnoreMask
    RenderFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QWidget.RenderFlag'>"
    RenderFlags = None # (!) real value is "<class 'PySide2.QtWidgets.QWidget.RenderFlags'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507A53C0>'


