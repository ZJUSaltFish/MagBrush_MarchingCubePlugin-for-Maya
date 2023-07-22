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

class QGraphicsTextItem(QGraphicsObject):
    """
    QGraphicsTextItem(parent: typing.Optional[QGraphicsItem] = None)
    QGraphicsTextItem(text: str, parent: typing.Optional[QGraphicsItem] = None)
    """
    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, point: Union[QPointF, QPoint]) -> bool """
        return False

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultTextColor(self): # real signature unknown; restored from __doc__
        """ defaultTextColor(self) -> QColor """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> QTextDocument """
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

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: QFocusEvent) """
        pass

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: QFocusEvent) """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
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

    def inputMethodEvent(self, event): # real signature unknown; restored from __doc__
        """ inputMethodEvent(self, event: QInputMethodEvent) """
        pass

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: Qt.InputMethodQuery) -> Any """
        pass

    def isObscuredBy(self, item): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, item: QGraphicsItem) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: QKeyEvent) """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: QKeyEvent) """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
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

    def linkHovered(self, *args, **kwargs): # real signature unknown
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

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def openExternalLinks(self): # real signature unknown; restored from __doc__
        """ openExternalLinks(self) -> bool """
        return False

    def paint(self, painter, option, widget): # real signature unknown; restored from __doc__
        """ paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget) """
        pass

    def prepareGeometryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
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

    def setDefaultTextColor(self, c, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setDefaultTextColor(self, c: Union[QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setDocument(self, document): # real signature unknown; restored from __doc__
        """ setDocument(self, document: QTextDocument) """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: QFont) """
        pass

    def setHtml(self, html): # real signature unknown; restored from __doc__
        """ setHtml(self, html: str) """
        pass

    def setOpenExternalLinks(self, open): # real signature unknown; restored from __doc__
        """ setOpenExternalLinks(self, open: bool) """
        pass

    def setPlainText(self, text): # real signature unknown; restored from __doc__
        """ setPlainText(self, text: str) """
        pass

    def setTabChangesFocus(self, b): # real signature unknown; restored from __doc__
        """ setTabChangesFocus(self, b: bool) """
        pass

    def setTextCursor(self, cursor): # real signature unknown; restored from __doc__
        """ setTextCursor(self, cursor: QTextCursor) """
        pass

    def setTextInteractionFlags(self, flags, Qt_TextInteractionFlags=None, Qt_TextInteractionFlag=None): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, flags: Union[Qt.TextInteractionFlags, Qt.TextInteractionFlag]) """
        pass

    def setTextWidth(self, width): # real signature unknown; restored from __doc__
        """ setTextWidth(self, width: float) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def tabChangesFocus(self): # real signature unknown; restored from __doc__
        """ tabChangesFocus(self) -> bool """
        return False

    def textCursor(self): # real signature unknown; restored from __doc__
        """ textCursor(self) -> QTextCursor """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> Qt.TextInteractionFlags """
        pass

    def textWidth(self): # real signature unknown; restored from __doc__
        """ textWidth(self) -> float """
        return 0.0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toHtml(self): # real signature unknown; restored from __doc__
        """ toHtml(self) -> str """
        return ""

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


