# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGraphicsScene(__PyQt5_QtCore.QObject):
    """
    QGraphicsScene(parent: typing.Optional[QObject] = None)
    QGraphicsScene(sceneRect: QRectF, parent: typing.Optional[QObject] = None)
    QGraphicsScene(x: float, y: float, width: float, height: float, parent: typing.Optional[QObject] = None)
    """
    def activePanel(self): # real signature unknown; restored from __doc__
        """ activePanel(self) -> QGraphicsItem """
        return QGraphicsItem

    def activeWindow(self): # real signature unknown; restored from __doc__
        """ activeWindow(self) -> QGraphicsWidget """
        return QGraphicsWidget

    def addEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addEllipse(self, rect: QRectF, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsEllipseItem
        addEllipse(self, x: float, y: float, w: float, h: float, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsEllipseItem
        """
        pass

    def addItem(self, item): # real signature unknown; restored from __doc__
        """ addItem(self, item: QGraphicsItem) """
        pass

    def addLine(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addLine(self, line: QLineF, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen()) -> QGraphicsLineItem
        addLine(self, x1: float, y1: float, x2: float, y2: float, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen()) -> QGraphicsLineItem
        """
        pass

    def addPath(self, path, pen, QPen=None, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addPath(self, path: QPainterPath, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsPathItem """
        pass

    def addPixmap(self, pixmap): # real signature unknown; restored from __doc__
        """ addPixmap(self, pixmap: QPixmap) -> QGraphicsPixmapItem """
        return QGraphicsPixmapItem

    def addPolygon(self, polygon, pen, QPen=None, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addPolygon(self, polygon: QPolygonF, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsPolygonItem """
        pass

    def addRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addRect(self, rect: QRectF, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsRectItem
        addRect(self, x: float, y: float, w: float, h: float, pen: Union[QPen, QColor, Qt.GlobalColor, QGradient] = QPen(), brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = QBrush()) -> QGraphicsRectItem
        """
        pass

    def addSimpleText(self, text, font=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addSimpleText(self, text: str, font: QFont = QFont()) -> QGraphicsSimpleTextItem """
        pass

    def addText(self, text, font=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addText(self, text: str, font: QFont = QFont()) -> QGraphicsTextItem """
        pass

    def addWidget(self, widget, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addWidget(self, widget: QWidget, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> QGraphicsProxyWidget """
        pass

    def advance(self): # real signature unknown; restored from __doc__
        """ advance(self) """
        pass

    def backgroundBrush(self): # real signature unknown; restored from __doc__
        """ backgroundBrush(self) -> QBrush """
        pass

    def bspTreeDepth(self): # real signature unknown; restored from __doc__
        """ bspTreeDepth(self) -> int """
        return 0

    def changed(self, *args, **kwargs): # real signature unknown
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

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ clearFocus(self) """
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) """
        pass

    def collidingItems(self, item, mode=None): # real signature unknown; restored from __doc__
        """ collidingItems(self, item: QGraphicsItem, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> List[QGraphicsItem] """
        return []

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent) """
        pass

    def createItemGroup(self, items, QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ createItemGroup(self, items: Iterable[QGraphicsItem]) -> QGraphicsItemGroup """
        return QGraphicsItemGroup

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroyItemGroup(self, group): # real signature unknown; restored from __doc__
        """ destroyItemGroup(self, group: QGraphicsItemGroup) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, event): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, event: QGraphicsSceneDragDropEvent) """
        pass

    def dragLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, event: QGraphicsSceneDragDropEvent) """
        pass

    def dragMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, event: QGraphicsSceneDragDropEvent) """
        pass

    def drawBackground(self, painter, rect): # real signature unknown; restored from __doc__
        """ drawBackground(self, painter: QPainter, rect: QRectF) """
        pass

    def drawForeground(self, painter, rect): # real signature unknown; restored from __doc__
        """ drawForeground(self, painter: QPainter, rect: QRectF) """
        pass

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: QGraphicsSceneDragDropEvent) """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: QEvent) -> bool """
        return False

    def eventFilter(self, watched, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, watched: QObject, event: QEvent) -> bool """
        return False

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: QFocusEvent) """
        pass

    def focusItem(self): # real signature unknown; restored from __doc__
        """ focusItem(self) -> QGraphicsItem """
        return QGraphicsItem

    def focusItemChanged(self, *args, **kwargs): # real signature unknown
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

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOnTouch(self): # real signature unknown; restored from __doc__
        """ focusOnTouch(self) -> bool """
        return False

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: QFocusEvent) """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        pass

    def foregroundBrush(self): # real signature unknown; restored from __doc__
        """ foregroundBrush(self) -> QBrush """
        pass

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def helpEvent(self, event): # real signature unknown; restored from __doc__
        """ helpEvent(self, event: QGraphicsSceneHelpEvent) """
        pass

    def inputMethodEvent(self, event): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: QInputMethodEvent) """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: Qt.InputMethodQuery) -> Any """
        pass

    def invalidate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        invalidate(self, rect: QRectF = QRectF(), layers: Union[QGraphicsScene.SceneLayers, QGraphicsScene.SceneLayer] = QGraphicsScene.AllLayers)
        invalidate(self, x: float, y: float, w: float, h: float, layers: Union[QGraphicsScene.SceneLayers, QGraphicsScene.SceneLayer] = QGraphicsScene.AllLayers)
        """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, pos: Union[QPointF, QPoint], deviceTransform: QTransform) -> QGraphicsItem
        itemAt(self, x: float, y: float, deviceTransform: QTransform) -> QGraphicsItem
        """
        return QGraphicsItem

    def itemIndexMethod(self): # real signature unknown; restored from __doc__
        """ itemIndexMethod(self) -> QGraphicsScene.ItemIndexMethod """
        pass

    def items(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        items(self, order: Qt.SortOrder = Qt.DescendingOrder) -> List[QGraphicsItem]
        items(self, pos: Union[QPointF, QPoint], mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, order: Qt.SortOrder = Qt.DescendingOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        items(self, rect: QRectF, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, order: Qt.SortOrder = Qt.DescendingOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        items(self, polygon: QPolygonF, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, order: Qt.SortOrder = Qt.DescendingOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        items(self, path: QPainterPath, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, order: Qt.SortOrder = Qt.DescendingOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        items(self, x: float, y: float, w: float, h: float, mode: Qt.ItemSelectionMode, order: Qt.SortOrder, deviceTransform: QTransform = QTransform()) -> List[QGraphicsItem]
        """
        return []

    def itemsBoundingRect(self): # real signature unknown; restored from __doc__
        """ itemsBoundingRect(self) -> QRectF """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: QKeyEvent) """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: QKeyEvent) """
        pass

    def minimumRenderSize(self): # real signature unknown; restored from __doc__
        """ minimumRenderSize(self) -> float """
        return 0.0

    def mouseDoubleClickEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) """
        pass

    def mouseGrabberItem(self): # real signature unknown; restored from __doc__
        """ mouseGrabberItem(self) -> QGraphicsItem """
        return QGraphicsItem

    def mouseMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) """
        pass

    def mousePressEvent(self, event): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: QGraphicsSceneMouseEvent) """
        pass

    def mouseReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> QPalette """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeItem(self, item): # real signature unknown; restored from __doc__
        """ removeItem(self, item: QGraphicsItem) """
        pass

    def render(self, painter, target=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ render(self, painter: QPainter, target: QRectF = QRectF(), source: QRectF = QRectF(), mode: Qt.AspectRatioMode = Qt.KeepAspectRatio) """
        pass

    def sceneRect(self): # real signature unknown; restored from __doc__
        """ sceneRect(self) -> QRectF """
        pass

    def sceneRectChanged(self, *args, **kwargs): # real signature unknown
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

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> List[QGraphicsItem] """
        return []

    def selectionArea(self): # real signature unknown; restored from __doc__
        """ selectionArea(self) -> QPainterPath """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sendEvent(self, item, event): # real signature unknown; restored from __doc__
        """ sendEvent(self, item: QGraphicsItem, event: QEvent) -> bool """
        return False

    def setActivePanel(self, item): # real signature unknown; restored from __doc__
        """ setActivePanel(self, item: QGraphicsItem) """
        pass

    def setActiveWindow(self, widget): # real signature unknown; restored from __doc__
        """ setActiveWindow(self, widget: QGraphicsWidget) """
        pass

    def setBackgroundBrush(self, brush, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackgroundBrush(self, brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setBspTreeDepth(self, depth): # real signature unknown; restored from __doc__
        """ setBspTreeDepth(self, depth: int) """
        pass

    def setFocus(self, focusReason=None): # real signature unknown; restored from __doc__
        """ setFocus(self, focusReason: Qt.FocusReason = Qt.OtherFocusReason) """
        pass

    def setFocusItem(self, item, focusReason=None): # real signature unknown; restored from __doc__
        """ setFocusItem(self, item: QGraphicsItem, focusReason: Qt.FocusReason = Qt.OtherFocusReason) """
        pass

    def setFocusOnTouch(self, enabled): # real signature unknown; restored from __doc__
        """ setFocusOnTouch(self, enabled: bool) """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: QFont) """
        pass

    def setForegroundBrush(self, brush, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setForegroundBrush(self, brush: Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setItemIndexMethod(self, method): # real signature unknown; restored from __doc__
        """ setItemIndexMethod(self, method: QGraphicsScene.ItemIndexMethod) """
        pass

    def setMinimumRenderSize(self, minSize): # real signature unknown; restored from __doc__
        """ setMinimumRenderSize(self, minSize: float) """
        pass

    def setPalette(self, palette): # real signature unknown; restored from __doc__
        """ setPalette(self, palette: QPalette) """
        pass

    def setSceneRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSceneRect(self, rect: QRectF)
        setSceneRect(self, x: float, y: float, w: float, h: float)
        """
        pass

    def setSelectionArea(self, path, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSelectionArea(self, path: QPainterPath, deviceTransform: QTransform)
        setSelectionArea(self, path: QPainterPath, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, deviceTransform: QTransform = QTransform())
        setSelectionArea(self, path: QPainterPath, selectionOperation: Qt.ItemSelectionOperation, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape, deviceTransform: QTransform = QTransform())
        """
        pass

    def setStickyFocus(self, enabled): # real signature unknown; restored from __doc__
        """ setStickyFocus(self, enabled: bool) """
        pass

    def setStyle(self, style): # real signature unknown; restored from __doc__
        """ setStyle(self, style: QStyle) """
        pass

    def stickyFocus(self): # real signature unknown; restored from __doc__
        """ stickyFocus(self) -> bool """
        return False

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QStyle """
        return QStyle

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        update(self, rect: QRectF = QRectF())
        update(self, x: float, y: float, w: float, h: float)
        """
        pass

    def views(self): # real signature unknown; restored from __doc__
        """ views(self) -> List[QGraphicsView] """
        return []

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: QGraphicsSceneWheelEvent) """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllLayers = 65535
    BackgroundLayer = 2
    BspTreeIndex = 0
    ForegroundLayer = 4
    ItemLayer = 1
    NoIndex = -1


