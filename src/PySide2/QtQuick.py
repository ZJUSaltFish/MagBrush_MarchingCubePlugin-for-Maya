# encoding: utf-8
# module PySide2.QtQuick
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtQuick.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import PySide2.QtQml as __PySide2_QtQml
import Shiboken as __Shiboken


# no functions
# classes

class QQuickImageProvider(__PySide2_QtQml.QQmlImageProviderBase):
    """ QQuickImageProvider(self, type: PySide2.QtQml.QQmlImageProviderBase.ImageType, flags: PySide2.QtQml.QQmlImageProviderBase.Flags = Default(QQmlImageProviderBase.Flags)) -> None """
    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtQml.QQmlImageProviderBase.Flags """
        pass

    def imageType(self): # real signature unknown; restored from __doc__
        """ imageType(self) -> PySide2.QtQml.QQmlImageProviderBase.ImageType """
        pass

    def requestImage(self, id, size, requestedSize): # real signature unknown; restored from __doc__
        """ requestImage(self, id: str, size: PySide2.QtCore.QSize, requestedSize: PySide2.QtCore.QSize) -> PySide2.QtGui.QImage """
        pass

    def requestPixmap(self, id, size, requestedSize): # real signature unknown; restored from __doc__
        """ requestPixmap(self, id: str, size: PySide2.QtCore.QSize, requestedSize: PySide2.QtCore.QSize) -> PySide2.QtGui.QPixmap """
        pass

    def requestTexture(self, id, size, requestedSize): # real signature unknown; restored from __doc__
        """ requestTexture(self, id: str, size: PySide2.QtCore.QSize, requestedSize: PySide2.QtCore.QSize) -> PySide2.QtQuick.QQuickTextureFactory """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QQuickAsyncImageProvider(QQuickImageProvider):
    """ QQuickAsyncImageProvider(self) -> None """
    def requestImageResponse(self, id, requestedSize): # real signature unknown; restored from __doc__
        """ requestImageResponse(self, id: str, requestedSize: PySide2.QtCore.QSize) -> PySide2.QtQuick.QQuickImageResponse """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QQuickItem(__PySide2_QtCore.QObject, __PySide2_QtQml.QQmlParserStatus):
    """ QQuickItem(self, parent: typing.Optional[PySide2.QtQuick.QQuickItem] = None) -> None """
    def acceptedMouseButtons(self): # real signature unknown; restored from __doc__
        """ acceptedMouseButtons(self) -> PySide2.QtCore.Qt.MouseButtons """
        pass

    def acceptHoverEvents(self): # real signature unknown; restored from __doc__
        """ acceptHoverEvents(self) -> bool """
        return False

    def acceptTouchEvents(self): # real signature unknown; restored from __doc__
        """ acceptTouchEvents(self) -> bool """
        return False

    def activeFocusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def activeFocusOnTab(self): # real signature unknown; restored from __doc__
        """ activeFocusOnTab(self) -> bool """
        return False

    def activeFocusOnTabChanged(self, *args, **kwargs): # real signature unknown
        pass

    def antialiasing(self): # real signature unknown; restored from __doc__
        """ antialiasing(self) -> bool """
        return False

    def antialiasingChanged(self, *args, **kwargs): # real signature unknown
        pass

    def baselineOffset(self): # real signature unknown; restored from __doc__
        """ baselineOffset(self) -> float """
        return 0.0

    def baselineOffsetChanged(self, *args, **kwargs): # real signature unknown
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def childAt(self, x, y): # real signature unknown; restored from __doc__
        """ childAt(self, x: float, y: float) -> PySide2.QtQuick.QQuickItem """
        pass

    def childItems(self): # real signature unknown; restored from __doc__
        """ childItems(self) -> typing.List[PySide2.QtQuick.QQuickItem] """
        pass

    def childMouseEventFilter(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ childMouseEventFilter(self, arg__1: PySide2.QtQuick.QQuickItem, arg__2: PySide2.QtCore.QEvent) -> bool """
        return False

    def childrenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRect(self): # real signature unknown; restored from __doc__
        """ childrenRect(self) -> PySide2.QtCore.QRectF """
        pass

    def childrenRectChanged(self, *args, **kwargs): # real signature unknown
        pass

    def classBegin(self): # real signature unknown; restored from __doc__
        """ classBegin(self) -> None """
        pass

    def clip(self): # real signature unknown; restored from __doc__
        """ clip(self) -> bool """
        return False

    def clipChanged(self, *args, **kwargs): # real signature unknown
        pass

    def clipRect(self): # real signature unknown; restored from __doc__
        """ clipRect(self) -> PySide2.QtCore.QRectF """
        pass

    def componentComplete(self): # real signature unknown; restored from __doc__
        """ componentComplete(self) -> None """
        pass

    def containmentMask(self): # real signature unknown; restored from __doc__
        """ containmentMask(self) -> PySide2.QtCore.QObject """
        pass

    def containmentMaskChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, point): # real signature unknown; restored from __doc__
        """ contains(self, point: PySide2.QtCore.QPointF) -> bool """
        return False

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> PySide2.QtGui.QCursor """
        pass

    def dragEnterEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, arg__1: PySide2.QtGui.QDragEnterEvent) -> None """
        pass

    def dragLeaveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, arg__1: PySide2.QtGui.QDragLeaveEvent) -> None """
        pass

    def dragMoveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, arg__1: PySide2.QtGui.QDragMoveEvent) -> None """
        pass

    def dropEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ dropEvent(self, arg__1: PySide2.QtGui.QDropEvent) -> None """
        pass

    def enabledChanged(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def filtersChildMouseEvents(self): # real signature unknown; restored from __doc__
        """ filtersChildMouseEvents(self) -> bool """
        return False

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtQuick.QQuickItem.Flags """
        pass

    def focusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusInEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusOutEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def forceActiveFocus(self): # real signature unknown; restored from __doc__
        """
        forceActiveFocus(self) -> None
        forceActiveFocus(self, reason: PySide2.QtCore.Qt.FocusReason) -> None
        """
        pass

    def geometryChanged(self, newGeometry, oldGeometry): # real signature unknown; restored from __doc__
        """ geometryChanged(self, newGeometry: PySide2.QtCore.QRectF, oldGeometry: PySide2.QtCore.QRectF) -> None """
        pass

    def grabMouse(self): # real signature unknown; restored from __doc__
        """ grabMouse(self) -> None """
        pass

    def grabToImage(self, callback, targetSize=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        grabToImage(self, callback: PySide2.QtQml.QJSValue, targetSize: PySide2.QtCore.QSize = Default(QSize)) -> bool
        grabToImage(self, targetSize: PySide2.QtCore.QSize = Default(QSize)) -> typing.Tuple[PySide2.QtQuick.QQuickItemGrabResult]
        """
        pass

    def grabTouchPoints(self, ids, p_int=None): # real signature unknown; restored from __doc__
        """ grabTouchPoints(self, ids: typing.List[int]) -> None """
        pass

    def hasActiveFocus(self): # real signature unknown; restored from __doc__
        """ hasActiveFocus(self) -> bool """
        return False

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ hasFocus(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> float """
        return 0.0

    def heightChanged(self, *args, **kwargs): # real signature unknown
        pass

    def heightValid(self): # real signature unknown; restored from __doc__
        """ heightValid(self) -> bool """
        return False

    def hoverEnterEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverEnterEvent(self, event: PySide2.QtGui.QHoverEvent) -> None """
        pass

    def hoverLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, event: PySide2.QtGui.QHoverEvent) -> None """
        pass

    def hoverMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, event: PySide2.QtGui.QHoverEvent) -> None """
        pass

    def implicitHeight(self): # real signature unknown; restored from __doc__
        """ implicitHeight(self) -> float """
        return 0.0

    def implicitHeightChanged(self, *args, **kwargs): # real signature unknown
        pass

    def implicitWidth(self): # real signature unknown; restored from __doc__
        """ implicitWidth(self) -> float """
        return 0.0

    def implicitWidthChanged(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, arg__1: PySide2.QtGui.QInputMethodEvent) -> None """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any """
        pass

    def isAncestorOf(self, child): # real signature unknown; restored from __doc__
        """ isAncestorOf(self, child: PySide2.QtQuick.QQuickItem) -> bool """
        return False

    def isComponentComplete(self): # real signature unknown; restored from __doc__
        """ isComponentComplete(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isFocusScope(self): # real signature unknown; restored from __doc__
        """ isFocusScope(self) -> bool """
        return False

    def isTextureProvider(self): # real signature unknown; restored from __doc__
        """ isTextureProvider(self) -> bool """
        return False

    def isUnderMouse(self): # real signature unknown; restored from __doc__
        """ isUnderMouse(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def itemTransform(self, arg__1): # real signature unknown; restored from __doc__
        """ itemTransform(self, arg__1: PySide2.QtQuick.QQuickItem) -> typing.Tuple[PySide2.QtGui.QTransform, bool] """
        pass

    def keepMouseGrab(self): # real signature unknown; restored from __doc__
        """ keepMouseGrab(self) -> bool """
        return False

    def keepTouchGrab(self): # real signature unknown; restored from __doc__
        """ keepTouchGrab(self) -> bool """
        return False

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def mapFromGlobal(self, point): # real signature unknown; restored from __doc__
        """ mapFromGlobal(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF """
        pass

    def mapFromItem(self, item, point): # real signature unknown; restored from __doc__
        """ mapFromItem(self, item: PySide2.QtQuick.QQuickItem, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF """
        pass

    def mapFromScene(self, point): # real signature unknown; restored from __doc__
        """ mapFromScene(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF """
        pass

    def mapRectFromItem(self, item, rect): # real signature unknown; restored from __doc__
        """ mapRectFromItem(self, item: PySide2.QtQuick.QQuickItem, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF """
        pass

    def mapRectFromScene(self, rect): # real signature unknown; restored from __doc__
        """ mapRectFromScene(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF """
        pass

    def mapRectToItem(self, item, rect): # real signature unknown; restored from __doc__
        """ mapRectToItem(self, item: PySide2.QtQuick.QQuickItem, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF """
        pass

    def mapRectToScene(self, rect): # real signature unknown; restored from __doc__
        """ mapRectToScene(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF """
        pass

    def mapToGlobal(self, point): # real signature unknown; restored from __doc__
        """ mapToGlobal(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF """
        pass

    def mapToItem(self, item, point): # real signature unknown; restored from __doc__
        """ mapToItem(self, item: PySide2.QtQuick.QQuickItem, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF """
        pass

    def mapToScene(self, point): # real signature unknown; restored from __doc__
        """ mapToScene(self, point: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF """
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

    def mouseUngrabEvent(self): # real signature unknown; restored from __doc__
        """ mouseUngrabEvent(self) -> None """
        pass

    def nextItemInFocusChain(self, forward=True): # real signature unknown; restored from __doc__
        """ nextItemInFocusChain(self, forward: bool = True) -> PySide2.QtQuick.QQuickItem """
        pass

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def opacityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def parentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def parentItem(self): # real signature unknown; restored from __doc__
        """ parentItem(self) -> PySide2.QtQuick.QQuickItem """
        pass

    def polish(self): # real signature unknown; restored from __doc__
        """ polish(self) -> None """
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> PySide2.QtCore.QPointF """
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) -> None """
        pass

    def resetAntialiasing(self): # real signature unknown; restored from __doc__
        """ resetAntialiasing(self) -> None """
        pass

    def resetHeight(self): # real signature unknown; restored from __doc__
        """ resetHeight(self) -> None """
        pass

    def resetWidth(self): # real signature unknown; restored from __doc__
        """ resetWidth(self) -> None """
        pass

    def rotation(self): # real signature unknown; restored from __doc__
        """ rotation(self) -> float """
        return 0.0

    def rotationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def scale(self): # real signature unknown; restored from __doc__
        """ scale(self) -> float """
        return 0.0

    def scaleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def scopedFocusItem(self): # real signature unknown; restored from __doc__
        """ scopedFocusItem(self) -> PySide2.QtQuick.QQuickItem """
        pass

    def setAcceptedMouseButtons(self, buttons): # real signature unknown; restored from __doc__
        """ setAcceptedMouseButtons(self, buttons: PySide2.QtCore.Qt.MouseButtons) -> None """
        pass

    def setAcceptHoverEvents(self, enabled): # real signature unknown; restored from __doc__
        """ setAcceptHoverEvents(self, enabled: bool) -> None """
        pass

    def setAcceptTouchEvents(self, accept): # real signature unknown; restored from __doc__
        """ setAcceptTouchEvents(self, accept: bool) -> None """
        pass

    def setActiveFocusOnTab(self, arg__1): # real signature unknown; restored from __doc__
        """ setActiveFocusOnTab(self, arg__1: bool) -> None """
        pass

    def setAntialiasing(self, arg__1): # real signature unknown; restored from __doc__
        """ setAntialiasing(self, arg__1: bool) -> None """
        pass

    def setBaselineOffset(self, arg__1): # real signature unknown; restored from __doc__
        """ setBaselineOffset(self, arg__1: float) -> None """
        pass

    def setClip(self, arg__1): # real signature unknown; restored from __doc__
        """ setClip(self, arg__1: bool) -> None """
        pass

    def setContainmentMask(self, mask): # real signature unknown; restored from __doc__
        """ setContainmentMask(self, mask: PySide2.QtCore.QObject) -> None """
        pass

    def setCursor(self, cursor): # real signature unknown; restored from __doc__
        """ setCursor(self, cursor: PySide2.QtGui.QCursor) -> None """
        pass

    def setEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setEnabled(self, arg__1: bool) -> None """
        pass

    def setFiltersChildMouseEvents(self, filter): # real signature unknown; restored from __doc__
        """ setFiltersChildMouseEvents(self, filter: bool) -> None """
        pass

    def setFlag(self, flag, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, flag: PySide2.QtQuick.QQuickItem.Flag, enabled: bool = True) -> None """
        pass

    def setFlags(self, flags): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: PySide2.QtQuick.QQuickItem.Flags) -> None """
        pass

    def setFocus(self, arg__1): # real signature unknown; restored from __doc__
        """
        setFocus(self, arg__1: bool) -> None
        setFocus(self, focus: bool, reason: PySide2.QtCore.Qt.FocusReason) -> None
        """
        pass

    def setHeight(self, arg__1): # real signature unknown; restored from __doc__
        """ setHeight(self, arg__1: float) -> None """
        pass

    def setImplicitHeight(self, arg__1): # real signature unknown; restored from __doc__
        """ setImplicitHeight(self, arg__1: float) -> None """
        pass

    def setImplicitSize(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ setImplicitSize(self, arg__1: float, arg__2: float) -> None """
        pass

    def setImplicitWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ setImplicitWidth(self, arg__1: float) -> None """
        pass

    def setKeepMouseGrab(self, arg__1): # real signature unknown; restored from __doc__
        """ setKeepMouseGrab(self, arg__1: bool) -> None """
        pass

    def setKeepTouchGrab(self, arg__1): # real signature unknown; restored from __doc__
        """ setKeepTouchGrab(self, arg__1: bool) -> None """
        pass

    def setOpacity(self, arg__1): # real signature unknown; restored from __doc__
        """ setOpacity(self, arg__1: float) -> None """
        pass

    def setParentItem(self, parent): # real signature unknown; restored from __doc__
        """ setParentItem(self, parent: PySide2.QtQuick.QQuickItem) -> None """
        pass

    def setPosition(self, arg__1): # real signature unknown; restored from __doc__
        """ setPosition(self, arg__1: PySide2.QtCore.QPointF) -> None """
        pass

    def setRotation(self, arg__1): # real signature unknown; restored from __doc__
        """ setRotation(self, arg__1: float) -> None """
        pass

    def setScale(self, arg__1): # real signature unknown; restored from __doc__
        """ setScale(self, arg__1: float) -> None """
        pass

    def setSize(self, size): # real signature unknown; restored from __doc__
        """ setSize(self, size: PySide2.QtCore.QSizeF) -> None """
        pass

    def setSmooth(self, arg__1): # real signature unknown; restored from __doc__
        """ setSmooth(self, arg__1: bool) -> None """
        pass

    def setState(self, arg__1): # real signature unknown; restored from __doc__
        """ setState(self, arg__1: str) -> None """
        pass

    def setTransformOrigin(self, arg__1): # real signature unknown; restored from __doc__
        """ setTransformOrigin(self, arg__1: PySide2.QtQuick.QQuickItem.TransformOrigin) -> None """
        pass

    def setTransformOriginPoint(self, arg__1): # real signature unknown; restored from __doc__
        """ setTransformOriginPoint(self, arg__1: PySide2.QtCore.QPointF) -> None """
        pass

    def setVisible(self, arg__1): # real signature unknown; restored from __doc__
        """ setVisible(self, arg__1: bool) -> None """
        pass

    def setWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ setWidth(self, arg__1: float) -> None """
        pass

    def setX(self, arg__1): # real signature unknown; restored from __doc__
        """ setX(self, arg__1: float) -> None """
        pass

    def setY(self, arg__1): # real signature unknown; restored from __doc__
        """ setY(self, arg__1: float) -> None """
        pass

    def setZ(self, arg__1): # real signature unknown; restored from __doc__
        """ setZ(self, arg__1: float) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSizeF """
        pass

    def smooth(self): # real signature unknown; restored from __doc__
        """ smooth(self) -> bool """
        return False

    def smoothChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stackAfter(self, arg__1): # real signature unknown; restored from __doc__
        """ stackAfter(self, arg__1: PySide2.QtQuick.QQuickItem) -> None """
        pass

    def stackBefore(self, arg__1): # real signature unknown; restored from __doc__
        """ stackBefore(self, arg__1: PySide2.QtQuick.QQuickItem) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> str """
        return ""

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def textureProvider(self): # real signature unknown; restored from __doc__
        """ textureProvider(self) -> PySide2.QtQuick.QSGTextureProvider """
        pass

    def touchEvent(self, event): # real signature unknown; restored from __doc__
        """ touchEvent(self, event: PySide2.QtGui.QTouchEvent) -> None """
        pass

    def touchUngrabEvent(self): # real signature unknown; restored from __doc__
        """ touchUngrabEvent(self) -> None """
        pass

    def transformOrigin(self): # real signature unknown; restored from __doc__
        """ transformOrigin(self) -> PySide2.QtQuick.QQuickItem.TransformOrigin """
        pass

    def transformOriginChanged(self, *args, **kwargs): # real signature unknown
        pass

    def transformOriginPoint(self): # real signature unknown; restored from __doc__
        """ transformOriginPoint(self) -> PySide2.QtCore.QPointF """
        pass

    def ungrabMouse(self): # real signature unknown; restored from __doc__
        """ ungrabMouse(self) -> None """
        pass

    def ungrabTouchPoints(self): # real signature unknown; restored from __doc__
        """ ungrabTouchPoints(self) -> None """
        pass

    def unsetCursor(self): # real signature unknown; restored from __doc__
        """ unsetCursor(self) -> None """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) -> None """
        pass

    def updateInputMethod(self, queries=None): # real signature unknown; restored from __doc__
        """ updateInputMethod(self, queries: PySide2.QtCore.Qt.InputMethodQueries = PySide2.QtCore.Qt.InputMethodQuery.ImQueryInput) -> None """
        pass

    def updatePaintNode(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ updatePaintNode(self, arg__1: PySide2.QtQuick.QSGNode, arg__2: PySide2.QtQuick.QQuickItem.UpdatePaintNodeData) -> PySide2.QtQuick.QSGNode """
        pass

    def updatePolish(self): # real signature unknown; restored from __doc__
        """ updatePolish(self) -> None """
        pass

    def visibleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def visibleChildrenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> float """
        return 0.0

    def widthChanged(self, *args, **kwargs): # real signature unknown
        pass

    def widthValid(self): # real signature unknown; restored from __doc__
        """ widthValid(self) -> bool """
        return False

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> PySide2.QtQuick.QQuickWindow """
        pass

    def windowChanged(self, *args, **kwargs): # real signature unknown
        pass

    def windowDeactivateEvent(self): # real signature unknown; restored from __doc__
        """ windowDeactivateEvent(self) -> None """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> float """
        return 0.0

    def xChanged(self, *args, **kwargs): # real signature unknown
        pass

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> float """
        return 0.0

    def yChanged(self, *args, **kwargs): # real signature unknown
        pass

    def z(self): # real signature unknown; restored from __doc__
        """ z(self) -> float """
        return 0.0

    def zChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtQuick_QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    Bottom = PySide2.QtQuick.QQuickItem.TransformOrigin.Bottom
    BottomLeft = PySide2.QtQuick.QQuickItem.TransformOrigin.BottomLeft
    BottomRight = PySide2.QtQuick.QQuickItem.TransformOrigin.BottomRight
    Center = PySide2.QtQuick.QQuickItem.TransformOrigin.Center
    Flag = None # (!) real value is "<class 'PySide2.QtQuick.QQuickItem.Flag'>"
    Flags = None # (!) real value is "<class 'PySide2.QtQuick.QQuickItem.Flags'>"
    ItemAcceptsDrops = PySide2.QtQuick.QQuickItem.Flag.ItemAcceptsDrops
    ItemAcceptsInputMethod = PySide2.QtQuick.QQuickItem.Flag.ItemAcceptsInputMethod
    ItemActiveFocusHasChanged = PySide2.QtQuick.QQuickItem.ItemChange.ItemActiveFocusHasChanged
    ItemAntialiasingHasChanged = PySide2.QtQuick.QQuickItem.ItemChange.ItemAntialiasingHasChanged
    ItemChange = None # (!) real value is "<class 'PySide2.QtQuick.QQuickItem.ItemChange'>"
    ItemChildAddedChange = PySide2.QtQuick.QQuickItem.ItemChange.ItemChildAddedChange
    ItemChildRemovedChange = PySide2.QtQuick.QQuickItem.ItemChange.ItemChildRemovedChange
    ItemClipsChildrenToShape = PySide2.QtQuick.QQuickItem.Flag.ItemClipsChildrenToShape
    ItemDevicePixelRatioHasChanged = PySide2.QtQuick.QQuickItem.ItemChange.ItemDevicePixelRatioHasChanged
    ItemEnabledHasChanged = PySide2.QtQuick.QQuickItem.ItemChange.ItemEnabledHasChanged
    ItemHasContents = PySide2.QtQuick.QQuickItem.Flag.ItemHasContents
    ItemIsFocusScope = PySide2.QtQuick.QQuickItem.Flag.ItemIsFocusScope
    ItemOpacityHasChanged = PySide2.QtQuick.QQuickItem.ItemChange.ItemOpacityHasChanged
    ItemParentHasChanged = PySide2.QtQuick.QQuickItem.ItemChange.ItemParentHasChanged
    ItemRotationHasChanged = PySide2.QtQuick.QQuickItem.ItemChange.ItemRotationHasChanged
    ItemSceneChange = PySide2.QtQuick.QQuickItem.ItemChange.ItemSceneChange
    ItemVisibleHasChanged = PySide2.QtQuick.QQuickItem.ItemChange.ItemVisibleHasChanged
    Left = PySide2.QtQuick.QQuickItem.TransformOrigin.Left
    Right = PySide2.QtQuick.QQuickItem.TransformOrigin.Right
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812BB600>'
    Top = PySide2.QtQuick.QQuickItem.TransformOrigin.Top
    TopLeft = PySide2.QtQuick.QQuickItem.TransformOrigin.TopLeft
    TopRight = PySide2.QtQuick.QQuickItem.TransformOrigin.TopRight
    TransformOrigin = None # (!) real value is "<class 'PySide2.QtQuick.QQuickItem.TransformOrigin'>"
    UpdatePaintNodeData = None # (!) real value is "<class 'PySide2.QtQuick.QQuickItem.UpdatePaintNodeData'>"


class QQuickFramebufferObject(QQuickItem):
    """ QQuickFramebufferObject(self, parent: typing.Optional[PySide2.QtQuick.QQuickItem] = None) -> None """
    def createRenderer(self): # real signature unknown; restored from __doc__
        """ createRenderer(self) -> PySide2.QtQuick.QQuickFramebufferObject.Renderer """
        pass

    def geometryChanged(self, newGeometry, oldGeometry): # real signature unknown; restored from __doc__
        """ geometryChanged(self, newGeometry: PySide2.QtCore.QRectF, oldGeometry: PySide2.QtCore.QRectF) -> None """
        pass

    def isTextureProvider(self): # real signature unknown; restored from __doc__
        """ isTextureProvider(self) -> bool """
        return False

    def mirrorVertically(self): # real signature unknown; restored from __doc__
        """ mirrorVertically(self) -> bool """
        return False

    def mirrorVerticallyChanged(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) -> None """
        pass

    def setMirrorVertically(self, enable): # real signature unknown; restored from __doc__
        """ setMirrorVertically(self, enable: bool) -> None """
        pass

    def setTextureFollowsItemSize(self, follows): # real signature unknown; restored from __doc__
        """ setTextureFollowsItemSize(self, follows: bool) -> None """
        pass

    def textureFollowsItemSize(self): # real signature unknown; restored from __doc__
        """ textureFollowsItemSize(self) -> bool """
        return False

    def textureFollowsItemSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def textureProvider(self): # real signature unknown; restored from __doc__
        """ textureProvider(self) -> PySide2.QtQuick.QSGTextureProvider """
        pass

    def updatePaintNode(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ updatePaintNode(self, arg__1: PySide2.QtQuick.QSGNode, arg__2: PySide2.QtQuick.QQuickItem.UpdatePaintNodeData) -> PySide2.QtQuick.QSGNode """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtQuick_QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Renderer = None # (!) real value is "<class 'PySide2.QtQuick.QQuickFramebufferObject.Renderer'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812CC080>'


class QQuickImageResponse(__PySide2_QtCore.QObject):
    """ QQuickImageResponse(self) -> None """
    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) -> None """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def textureFactory(self): # real signature unknown; restored from __doc__
        """ textureFactory(self) -> PySide2.QtQuick.QQuickTextureFactory """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812CC340>'


class QQuickItemGrabResult(__PySide2_QtCore.QObject):
    # no doc
    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def image(self): # real signature unknown; restored from __doc__
        """ image(self) -> PySide2.QtGui.QImage """
        pass

    def ready(self, *args, **kwargs): # real signature unknown
        pass

    def saveToFile(self, fileName): # real signature unknown; restored from __doc__
        """ saveToFile(self, fileName: str) -> bool """
        return False

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812B9800>'


class QQuickPaintedItem(QQuickItem):
    """ QQuickPaintedItem(self, parent: typing.Optional[PySide2.QtQuick.QQuickItem] = None) -> None """
    def antialiasing(self): # real signature unknown; restored from __doc__
        """ antialiasing(self) -> bool """
        return False

    def contentsBoundingRect(self): # real signature unknown; restored from __doc__
        """ contentsBoundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def contentsScale(self): # real signature unknown; restored from __doc__
        """ contentsScale(self) -> float """
        return 0.0

    def contentsScaleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contentsSize(self): # real signature unknown; restored from __doc__
        """ contentsSize(self) -> PySide2.QtCore.QSize """
        pass

    def contentsSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def fillColor(self): # real signature unknown; restored from __doc__
        """ fillColor(self) -> PySide2.QtGui.QColor """
        pass

    def fillColorChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isTextureProvider(self): # real signature unknown; restored from __doc__
        """ isTextureProvider(self) -> bool """
        return False

    def mipmap(self): # real signature unknown; restored from __doc__
        """ mipmap(self) -> bool """
        return False

    def opaquePainting(self): # real signature unknown; restored from __doc__
        """ opaquePainting(self) -> bool """
        return False

    def paint(self, painter): # real signature unknown; restored from __doc__
        """ paint(self, painter: PySide2.QtGui.QPainter) -> None """
        pass

    def performanceHints(self): # real signature unknown; restored from __doc__
        """ performanceHints(self) -> PySide2.QtQuick.QQuickPaintedItem.PerformanceHints """
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) -> None """
        pass

    def renderTarget(self): # real signature unknown; restored from __doc__
        """ renderTarget(self) -> PySide2.QtQuick.QQuickPaintedItem.RenderTarget """
        pass

    def renderTargetChanged(self, *args, **kwargs): # real signature unknown
        pass

    def resetContentsSize(self): # real signature unknown; restored from __doc__
        """ resetContentsSize(self) -> None """
        pass

    def setAntialiasing(self, enable): # real signature unknown; restored from __doc__
        """ setAntialiasing(self, enable: bool) -> None """
        pass

    def setContentsScale(self, arg__1): # real signature unknown; restored from __doc__
        """ setContentsScale(self, arg__1: float) -> None """
        pass

    def setContentsSize(self, arg__1): # real signature unknown; restored from __doc__
        """ setContentsSize(self, arg__1: PySide2.QtCore.QSize) -> None """
        pass

    def setFillColor(self, arg__1): # real signature unknown; restored from __doc__
        """ setFillColor(self, arg__1: PySide2.QtGui.QColor) -> None """
        pass

    def setMipmap(self, enable): # real signature unknown; restored from __doc__
        """ setMipmap(self, enable: bool) -> None """
        pass

    def setOpaquePainting(self, opaque): # real signature unknown; restored from __doc__
        """ setOpaquePainting(self, opaque: bool) -> None """
        pass

    def setPerformanceHint(self, hint, enabled=True): # real signature unknown; restored from __doc__
        """ setPerformanceHint(self, hint: PySide2.QtQuick.QQuickPaintedItem.PerformanceHint, enabled: bool = True) -> None """
        pass

    def setPerformanceHints(self, hints): # real signature unknown; restored from __doc__
        """ setPerformanceHints(self, hints: PySide2.QtQuick.QQuickPaintedItem.PerformanceHints) -> None """
        pass

    def setRenderTarget(self, target): # real signature unknown; restored from __doc__
        """ setRenderTarget(self, target: PySide2.QtQuick.QQuickPaintedItem.RenderTarget) -> None """
        pass

    def setTextureSize(self, size): # real signature unknown; restored from __doc__
        """ setTextureSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def textureProvider(self): # real signature unknown; restored from __doc__
        """ textureProvider(self) -> PySide2.QtQuick.QSGTextureProvider """
        pass

    def textureSize(self): # real signature unknown; restored from __doc__
        """ textureSize(self) -> PySide2.QtCore.QSize """
        pass

    def textureSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def update(self): # real signature unknown; restored from __doc__
        """
        update(self) -> None
        update(self, rect: PySide2.QtCore.QRect = Default(QRect)) -> None
        """
        pass

    def updatePaintNode(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ updatePaintNode(self, arg__1: PySide2.QtQuick.QSGNode, arg__2: PySide2.QtQuick.QQuickItem.UpdatePaintNodeData) -> PySide2.QtQuick.QSGNode """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtQuick_QQuickItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    FastFBOResizing = PySide2.QtQuick.QQuickPaintedItem.PerformanceHint.FastFBOResizing
    FramebufferObject = PySide2.QtQuick.QQuickPaintedItem.RenderTarget.FramebufferObject
    Image = PySide2.QtQuick.QQuickPaintedItem.RenderTarget.Image
    InvertedYFramebufferObject = PySide2.QtQuick.QQuickPaintedItem.RenderTarget.InvertedYFramebufferObject
    PerformanceHint = None # (!) real value is "<class 'PySide2.QtQuick.QQuickPaintedItem.PerformanceHint'>"
    PerformanceHints = None # (!) real value is "<class 'PySide2.QtQuick.QQuickPaintedItem.PerformanceHints'>"
    RenderTarget = None # (!) real value is "<class 'PySide2.QtQuick.QQuickPaintedItem.RenderTarget'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812BBF40>'


class QQuickRenderControl(__PySide2_QtCore.QObject):
    """ QQuickRenderControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def grab(self): # real signature unknown; restored from __doc__
        """ grab(self) -> PySide2.QtGui.QImage """
        pass

    def initialize(self, gl): # real signature unknown; restored from __doc__
        """ initialize(self, gl: PySide2.QtGui.QOpenGLContext) -> None """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

    def polishItems(self): # real signature unknown; restored from __doc__
        """ polishItems(self) -> None """
        pass

    def prepareThread(self, targetThread): # real signature unknown; restored from __doc__
        """ prepareThread(self, targetThread: PySide2.QtCore.QThread) -> None """
        pass

    def render(self): # real signature unknown; restored from __doc__
        """ render(self) -> None """
        pass

    def renderRequested(self, *args, **kwargs): # real signature unknown
        pass

    def renderWindow(self, offset): # real signature unknown; restored from __doc__
        """ renderWindow(self, offset: PySide2.QtCore.QPoint) -> PySide2.QtGui.QWindow """
        pass

    def renderWindowFor(self, win, offset, PySide2_QtCore_QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ renderWindowFor(win: PySide2.QtQuick.QQuickWindow, offset: typing.Optional[PySide2.QtCore.QPoint] = None) -> PySide2.QtGui.QWindow """
        pass

    def sceneChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sync(self): # real signature unknown; restored from __doc__
        """ sync(self) -> bool """
        return False

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812B96C0>'


class QQuickTextDocument(__PySide2_QtCore.QObject):
    """ QQuickTextDocument(self, parent: PySide2.QtQuick.QQuickItem) -> None """
    def textDocument(self): # real signature unknown; restored from __doc__
        """ textDocument(self) -> PySide2.QtGui.QTextDocument """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812B93C0>'


class QQuickTextureFactory(__PySide2_QtCore.QObject):
    """ QQuickTextureFactory(self) -> None """
    def createTexture(self, window): # real signature unknown; restored from __doc__
        """ createTexture(self, window: PySide2.QtQuick.QQuickWindow) -> PySide2.QtQuick.QSGTexture """
        pass

    def image(self): # real signature unknown; restored from __doc__
        """ image(self) -> PySide2.QtGui.QImage """
        pass

    def textureByteCount(self): # real signature unknown; restored from __doc__
        """ textureByteCount(self) -> int """
        return 0

    def textureFactoryForImage(self, image): # real signature unknown; restored from __doc__
        """ textureFactoryForImage(image: PySide2.QtGui.QImage) -> PySide2.QtQuick.QQuickTextureFactory """
        pass

    def textureSize(self): # real signature unknown; restored from __doc__
        """ textureSize(self) -> PySide2.QtCore.QSize """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812B9280>'


class QQuickTransform(__PySide2_QtCore.QObject):
    """ QQuickTransform(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def appendToItem(self, arg__1): # real signature unknown; restored from __doc__
        """ appendToItem(self, arg__1: PySide2.QtQuick.QQuickItem) -> None """
        pass

    def applyTo(self, matrix): # real signature unknown; restored from __doc__
        """ applyTo(self, matrix: PySide2.QtGui.QMatrix4x4) -> None """
        pass

    def prependToItem(self, arg__1): # real signature unknown; restored from __doc__
        """ prependToItem(self, arg__1: PySide2.QtQuick.QQuickItem) -> None """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) -> None """
        pass

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812B9140>'


class QQuickWindow(__PySide2_QtGui.QWindow):
    """
    QQuickWindow(self, parent: typing.Optional[PySide2.QtGui.QWindow] = None) -> None
    QQuickWindow(self, renderControl: PySide2.QtQuick.QQuickRenderControl) -> None
    """
    def accessibleRoot(self): # real signature unknown; restored from __doc__
        """ accessibleRoot(self) -> PySide2.QtGui.QAccessibleInterface """
        pass

    def activeFocusItem(self): # real signature unknown; restored from __doc__
        """ activeFocusItem(self) -> PySide2.QtQuick.QQuickItem """
        pass

    def activeFocusItemChanged(self, *args, **kwargs): # real signature unknown
        pass

    def afterAnimating(self, *args, **kwargs): # real signature unknown
        pass

    def afterRendering(self, *args, **kwargs): # real signature unknown
        pass

    def afterRenderPassRecording(self, *args, **kwargs): # real signature unknown
        pass

    def afterSynchronizing(self, *args, **kwargs): # real signature unknown
        pass

    def beforeRendering(self, *args, **kwargs): # real signature unknown
        pass

    def beforeRenderPassRecording(self, *args, **kwargs): # real signature unknown
        pass

    def beforeSynchronizing(self, *args, **kwargs): # real signature unknown
        pass

    def beginExternalCommands(self): # real signature unknown; restored from __doc__
        """ beginExternalCommands(self) -> None """
        pass

    def clearBeforeRendering(self): # real signature unknown; restored from __doc__
        """ clearBeforeRendering(self) -> bool """
        return False

    def closing(self, *args, **kwargs): # real signature unknown
        pass

    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> PySide2.QtGui.QColor """
        pass

    def colorChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contentItem(self): # real signature unknown; restored from __doc__
        """ contentItem(self) -> PySide2.QtQuick.QQuickItem """
        pass

    def createTextureFromId(self, id, size, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTextureFromId(self, id: int, size: PySide2.QtCore.QSize, options: PySide2.QtQuick.QQuickWindow.CreateTextureOptions = Default(QQuickWindow.CreateTextureOption)) -> PySide2.QtQuick.QSGTexture """
        pass

    def createTextureFromImage(self, image): # real signature unknown; restored from __doc__
        """
        createTextureFromImage(self, image: PySide2.QtGui.QImage) -> PySide2.QtQuick.QSGTexture
        createTextureFromImage(self, image: PySide2.QtGui.QImage, options: PySide2.QtQuick.QQuickWindow.CreateTextureOptions) -> PySide2.QtQuick.QSGTexture
        """
        pass

    def createTextureFromNativeObject(self, type, nativeObjectPtr, nativeLayout, size, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTextureFromNativeObject(self, type: PySide2.QtQuick.QQuickWindow.NativeObjectType, nativeObjectPtr: int, nativeLayout: int, size: PySide2.QtCore.QSize, options: PySide2.QtQuick.QQuickWindow.CreateTextureOptions = Default(QQuickWindow.CreateTextureOption)) -> PySide2.QtQuick.QSGTexture """
        pass

    def effectiveDevicePixelRatio(self): # real signature unknown; restored from __doc__
        """ effectiveDevicePixelRatio(self) -> float """
        return 0.0

    def endExternalCommands(self): # real signature unknown; restored from __doc__
        """ endExternalCommands(self) -> None """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def exposeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ exposeEvent(self, arg__1: PySide2.QtGui.QExposeEvent) -> None """
        pass

    def focusInEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusInEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusObject(self): # real signature unknown; restored from __doc__
        """ focusObject(self) -> PySide2.QtCore.QObject """
        pass

    def focusOutEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, arg__1: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def frameSwapped(self, *args, **kwargs): # real signature unknown
        pass

    def grabWindow(self): # real signature unknown; restored from __doc__
        """ grabWindow(self) -> PySide2.QtGui.QImage """
        pass

    def hasDefaultAlphaBuffer(self): # real signature unknown; restored from __doc__
        """ hasDefaultAlphaBuffer() -> bool """
        return False

    def hideEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ hideEvent(self, arg__1: PySide2.QtGui.QHideEvent) -> None """
        pass

    def incubationController(self): # real signature unknown; restored from __doc__
        """ incubationController(self) -> PySide2.QtQml.QQmlIncubationController """
        pass

    def isPersistentOpenGLContext(self): # real signature unknown; restored from __doc__
        """ isPersistentOpenGLContext(self) -> bool """
        return False

    def isPersistentSceneGraph(self): # real signature unknown; restored from __doc__
        """ isPersistentSceneGraph(self) -> bool """
        return False

    def isSceneGraphInitialized(self): # real signature unknown; restored from __doc__
        """ isSceneGraphInitialized(self) -> bool """
        return False

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def mouseDoubleClickEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseGrabberItem(self): # real signature unknown; restored from __doc__
        """ mouseGrabberItem(self) -> PySide2.QtQuick.QQuickItem """
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

    def openglContext(self): # real signature unknown; restored from __doc__
        """ openglContext(self) -> PySide2.QtGui.QOpenGLContext """
        pass

    def openglContextCreated(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) -> None """
        pass

    def renderTarget(self): # real signature unknown; restored from __doc__
        """ renderTarget(self) -> PySide2.QtGui.QOpenGLFramebufferObject """
        pass

    def renderTargetId(self): # real signature unknown; restored from __doc__
        """ renderTargetId(self) -> int """
        return 0

    def renderTargetSize(self): # real signature unknown; restored from __doc__
        """ renderTargetSize(self) -> PySide2.QtCore.QSize """
        pass

    def resetOpenGLState(self): # real signature unknown; restored from __doc__
        """ resetOpenGLState(self) -> None """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def sceneGraphAboutToStop(self, *args, **kwargs): # real signature unknown
        pass

    def sceneGraphBackend(self): # real signature unknown; restored from __doc__
        """ sceneGraphBackend() -> str """
        return ""

    def sceneGraphError(self, *args, **kwargs): # real signature unknown
        pass

    def sceneGraphInitialized(self, *args, **kwargs): # real signature unknown
        pass

    def sceneGraphInvalidated(self, *args, **kwargs): # real signature unknown
        pass

    def scheduleRenderJob(self, job, schedule): # real signature unknown; restored from __doc__
        """ scheduleRenderJob(self, job: PySide2.QtCore.QRunnable, schedule: PySide2.QtQuick.QQuickWindow.RenderStage) -> None """
        pass

    def sendEvent(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ sendEvent(self, arg__1: PySide2.QtQuick.QQuickItem, arg__2: PySide2.QtCore.QEvent) -> bool """
        return False

    def setClearBeforeRendering(self, enabled): # real signature unknown; restored from __doc__
        """ setClearBeforeRendering(self, enabled: bool) -> None """
        pass

    def setColor(self, color): # real signature unknown; restored from __doc__
        """ setColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setDefaultAlphaBuffer(self, useAlpha): # real signature unknown; restored from __doc__
        """ setDefaultAlphaBuffer(useAlpha: bool) -> None """
        pass

    def setPersistentOpenGLContext(self, persistent): # real signature unknown; restored from __doc__
        """ setPersistentOpenGLContext(self, persistent: bool) -> None """
        pass

    def setPersistentSceneGraph(self, persistent): # real signature unknown; restored from __doc__
        """ setPersistentSceneGraph(self, persistent: bool) -> None """
        pass

    def setRenderTarget(self, fbo): # real signature unknown; restored from __doc__
        """
        setRenderTarget(self, fbo: PySide2.QtGui.QOpenGLFramebufferObject) -> None
        setRenderTarget(self, fboId: int, size: PySide2.QtCore.QSize) -> None
        """
        pass

    def setSceneGraphBackend(self, backend): # real signature unknown; restored from __doc__
        """ setSceneGraphBackend(backend: str) -> None """
        pass

    def setTextRenderType(self, renderType): # real signature unknown; restored from __doc__
        """ setTextRenderType(renderType: PySide2.QtQuick.QQuickWindow.TextRenderType) -> None """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def tabletEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ tabletEvent(self, arg__1: PySide2.QtGui.QTabletEvent) -> None """
        pass

    def textRenderType(self): # real signature unknown; restored from __doc__
        """ textRenderType() -> PySide2.QtQuick.QQuickWindow.TextRenderType """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) -> None """
        pass

    def wheelEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ wheelEvent(self, arg__1: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtGui_QWindow=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    AfterRenderingStage = PySide2.QtQuick.QQuickWindow.RenderStage.AfterRenderingStage
    AfterSwapStage = PySide2.QtQuick.QQuickWindow.RenderStage.AfterSwapStage
    AfterSynchronizingStage = PySide2.QtQuick.QQuickWindow.RenderStage.AfterSynchronizingStage
    BeforeRenderingStage = PySide2.QtQuick.QQuickWindow.RenderStage.BeforeRenderingStage
    BeforeSynchronizingStage = PySide2.QtQuick.QQuickWindow.RenderStage.BeforeSynchronizingStage
    ContextNotAvailable = PySide2.QtQuick.QQuickWindow.SceneGraphError.ContextNotAvailable
    CreateTextureOption = None # (!) real value is "<class 'PySide2.QtQuick.QQuickWindow.CreateTextureOption'>"
    CreateTextureOptions = None # (!) real value is "<class 'PySide2.QtQuick.QQuickWindow.CreateTextureOptions'>"
    NativeObjectTexture = PySide2.QtQuick.QQuickWindow.NativeObjectType.NativeObjectTexture
    NativeObjectType = None # (!) real value is "<class 'PySide2.QtQuick.QQuickWindow.NativeObjectType'>"
    NativeTextRendering = PySide2.QtQuick.QQuickWindow.TextRenderType.NativeTextRendering
    NoStage = PySide2.QtQuick.QQuickWindow.RenderStage.NoStage
    QtTextRendering = PySide2.QtQuick.QQuickWindow.TextRenderType.QtTextRendering
    RenderStage = None # (!) real value is "<class 'PySide2.QtQuick.QQuickWindow.RenderStage'>"
    SceneGraphError = None # (!) real value is "<class 'PySide2.QtQuick.QQuickWindow.SceneGraphError'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812AAD00>'
    TextRenderType = None # (!) real value is "<class 'PySide2.QtQuick.QQuickWindow.TextRenderType'>"
    TextureCanUseAtlas = PySide2.QtQuick.QQuickWindow.CreateTextureOption.TextureCanUseAtlas
    TextureHasAlphaChannel = PySide2.QtQuick.QQuickWindow.CreateTextureOption.TextureHasAlphaChannel
    TextureHasMipmaps = PySide2.QtQuick.QQuickWindow.CreateTextureOption.TextureHasMipmaps
    TextureIsOpaque = PySide2.QtQuick.QQuickWindow.CreateTextureOption.TextureIsOpaque
    TextureOwnsGLTexture = PySide2.QtQuick.QQuickWindow.CreateTextureOption.TextureOwnsGLTexture


class QQuickView(QQuickWindow):
    """
    QQuickView(self, engine: PySide2.QtQml.QQmlEngine, parent: PySide2.QtGui.QWindow) -> None
    QQuickView(self, parent: typing.Optional[PySide2.QtGui.QWindow] = None) -> None
    QQuickView(self, source: PySide2.QtCore.QUrl, parent: typing.Optional[PySide2.QtGui.QWindow] = None) -> None
    QQuickView(self, source: PySide2.QtCore.QUrl, renderControl: PySide2.QtQuick.QQuickRenderControl) -> None
    """
    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> PySide2.QtQml.QQmlEngine """
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> typing.List[PySide2.QtQml.QQmlError] """
        pass

    def initialSize(self): # real signature unknown; restored from __doc__
        """ initialSize(self) -> PySide2.QtCore.QSize """
        pass

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
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

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ resizeMode(self) -> PySide2.QtQuick.QQuickView.ResizeMode """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ rootContext(self) -> PySide2.QtQml.QQmlContext """
        pass

    def rootObject(self): # real signature unknown; restored from __doc__
        """ rootObject(self) -> PySide2.QtQuick.QQuickItem """
        pass

    def setContent(self, url, component, item): # real signature unknown; restored from __doc__
        """ setContent(self, url: PySide2.QtCore.QUrl, component: PySide2.QtQml.QQmlComponent, item: PySide2.QtCore.QObject) -> None """
        pass

    def setInitialProperties(self, initialProperties, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setInitialProperties(self, initialProperties: typing.Dict[str, typing.Any]) -> None """
        pass

    def setResizeMode(self, arg__1): # real signature unknown; restored from __doc__
        """ setResizeMode(self, arg__1: PySide2.QtQuick.QQuickView.ResizeMode) -> None """
        pass

    def setSource(self, arg__1): # real signature unknown; restored from __doc__
        """ setSource(self, arg__1: PySide2.QtCore.QUrl) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> PySide2.QtCore.QUrl """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtQuick.QQuickView.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, engine, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Error = PySide2.QtQuick.QQuickView.Status.Error
    Loading = PySide2.QtQuick.QQuickView.Status.Loading
    Null = PySide2.QtQuick.QQuickView.Status.Null
    Ready = PySide2.QtQuick.QQuickView.Status.Ready
    ResizeMode = None # (!) real value is "<class 'PySide2.QtQuick.QQuickView.ResizeMode'>"
    SizeRootObjectToView = PySide2.QtQuick.QQuickView.ResizeMode.SizeRootObjectToView
    SizeViewToRootObject = PySide2.QtQuick.QQuickView.ResizeMode.SizeViewToRootObject
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812AB440>'
    Status = None # (!) real value is "<class 'PySide2.QtQuick.QQuickView.Status'>"


class QSGAbstractRenderer(__PySide2_QtCore.QObject):
    """ QSGAbstractRenderer(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def clearColor(self): # real signature unknown; restored from __doc__
        """ clearColor(self) -> PySide2.QtGui.QColor """
        pass

    def clearMode(self): # real signature unknown; restored from __doc__
        """ clearMode(self) -> PySide2.QtQuick.QSGAbstractRenderer.ClearMode """
        pass

    def deviceRect(self): # real signature unknown; restored from __doc__
        """ deviceRect(self) -> PySide2.QtCore.QRect """
        pass

    def nodeChanged(self, node, state): # real signature unknown; restored from __doc__
        """ nodeChanged(self, node: PySide2.QtQuick.QSGNode, state: PySide2.QtQuick.QSGNode.DirtyState) -> None """
        pass

    def projectionMatrix(self): # real signature unknown; restored from __doc__
        """ projectionMatrix(self) -> PySide2.QtGui.QMatrix4x4 """
        pass

    def projectionMatrixWithNativeNDC(self): # real signature unknown; restored from __doc__
        """ projectionMatrixWithNativeNDC(self) -> PySide2.QtGui.QMatrix4x4 """
        pass

    def renderScene(self, fboId=0): # real signature unknown; restored from __doc__
        """ renderScene(self, fboId: int = 0) -> None """
        pass

    def sceneGraphChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setClearColor(self, color): # real signature unknown; restored from __doc__
        """ setClearColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setClearMode(self, mode): # real signature unknown; restored from __doc__
        """ setClearMode(self, mode: PySide2.QtQuick.QSGAbstractRenderer.ClearMode) -> None """
        pass

    def setDeviceRect(self, rect): # real signature unknown; restored from __doc__
        """
        setDeviceRect(self, rect: PySide2.QtCore.QRect) -> None
        setDeviceRect(self, size: PySide2.QtCore.QSize) -> None
        """
        pass

    def setProjectionMatrix(self, matrix): # real signature unknown; restored from __doc__
        """ setProjectionMatrix(self, matrix: PySide2.QtGui.QMatrix4x4) -> None """
        pass

    def setProjectionMatrixToRect(self, rect): # real signature unknown; restored from __doc__
        """
        setProjectionMatrixToRect(self, rect: PySide2.QtCore.QRectF) -> None
        setProjectionMatrixToRect(self, rect: PySide2.QtCore.QRectF, flags: PySide2.QtQuick.QSGAbstractRenderer.MatrixTransformFlags) -> None
        """
        pass

    def setProjectionMatrixWithNativeNDC(self, matrix): # real signature unknown; restored from __doc__
        """ setProjectionMatrixWithNativeNDC(self, matrix: PySide2.QtGui.QMatrix4x4) -> None """
        pass

    def setViewportRect(self, rect): # real signature unknown; restored from __doc__
        """
        setViewportRect(self, rect: PySide2.QtCore.QRect) -> None
        setViewportRect(self, size: PySide2.QtCore.QSize) -> None
        """
        pass

    def viewportRect(self): # real signature unknown; restored from __doc__
        """ viewportRect(self) -> PySide2.QtCore.QRect """
        pass

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

    ClearColorBuffer = PySide2.QtQuick.QSGAbstractRenderer.ClearModeBit.ClearColorBuffer
    ClearDepthBuffer = PySide2.QtQuick.QSGAbstractRenderer.ClearModeBit.ClearDepthBuffer
    ClearMode = None # (!) real value is "<class 'PySide2.QtQuick.QSGAbstractRenderer.ClearMode'>"
    ClearModeBit = None # (!) real value is "<class 'PySide2.QtQuick.QSGAbstractRenderer.ClearModeBit'>"
    ClearStencilBuffer = PySide2.QtQuick.QSGAbstractRenderer.ClearModeBit.ClearStencilBuffer
    MatrixTransformFlag = None # (!) real value is "<class 'PySide2.QtQuick.QSGAbstractRenderer.MatrixTransformFlag'>"
    MatrixTransformFlags = None # (!) real value is "<class 'PySide2.QtQuick.QSGAbstractRenderer.MatrixTransformFlags'>"
    MatrixTransformFlipY = PySide2.QtQuick.QSGAbstractRenderer.MatrixTransformFlag.MatrixTransformFlipY
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812B8EC0>'


class QSGNode(__Shiboken.Object):
    """
    QSGNode(self) -> None
    QSGNode(self, type: PySide2.QtQuick.QSGNode.NodeType) -> None
    """
    def appendChildNode(self, node): # real signature unknown; restored from __doc__
        """ appendChildNode(self, node: PySide2.QtQuick.QSGNode) -> None """
        pass

    def childAtIndex(self, i): # real signature unknown; restored from __doc__
        """ childAtIndex(self, i: int) -> PySide2.QtQuick.QSGNode """
        pass

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def clearDirty(self): # real signature unknown; restored from __doc__
        """ clearDirty(self) -> None """
        pass

    def dirtyState(self): # real signature unknown; restored from __doc__
        """ dirtyState(self) -> PySide2.QtQuick.QSGNode.DirtyState """
        pass

    def firstChild(self): # real signature unknown; restored from __doc__
        """ firstChild(self) -> PySide2.QtQuick.QSGNode """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtQuick.QSGNode.Flags """
        pass

    def insertChildNodeAfter(self, node, after): # real signature unknown; restored from __doc__
        """ insertChildNodeAfter(self, node: PySide2.QtQuick.QSGNode, after: PySide2.QtQuick.QSGNode) -> None """
        pass

    def insertChildNodeBefore(self, node, before): # real signature unknown; restored from __doc__
        """ insertChildNodeBefore(self, node: PySide2.QtQuick.QSGNode, before: PySide2.QtQuick.QSGNode) -> None """
        pass

    def isSubtreeBlocked(self): # real signature unknown; restored from __doc__
        """ isSubtreeBlocked(self) -> bool """
        return False

    def lastChild(self): # real signature unknown; restored from __doc__
        """ lastChild(self) -> PySide2.QtQuick.QSGNode """
        pass

    def markDirty(self, bits): # real signature unknown; restored from __doc__
        """ markDirty(self, bits: PySide2.QtQuick.QSGNode.DirtyState) -> None """
        pass

    def nextSibling(self): # real signature unknown; restored from __doc__
        """ nextSibling(self) -> PySide2.QtQuick.QSGNode """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> PySide2.QtQuick.QSGNode """
        pass

    def prependChildNode(self, node): # real signature unknown; restored from __doc__
        """ prependChildNode(self, node: PySide2.QtQuick.QSGNode) -> None """
        pass

    def preprocess(self): # real signature unknown; restored from __doc__
        """ preprocess(self) -> None """
        pass

    def previousSibling(self): # real signature unknown; restored from __doc__
        """ previousSibling(self) -> PySide2.QtQuick.QSGNode """
        pass

    def removeAllChildNodes(self): # real signature unknown; restored from __doc__
        """ removeAllChildNodes(self) -> None """
        pass

    def removeChildNode(self, node): # real signature unknown; restored from __doc__
        """ removeChildNode(self, node: PySide2.QtQuick.QSGNode) -> None """
        pass

    def reparentChildNodesTo(self, newParent): # real signature unknown; restored from __doc__
        """ reparentChildNodesTo(self, newParent: PySide2.QtQuick.QSGNode) -> None """
        pass

    def setFlag(self, arg__1, arg__2=True): # real signature unknown; restored from __doc__
        """ setFlag(self, arg__1: PySide2.QtQuick.QSGNode.Flag, arg__2: bool = True) -> None """
        pass

    def setFlags(self, arg__1, arg__2=True): # real signature unknown; restored from __doc__
        """ setFlags(self, arg__1: PySide2.QtQuick.QSGNode.Flags, arg__2: bool = True) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtQuick.QSGNode.NodeType """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
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

    BasicNodeType = PySide2.QtQuick.QSGNode.NodeType.BasicNodeType
    ClipNodeType = PySide2.QtQuick.QSGNode.NodeType.ClipNodeType
    DirtyForceUpdate = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtyForceUpdate
    DirtyGeometry = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtyGeometry
    DirtyMaterial = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtyMaterial
    DirtyMatrix = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtyMatrix
    DirtyNodeAdded = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtyNodeAdded
    DirtyNodeRemoved = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtyNodeRemoved
    DirtyOpacity = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtyOpacity
    DirtyPropagationMask = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtyPropagationMask
    DirtyState = None # (!) real value is "<class 'PySide2.QtQuick.QSGNode.DirtyState'>"
    DirtyStateBit = None # (!) real value is "<class 'PySide2.QtQuick.QSGNode.DirtyStateBit'>"
    DirtySubtreeBlocked = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtySubtreeBlocked
    DirtyUsePreprocess = PySide2.QtQuick.QSGNode.DirtyStateBit.DirtyUsePreprocess
    Flag = None # (!) real value is "<class 'PySide2.QtQuick.QSGNode.Flag'>"
    Flags = None # (!) real value is "<class 'PySide2.QtQuick.QSGNode.Flags'>"
    GeometryNodeType = PySide2.QtQuick.QSGNode.NodeType.GeometryNodeType
    IsVisitableNode = PySide2.QtQuick.QSGNode.Flag.IsVisitableNode
    NodeType = None # (!) real value is "<class 'PySide2.QtQuick.QSGNode.NodeType'>"
    OpacityNodeType = PySide2.QtQuick.QSGNode.NodeType.OpacityNodeType
    OwnedByParent = PySide2.QtQuick.QSGNode.Flag.OwnedByParent
    OwnsGeometry = PySide2.QtQuick.QSGNode.Flag.OwnsGeometry
    OwnsMaterial = PySide2.QtQuick.QSGNode.Flag.OwnsMaterial
    OwnsOpaqueMaterial = PySide2.QtQuick.QSGNode.Flag.OwnsOpaqueMaterial
    RenderNodeType = PySide2.QtQuick.QSGNode.NodeType.RenderNodeType
    RootNodeType = PySide2.QtQuick.QSGNode.NodeType.RootNodeType
    TransformNodeType = PySide2.QtQuick.QSGNode.NodeType.TransformNodeType
    UsePreprocess = PySide2.QtQuick.QSGNode.Flag.UsePreprocess


class QSGBasicGeometryNode(QSGNode):
    """ QSGBasicGeometryNode(self, type: PySide2.QtQuick.QSGNode.NodeType) -> None """
    def clipList(self): # real signature unknown; restored from __doc__
        """ clipList(self) -> PySide2.QtQuick.QSGClipNode """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> PySide2.QtQuick.QSGGeometry """
        pass

    def matrix(self): # real signature unknown; restored from __doc__
        """ matrix(self) -> PySide2.QtGui.QMatrix4x4 """
        pass

    def setGeometry(self, geometry): # real signature unknown; restored from __doc__
        """ setGeometry(self, geometry: PySide2.QtQuick.QSGGeometry) -> None """
        pass

    def setRendererClipList(self, c): # real signature unknown; restored from __doc__
        """ setRendererClipList(self, c: PySide2.QtQuick.QSGClipNode) -> None """
        pass

    def setRendererMatrix(self, m): # real signature unknown; restored from __doc__
        """ setRendererMatrix(self, m: PySide2.QtGui.QMatrix4x4) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QSGClipNode(QSGBasicGeometryNode):
    """ QSGClipNode(self) -> None """
    def clipRect(self): # real signature unknown; restored from __doc__
        """ clipRect(self) -> PySide2.QtCore.QRectF """
        pass

    def isRectangular(self): # real signature unknown; restored from __doc__
        """ isRectangular(self) -> bool """
        return False

    def setClipRect(self, arg__1): # real signature unknown; restored from __doc__
        """ setClipRect(self, arg__1: PySide2.QtCore.QRectF) -> None """
        pass

    def setIsRectangular(self, rectHint): # real signature unknown; restored from __doc__
        """ setIsRectangular(self, rectHint: bool) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QSGTexture(__PySide2_QtCore.QObject):
    """ QSGTexture(self) -> None """
    def anisotropyLevel(self): # real signature unknown; restored from __doc__
        """ anisotropyLevel(self) -> PySide2.QtQuick.QSGTexture.AnisotropyLevel """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> None """
        pass

    def comparisonKey(self): # real signature unknown; restored from __doc__
        """ comparisonKey(self) -> int """
        return 0

    def convertToNormalizedSourceRect(self, rect): # real signature unknown; restored from __doc__
        """ convertToNormalizedSourceRect(self, rect: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF """
        pass

    def filtering(self): # real signature unknown; restored from __doc__
        """ filtering(self) -> PySide2.QtQuick.QSGTexture.Filtering """
        pass

    def hasAlphaChannel(self): # real signature unknown; restored from __doc__
        """ hasAlphaChannel(self) -> bool """
        return False

    def hasMipmaps(self): # real signature unknown; restored from __doc__
        """ hasMipmaps(self) -> bool """
        return False

    def horizontalWrapMode(self): # real signature unknown; restored from __doc__
        """ horizontalWrapMode(self) -> PySide2.QtQuick.QSGTexture.WrapMode """
        pass

    def isAtlasTexture(self): # real signature unknown; restored from __doc__
        """ isAtlasTexture(self) -> bool """
        return False

    def mipmapFiltering(self): # real signature unknown; restored from __doc__
        """ mipmapFiltering(self) -> PySide2.QtQuick.QSGTexture.Filtering """
        pass

    def normalizedTextureSubRect(self): # real signature unknown; restored from __doc__
        """ normalizedTextureSubRect(self) -> PySide2.QtCore.QRectF """
        pass

    def removedFromAtlas(self): # real signature unknown; restored from __doc__
        """ removedFromAtlas(self) -> PySide2.QtQuick.QSGTexture """
        pass

    def setAnisotropyLevel(self, level): # real signature unknown; restored from __doc__
        """ setAnisotropyLevel(self, level: PySide2.QtQuick.QSGTexture.AnisotropyLevel) -> None """
        pass

    def setFiltering(self, filter): # real signature unknown; restored from __doc__
        """ setFiltering(self, filter: PySide2.QtQuick.QSGTexture.Filtering) -> None """
        pass

    def setHorizontalWrapMode(self, hwrap): # real signature unknown; restored from __doc__
        """ setHorizontalWrapMode(self, hwrap: PySide2.QtQuick.QSGTexture.WrapMode) -> None """
        pass

    def setMipmapFiltering(self, filter): # real signature unknown; restored from __doc__
        """ setMipmapFiltering(self, filter: PySide2.QtQuick.QSGTexture.Filtering) -> None """
        pass

    def setVerticalWrapMode(self, vwrap): # real signature unknown; restored from __doc__
        """ setVerticalWrapMode(self, vwrap: PySide2.QtQuick.QSGTexture.WrapMode) -> None """
        pass

    def textureId(self): # real signature unknown; restored from __doc__
        """ textureId(self) -> int """
        return 0

    def textureSize(self): # real signature unknown; restored from __doc__
        """ textureSize(self) -> PySide2.QtCore.QSize """
        pass

    def updateBindOptions(self, force=False): # real signature unknown; restored from __doc__
        """ updateBindOptions(self, force: bool = False) -> None """
        pass

    def verticalWrapMode(self): # real signature unknown; restored from __doc__
        """ verticalWrapMode(self) -> PySide2.QtQuick.QSGTexture.WrapMode """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Anisotropy16x = PySide2.QtQuick.QSGTexture.AnisotropyLevel.Anisotropy16x
    Anisotropy2x = PySide2.QtQuick.QSGTexture.AnisotropyLevel.Anisotropy2x
    Anisotropy4x = PySide2.QtQuick.QSGTexture.AnisotropyLevel.Anisotropy4x
    Anisotropy8x = PySide2.QtQuick.QSGTexture.AnisotropyLevel.Anisotropy8x
    AnisotropyLevel = None # (!) real value is "<class 'PySide2.QtQuick.QSGTexture.AnisotropyLevel'>"
    AnisotropyNone = PySide2.QtQuick.QSGTexture.AnisotropyLevel.AnisotropyNone
    ClampToEdge = PySide2.QtQuick.QSGTexture.WrapMode.ClampToEdge
    Filtering = None # (!) real value is "<class 'PySide2.QtQuick.QSGTexture.Filtering'>"
    Linear = PySide2.QtQuick.QSGTexture.Filtering.Linear
    MirroredRepeat = PySide2.QtQuick.QSGTexture.WrapMode.MirroredRepeat
    Nearest = PySide2.QtQuick.QSGTexture.Filtering.Nearest
    None_ = PySide2.QtQuick.QSGTexture.Filtering.None_
    Repeat = PySide2.QtQuick.QSGTexture.WrapMode.Repeat
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812ABEC0>'
    WrapMode = None # (!) real value is "<class 'PySide2.QtQuick.QSGTexture.WrapMode'>"


class QSGDynamicTexture(QSGTexture):
    """ QSGDynamicTexture(self) -> None """
    def updateTexture(self): # real signature unknown; restored from __doc__
        """ updateTexture(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812B8080>'


class QSGEngine(__PySide2_QtCore.QObject):
    """ QSGEngine(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def createRenderer(self): # real signature unknown; restored from __doc__
        """ createRenderer(self) -> PySide2.QtQuick.QSGAbstractRenderer """
        pass

    def createTextureFromId(self, id, size, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTextureFromId(self, id: int, size: PySide2.QtCore.QSize, options: PySide2.QtQuick.QSGEngine.CreateTextureOptions = Default(QSGEngine.CreateTextureOption)) -> PySide2.QtQuick.QSGTexture """
        pass

    def createTextureFromImage(self, image, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTextureFromImage(self, image: PySide2.QtGui.QImage, options: PySide2.QtQuick.QSGEngine.CreateTextureOptions = Default(QSGEngine.CreateTextureOption)) -> PySide2.QtQuick.QSGTexture """
        pass

    def initialize(self, context): # real signature unknown; restored from __doc__
        """ initialize(self, context: PySide2.QtGui.QOpenGLContext) -> None """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

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

    CreateTextureOption = None # (!) real value is "<class 'PySide2.QtQuick.QSGEngine.CreateTextureOption'>"
    CreateTextureOptions = None # (!) real value is "<class 'PySide2.QtQuick.QSGEngine.CreateTextureOptions'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812B8540>'
    TextureCanUseAtlas = PySide2.QtQuick.QSGEngine.CreateTextureOption.TextureCanUseAtlas
    TextureHasAlphaChannel = PySide2.QtQuick.QSGEngine.CreateTextureOption.TextureHasAlphaChannel
    TextureIsOpaque = PySide2.QtQuick.QSGEngine.CreateTextureOption.TextureIsOpaque
    TextureOwnsGLTexture = PySide2.QtQuick.QSGEngine.CreateTextureOption.TextureOwnsGLTexture


class QSGGeometry(__Shiboken.Object):
    """ QSGGeometry(self, attribs: PySide2.QtQuick.QSGGeometry.AttributeSet, vertexCount: int, indexCount: int = 0, indexType: int = <class 'int'>) -> None """
    def allocate(self, vertexCount, indexCount=0): # real signature unknown; restored from __doc__
        """ allocate(self, vertexCount: int, indexCount: int = 0) -> None """
        pass

    def attributeCount(self): # real signature unknown; restored from __doc__
        """ attributeCount(self) -> int """
        return 0

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> PySide2.QtQuick.QSGGeometry.Attribute """
        pass

    def defaultAttributes_ColoredPoint2D(self): # real signature unknown; restored from __doc__
        """ defaultAttributes_ColoredPoint2D() -> PySide2.QtQuick.QSGGeometry.AttributeSet """
        pass

    def defaultAttributes_Point2D(self): # real signature unknown; restored from __doc__
        """ defaultAttributes_Point2D() -> PySide2.QtQuick.QSGGeometry.AttributeSet """
        pass

    def defaultAttributes_TexturedPoint2D(self): # real signature unknown; restored from __doc__
        """ defaultAttributes_TexturedPoint2D() -> PySide2.QtQuick.QSGGeometry.AttributeSet """
        pass

    def drawingMode(self): # real signature unknown; restored from __doc__
        """ drawingMode(self) -> int """
        return 0

    def indexCount(self): # real signature unknown; restored from __doc__
        """ indexCount(self) -> int """
        return 0

    def indexData(self): # real signature unknown; restored from __doc__
        """ indexData(self) -> int """
        return 0

    def indexDataAsUInt(self): # real signature unknown; restored from __doc__
        """ indexDataAsUInt(self) -> typing.List[int] """
        pass

    def indexDataAsUShort(self): # real signature unknown; restored from __doc__
        """ indexDataAsUShort(self) -> typing.List[int] """
        pass

    def indexDataPattern(self): # real signature unknown; restored from __doc__
        """ indexDataPattern(self) -> PySide2.QtQuick.QSGGeometry.DataPattern """
        pass

    def indexType(self): # real signature unknown; restored from __doc__
        """ indexType(self) -> int """
        return 0

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> float """
        return 0.0

    def markIndexDataDirty(self): # real signature unknown; restored from __doc__
        """ markIndexDataDirty(self) -> None """
        pass

    def markVertexDataDirty(self): # real signature unknown; restored from __doc__
        """ markVertexDataDirty(self) -> None """
        pass

    def setDrawingMode(self, mode): # real signature unknown; restored from __doc__
        """ setDrawingMode(self, mode: int) -> None """
        pass

    def setIndexDataPattern(self, p): # real signature unknown; restored from __doc__
        """ setIndexDataPattern(self, p: PySide2.QtQuick.QSGGeometry.DataPattern) -> None """
        pass

    def setLineWidth(self, w): # real signature unknown; restored from __doc__
        """ setLineWidth(self, w: float) -> None """
        pass

    def setVertexDataPattern(self, p): # real signature unknown; restored from __doc__
        """ setVertexDataPattern(self, p: PySide2.QtQuick.QSGGeometry.DataPattern) -> None """
        pass

    def sizeOfIndex(self): # real signature unknown; restored from __doc__
        """ sizeOfIndex(self) -> int """
        return 0

    def sizeOfVertex(self): # real signature unknown; restored from __doc__
        """ sizeOfVertex(self) -> int """
        return 0

    def updateColoredRectGeometry(self, g, rect): # real signature unknown; restored from __doc__
        """ updateColoredRectGeometry(g: PySide2.QtQuick.QSGGeometry, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def updateRectGeometry(self, g, rect): # real signature unknown; restored from __doc__
        """ updateRectGeometry(g: PySide2.QtQuick.QSGGeometry, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def updateTexturedRectGeometry(self, g, rect, sourceRect): # real signature unknown; restored from __doc__
        """ updateTexturedRectGeometry(g: PySide2.QtQuick.QSGGeometry, rect: PySide2.QtCore.QRectF, sourceRect: PySide2.QtCore.QRectF) -> None """
        pass

    def vertexCount(self): # real signature unknown; restored from __doc__
        """ vertexCount(self) -> int """
        return 0

    def vertexData(self): # real signature unknown; restored from __doc__
        """ vertexData(self) -> int """
        return 0

    def vertexDataAsColoredPoint2D(self): # real signature unknown; restored from __doc__
        """ vertexDataAsColoredPoint2D(self) -> PySide2.QtQuick.QSGGeometry.ColoredPoint2D """
        pass

    def vertexDataAsPoint2D(self): # real signature unknown; restored from __doc__
        """ vertexDataAsPoint2D(self) -> PySide2.QtQuick.QSGGeometry.Point2D """
        pass

    def vertexDataAsTexturedPoint2D(self): # real signature unknown; restored from __doc__
        """ vertexDataAsTexturedPoint2D(self) -> PySide2.QtQuick.QSGGeometry.TexturedPoint2D """
        pass

    def vertexDataPattern(self): # real signature unknown; restored from __doc__
        """ vertexDataPattern(self) -> PySide2.QtQuick.QSGGeometry.DataPattern """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, attribs, vertexCount, indexCount=0, indexType, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AlwaysUploadPattern = PySide2.QtQuick.QSGGeometry.DataPattern.AlwaysUploadPattern
    Attribute = None # (!) real value is "<class 'PySide2.QtQuick.QSGGeometry.Attribute'>"
    AttributeSet = None # (!) real value is "<class 'PySide2.QtQuick.QSGGeometry.AttributeSet'>"
    AttributeType = None # (!) real value is "<class 'PySide2.QtQuick.QSGGeometry.AttributeType'>"
    Bytes2Type = PySide2.QtQuick.QSGGeometry.Type.Bytes2Type
    Bytes3Type = PySide2.QtQuick.QSGGeometry.Type.Bytes3Type
    Bytes4Type = PySide2.QtQuick.QSGGeometry.Type.Bytes4Type
    ByteType = PySide2.QtQuick.QSGGeometry.Type.ByteType
    ColorAttribute = PySide2.QtQuick.QSGGeometry.AttributeType.ColorAttribute
    ColoredPoint2D = None # (!) real value is "<class 'PySide2.QtQuick.QSGGeometry.ColoredPoint2D'>"
    DataPattern = None # (!) real value is "<class 'PySide2.QtQuick.QSGGeometry.DataPattern'>"
    DoubleType = PySide2.QtQuick.QSGGeometry.Type.DoubleType
    DrawingMode = None # (!) real value is "<class 'PySide2.QtQuick.QSGGeometry.DrawingMode'>"
    DrawLineLoop = PySide2.QtQuick.QSGGeometry.DrawingMode.DrawLineLoop
    DrawLines = PySide2.QtQuick.QSGGeometry.DrawingMode.DrawLines
    DrawLineStrip = PySide2.QtQuick.QSGGeometry.DrawingMode.DrawLineStrip
    DrawPoints = PySide2.QtQuick.QSGGeometry.DrawingMode.DrawPoints
    DrawTriangleFan = PySide2.QtQuick.QSGGeometry.DrawingMode.DrawTriangleFan
    DrawTriangles = PySide2.QtQuick.QSGGeometry.DrawingMode.DrawTriangles
    DrawTriangleStrip = PySide2.QtQuick.QSGGeometry.DrawingMode.DrawTriangleStrip
    DynamicPattern = PySide2.QtQuick.QSGGeometry.DataPattern.DynamicPattern
    FloatType = PySide2.QtQuick.QSGGeometry.Type.FloatType
    IntType = PySide2.QtQuick.QSGGeometry.Type.IntType
    Point2D = None # (!) real value is "<class 'PySide2.QtQuick.QSGGeometry.Point2D'>"
    PositionAttribute = PySide2.QtQuick.QSGGeometry.AttributeType.PositionAttribute
    ShortType = PySide2.QtQuick.QSGGeometry.Type.ShortType
    StaticPattern = PySide2.QtQuick.QSGGeometry.DataPattern.StaticPattern
    StreamPattern = PySide2.QtQuick.QSGGeometry.DataPattern.StreamPattern
    TexCoord1Attribute = PySide2.QtQuick.QSGGeometry.AttributeType.TexCoord1Attribute
    TexCoord2Attribute = PySide2.QtQuick.QSGGeometry.AttributeType.TexCoord2Attribute
    TexCoordAttribute = PySide2.QtQuick.QSGGeometry.AttributeType.TexCoordAttribute
    TexturedPoint2D = None # (!) real value is "<class 'PySide2.QtQuick.QSGGeometry.TexturedPoint2D'>"
    Type = None # (!) real value is "<class 'PySide2.QtQuick.QSGGeometry.Type'>"
    UnknownAttribute = PySide2.QtQuick.QSGGeometry.AttributeType.UnknownAttribute
    UnsignedByteType = PySide2.QtQuick.QSGGeometry.Type.UnsignedByteType
    UnsignedIntType = PySide2.QtQuick.QSGGeometry.Type.UnsignedIntType
    UnsignedShortType = PySide2.QtQuick.QSGGeometry.Type.UnsignedShortType


class QSGGeometryNode(QSGBasicGeometryNode):
    """ QSGGeometryNode(self) -> None """
    def inheritedOpacity(self): # real signature unknown; restored from __doc__
        """ inheritedOpacity(self) -> float """
        return 0.0

    def renderOrder(self): # real signature unknown; restored from __doc__
        """ renderOrder(self) -> int """
        return 0

    def setInheritedOpacity(self, opacity): # real signature unknown; restored from __doc__
        """ setInheritedOpacity(self, opacity: float) -> None """
        pass

    def setRenderOrder(self, order): # real signature unknown; restored from __doc__
        """ setRenderOrder(self, order: int) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
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


class QSGMaterialType(__Shiboken.Object):
    """ QSGMaterialType(self) -> None """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QSGOpacityNode(QSGNode):
    """ QSGOpacityNode(self) -> None """
    def combinedOpacity(self): # real signature unknown; restored from __doc__
        """ combinedOpacity(self) -> float """
        return 0.0

    def isSubtreeBlocked(self): # real signature unknown; restored from __doc__
        """ isSubtreeBlocked(self) -> bool """
        return False

    def opacity(self): # real signature unknown; restored from __doc__
        """ opacity(self) -> float """
        return 0.0

    def setCombinedOpacity(self, opacity): # real signature unknown; restored from __doc__
        """ setCombinedOpacity(self, opacity: float) -> None """
        pass

    def setOpacity(self, opacity): # real signature unknown; restored from __doc__
        """ setOpacity(self, opacity: float) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
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


class QSGSimpleRectNode(QSGGeometryNode):
    """
    QSGSimpleRectNode(self) -> None
    QSGSimpleRectNode(self, rect: PySide2.QtCore.QRectF, color: PySide2.QtGui.QColor) -> None
    """
    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> PySide2.QtGui.QColor """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> PySide2.QtCore.QRectF """
        pass

    def setColor(self, color): # real signature unknown; restored from __doc__
        """ setColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setRect(self, rect): # real signature unknown; restored from __doc__
        """
        setRect(self, rect: PySide2.QtCore.QRectF) -> None
        setRect(self, x: float, y: float, w: float, h: float) -> None
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QSGSimpleTextureNode(QSGGeometryNode):
    """ QSGSimpleTextureNode(self) -> None """
    def filtering(self): # real signature unknown; restored from __doc__
        """ filtering(self) -> PySide2.QtQuick.QSGTexture.Filtering """
        pass

    def ownsTexture(self): # real signature unknown; restored from __doc__
        """ ownsTexture(self) -> bool """
        return False

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> PySide2.QtCore.QRectF """
        pass

    def setFiltering(self, filtering): # real signature unknown; restored from __doc__
        """ setFiltering(self, filtering: PySide2.QtQuick.QSGTexture.Filtering) -> None """
        pass

    def setOwnsTexture(self, owns): # real signature unknown; restored from __doc__
        """ setOwnsTexture(self, owns: bool) -> None """
        pass

    def setRect(self, rect): # real signature unknown; restored from __doc__
        """
        setRect(self, rect: PySide2.QtCore.QRectF) -> None
        setRect(self, x: float, y: float, w: float, h: float) -> None
        """
        pass

    def setSourceRect(self, r): # real signature unknown; restored from __doc__
        """
        setSourceRect(self, r: PySide2.QtCore.QRectF) -> None
        setSourceRect(self, x: float, y: float, w: float, h: float) -> None
        """
        pass

    def setTexture(self, texture): # real signature unknown; restored from __doc__
        """ setTexture(self, texture: PySide2.QtQuick.QSGTexture) -> None """
        pass

    def setTextureCoordinatesTransform(self, mode): # real signature unknown; restored from __doc__
        """ setTextureCoordinatesTransform(self, mode: PySide2.QtQuick.QSGSimpleTextureNode.TextureCoordinatesTransformMode) -> None """
        pass

    def sourceRect(self): # real signature unknown; restored from __doc__
        """ sourceRect(self) -> PySide2.QtCore.QRectF """
        pass

    def texture(self): # real signature unknown; restored from __doc__
        """ texture(self) -> PySide2.QtQuick.QSGTexture """
        pass

    def textureCoordinatesTransform(self): # real signature unknown; restored from __doc__
        """ textureCoordinatesTransform(self) -> PySide2.QtQuick.QSGSimpleTextureNode.TextureCoordinatesTransformMode """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    MirrorHorizontally = PySide2.QtQuick.QSGSimpleTextureNode.TextureCoordinatesTransformFlag.MirrorHorizontally
    MirrorVertically = PySide2.QtQuick.QSGSimpleTextureNode.TextureCoordinatesTransformFlag.MirrorVertically
    NoTransform = PySide2.QtQuick.QSGSimpleTextureNode.TextureCoordinatesTransformFlag.NoTransform
    TextureCoordinatesTransformFlag = None # (!) real value is "<class 'PySide2.QtQuick.QSGSimpleTextureNode.TextureCoordinatesTransformFlag'>"
    TextureCoordinatesTransformMode = None # (!) real value is "<class 'PySide2.QtQuick.QSGSimpleTextureNode.TextureCoordinatesTransformMode'>"


class QSGTextureProvider(__PySide2_QtCore.QObject):
    """ QSGTextureProvider(self) -> None """
    def texture(self): # real signature unknown; restored from __doc__
        """ texture(self) -> PySide2.QtQuick.QSGTexture """
        pass

    def textureChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001F1812AB540>'


class QSGTransformNode(QSGNode):
    """ QSGTransformNode(self) -> None """
    def combinedMatrix(self): # real signature unknown; restored from __doc__
        """ combinedMatrix(self) -> PySide2.QtGui.QMatrix4x4 """
        pass

    def matrix(self): # real signature unknown; restored from __doc__
        """ matrix(self) -> PySide2.QtGui.QMatrix4x4 """
        pass

    def setCombinedMatrix(self, matrix): # real signature unknown; restored from __doc__
        """ setCombinedMatrix(self, matrix: PySide2.QtGui.QMatrix4x4) -> None """
        pass

    def setMatrix(self, matrix): # real signature unknown; restored from __doc__
        """ setMatrix(self, matrix: PySide2.QtGui.QMatrix4x4) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
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


class QSharedPointer<QQuickItemGrabResult >(__Shiboken.Object):
    # no doc
    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> PySide2.QtQuick.QQuickItemGrabResult """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F1805317B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtQuick', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F1805317B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtQuick.cp310-win_amd64.pyd')"

