# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QGraphicsWidget import QGraphicsWidget

class QGraphicsProxyWidget(QGraphicsWidget):
    """ QGraphicsProxyWidget(self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None, wFlags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: PySide2.QtWidgets.QGraphicsSceneContextMenuEvent) -> None """
        pass

    def createProxyForChildWidget(self, child): # real signature unknown; restored from __doc__
        """ createProxyForChildWidget(self, child: PySide2.QtWidgets.QWidget) -> PySide2.QtWidgets.QGraphicsProxyWidget """
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

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, p_object, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, object: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def focusInEvent(self, event): # real signature unknown; restored from __doc__
        """ focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusNextPrevChild(self, next): # real signature unknown; restored from __doc__
        """ focusNextPrevChild(self, next: bool) -> bool """
        return False

    def focusOutEvent(self, event): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def grabMouseEvent(self, event): # real signature unknown; restored from __doc__
        """ grabMouseEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def hideEvent(self, event): # real signature unknown; restored from __doc__
        """ hideEvent(self, event: PySide2.QtGui.QHideEvent) -> None """
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

    def itemChange(self, change, value): # real signature unknown; restored from __doc__
        """ itemChange(self, change: PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange, value: typing.Any) -> typing.Any """
        pass

    def keyPressEvent(self, event): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, event): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent) -> None """
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

    def newProxyWidget(self, arg__1): # real signature unknown; restored from __doc__
        """ newProxyWidget(self, arg__1: PySide2.QtWidgets.QWidget) -> PySide2.QtWidgets.QGraphicsProxyWidget """
        pass

    def paint(self, painter, option, widget): # real signature unknown; restored from __doc__
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtWidgets.QGraphicsSceneResizeEvent) -> None """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def setWidget(self, widget): # real signature unknown; restored from __doc__
        """ setWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: PySide2.QtCore.Qt.SizeHint, constraint: PySide2.QtCore.QSizeF = Default(QSizeF)) -> PySide2.QtCore.QSizeF """
        pass

    def subWidgetRect(self, widget): # real signature unknown; restored from __doc__
        """ subWidgetRect(self, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtCore.QRectF """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabMouseEvent(self, event): # real signature unknown; restored from __doc__
        """ ungrabMouseEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: PySide2.QtWidgets.QGraphicsSceneWheelEvent) -> None """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> PySide2.QtWidgets.QWidget """
        pass

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50859300>'


