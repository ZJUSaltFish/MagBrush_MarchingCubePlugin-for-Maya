# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsObject import QGraphicsObject

from .QGraphicsLayoutItem import QGraphicsLayoutItem

class QGraphicsWidget(QGraphicsObject, QGraphicsLayoutItem):
    """ QGraphicsWidget(parent: typing.Optional[QGraphicsItem] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> List[QAction] """
        return []

    def addAction(self, action): # real signature unknown; restored from __doc__
        """ addAction(self, action: QAction) """
        pass

    def addActions(self, actions, QAction=None): # real signature unknown; restored from __doc__
        """ addActions(self, actions: Iterable[QAction]) """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) """
        pass

    def autoFillBackground(self): # real signature unknown; restored from __doc__
        """ autoFillBackground(self) -> bool """
        return False

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def closeEvent(self, event): # real signature unknown; restored from __doc__
        """ closeEvent(self, event: QCloseEvent) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: QEvent) -> bool """
        return False

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: QFocusEvent) """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: QFocusEvent) """
        pass

    def focusPolicy(self): # real signature unknown; restored from __doc__
        """ focusPolicy(self) -> Qt.FocusPolicy """
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget(self) -> QGraphicsWidget """
        return QGraphicsWidget

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> Tuple[float, float, float, float] """
        pass

    def getWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ getWindowFrameMargins(self) -> Tuple[float, float, float, float] """
        pass

    def grabKeyboardEvent(self, event): # real signature unknown; restored from __doc__
        """ grabKeyboardEvent(self, event: QEvent) """
        pass

    def grabMouseEvent(self, event): # real signature unknown; restored from __doc__
        """ grabMouseEvent(self, event: QEvent) """
        pass

    def grabShortcut(self, sequence, QKeySequence=None, QKeySequence_StandardKey=None, p_str=None, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ grabShortcut(self, sequence: Union[QKeySequence, QKeySequence.StandardKey, str, int], context: Qt.ShortcutContext = Qt.WindowShortcut) -> int """
        pass

    def hideEvent(self, event): # real signature unknown; restored from __doc__
        """ hideEvent(self, event: QHideEvent) """
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, event: QGraphicsSceneHoverEvent) """
        pass

    def hoverMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, event: QGraphicsSceneHoverEvent) """
        pass

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: QStyleOption) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertAction(self, before, action): # real signature unknown; restored from __doc__
        """ insertAction(self, before: QAction, action: QAction) """
        pass

    def insertActions(self, before, actions, QAction=None): # real signature unknown; restored from __doc__
        """ insertActions(self, before: QAction, actions: Iterable[QAction]) """
        pass

    def isActiveWindow(self): # real signature unknown; restored from __doc__
        """ isActiveWindow(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, change, value): # real signature unknown; restored from __doc__
        """ itemChange(self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any """
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> QGraphicsLayout """
        return QGraphicsLayout

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> Qt.LayoutDirection """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, event): # real signature unknown; restored from __doc__
        """ moveEvent(self, event: QGraphicsSceneMoveEvent) """
        pass

    def paint(self, painter, option, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: typing.Optional[QWidget] = None) """
        pass

    def paintWindowFrame(self, painter, option, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paintWindowFrame(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: typing.Optional[QWidget] = None) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> QPalette """
        pass

    def polishEvent(self): # real signature unknown; restored from __doc__
        """ polishEvent(self) """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRectF """
        pass

    def releaseShortcut(self, id): # real signature unknown; restored from __doc__
        """ releaseShortcut(self, id: int) """
        pass

    def removeAction(self, action): # real signature unknown; restored from __doc__
        """ removeAction(self, action: QAction) """
        pass

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, size: QSizeF)
        resize(self, w: float, h: float)
        """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: QGraphicsSceneResizeEvent) """
        pass

    def sceneEvent(self, event): # real signature unknown; restored from __doc__
        """ sceneEvent(self, event: QEvent) -> bool """
        return False

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAttribute(self, attribute, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(self, attribute: Qt.WidgetAttribute, on: bool = True) """
        pass

    def setAutoFillBackground(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoFillBackground(self, enabled: bool) """
        pass

    def setContentsMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContentsMargins(self, margins: QMarginsF)
        setContentsMargins(self, left: float, top: float, right: float, bottom: float)
        """
        pass

    def setFocusPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setFocusPolicy(self, policy: Qt.FocusPolicy) """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: QFont) """
        pass

    def setGeometry(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGeometry(self, rect: QRectF)
        setGeometry(self, ax: float, ay: float, aw: float, ah: float)
        """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setLayout(self, layout): # real signature unknown; restored from __doc__
        """ setLayout(self, layout: QGraphicsLayout) """
        pass

    def setLayoutDirection(self, direction): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, direction: Qt.LayoutDirection) """
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setPalette(self, palette): # real signature unknown; restored from __doc__
        """ setPalette(self, palette: QPalette) """
        pass

    def setShortcutAutoRepeat(self, id, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutAutoRepeat(self, id: int, enabled: bool = True) """
        pass

    def setShortcutEnabled(self, id, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutEnabled(self, id: int, enabled: bool = True) """
        pass

    def setStyle(self, style): # real signature unknown; restored from __doc__
        """ setStyle(self, style: QStyle) """
        pass

    def setTabOrder(self, first, second): # real signature unknown; restored from __doc__
        """ setTabOrder(first: QGraphicsWidget, second: QGraphicsWidget) """
        pass

    def setWindowFlags(self, wFlags, Qt_WindowFlags=None, Qt_WindowType=None): # real signature unknown; restored from __doc__
        """ setWindowFlags(self, wFlags: Union[Qt.WindowFlags, Qt.WindowType]) """
        pass

    def setWindowFrameMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setWindowFrameMargins(self, margins: QMarginsF)
        setWindowFrameMargins(self, left: float, top: float, right: float, bottom: float)
        """
        pass

    def setWindowTitle(self, title): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, title: str) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: QShowEvent) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSizeF """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QStyle """
        return QStyle

    def testAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ testAttribute(self, attribute: Qt.WidgetAttribute) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboardEvent(self, event): # real signature unknown; restored from __doc__
        """ ungrabKeyboardEvent(self, event: QEvent) """
        pass

    def ungrabMouseEvent(self, event): # real signature unknown; restored from __doc__
        """ ungrabMouseEvent(self, event: QEvent) """
        pass

    def unsetLayoutDirection(self): # real signature unknown; restored from __doc__
        """ unsetLayoutDirection(self) """
        pass

    def unsetWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ unsetWindowFrameMargins(self) """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ updateGeometry(self) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowFlags(self): # real signature unknown; restored from __doc__
        """ windowFlags(self) -> Qt.WindowFlags """
        pass

    def windowFrameEvent(self, e): # real signature unknown; restored from __doc__
        """ windowFrameEvent(self, e: QEvent) -> bool """
        return False

    def windowFrameGeometry(self): # real signature unknown; restored from __doc__
        """ windowFrameGeometry(self) -> QRectF """
        pass

    def windowFrameRect(self): # real signature unknown; restored from __doc__
        """ windowFrameRect(self) -> QRectF """
        pass

    def windowFrameSectionAt(self, pos, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ windowFrameSectionAt(self, pos: Union[QPointF, QPoint]) -> Qt.WindowFrameSection """
        pass

    def windowTitle(self): # real signature unknown; restored from __doc__
        """ windowTitle(self) -> str """
        return ""

    def windowType(self): # real signature unknown; restored from __doc__
        """ windowType(self) -> Qt.WindowType """
        pass

    def __init__(self, parent, QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


