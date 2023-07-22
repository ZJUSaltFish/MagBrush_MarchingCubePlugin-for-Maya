# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsWidget import QGraphicsWidget

class QGraphicsProxyWidget(QGraphicsWidget):
    """ QGraphicsProxyWidget(parent: typing.Optional[QGraphicsItem] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent) """
        pass

    def createProxyForChildWidget(self, child): # real signature unknown; restored from __doc__
        """ createProxyForChildWidget(self, child: QWidget) -> QGraphicsProxyWidget """
        return QGraphicsProxyWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
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

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: QGraphicsSceneDragDropEvent) """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: QEvent) -> bool """
        return False

    def eventFilter(self, p_object, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, object: QObject, event: QEvent) -> bool """
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

    def grabKeyboardEvent(self, *args, **kwargs): # real signature unknown
        pass

    def grabMouseEvent(self, event): # real signature unknown; restored from __doc__
        """ grabMouseEvent(self, event: QEvent) """
        pass

    def hideEvent(self, event): # real signature unknown; restored from __doc__
        """ hideEvent(self, event: QHideEvent) """
        pass

    def hoverEnterEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverEnterEvent(self, event: QGraphicsSceneHoverEvent) """
        pass

    def hoverLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, event: QGraphicsSceneHoverEvent) """
        pass

    def hoverMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, event: QGraphicsSceneHoverEvent) """
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, event): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: QInputMethodEvent) """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: Qt.InputMethodQuery) -> Any """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, change, value): # real signature unknown; restored from __doc__
        """ itemChange(self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: QKeyEvent) """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: QKeyEvent) """
        pass

    def mouseDoubleClickEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) """
        pass

    def mouseMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) """
        pass

    def mousePressEvent(self, event): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, event: QGraphicsSceneMouseEvent) """
        pass

    def mouseReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def newProxyWidget(self, a0): # real signature unknown; restored from __doc__
        """ newProxyWidget(self, a0: QWidget) -> QGraphicsProxyWidget """
        return QGraphicsProxyWidget

    def paint(self, painter, option, widget): # real signature unknown; restored from __doc__
        """ paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget) """
        pass

    def polishEvent(self, *args, **kwargs): # real signature unknown
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: QGraphicsSceneResizeEvent) """
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: QRectF) """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setWidget(self, widget): # real signature unknown; restored from __doc__
        """ setWidget(self, widget: QWidget) """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: QShowEvent) """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def subWidgetRect(self, widget): # real signature unknown; restored from __doc__
        """ subWidgetRect(self, widget: QWidget) -> QRectF """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboardEvent(self, *args, **kwargs): # real signature unknown
        pass

    def ungrabMouseEvent(self, event): # real signature unknown; restored from __doc__
        """ ungrabMouseEvent(self, event: QEvent) """
        pass

    def updateGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: QGraphicsSceneWheelEvent) """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> QWidget """
        return QWidget

    def windowFrameEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowFrameSectionAt(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


