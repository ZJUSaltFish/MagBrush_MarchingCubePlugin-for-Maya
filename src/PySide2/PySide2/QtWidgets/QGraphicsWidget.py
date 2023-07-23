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

from .QGraphicsLayoutItem import QGraphicsLayoutItem

class QGraphicsWidget(QGraphicsObject, QGraphicsLayoutItem):
    """ QGraphicsWidget(self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = None, wFlags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def actions(self): # real signature unknown; restored from __doc__
        """ actions(self) -> typing.List[PySide2.QtWidgets.QAction] """
        pass

    def addAction(self, action): # real signature unknown; restored from __doc__
        """ addAction(self, action: PySide2.QtWidgets.QAction) -> None """
        pass

    def addActions(self, actions, PySide2_QtWidgets_QAction=None): # real signature unknown; restored from __doc__
        """ addActions(self, actions: typing.Sequence[PySide2.QtWidgets.QAction]) -> None """
        pass

    def adjustSize(self): # real signature unknown; restored from __doc__
        """ adjustSize(self) -> None """
        pass

    def autoFillBackground(self): # real signature unknown; restored from __doc__
        """ autoFillBackground(self) -> bool """
        return False

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRectF """
        pass

    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def closeEvent(self, event): # real signature unknown; restored from __doc__
        """ closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
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

    def focusPolicy(self): # real signature unknown; restored from __doc__
        """ focusPolicy(self) -> PySide2.QtCore.Qt.FocusPolicy """
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget(self) -> PySide2.QtWidgets.QGraphicsWidget """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> PySide2.QtGui.QFont """
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> typing.Tuple[float, float, float, float] """
        pass

    def getWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ getWindowFrameMargins(self) -> typing.Tuple[float, float, float, float] """
        pass

    def grabKeyboardEvent(self, event): # real signature unknown; restored from __doc__
        """ grabKeyboardEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def grabMouseEvent(self, event): # real signature unknown; restored from __doc__
        """ grabMouseEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def grabShortcut(self, sequence, context=None): # real signature unknown; restored from __doc__
        """ grabShortcut(self, sequence: PySide2.QtGui.QKeySequence, context: PySide2.QtCore.Qt.ShortcutContext = PySide2.QtCore.Qt.ShortcutContext.WindowShortcut) -> int """
        return 0

    def hideEvent(self, event): # real signature unknown; restored from __doc__
        """ hideEvent(self, event: PySide2.QtGui.QHideEvent) -> None """
        pass

    def hoverLeaveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverLeaveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneHoverEvent) -> None """
        pass

    def hoverMoveEvent(self, event): # real signature unknown; restored from __doc__
        """ hoverMoveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneHoverEvent) -> None """
        pass

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOption) -> None """
        pass

    def insertAction(self, before, action): # real signature unknown; restored from __doc__
        """ insertAction(self, before: PySide2.QtWidgets.QAction, action: PySide2.QtWidgets.QAction) -> None """
        pass

    def insertActions(self, before, actions, PySide2_QtWidgets_QAction=None): # real signature unknown; restored from __doc__
        """ insertActions(self, before: PySide2.QtWidgets.QAction, actions: typing.Sequence[PySide2.QtWidgets.QAction]) -> None """
        pass

    def isActiveWindow(self): # real signature unknown; restored from __doc__
        """ isActiveWindow(self) -> bool """
        return False

    def itemChange(self, change, value): # real signature unknown; restored from __doc__
        """ itemChange(self, change: PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange, value: typing.Any) -> typing.Any """
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> PySide2.QtWidgets.QGraphicsLayout """
        pass

    def layoutChanged(self, *args, **kwargs): # real signature unknown
        pass

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection(self) -> PySide2.QtCore.Qt.LayoutDirection """
        pass

    def moveEvent(self, event): # real signature unknown; restored from __doc__
        """ moveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMoveEvent) -> None """
        pass

    def paint(self, painter, option, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def paintWindowFrame(self, painter, option, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paintWindowFrame(self, painter: PySide2.QtGui.QPainter, option: PySide2.QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette(self) -> PySide2.QtGui.QPalette """
        pass

    def polishEvent(self): # real signature unknown; restored from __doc__
        """ polishEvent(self) -> None """
        pass

    def propertyChange(self, propertyName, value): # real signature unknown; restored from __doc__
        """ propertyChange(self, propertyName: str, value: typing.Any) -> typing.Any """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> PySide2.QtCore.QRectF """
        pass

    def releaseShortcut(self, id): # real signature unknown; restored from __doc__
        """ releaseShortcut(self, id: int) -> None """
        pass

    def removeAction(self, action): # real signature unknown; restored from __doc__
        """ removeAction(self, action: PySide2.QtWidgets.QAction) -> None """
        pass

    def resize(self, size): # real signature unknown; restored from __doc__
        """
        resize(self, size: PySide2.QtCore.QSizeF) -> None
        resize(self, w: float, h: float) -> None
        """
        pass

    def resizeEvent(self, event): # real signature unknown; restored from __doc__
        """ resizeEvent(self, event: PySide2.QtWidgets.QGraphicsSceneResizeEvent) -> None """
        pass

    def sceneEvent(self, event): # real signature unknown; restored from __doc__
        """ sceneEvent(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def setAttribute(self, attribute, on=True): # real signature unknown; restored from __doc__
        """ setAttribute(self, attribute: PySide2.QtCore.Qt.WidgetAttribute, on: bool = True) -> None """
        pass

    def setAutoFillBackground(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoFillBackground(self, enabled: bool) -> None """
        pass

    def setContentsMargins(self, left, top, right, bottom): # real signature unknown; restored from __doc__
        """
        setContentsMargins(self, left: float, top: float, right: float, bottom: float) -> None
        setContentsMargins(self, margins: PySide2.QtCore.QMarginsF) -> None
        """
        pass

    def setFocusPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setFocusPolicy(self, policy: PySide2.QtCore.Qt.FocusPolicy) -> None """
        pass

    def setFont(self, font): # real signature unknown; restored from __doc__
        """ setFont(self, font: PySide2.QtGui.QFont) -> None """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """
        setGeometry(self, rect: PySide2.QtCore.QRectF) -> None
        setGeometry(self, x: float, y: float, w: float, h: float) -> None
        """
        pass

    def setLayout(self, layout): # real signature unknown; restored from __doc__
        """ setLayout(self, layout: PySide2.QtWidgets.QGraphicsLayout) -> None """
        pass

    def setLayoutDirection(self, direction): # real signature unknown; restored from __doc__
        """ setLayoutDirection(self, direction: PySide2.QtCore.Qt.LayoutDirection) -> None """
        pass

    def setPalette(self, palette): # real signature unknown; restored from __doc__
        """ setPalette(self, palette: PySide2.QtGui.QPalette) -> None """
        pass

    def setShortcutAutoRepeat(self, id, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutAutoRepeat(self, id: int, enabled: bool = True) -> None """
        pass

    def setShortcutEnabled(self, id, enabled=True): # real signature unknown; restored from __doc__
        """ setShortcutEnabled(self, id: int, enabled: bool = True) -> None """
        pass

    def setStyle(self, style): # real signature unknown; restored from __doc__
        """ setStyle(self, style: PySide2.QtWidgets.QStyle) -> None """
        pass

    def setTabOrder(self, first, second): # real signature unknown; restored from __doc__
        """ setTabOrder(first: PySide2.QtWidgets.QGraphicsWidget, second: PySide2.QtWidgets.QGraphicsWidget) -> None """
        pass

    def setWindowFlags(self, wFlags): # real signature unknown; restored from __doc__
        """ setWindowFlags(self, wFlags: PySide2.QtCore.Qt.WindowFlags) -> None """
        pass

    def setWindowFrameMargins(self, left, top, right, bottom): # real signature unknown; restored from __doc__
        """
        setWindowFrameMargins(self, left: float, top: float, right: float, bottom: float) -> None
        setWindowFrameMargins(self, margins: PySide2.QtCore.QMarginsF) -> None
        """
        pass

    def setWindowTitle(self, title): # real signature unknown; restored from __doc__
        """ setWindowTitle(self, title: str) -> None """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> PySide2.QtGui.QPainterPath """
        pass

    def showEvent(self, event): # real signature unknown; restored from __doc__
        """ showEvent(self, event: PySide2.QtGui.QShowEvent) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSizeF """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: PySide2.QtCore.Qt.SizeHint, constraint: PySide2.QtCore.QSizeF = Default(QSizeF)) -> PySide2.QtCore.QSizeF """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> PySide2.QtWidgets.QStyle """
        pass

    def testAttribute(self, attribute): # real signature unknown; restored from __doc__
        """ testAttribute(self, attribute: PySide2.QtCore.Qt.WidgetAttribute) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def ungrabKeyboardEvent(self, event): # real signature unknown; restored from __doc__
        """ ungrabKeyboardEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def ungrabMouseEvent(self, event): # real signature unknown; restored from __doc__
        """ ungrabMouseEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def unsetLayoutDirection(self): # real signature unknown; restored from __doc__
        """ unsetLayoutDirection(self) -> None """
        pass

    def unsetWindowFrameMargins(self): # real signature unknown; restored from __doc__
        """ unsetWindowFrameMargins(self) -> None """
        pass

    def updateGeometry(self): # real signature unknown; restored from __doc__
        """ updateGeometry(self) -> None """
        pass

    def windowFlags(self): # real signature unknown; restored from __doc__
        """ windowFlags(self) -> PySide2.QtCore.Qt.WindowFlags """
        pass

    def windowFrameEvent(self, e): # real signature unknown; restored from __doc__
        """ windowFrameEvent(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def windowFrameGeometry(self): # real signature unknown; restored from __doc__
        """ windowFrameGeometry(self) -> PySide2.QtCore.QRectF """
        pass

    def windowFrameRect(self): # real signature unknown; restored from __doc__
        """ windowFrameRect(self) -> PySide2.QtCore.QRectF """
        pass

    def windowFrameSectionAt(self, pos): # real signature unknown; restored from __doc__
        """ windowFrameSectionAt(self, pos: PySide2.QtCore.QPointF) -> PySide2.QtCore.Qt.WindowFrameSection """
        pass

    def windowTitle(self): # real signature unknown; restored from __doc__
        """ windowTitle(self) -> str """
        return ""

    def windowType(self): # real signature unknown; restored from __doc__
        """ windowType(self) -> PySide2.QtCore.Qt.WindowType """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50859180>'


