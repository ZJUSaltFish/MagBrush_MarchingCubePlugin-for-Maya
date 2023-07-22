# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QGraphicsObject import QGraphicsObject

class QGraphicsTextItem(QGraphicsObject):
    """
    QGraphicsTextItem(self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None
    QGraphicsTextItem(self, text: str, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None) -> None
    """
    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) -> None """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def contains(self, point): # real signature unknown; restored from __doc__
        """ contains(self, point: PySide2.QtCore.QPointF) -> bool """
        return False

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: PySide2.QtWidgets.QGraphicsSceneContextMenuEvent) -> None """
        pass

    def defaultTextColor(self): # real signature unknown; restored from __doc__
        """ defaultTextColor(self) -> PySide2.QtGui.QColor """
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> PySide2.QtGui.QTextDocument """
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

    def extension(self, variant): # real signature unknown; restored from __doc__
        """ extension(self, variant: typing.Any) -> typing.Any """
        pass

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
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

    def inputMethodQuery(self, query): # real signature unknown; restored from __doc__
        """ inputMethodQuery(self, query: PySide2.QtCore.Qt.InputMethodQuery) -> typing.Any """
        pass

    def isObscuredBy(self, item): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, item: PySide2.QtWidgets.QGraphicsItem) -> bool """
        return False

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
        pass

    def linkHovered(self, *args, **kwargs): # real signature unknown
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

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> PySide2.QtGui.QPainterPath """
        pass

    def openExternalLinks(self): # real signature unknown; restored from __doc__
        """ openExternalLinks(self) -> bool """
        return False

    def paint(self, painter, option, widget): # real signature unknown; restored from __doc__
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def sceneEvent(self, event): # real signature unknown; restored from __doc__
        """ sceneEvent(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def setDefaultTextColor(self, c): # real signature unknown; restored from __doc__
        """ setDefaultTextColor(self, c: PySide2.QtGui.QColor) -> None """
        pass

    def setDocument(self, document): # real signature unknown; restored from __doc__
        """ setDocument(self, document: PySide2.QtGui.QTextDocument) -> None """
        pass

    def setExtension(self, extension, variant): # real signature unknown; restored from __doc__
        """ setExtension(self, extension: PySide2.QtWidgets.QGraphicsItem.Extension, variant: typing.Any) -> None """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: PySide2.QtGui.QFont) -> None """
        pass

    def setHtml(self, html): # real signature unknown; restored from __doc__
        """ setHtml(self, html: str) -> None """
        pass

    def setOpenExternalLinks(self, open): # real signature unknown; restored from __doc__
        """ setOpenExternalLinks(self, open: bool) -> None """
        pass

    def setPlainText(self, text): # real signature unknown; restored from __doc__
        """ setPlainText(self, text: str) -> None """
        pass

    def setTabChangesFocus(self, b): # real signature unknown; restored from __doc__
        """ setTabChangesFocus(self, b: bool) -> None """
        pass

    def setTextCursor(self, cursor): # real signature unknown; restored from __doc__
        """ setTextCursor(self, cursor: PySide2.QtGui.QTextCursor) -> None """
        pass

    def setTextInteractionFlags(self, flags): # real signature unknown; restored from __doc__
        """ setTextInteractionFlags(self, flags: PySide2.QtCore.Qt.TextInteractionFlags) -> None """
        pass

    def setTextWidth(self, width): # real signature unknown; restored from __doc__
        """ setTextWidth(self, width: float) -> None """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> PySide2.QtGui.QPainterPath """
        pass

    def supportsExtension(self, extension): # real signature unknown; restored from __doc__
        """ supportsExtension(self, extension: PySide2.QtWidgets.QGraphicsItem.Extension) -> bool """
        return False

    def tabChangesFocus(self): # real signature unknown; restored from __doc__
        """ tabChangesFocus(self) -> bool """
        return False

    def textCursor(self): # real signature unknown; restored from __doc__
        """ textCursor(self) -> PySide2.QtGui.QTextCursor """
        pass

    def textInteractionFlags(self): # real signature unknown; restored from __doc__
        """ textInteractionFlags(self) -> PySide2.QtCore.Qt.TextInteractionFlags """
        pass

    def textWidth(self): # real signature unknown; restored from __doc__
        """ textWidth(self) -> float """
        return 0.0

    def toHtml(self): # real signature unknown; restored from __doc__
        """ toHtml(self) -> str """
        return ""

    def toPlainText(self): # real signature unknown; restored from __doc__
        """ toPlainText(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QGraphicsItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50859380>'


