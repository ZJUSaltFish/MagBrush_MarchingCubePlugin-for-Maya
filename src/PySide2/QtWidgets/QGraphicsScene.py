# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QGraphicsScene(__PySide2_QtCore.QObject):
    """
    QGraphicsScene(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QGraphicsScene(self, sceneRect: PySide2.QtCore.QRectF, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QGraphicsScene(self, x: float, y: float, width: float, height: float, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def activePanel(self): # real signature unknown; restored from __doc__
        """ activePanel(self) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def activeWindow(self): # real signature unknown; restored from __doc__
        """ activeWindow(self) -> PySide2.QtWidgets.QGraphicsWidget """
        pass

    def addEllipse(self, rect, pen=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addEllipse(self, rect: PySide2.QtCore.QRectF, pen: PySide2.QtGui.QPen = Default(QPen), brush: PySide2.QtGui.QBrush = Default(QBrush)) -> PySide2.QtWidgets.QGraphicsEllipseItem
        addEllipse(self, x: float, y: float, w: float, h: float, pen: PySide2.QtGui.QPen = Default(QPen), brush: PySide2.QtGui.QBrush = Default(QBrush)) -> PySide2.QtWidgets.QGraphicsEllipseItem
        """
        pass

    def addItem(self, item): # real signature unknown; restored from __doc__
        """ addItem(self, item: PySide2.QtWidgets.QGraphicsItem) -> None """
        pass

    def addLine(self, line, pen=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addLine(self, line: PySide2.QtCore.QLineF, pen: PySide2.QtGui.QPen = Default(QPen)) -> PySide2.QtWidgets.QGraphicsLineItem
        addLine(self, x1: float, y1: float, x2: float, y2: float, pen: PySide2.QtGui.QPen = Default(QPen)) -> PySide2.QtWidgets.QGraphicsLineItem
        """
        pass

    def addPath(self, path, pen=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addPath(self, path: PySide2.QtGui.QPainterPath, pen: PySide2.QtGui.QPen = Default(QPen), brush: PySide2.QtGui.QBrush = Default(QBrush)) -> PySide2.QtWidgets.QGraphicsPathItem """
        pass

    def addPixmap(self, pixmap): # real signature unknown; restored from __doc__
        """ addPixmap(self, pixmap: PySide2.QtGui.QPixmap) -> PySide2.QtWidgets.QGraphicsPixmapItem """
        pass

    def addPolygon(self, polygon, pen=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addPolygon(self, polygon: PySide2.QtGui.QPolygonF, pen: PySide2.QtGui.QPen = Default(QPen), brush: PySide2.QtGui.QBrush = Default(QBrush)) -> PySide2.QtWidgets.QGraphicsPolygonItem """
        pass

    def addRect(self, rect, pen=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addRect(self, rect: PySide2.QtCore.QRectF, pen: PySide2.QtGui.QPen = Default(QPen), brush: PySide2.QtGui.QBrush = Default(QBrush)) -> PySide2.QtWidgets.QGraphicsRectItem
        addRect(self, x: float, y: float, w: float, h: float, pen: PySide2.QtGui.QPen = Default(QPen), brush: PySide2.QtGui.QBrush = Default(QBrush)) -> PySide2.QtWidgets.QGraphicsRectItem
        """
        pass

    def addSimpleText(self, text, font=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addSimpleText(self, text: str, font: PySide2.QtGui.QFont = Default(QFont)) -> PySide2.QtWidgets.QGraphicsSimpleTextItem """
        pass

    def addText(self, text, font=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addText(self, text: str, font: PySide2.QtGui.QFont = Default(QFont)) -> PySide2.QtWidgets.QGraphicsTextItem """
        pass

    def addWidget(self, widget, wFlags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addWidget(self, widget: PySide2.QtWidgets.QWidget, wFlags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> PySide2.QtWidgets.QGraphicsProxyWidget """
        pass

    def advance(self): # real signature unknown; restored from __doc__
        """ advance(self) -> None """
        pass

    def backgroundBrush(self): # real signature unknown; restored from __doc__
        """ backgroundBrush(self) -> PySide2.QtGui.QBrush """
        pass

    def bspTreeDepth(self): # real signature unknown; restored from __doc__
        """ bspTreeDepth(self) -> int """
        return 0

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ clearFocus(self) -> None """
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) -> None """
        pass

    def collidingItems(self, item, mode=None): # real signature unknown; restored from __doc__
        """ collidingItems(self, item: PySide2.QtWidgets.QGraphicsItem, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape) -> typing.List[PySide2.QtWidgets.QGraphicsItem] """
        pass

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: PySide2.QtWidgets.QGraphicsSceneContextMenuEvent) -> None """
        pass

    def createItemGroup(self, items, PySide2_QtWidgets_QGraphicsItem=None): # real signature unknown; restored from __doc__
        """ createItemGroup(self, items: typing.Sequence[PySide2.QtWidgets.QGraphicsItem]) -> PySide2.QtWidgets.QGraphicsItemGroup """
        pass

    def destroyItemGroup(self, group): # real signature unknown; restored from __doc__
        """ destroyItemGroup(self, group: PySide2.QtWidgets.QGraphicsItemGroup) -> None """
        pass

    def dragEnterEvent(self, event): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, event: PySide2.QtWidgets.QGraphicsSceneDragDropEvent) -> None """
        pass

    def dragLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneDragDropEvent) -> None """
        pass

    def dragMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneDragDropEvent) -> None """
        pass

    def drawBackground(self, painter, rect): # real signature unknown; restored from __doc__
        """ drawBackground(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def drawForeground(self, painter, rect): # real signature unknown; restored from __doc__
        """ drawForeground(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: PySide2.QtWidgets.QGraphicsSceneDragDropEvent) -> None """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, watched, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, watched: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusItem(self): # real signature unknown; restored from __doc__
        """ focusItem(self) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def focusItemChanged(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOnTouch(self): # real signature unknown; restored from __doc__
        """ focusOnTouch(self) -> bool """
        return False

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def foregroundBrush(self): # real signature unknown; restored from __doc__
        """ foregroundBrush(self) -> PySide2.QtGui.QBrush """
        pass

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def helpEvent(self, event): # real signature unknown; restored from __doc__
        """ helpEvent(self, event: PySide2.QtWidgets.QGraphicsSceneHelpEvent) -> None """
        pass

    def inputMethodEvent(self, event): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: PySide2.QtGui.QInputMethodEvent) -> None """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any """
        pass

    def invalidate(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        invalidate(self, rect: PySide2.QtCore.QRectF = Default(QRectF), layers: PySide2.QtWidgets.QGraphicsScene.SceneLayers = PySide2.QtWidgets.QGraphicsScene.SceneLayer.AllLayers) -> None
        invalidate(self, x: float, y: float, w: float, h: float, layers: PySide2.QtWidgets.QGraphicsScene.SceneLayers = PySide2.QtWidgets.QGraphicsScene.SceneLayer.AllLayers) -> None
        """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSortCacheEnabled(self): # real signature unknown; restored from __doc__
        """ isSortCacheEnabled(self) -> bool """
        return False

    def itemAt(self, pos, deviceTransform): # real signature unknown; restored from __doc__
        """
        itemAt(self, pos: PySide2.QtCore.QPointF, deviceTransform: PySide2.QtGui.QTransform) -> PySide2.QtWidgets.QGraphicsItem
        itemAt(self, x: float, y: float, deviceTransform: PySide2.QtGui.QTransform) -> PySide2.QtWidgets.QGraphicsItem
        """
        pass

    def itemIndexMethod(self): # real signature unknown; restored from __doc__
        """ itemIndexMethod(self) -> PySide2.QtWidgets.QGraphicsScene.ItemIndexMethod """
        pass

    def items(self, order=None): # real signature unknown; restored from __doc__
        """
        items(self, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.DescendingOrder) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, path: PySide2.QtGui.QPainterPath, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.DescendingOrder, deviceTransform: PySide2.QtGui.QTransform = Default(QTransform)) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, polygon: PySide2.QtGui.QPolygonF, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.DescendingOrder, deviceTransform: PySide2.QtGui.QTransform = Default(QTransform)) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, pos: PySide2.QtCore.QPointF, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.DescendingOrder, deviceTransform: PySide2.QtGui.QTransform = Default(QTransform)) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, rect: PySide2.QtCore.QRectF, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.DescendingOrder, deviceTransform: PySide2.QtGui.QTransform = Default(QTransform)) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, x: float, y: float, w: float, h: float, mode: PySide2.QtCore.Qt.ItemSelectionMode, order: PySide2.QtCore.Qt.SortOrder, deviceTransform: PySide2.QtGui.QTransform = Default(QTransform)) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        """
        pass

    def itemsBoundingRect(self): # real signature unknown; restored from __doc__
        """ itemsBoundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def minimumRenderSize(self): # real signature unknown; restored from __doc__
        """ minimumRenderSize(self) -> float """
        return 0.0

    def mouseDoubleClickEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMouseEvent) -> None """
        pass

    def mouseGrabberItem(self): # real signature unknown; restored from __doc__
        """ mouseGrabberItem(self) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def mouseMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMouseEvent) -> None """
        pass

    def mousePressEvent(self, event): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMouseEvent) -> None """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> PySide2.QtGui.QPalette """
        pass

    def removeItem(self, item): # real signature unknown; restored from __doc__
        """ removeItem(self, item: PySide2.QtWidgets.QGraphicsItem) -> None """
        pass

    def render(self, painter, target=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ render(self, painter: PySide2.QtGui.QPainter, target: PySide2.QtCore.QRectF = Default(QRectF), source: PySide2.QtCore.QRectF = Default(QRectF), aspectRatioMode: PySide2.QtCore.Qt.AspectRatioMode = PySide2.QtCore.Qt.AspectRatioMode.KeepAspectRatio) -> None """
        pass

    def sceneRect(self): # real signature unknown; restored from __doc__
        """ sceneRect(self) -> PySide2.QtCore.QRectF """
        pass

    def sceneRectChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> typing.List[PySide2.QtWidgets.QGraphicsItem] """
        pass

    def selectionArea(self): # real signature unknown; restored from __doc__
        """ selectionArea(self) -> PySide2.QtGui.QPainterPath """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sendEvent(self, item, event): # real signature unknown; restored from __doc__
        """ sendEvent(self, item: PySide2.QtWidgets.QGraphicsItem, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def setActivePanel(self, item): # real signature unknown; restored from __doc__
        """ setActivePanel(self, item: PySide2.QtWidgets.QGraphicsItem) -> None """
        pass

    def setActiveWindow(self, widget): # real signature unknown; restored from __doc__
        """ setActiveWindow(self, widget: PySide2.QtWidgets.QGraphicsWidget) -> None """
        pass

    def setBackgroundBrush(self, brush): # real signature unknown; restored from __doc__
        """ setBackgroundBrush(self, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setBspTreeDepth(self, depth): # real signature unknown; restored from __doc__
        """ setBspTreeDepth(self, depth: int) -> None """
        pass

    def setFocus(self, focusReason=None): # real signature unknown; restored from __doc__
        """ setFocus(self, focusReason: PySide2.QtCore.Qt.FocusReason = PySide2.QtCore.Qt.FocusReason.OtherFocusReason) -> None """
        pass

    def setFocusItem(self, item, focusReason=None): # real signature unknown; restored from __doc__
        """ setFocusItem(self, item: PySide2.QtWidgets.QGraphicsItem, focusReason: PySide2.QtCore.Qt.FocusReason = PySide2.QtCore.Qt.FocusReason.OtherFocusReason) -> None """
        pass

    def setFocusOnTouch(self, enabled): # real signature unknown; restored from __doc__
        """ setFocusOnTouch(self, enabled: bool) -> None """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: PySide2.QtGui.QFont) -> None """
        pass

    def setForegroundBrush(self, brush): # real signature unknown; restored from __doc__
        """ setForegroundBrush(self, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setItemIndexMethod(self, method): # real signature unknown; restored from __doc__
        """ setItemIndexMethod(self, method: PySide2.QtWidgets.QGraphicsScene.ItemIndexMethod) -> None """
        pass

    def setMinimumRenderSize(self, minSize): # real signature unknown; restored from __doc__
        """ setMinimumRenderSize(self, minSize: float) -> None """
        pass

    def setPalette(self, palette): # real signature unknown; restored from __doc__
        """ setPalette(self, palette: PySide2.QtGui.QPalette) -> None """
        pass

    def setSceneRect(self, rect): # real signature unknown; restored from __doc__
        """
        setSceneRect(self, rect: PySide2.QtCore.QRectF) -> None
        setSceneRect(self, x: float, y: float, w: float, h: float) -> None
        """
        pass

    def setSelectionArea(self, path, deviceTransform): # real signature unknown; restored from __doc__
        """
        setSelectionArea(self, path: PySide2.QtGui.QPainterPath, deviceTransform: PySide2.QtGui.QTransform) -> None
        setSelectionArea(self, path: PySide2.QtGui.QPainterPath, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape, deviceTransform: PySide2.QtGui.QTransform = Default(QTransform)) -> None
        setSelectionArea(self, path: PySide2.QtGui.QPainterPath, selectionOperation: PySide2.QtCore.Qt.ItemSelectionOperation, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape, deviceTransform: PySide2.QtGui.QTransform = Default(QTransform)) -> None
        """
        pass

    def setSortCacheEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setSortCacheEnabled(self, enabled: bool) -> None """
        pass

    def setStickyFocus(self, enabled): # real signature unknown; restored from __doc__
        """ setStickyFocus(self, enabled: bool) -> None """
        pass

    def setStyle(self, style): # real signature unknown; restored from __doc__
        """ setStyle(self, style: PySide2.QtWidgets.QStyle) -> None """
        pass

    def stickyFocus(self): # real signature unknown; restored from __doc__
        """ stickyFocus(self) -> bool """
        return False

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> PySide2.QtWidgets.QStyle """
        pass

    def update(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        update(self, rect: PySide2.QtCore.QRectF = Default(QRectF)) -> None
        update(self, x: float, y: float, w: float, h: float) -> None
        """
        pass

    def views(self): # real signature unknown; restored from __doc__
        """ views(self) -> typing.List[PySide2.QtWidgets.QGraphicsView] """
        pass

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: PySide2.QtWidgets.QGraphicsSceneWheelEvent) -> None """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AllLayers = PySide2.QtWidgets.QGraphicsScene.SceneLayer.AllLayers
    BackgroundLayer = PySide2.QtWidgets.QGraphicsScene.SceneLayer.BackgroundLayer
    BspTreeIndex = PySide2.QtWidgets.QGraphicsScene.ItemIndexMethod.BspTreeIndex
    ForegroundLayer = PySide2.QtWidgets.QGraphicsScene.SceneLayer.ForegroundLayer
    ItemIndexMethod = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsScene.ItemIndexMethod'>"
    ItemLayer = PySide2.QtWidgets.QGraphicsScene.SceneLayer.ItemLayer
    NoIndex = PySide2.QtWidgets.QGraphicsScene.ItemIndexMethod.NoIndex
    SceneLayer = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsScene.SceneLayer'>"
    SceneLayers = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsScene.SceneLayers'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50797B80>'


