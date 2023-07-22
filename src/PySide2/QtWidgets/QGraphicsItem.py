# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QGraphicsItem(__Shiboken.Object):
    """ QGraphicsItem(self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None """
    def acceptDrops(self): # real signature unknown; restored from __doc__
        """ acceptDrops(self) -> bool """
        return False

    def acceptedMouseButtons(self): # real signature unknown; restored from __doc__
        """ acceptedMouseButtons(self) -> PySide2.QtCore.Qt.MouseButtons """
        pass

    def acceptHoverEvents(self): # real signature unknown; restored from __doc__
        """ acceptHoverEvents(self) -> bool """
        return False

    def acceptTouchEvents(self): # real signature unknown; restored from __doc__
        """ acceptTouchEvents(self) -> bool """
        return False

    def addToIndex(self): # real signature unknown; restored from __doc__
        """ addToIndex(self) -> None """
        pass

    def advance(self, phase): # real signature unknown; restored from __doc__
        """ advance(self, phase: int) -> None """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def boundingRegion(self, itemToDeviceTransform): # real signature unknown; restored from __doc__
        """ boundingRegion(self, itemToDeviceTransform: PySide2.QtGui.QTransform) -> PySide2.QtGui.QRegion """
        pass

    def boundingRegionGranularity(self): # real signature unknown; restored from __doc__
        """ boundingRegionGranularity(self) -> float """
        return 0.0

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ cacheMode(self) -> PySide2.QtWidgets.QGraphicsItem.CacheMode """
        pass

    def childItems(self): # real signature unknown; restored from __doc__
        """ childItems(self) -> typing.List[PySide2.QtWidgets.QGraphicsItem] """
        pass

    def childrenBoundingRect(self): # real signature unknown; restored from __doc__
        """ childrenBoundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def clearFocus(self): # real signature unknown; restored from __doc__
        """ clearFocus(self) -> None """
        pass

    def clipPath(self): # real signature unknown; restored from __doc__
        """ clipPath(self) -> PySide2.QtGui.QPainterPath """
        pass

    def collidesWithItem(self, other, mode=None): # real signature unknown; restored from __doc__
        """ collidesWithItem(self, other: PySide2.QtWidgets.QGraphicsItem, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape) -> bool """
        return False

    def collidesWithPath(self, path, mode=None): # real signature unknown; restored from __doc__
        """ collidesWithPath(self, path: PySide2.QtGui.QPainterPath, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape) -> bool """
        return False

    def collidingItems(self, mode=None): # real signature unknown; restored from __doc__
        """ collidingItems(self, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape) -> typing.List[PySide2.QtWidgets.QGraphicsItem] """
        pass

    def commonAncestorItem(self, other): # real signature unknown; restored from __doc__
        """ commonAncestorItem(self, other: PySide2.QtWidgets.QGraphicsItem) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def contains(self, point): # real signature unknown; restored from __doc__
        """ contains(self, point: PySide2.QtCore.QPointF) -> bool """
        return False

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: PySide2.QtWidgets.QGraphicsSceneContextMenuEvent) -> None """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> PySide2.QtGui.QCursor """
        pass

    def data(self, key): # real signature unknown; restored from __doc__
        """ data(self, key: int) -> typing.Any """
        pass

    def deviceTransform(self, viewportTransform): # real signature unknown; restored from __doc__
        """ deviceTransform(self, viewportTransform: PySide2.QtGui.QTransform) -> PySide2.QtGui.QTransform """
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

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: PySide2.QtWidgets.QGraphicsSceneDragDropEvent) -> None """
        pass

    def effectiveOpacity(self): # real signature unknown; restored from __doc__
        """ effectiveOpacity(self) -> float """
        return 0.0

    def ensureVisible(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        ensureVisible(self, rect: PySide2.QtCore.QRectF = Default(QRectF), xmargin: int = 50, ymargin: int = 50) -> None
        ensureVisible(self, x: float, y: float, w: float, h: float, xmargin: int = 50, ymargin: int = 50) -> None
        """
        pass

    def extension(self, variant): # real signature unknown; restored from __doc__
        """ extension(self, variant: typing.Any) -> typing.Any """
        pass

    def filtersChildEvents(self): # real signature unknown; restored from __doc__
        """ filtersChildEvents(self) -> bool """
        return False

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlags """
        pass

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusItem(self): # real signature unknown; restored from __doc__
        """ focusItem(self) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusProxy(self): # real signature unknown; restored from __doc__
        """ focusProxy(self) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def focusScopeItem(self): # real signature unknown; restored from __doc__
        """ focusScopeItem(self) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def grabKeyboard(self): # real signature unknown; restored from __doc__
        """ grabKeyboard(self) -> None """
        pass

    def grabMouse(self): # real signature unknown; restored from __doc__
        """ grabMouse(self) -> None """
        pass

    def graphicsEffect(self): # real signature unknown; restored from __doc__
        """ graphicsEffect(self) -> PySide2.QtWidgets.QGraphicsEffect """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> PySide2.QtWidgets.QGraphicsItemGroup """
        pass

    def handlesChildEvents(self): # real signature unknown; restored from __doc__
        """ handlesChildEvents(self) -> bool """
        return False

    def hasCursor(self): # real signature unknown; restored from __doc__
        """ hasCursor(self) -> bool """
        return False

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) -> None """
        pass

    def hoverEnterEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverEnterEvent(self, event: PySide2.QtWidgets.QGraphicsSceneHoverEvent) -> None """
        pass

    def hoverLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneHoverEvent) -> None """
        pass

    def hoverMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneHoverEvent) -> None """
        pass

    def inputMethodEvent(self, event): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: PySide2.QtGui.QInputMethodEvent) -> None """
        pass

    def inputMethodHints(self): # real signature unknown; restored from __doc__
        """ inputMethodHints(self) -> PySide2.QtCore.Qt.InputMethodHints """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any """
        pass

    def installSceneEventFilter(self, filterItem): # real signature unknown; restored from __doc__
        """ installSceneEventFilter(self, filterItem: PySide2.QtWidgets.QGraphicsItem) -> None """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isAncestorOf(self, child): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, child: PySide2.QtWidgets.QGraphicsItem) -> bool """
        return False

    def isBlockedByModalPanel(self, blockingPanel, PySide2_QtWidgets_QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isBlockedByModalPanel(self, blockingPanel: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> bool """
        pass

    def isClipped(self): # real signature unknown; restored from __doc__
        """ isClipped(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isObscured(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        isObscured(self, rect: PySide2.QtCore.QRectF = Default(QRectF)) -> bool
        isObscured(self, x: float, y: float, w: float, h: float) -> bool
        """
        pass

    def isObscuredBy(self, item): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, item: PySide2.QtWidgets.QGraphicsItem) -> bool """
        return False

    def isPanel(self): # real signature unknown; restored from __doc__
        """ isPanel(self) -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ isSelected(self) -> bool """
        return False

    def isUnderMouse(self): # real signature unknown; restored from __doc__
        """ isUnderMouse(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def isVisibleTo(self, parent): # real signature unknown; restored from __doc__
        """ isVisibleTo(self, parent: PySide2.QtWidgets.QGraphicsItem) -> bool """
        return False

    def isWidget(self): # real signature unknown; restored from __doc__
        """ isWidget(self) -> bool """
        return False

    def isWindow(self): # real signature unknown; restored from __doc__
        """ isWindow(self) -> bool """
        return False

    def itemChange(self, change, value): # real signature unknown; restored from __doc__
        """ itemChange(self, change: PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange, value: typing.Any) -> typing.Any """
        pass

    def itemTransform(self, other): # real signature unknown; restored from __doc__
        """ itemTransform(self, other: PySide2.QtWidgets.QGraphicsItem) -> typing.Tuple[PySide2.QtGui.QTransform, bool] """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def mapFromItem(self, item, path): # real signature unknown; restored from __doc__
        """
        mapFromItem(self, item: PySide2.QtWidgets.QGraphicsItem, path: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        mapFromItem(self, item: PySide2.QtWidgets.QGraphicsItem, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        mapFromItem(self, item: PySide2.QtWidgets.QGraphicsItem, polygon: PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF
        mapFromItem(self, item: PySide2.QtWidgets.QGraphicsItem, rect: PySide2.QtCore.QRectF) -> PySide2.QtGui.QPolygonF
        mapFromItem(self, item: PySide2.QtWidgets.QGraphicsItem, x: float, y: float) -> PySide2.QtCore.QPointF
        mapFromItem(self, item: PySide2.QtWidgets.QGraphicsItem, x: float, y: float, w: float, h: float) -> PySide2.QtGui.QPolygonF
        """
        pass

    def mapFromParent(self, path): # real signature unknown; restored from __doc__
        """
        mapFromParent(self, path: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        mapFromParent(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        mapFromParent(self, polygon: PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF
        mapFromParent(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtGui.QPolygonF
        mapFromParent(self, x: float, y: float) -> PySide2.QtCore.QPointF
        mapFromParent(self, x: float, y: float, w: float, h: float) -> PySide2.QtGui.QPolygonF
        """
        pass

    def mapFromScene(self, path): # real signature unknown; restored from __doc__
        """
        mapFromScene(self, path: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        mapFromScene(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        mapFromScene(self, polygon: PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF
        mapFromScene(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtGui.QPolygonF
        mapFromScene(self, x: float, y: float) -> PySide2.QtCore.QPointF
        mapFromScene(self, x: float, y: float, w: float, h: float) -> PySide2.QtGui.QPolygonF
        """
        pass

    def mapRectFromItem(self, item, rect): # real signature unknown; restored from __doc__
        """
        mapRectFromItem(self, item: PySide2.QtWidgets.QGraphicsItem, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        mapRectFromItem(self, item: PySide2.QtWidgets.QGraphicsItem, x: float, y: float, w: float, h: float) -> PySide2.QtCore.QRectF
        """
        pass

    def mapRectFromParent(self, rect): # real signature unknown; restored from __doc__
        """
        mapRectFromParent(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        mapRectFromParent(self, x: float, y: float, w: float, h: float) -> PySide2.QtCore.QRectF
        """
        pass

    def mapRectFromScene(self, rect): # real signature unknown; restored from __doc__
        """
        mapRectFromScene(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        mapRectFromScene(self, x: float, y: float, w: float, h: float) -> PySide2.QtCore.QRectF
        """
        pass

    def mapRectToItem(self, item, rect): # real signature unknown; restored from __doc__
        """
        mapRectToItem(self, item: PySide2.QtWidgets.QGraphicsItem, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        mapRectToItem(self, item: PySide2.QtWidgets.QGraphicsItem, x: float, y: float, w: float, h: float) -> PySide2.QtCore.QRectF
        """
        pass

    def mapRectToParent(self, rect): # real signature unknown; restored from __doc__
        """
        mapRectToParent(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        mapRectToParent(self, x: float, y: float, w: float, h: float) -> PySide2.QtCore.QRectF
        """
        pass

    def mapRectToScene(self, rect): # real signature unknown; restored from __doc__
        """
        mapRectToScene(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF
        mapRectToScene(self, x: float, y: float, w: float, h: float) -> PySide2.QtCore.QRectF
        """
        pass

    def mapToItem(self, item, path): # real signature unknown; restored from __doc__
        """
        mapToItem(self, item: PySide2.QtWidgets.QGraphicsItem, path: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        mapToItem(self, item: PySide2.QtWidgets.QGraphicsItem, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        mapToItem(self, item: PySide2.QtWidgets.QGraphicsItem, polygon: PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF
        mapToItem(self, item: PySide2.QtWidgets.QGraphicsItem, rect: PySide2.QtCore.QRectF) -> PySide2.QtGui.QPolygonF
        mapToItem(self, item: PySide2.QtWidgets.QGraphicsItem, x: float, y: float) -> PySide2.QtCore.QPointF
        mapToItem(self, item: PySide2.QtWidgets.QGraphicsItem, x: float, y: float, w: float, h: float) -> PySide2.QtGui.QPolygonF
        """
        pass

    def mapToParent(self, path): # real signature unknown; restored from __doc__
        """
        mapToParent(self, path: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        mapToParent(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        mapToParent(self, polygon: PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF
        mapToParent(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtGui.QPolygonF
        mapToParent(self, x: float, y: float) -> PySide2.QtCore.QPointF
        mapToParent(self, x: float, y: float, w: float, h: float) -> PySide2.QtGui.QPolygonF
        """
        pass

    def mapToScene(self, path): # real signature unknown; restored from __doc__
        """
        mapToScene(self, path: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        mapToScene(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF
        mapToScene(self, polygon: PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygonF
        mapToScene(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtGui.QPolygonF
        mapToScene(self, x: float, y: float) -> PySide2.QtCore.QPointF
        mapToScene(self, x: float, y: float, w: float, h: float) -> PySide2.QtGui.QPolygonF
        """
        pass

    def matrix(self): # real signature unknown; restored from __doc__
        """ matrix(self) -> PySide2.QtGui.QMatrix """
        pass

    def mouseDoubleClickEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMouseEvent) -> None """
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

    def moveBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ moveBy(self, dx: float, dy: float) -> None """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> PySide2.QtGui.QPainterPath """
        pass

    def paint(self, painter, option, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def panel(self): # real signature unknown; restored from __doc__
        """ panel(self) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def panelModality(self): # real signature unknown; restored from __doc__
        """ panelModality(self) -> PySide2.QtWidgets.QGraphicsItem.PanelModality """
        pass

    def parentItem(self): # real signature unknown; restored from __doc__
        """ parentItem(self) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def parentObject(self): # real signature unknown; restored from __doc__
        """ parentObject(self) -> PySide2.QtWidgets.QGraphicsObject """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> PySide2.QtWidgets.QGraphicsWidget """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> PySide2.QtCore.QPointF """
        pass

    def prepareGeometryChange(self): # real signature unknown; restored from __doc__
        """ prepareGeometryChange(self) -> None """
        pass

    def removeFromIndex(self): # real signature unknown; restored from __doc__
        """ removeFromIndex(self) -> None """
        pass

    def removeSceneEventFilter(self, filterItem): # real signature unknown; restored from __doc__
        """ removeSceneEventFilter(self, filterItem: PySide2.QtWidgets.QGraphicsItem) -> None """
        pass

    def resetMatrix(self): # real signature unknown; restored from __doc__
        """ resetMatrix(self) -> None """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ resetTransform(self) -> None """
        pass

    def rotation(self): # real signature unknown; restored from __doc__
        """ rotation(self) -> float """
        return 0.0

    def scale(self): # real signature unknown; restored from __doc__
        """ scale(self) -> float """
        return 0.0

    def scene(self): # real signature unknown; restored from __doc__
        """ scene(self) -> PySide2.QtWidgets.QGraphicsScene """
        pass

    def sceneBoundingRect(self): # real signature unknown; restored from __doc__
        """ sceneBoundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def sceneEvent(self, event): # real signature unknown; restored from __doc__
        """ sceneEvent(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def sceneEventFilter(self, watched, event): # real signature unknown; restored from __doc__
        """ sceneEventFilter(self, watched: PySide2.QtWidgets.QGraphicsItem, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def sceneMatrix(self): # real signature unknown; restored from __doc__
        """ sceneMatrix(self) -> PySide2.QtGui.QMatrix """
        pass

    def scenePos(self): # real signature unknown; restored from __doc__
        """ scenePos(self) -> PySide2.QtCore.QPointF """
        pass

    def sceneTransform(self): # real signature unknown; restored from __doc__
        """ sceneTransform(self) -> PySide2.QtGui.QTransform """
        pass

    def scroll(self, dx, dy, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ scroll(self, dx: float, dy: float, rect: PySide2.QtCore.QRectF = Default(QRectF)) -> None """
        pass

    def setAcceptDrops(self, on): # real signature unknown; restored from __doc__
        """ setAcceptDrops(self, on: bool) -> None """
        pass

    def setAcceptedMouseButtons(self, buttons): # real signature unknown; restored from __doc__
        """ setAcceptedMouseButtons(self, buttons: PySide2.QtCore.Qt.MouseButtons) -> None """
        pass

    def setAcceptHoverEvents(self, enabled): # real signature unknown; restored from __doc__
        """ setAcceptHoverEvents(self, enabled: bool) -> None """
        pass

    def setAcceptTouchEvents(self, enabled): # real signature unknown; restored from __doc__
        """ setAcceptTouchEvents(self, enabled: bool) -> None """
        pass

    def setActive(self, active): # real signature unknown; restored from __doc__
        """ setActive(self, active: bool) -> None """
        pass

    def setBoundingRegionGranularity(self, granularity): # real signature unknown; restored from __doc__
        """ setBoundingRegionGranularity(self, granularity: float) -> None """
        pass

    def setCacheMode(self, mode, cacheSize=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCacheMode(self, mode: PySide2.QtWidgets.QGraphicsItem.CacheMode, cacheSize: PySide2.QtCore.QSize = Default(QSize)) -> None """
        pass

    def setCursor(self, cursor): # real signature unknown; restored from __doc__
        """ setCursor(self, cursor: PySide2.QtGui.QCursor) -> None """
        pass

    def setData(self, key, value): # real signature unknown; restored from __doc__
        """ setData(self, key: int, value: typing.Any) -> None """
        pass

    def setEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setEnabled(self, enabled: bool) -> None """
        pass

    def setFiltersChildEvents(self, enabled): # real signature unknown; restored from __doc__
        """ setFiltersChildEvents(self, enabled: bool) -> None """
        pass

    def setFlag(self, flag, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, flag: PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag, enabled: bool = True) -> None """
        pass

    def setFlags(self, flags): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlags) -> None """
        pass

    def setFocus(self, focusReason=None): # real signature unknown; restored from __doc__
        """ setFocus(self, focusReason: PySide2.QtCore.Qt.FocusReason = PySide2.QtCore.Qt.FocusReason.OtherFocusReason) -> None """
        pass

    def setFocusProxy(self, item): # real signature unknown; restored from __doc__
        """ setFocusProxy(self, item: PySide2.QtWidgets.QGraphicsItem) -> None """
        pass

    def setGraphicsEffect(self, effect): # real signature unknown; restored from __doc__
        """ setGraphicsEffect(self, effect: PySide2.QtWidgets.QGraphicsEffect) -> None """
        pass

    def setGroup(self, group): # real signature unknown; restored from __doc__
        """ setGroup(self, group: PySide2.QtWidgets.QGraphicsItemGroup) -> None """
        pass

    def setHandlesChildEvents(self, enabled): # real signature unknown; restored from __doc__
        """ setHandlesChildEvents(self, enabled: bool) -> None """
        pass

    def setInputMethodHints(self, hints): # real signature unknown; restored from __doc__
        """ setInputMethodHints(self, hints: PySide2.QtCore.Qt.InputMethodHints) -> None """
        pass

    def setMatrix(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setMatrix(self, matrix: PySide2.QtGui.QMatrix, combine: bool = False) -> None """
        pass

    def setOpacity(self, opacity): # real signature unknown; restored from __doc__
        """ setOpacity(self, opacity: float) -> None """
        pass

    def setPanelModality(self, panelModality): # real signature unknown; restored from __doc__
        """ setPanelModality(self, panelModality: PySide2.QtWidgets.QGraphicsItem.PanelModality) -> None """
        pass

    def setParentItem(self, parent): # real signature unknown; restored from __doc__
        """ setParentItem(self, parent: PySide2.QtWidgets.QGraphicsItem) -> None """
        pass

    def setPos(self, pos): # real signature unknown; restored from __doc__
        """
        setPos(self, pos: PySide2.QtCore.QPointF) -> None
        setPos(self, x: float, y: float) -> None
        """
        pass

    def setRotation(self, angle): # real signature unknown; restored from __doc__
        """ setRotation(self, angle: float) -> None """
        pass

    def setScale(self, scale): # real signature unknown; restored from __doc__
        """ setScale(self, scale: float) -> None """
        pass

    def setSelected(self, selected): # real signature unknown; restored from __doc__
        """ setSelected(self, selected: bool) -> None """
        pass

    def setToolTip(self, toolTip): # real signature unknown; restored from __doc__
        """ setToolTip(self, toolTip: str) -> None """
        pass

    def setTransform(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setTransform(self, matrix: PySide2.QtGui.QTransform, combine: bool = False) -> None """
        pass

    def setTransformations(self, transformations, PySide2_QtWidgets_QGraphicsTransform=None): # real signature unknown; restored from __doc__
        """ setTransformations(self, transformations: typing.Sequence[PySide2.QtWidgets.QGraphicsTransform]) -> None """
        pass

    def setTransformOriginPoint(self, ax, ay): # real signature unknown; restored from __doc__
        """
        setTransformOriginPoint(self, ax: float, ay: float) -> None
        setTransformOriginPoint(self, origin: PySide2.QtCore.QPointF) -> None
        """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def setX(self, x): # real signature unknown; restored from __doc__
        """ setX(self, x: float) -> None """
        pass

    def setY(self, y): # real signature unknown; restored from __doc__
        """ setY(self, y: float) -> None """
        pass

    def setZValue(self, z): # real signature unknown; restored from __doc__
        """ setZValue(self, z: float) -> None """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> PySide2.QtGui.QPainterPath """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) -> None """
        pass

    def stackBefore(self, sibling): # real signature unknown; restored from __doc__
        """ stackBefore(self, sibling: PySide2.QtWidgets.QGraphicsItem) -> None """
        pass

    def toGraphicsObject(self): # real signature unknown; restored from __doc__
        """ toGraphicsObject(self) -> PySide2.QtWidgets.QGraphicsObject """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def topLevelItem(self): # real signature unknown; restored from __doc__
        """ topLevelItem(self) -> PySide2.QtWidgets.QGraphicsItem """
        pass

    def topLevelWidget(self): # real signature unknown; restored from __doc__
        """ topLevelWidget(self) -> PySide2.QtWidgets.QGraphicsWidget """
        pass

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> PySide2.QtGui.QTransform """
        pass

    def transformations(self): # real signature unknown; restored from __doc__
        """ transformations(self) -> typing.List[PySide2.QtWidgets.QGraphicsTransform] """
        pass

    def transformOriginPoint(self): # real signature unknown; restored from __doc__
        """ transformOriginPoint(self) -> PySide2.QtCore.QPointF """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboard(self): # real signature unknown; restored from __doc__
        """ ungrabKeyboard(self) -> None """
        pass

    def ungrabMouse(self): # real signature unknown; restored from __doc__
        """ ungrabMouse(self) -> None """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) -> None """
        pass

    def update(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        update(self, rect: PySide2.QtCore.QRectF = Default(QRectF)) -> None
        update(self, x: float, y: float, width: float, height: float) -> None
        """
        pass

    def updateMicroFocus(self): # real signature unknown; restored from __doc__
        """ updateMicroFocus(self) -> None """
        pass

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: PySide2.QtWidgets.QGraphicsSceneWheelEvent) -> None """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> PySide2.QtWidgets.QGraphicsWidget """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def zValue(self): # real signature unknown; restored from __doc__
        """ zValue(self) -> float """
        return 0.0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    CacheMode = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsItem.CacheMode'>"
    DeviceCoordinateCache = PySide2.QtWidgets.QGraphicsItem.CacheMode.DeviceCoordinateCache
    Extension = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsItem.Extension'>"
    GraphicsItemChange = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange'>"
    GraphicsItemFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag'>"
    GraphicsItemFlags = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlags'>"
    ItemAcceptsInputMethod = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemAcceptsInputMethod
    ItemChildAddedChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemChildAddedChange
    ItemChildRemovedChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemChildRemovedChange
    ItemClipsChildrenToShape = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemClipsChildrenToShape
    ItemClipsToShape = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemClipsToShape
    ItemContainsChildrenInShape = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemContainsChildrenInShape
    ItemCoordinateCache = PySide2.QtWidgets.QGraphicsItem.CacheMode.ItemCoordinateCache
    ItemCursorChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemCursorChange
    ItemCursorHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemCursorHasChanged
    ItemDoesntPropagateOpacityToChildren = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemDoesntPropagateOpacityToChildren
    ItemEnabledChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemEnabledChange
    ItemEnabledHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemEnabledHasChanged
    ItemFlagsChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemFlagsChange
    ItemFlagsHaveChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemFlagsHaveChanged
    ItemHasNoContents = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemHasNoContents
    ItemIgnoresParentOpacity = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIgnoresParentOpacity
    ItemIgnoresTransformations = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIgnoresTransformations
    ItemIsFocusable = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable
    ItemIsFocusScope = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusScope
    ItemIsMovable = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable
    ItemIsPanel = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsPanel
    ItemIsSelectable = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
    ItemMatrixChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemMatrixChange
    ItemNegativeZStacksBehindParent = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemNegativeZStacksBehindParent
    ItemOpacityChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemOpacityChange
    ItemOpacityHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemOpacityHasChanged
    ItemParentChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemParentChange
    ItemParentHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemParentHasChanged
    ItemPositionChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionChange
    ItemPositionHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged
    ItemRotationChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemRotationChange
    ItemRotationHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemRotationHasChanged
    ItemScaleChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemScaleChange
    ItemScaleHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemScaleHasChanged
    ItemSceneChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemSceneChange
    ItemSceneHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemSceneHasChanged
    ItemScenePositionHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemScenePositionHasChanged
    ItemSelectedChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemSelectedChange
    ItemSelectedHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemSelectedHasChanged
    ItemSendsGeometryChanges = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges
    ItemSendsScenePositionChanges = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges
    ItemStacksBehindParent = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemStacksBehindParent
    ItemStopsClickFocusPropagation = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemStopsClickFocusPropagation
    ItemStopsFocusHandling = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemStopsFocusHandling
    ItemToolTipChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemToolTipChange
    ItemToolTipHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemToolTipHasChanged
    ItemTransformChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemTransformChange
    ItemTransformHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemTransformHasChanged
    ItemTransformOriginPointChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemTransformOriginPointChange
    ItemTransformOriginPointHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemTransformOriginPointHasChanged
    ItemUsesExtendedStyleOption = PySide2.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemUsesExtendedStyleOption
    ItemVisibleChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemVisibleChange
    ItemVisibleHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemVisibleHasChanged
    ItemZValueChange = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemZValueChange
    ItemZValueHasChanged = PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemZValueHasChanged
    NoCache = PySide2.QtWidgets.QGraphicsItem.CacheMode.NoCache
    NonModal = PySide2.QtWidgets.QGraphicsItem.PanelModality.NonModal
    PanelModal = PySide2.QtWidgets.QGraphicsItem.PanelModality.PanelModal
    PanelModality = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsItem.PanelModality'>"
    SceneModal = PySide2.QtWidgets.QGraphicsItem.PanelModality.SceneModal
    UserExtension = PySide2.QtWidgets.QGraphicsItem.Extension.UserExtension
    UserType = 65536


