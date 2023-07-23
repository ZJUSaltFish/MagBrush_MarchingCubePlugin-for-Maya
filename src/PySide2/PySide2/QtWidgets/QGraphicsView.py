# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractScrollArea import QAbstractScrollArea

class QGraphicsView(QAbstractScrollArea):
    """
    QGraphicsView(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QGraphicsView(self, scene: PySide2.QtWidgets.QGraphicsScene, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def backgroundBrush(self): # real signature unknown; restored from __doc__
        """ backgroundBrush(self) -> PySide2.QtGui.QBrush """
        pass

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ cacheMode(self) -> PySide2.QtWidgets.QGraphicsView.CacheMode """
        pass

    def centerOn(self, item): # real signature unknown; restored from __doc__
        """
        centerOn(self, item: PySide2.QtWidgets.QGraphicsItem) -> None
        centerOn(self, pos: PySide2.QtCore.QPointF) -> None
        centerOn(self, x: float, y: float) -> None
        """
        pass

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def dragEnterEvent(self, event): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None """
        pass

    def dragLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, event: PySide2.QtGui.QDragLeaveEvent) -> None """
        pass

    def dragMode(self): # real signature unknown; restored from __doc__
        """ dragMode(self) -> PySide2.QtWidgets.QGraphicsView.DragMode """
        pass

    def dragMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, event: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def drawBackground(self, painter, rect): # real signature unknown; restored from __doc__
        """ drawBackground(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def drawForeground(self, painter, rect): # real signature unknown; restored from __doc__
        """ drawForeground(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def drawItems(self, painter, numItems, items, PySide2_QtWidgets_QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawItems(self, painter: PySide2.QtGui.QPainter, numItems: int, items: typing.Sequence[PySide2.QtWidgets.QGraphicsItem], options: typing.Sequence[PySide2.QtWidgets.QStyleOptionGraphicsItem]) -> None """
        pass

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None """
        pass

    def ensureVisible(self, item, xmargin=50, ymargin=50): # real signature unknown; restored from __doc__
        """
        ensureVisible(self, item: PySide2.QtWidgets.QGraphicsItem, xmargin: int = 50, ymargin: int = 50) -> None
        ensureVisible(self, rect: PySide2.QtCore.QRectF, xmargin: int = 50, ymargin: int = 50) -> None
        ensureVisible(self, x: float, y: float, w: float, h: float, xmargin: int = 50, ymargin: int = 50) -> None
        """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def fitInView(self, item, aspectRadioMode=None): # real signature unknown; restored from __doc__
        """
        fitInView(self, item: PySide2.QtWidgets.QGraphicsItem, aspectRadioMode: PySide2.QtCore.Qt.AspectRatioMode = PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio) -> None
        fitInView(self, rect: PySide2.QtCore.QRectF, aspectRadioMode: PySide2.QtCore.Qt.AspectRatioMode = PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio) -> None
        fitInView(self, x: float, y: float, w: float, h: float, aspectRadioMode: PySide2.QtCore.Qt.AspectRatioMode = PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio) -> None
        """
        pass

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def foregroundBrush(self): # real signature unknown; restored from __doc__
        """ foregroundBrush(self) -> PySide2.QtGui.QBrush """
        pass

    def inputMethodEvent(self, event): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: PySide2.QtGui.QInputMethodEvent) -> None """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any """
        pass

    def invalidateScene(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ invalidateScene(self, rect: PySide2.QtCore.QRectF = Default(QRectF), layers: PySide2.QtWidgets.QGraphicsScene.SceneLayers = PySide2.QtWidgets.QGraphicsScene.SceneLayer.AllLayers) -> None """
        pass

    def isInteractive(self): # real signature unknown; restored from __doc__
        """ isInteractive(self) -> bool """
        return False

    def isTransformed(self): # real signature unknown; restored from __doc__
        """ isTransformed(self) -> bool """
        return False

    def itemAt(self, pos): # real signature unknown; restored from __doc__
        """
        itemAt(self, pos: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QGraphicsItem
        itemAt(self, x: int, y: int) -> PySide2.QtWidgets.QGraphicsItem
        """
        pass

    def items(self): # real signature unknown; restored from __doc__
        """
        items(self) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, path: PySide2.QtGui.QPainterPath, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, polygon: PySide2.QtGui.QPolygon, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, pos: PySide2.QtCore.QPoint) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, rect: PySide2.QtCore.QRect, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, x: int, y: int) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        items(self, x: int, y: int, w: int, h: int, mode: PySide2.QtCore.Qt.ItemSelectionMode = PySide2.QtCore.Qt.ItemSelectionMode.IntersectsItemShape) -> typing.List[PySide2.QtWidgets.QGraphicsItem]
        """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def mapFromScene(self, path): # real signature unknown; restored from __doc__
        """
        mapFromScene(self, path: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        mapFromScene(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPoint
        mapFromScene(self, polygon: PySide2.QtGui.QPolygonF) -> PySide2.QtGui.QPolygon
        mapFromScene(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtGui.QPolygon
        mapFromScene(self, x: float, y: float) -> PySide2.QtCore.QPoint
        mapFromScene(self, x: float, y: float, w: float, h: float) -> PySide2.QtGui.QPolygon
        """
        pass

    def mapToScene(self, path): # real signature unknown; restored from __doc__
        """
        mapToScene(self, path: PySide2.QtGui.QPainterPath) -> PySide2.QtGui.QPainterPath
        mapToScene(self, point: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPointF
        mapToScene(self, polygon: PySide2.QtGui.QPolygon) -> PySide2.QtGui.QPolygonF
        mapToScene(self, rect: PySide2.QtCore.QRect) -> PySide2.QtGui.QPolygonF
        mapToScene(self, x: int, y: int) -> PySide2.QtCore.QPointF
        mapToScene(self, x: int, y: int, w: int, h: int) -> PySide2.QtGui.QPolygonF
        """
        pass

    def matrix(self): # real signature unknown; restored from __doc__
        """ matrix(self) -> PySide2.QtGui.QMatrix """
        pass

    def mouseDoubleClickEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, event: PySide2.QtGui.QMouseEvent) -> None """
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

    def optimizationFlags(self): # real signature unknown; restored from __doc__
        """ optimizationFlags(self) -> PySide2.QtWidgets.QGraphicsView.OptimizationFlags """
        pass

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def render(self, painter, target=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        render(self, painter: PySide2.QtGui.QPainter, target: PySide2.QtCore.QRectF = Default(QRectF), source: PySide2.QtCore.QRect = Default(QRect), aspectRatioMode: PySide2.QtCore.Qt.AspectRatioMode = PySide2.QtCore.Qt.AspectRatioMode.KeepAspectRatio) -> None
        render(self, target: PySide2.QtGui.QPaintDevice, targetOffset: PySide2.QtCore.QPoint = Default(QPoint), sourceRegion: PySide2.QtGui.QRegion = Default(QRegion), renderFlags: PySide2.QtWidgets.QWidget.RenderFlags = Instance(QWidget.RenderFlags(QWidget.DrawWindowBackground | QWidget.DrawChildren))) -> None
        """
        pass

    def renderHints(self): # real signature unknown; restored from __doc__
        """ renderHints(self) -> PySide2.QtGui.QPainter.RenderHints """
        pass

    def resetCachedContent(self): # real signature unknown; restored from __doc__
        """ resetCachedContent(self) -> None """
        pass

    def resetMatrix(self): # real signature unknown; restored from __doc__
        """ resetMatrix(self) -> None """
        pass

    def resetTransform(self): # real signature unknown; restored from __doc__
        """ resetTransform(self) -> None """
        pass

    def resizeAnchor(self): # real signature unknown; restored from __doc__
        """ resizeAnchor(self) -> PySide2.QtWidgets.QGraphicsView.ViewportAnchor """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def rotate(self, angle): # real signature unknown; restored from __doc__
        """ rotate(self, angle: float) -> None """
        pass

    def rubberBandChanged(self, *args, **kwargs): # real signature unknown
        pass

    def rubberBandRect(self): # real signature unknown; restored from __doc__
        """ rubberBandRect(self) -> PySide2.QtCore.QRect """
        pass

    def rubberBandSelectionMode(self): # real signature unknown; restored from __doc__
        """ rubberBandSelectionMode(self) -> PySide2.QtCore.Qt.ItemSelectionMode """
        pass

    def scale(self, sx, sy): # real signature unknown; restored from __doc__
        """ scale(self, sx: float, sy: float) -> None """
        pass

    def scene(self): # real signature unknown; restored from __doc__
        """ scene(self) -> PySide2.QtWidgets.QGraphicsScene """
        pass

    def sceneRect(self): # real signature unknown; restored from __doc__
        """ sceneRect(self) -> PySide2.QtCore.QRectF """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) -> None """
        pass

    def setAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setAlignment(self, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setBackgroundBrush(self, brush): # real signature unknown; restored from __doc__
        """ setBackgroundBrush(self, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setCacheMode(self, mode): # real signature unknown; restored from __doc__
        """ setCacheMode(self, mode: PySide2.QtWidgets.QGraphicsView.CacheMode) -> None """
        pass

    def setDragMode(self, mode): # real signature unknown; restored from __doc__
        """ setDragMode(self, mode: PySide2.QtWidgets.QGraphicsView.DragMode) -> None """
        pass

    def setForegroundBrush(self, brush): # real signature unknown; restored from __doc__
        """ setForegroundBrush(self, brush: PySide2.QtGui.QBrush) -> None """
        pass

    def setInteractive(self, allowed): # real signature unknown; restored from __doc__
        """ setInteractive(self, allowed: bool) -> None """
        pass

    def setMatrix(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setMatrix(self, matrix: PySide2.QtGui.QMatrix, combine: bool = False) -> None """
        pass

    def setOptimizationFlag(self, flag, enabled=True): # real signature unknown; restored from __doc__
        """ setOptimizationFlag(self, flag: PySide2.QtWidgets.QGraphicsView.OptimizationFlag, enabled: bool = True) -> None """
        pass

    def setOptimizationFlags(self, flags): # real signature unknown; restored from __doc__
        """ setOptimizationFlags(self, flags: PySide2.QtWidgets.QGraphicsView.OptimizationFlags) -> None """
        pass

    def setRenderHint(self, hint, enabled=True): # real signature unknown; restored from __doc__
        """ setRenderHint(self, hint: PySide2.QtGui.QPainter.RenderHint, enabled: bool = True) -> None """
        pass

    def setRenderHints(self, hints): # real signature unknown; restored from __doc__
        """ setRenderHints(self, hints: PySide2.QtGui.QPainter.RenderHints) -> None """
        pass

    def setResizeAnchor(self, anchor): # real signature unknown; restored from __doc__
        """ setResizeAnchor(self, anchor: PySide2.QtWidgets.QGraphicsView.ViewportAnchor) -> None """
        pass

    def setRubberBandSelectionMode(self, mode): # real signature unknown; restored from __doc__
        """ setRubberBandSelectionMode(self, mode: PySide2.QtCore.Qt.ItemSelectionMode) -> None """
        pass

    def setScene(self, scene): # real signature unknown; restored from __doc__
        """ setScene(self, scene: PySide2.QtWidgets.QGraphicsScene) -> None """
        pass

    def setSceneRect(self, rect): # real signature unknown; restored from __doc__
        """
        setSceneRect(self, rect: PySide2.QtCore.QRectF) -> None
        setSceneRect(self, x: float, y: float, w: float, h: float) -> None
        """
        pass

    def setTransform(self, matrix, combine=False): # real signature unknown; restored from __doc__
        """ setTransform(self, matrix: PySide2.QtGui.QTransform, combine: bool = False) -> None """
        pass

    def setTransformationAnchor(self, anchor): # real signature unknown; restored from __doc__
        """ setTransformationAnchor(self, anchor: PySide2.QtWidgets.QGraphicsView.ViewportAnchor) -> None """
        pass

    def setupViewport(self, widget): # real signature unknown; restored from __doc__
        """ setupViewport(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setViewportUpdateMode(self, mode): # real signature unknown; restored from __doc__
        """ setViewportUpdateMode(self, mode: PySide2.QtWidgets.QGraphicsView.ViewportUpdateMode) -> None """
        pass

    def shear(self, sh, sv): # real signature unknown; restored from __doc__
        """ shear(self, sh: float, sv: float) -> None """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def transform(self): # real signature unknown; restored from __doc__
        """ transform(self) -> PySide2.QtGui.QTransform """
        pass

    def transformationAnchor(self): # real signature unknown; restored from __doc__
        """ transformationAnchor(self) -> PySide2.QtWidgets.QGraphicsView.ViewportAnchor """
        pass

    def translate(self, dx, dy): # real signature unknown; restored from __doc__
        """ translate(self, dx: float, dy: float) -> None """
        pass

    def updateScene(self, rects, PySide2_QtCore_QRectF=None): # real signature unknown; restored from __doc__
        """ updateScene(self, rects: typing.Sequence[PySide2.QtCore.QRectF]) -> None """
        pass

    def updateSceneRect(self, rect): # real signature unknown; restored from __doc__
        """ updateSceneRect(self, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def viewportEvent(self, event): # real signature unknown; restored from __doc__
        """ viewportEvent(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def viewportTransform(self): # real signature unknown; restored from __doc__
        """ viewportTransform(self) -> PySide2.QtGui.QTransform """
        pass

    def viewportUpdateMode(self): # real signature unknown; restored from __doc__
        """ viewportUpdateMode(self) -> PySide2.QtWidgets.QGraphicsView.ViewportUpdateMode """
        pass

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AnchorUnderMouse = PySide2.QtWidgets.QGraphicsView.ViewportAnchor.AnchorUnderMouse
    AnchorViewCenter = PySide2.QtWidgets.QGraphicsView.ViewportAnchor.AnchorViewCenter
    BoundingRectViewportUpdate = PySide2.QtWidgets.QGraphicsView.ViewportUpdateMode.BoundingRectViewportUpdate
    CacheBackground = PySide2.QtWidgets.QGraphicsView.CacheModeFlag.CacheBackground
    CacheMode = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsView.CacheMode'>"
    CacheModeFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsView.CacheModeFlag'>"
    CacheNone = PySide2.QtWidgets.QGraphicsView.CacheModeFlag.CacheNone
    DontAdjustForAntialiasing = PySide2.QtWidgets.QGraphicsView.OptimizationFlag.DontAdjustForAntialiasing
    DontClipPainter = PySide2.QtWidgets.QGraphicsView.OptimizationFlag.DontClipPainter
    DontSavePainterState = PySide2.QtWidgets.QGraphicsView.OptimizationFlag.DontSavePainterState
    DragMode = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsView.DragMode'>"
    FullViewportUpdate = PySide2.QtWidgets.QGraphicsView.ViewportUpdateMode.FullViewportUpdate
    IndirectPainting = PySide2.QtWidgets.QGraphicsView.OptimizationFlag.IndirectPainting
    MinimalViewportUpdate = PySide2.QtWidgets.QGraphicsView.ViewportUpdateMode.MinimalViewportUpdate
    NoAnchor = PySide2.QtWidgets.QGraphicsView.ViewportAnchor.NoAnchor
    NoDrag = PySide2.QtWidgets.QGraphicsView.DragMode.NoDrag
    NoViewportUpdate = PySide2.QtWidgets.QGraphicsView.ViewportUpdateMode.NoViewportUpdate
    OptimizationFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsView.OptimizationFlag'>"
    OptimizationFlags = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsView.OptimizationFlags'>"
    RubberBandDrag = PySide2.QtWidgets.QGraphicsView.DragMode.RubberBandDrag
    ScrollHandDrag = PySide2.QtWidgets.QGraphicsView.DragMode.ScrollHandDrag
    SmartViewportUpdate = PySide2.QtWidgets.QGraphicsView.ViewportUpdateMode.SmartViewportUpdate
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50816100>'
    ViewportAnchor = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsView.ViewportAnchor'>"
    ViewportUpdateMode = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsView.ViewportUpdateMode'>"


