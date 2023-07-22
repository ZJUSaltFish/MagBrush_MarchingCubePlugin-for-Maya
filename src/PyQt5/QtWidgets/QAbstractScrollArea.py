# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QFrame import QFrame

class QAbstractScrollArea(QFrame):
    """ QAbstractScrollArea(parent: typing.Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addScrollBarWidget(self, widget, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ addScrollBarWidget(self, widget: QWidget, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, a0): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, a0: QContextMenuEvent) """
        pass

    def cornerWidget(self): # real signature unknown; restored from __doc__
        """ cornerWidget(self) -> QWidget """
        return QWidget

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, a0): # real signature unknown; restored from __doc__
        """ dragEnterEvent(self, a0: QDragEnterEvent) """
        pass

    def dragLeaveEvent(self, a0): # real signature unknown; restored from __doc__
        """ dragLeaveEvent(self, a0: QDragLeaveEvent) """
        pass

    def dragMoveEvent(self, a0): # real signature unknown; restored from __doc__
        """ dragMoveEvent(self, a0: QDragMoveEvent) """
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, a0): # real signature unknown; restored from __doc__
        """ dropEvent(self, a0: QDropEvent) """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0): # real signature unknown; restored from __doc__
        """ event(self, a0: QEvent) -> bool """
        return False

    def eventFilter(self, a0, a1): # real signature unknown; restored from __doc__
        """ eventFilter(self, a0: QObject, a1: QEvent) -> bool """
        return False

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalScrollBar(self): # real signature unknown; restored from __doc__
        """ horizontalScrollBar(self) -> QScrollBar """
        return QScrollBar

    def horizontalScrollBarPolicy(self): # real signature unknown; restored from __doc__
        """ horizontalScrollBarPolicy(self) -> Qt.ScrollBarPolicy """
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, a0): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maximumViewportSize(self): # real signature unknown; restored from __doc__
        """ maximumViewportSize(self) -> QSize """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, a0): # real signature unknown; restored from __doc__
        """ mouseDoubleClickEvent(self, a0: QMouseEvent) """
        pass

    def mouseMoveEvent(self, a0): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, a0: QMouseEvent) """
        pass

    def mousePressEvent(self, a0): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, a0: QMouseEvent) """
        pass

    def mouseReleaseEvent(self, a0): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, a0: QMouseEvent) """
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, a0): # real signature unknown; restored from __doc__
        """ paintEvent(self, a0: QPaintEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, a0): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: QResizeEvent) """
        pass

    def scrollBarWidgets(self, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ scrollBarWidgets(self, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) -> List[QWidget] """
        return []

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCornerWidget(self, widget): # real signature unknown; restored from __doc__
        """ setCornerWidget(self, widget: QWidget) """
        pass

    def setHorizontalScrollBar(self, scrollbar): # real signature unknown; restored from __doc__
        """ setHorizontalScrollBar(self, scrollbar: QScrollBar) """
        pass

    def setHorizontalScrollBarPolicy(self, a0): # real signature unknown; restored from __doc__
        """ setHorizontalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy) """
        pass

    def setSizeAdjustPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setSizeAdjustPolicy(self, policy: QAbstractScrollArea.SizeAdjustPolicy) """
        pass

    def setupViewport(self, viewport): # real signature unknown; restored from __doc__
        """ setupViewport(self, viewport: QWidget) """
        pass

    def setVerticalScrollBar(self, scrollbar): # real signature unknown; restored from __doc__
        """ setVerticalScrollBar(self, scrollbar: QScrollBar) """
        pass

    def setVerticalScrollBarPolicy(self, a0): # real signature unknown; restored from __doc__
        """ setVerticalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy) """
        pass

    def setViewport(self, widget): # real signature unknown; restored from __doc__
        """ setViewport(self, widget: QWidget) """
        pass

    def setViewportMargins(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setViewportMargins(self, left: int, top: int, right: int, bottom: int)
        setViewportMargins(self, margins: QMargins)
        """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeAdjustPolicy(self): # real signature unknown; restored from __doc__
        """ sizeAdjustPolicy(self) -> QAbstractScrollArea.SizeAdjustPolicy """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def verticalScrollBar(self): # real signature unknown; restored from __doc__
        """ verticalScrollBar(self) -> QScrollBar """
        return QScrollBar

    def verticalScrollBarPolicy(self): # real signature unknown; restored from __doc__
        """ verticalScrollBarPolicy(self) -> Qt.ScrollBarPolicy """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> QWidget """
        return QWidget

    def viewportEvent(self, a0): # real signature unknown; restored from __doc__
        """ viewportEvent(self, a0: QEvent) -> bool """
        return False

    def viewportMargins(self): # real signature unknown; restored from __doc__
        """ viewportMargins(self) -> QMargins """
        pass

    def viewportSizeHint(self): # real signature unknown; restored from __doc__
        """ viewportSizeHint(self) -> QSize """
        pass

    def wheelEvent(self, a0): # real signature unknown; restored from __doc__
        """ wheelEvent(self, a0: QWheelEvent) """
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AdjustIgnored = 0
    AdjustToContents = 2
    AdjustToContentsOnFirstShow = 1


