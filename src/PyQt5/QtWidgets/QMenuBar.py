# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QMenuBar(QWidget):
    """ QMenuBar(parent: typing.Optional[QWidget] = None) """
    def actionAt(self, a0): # real signature unknown; restored from __doc__
        """ actionAt(self, a0: QPoint) -> QAction """
        return QAction

    def actionEvent(self, a0): # real signature unknown; restored from __doc__
        """ actionEvent(self, a0: QActionEvent) """
        pass

    def actionGeometry(self, a0): # real signature unknown; restored from __doc__
        """ actionGeometry(self, a0: QAction) -> QRect """
        pass

    def activeAction(self): # real signature unknown; restored from __doc__
        """ activeAction(self) -> QAction """
        return QAction

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addAction(self, action: QAction)
        addAction(self, text: str) -> QAction
        addAction(self, text: str, slot: PYQT_SLOT) -> QAction
        """
        return QAction

    def addMenu(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addMenu(self, menu: QMenu) -> QAction
        addMenu(self, title: str) -> QMenu
        addMenu(self, icon: QIcon, title: str) -> QMenu
        """
        return QAction or QMenu

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> QAction """
        return QAction

    def changeEvent(self, a0): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cornerWidget(self, corner=None): # real signature unknown; restored from __doc__
        """ cornerWidget(self, corner: Qt.Corner = Qt.TopRightCorner) -> QWidget """
        return QWidget

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0): # real signature unknown; restored from __doc__
        """ event(self, a0: QEvent) -> bool """
        return False

    def eventFilter(self, a0, a1): # real signature unknown; restored from __doc__
        """ eventFilter(self, a0: QObject, a1: QEvent) -> bool """
        return False

    def focusInEvent(self, a0): # real signature unknown; restored from __doc__
        """ focusInEvent(self, a0: QFocusEvent) """
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, a0): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, a0: QFocusEvent) """
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def heightForWidth(self, a0): # real signature unknown; restored from __doc__
        """ heightForWidth(self, a0: int) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
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

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option, action): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: QStyleOptionMenuItem, action: QAction) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertMenu(self, before, menu): # real signature unknown; restored from __doc__
        """ insertMenu(self, before: QAction, menu: QMenu) -> QAction """
        return QAction

    def insertSeparator(self, before): # real signature unknown; restored from __doc__
        """ insertSeparator(self, before: QAction) -> QAction """
        return QAction

    def isDefaultUp(self): # real signature unknown; restored from __doc__
        """ isDefaultUp(self) -> bool """
        return False

    def isNativeMenuBar(self): # real signature unknown; restored from __doc__
        """ isNativeMenuBar(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, a0): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, a0: QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, a0): # real signature unknown; restored from __doc__
        """ leaveEvent(self, a0: QEvent) """
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveAction(self, action): # real signature unknown; restored from __doc__
        """ setActiveAction(self, action: QAction) """
        pass

    def setCornerWidget(self, widget, corner=None): # real signature unknown; restored from __doc__
        """ setCornerWidget(self, widget: QWidget, corner: Qt.Corner = Qt.TopRightCorner) """
        pass

    def setDefaultUp(self, a0): # real signature unknown; restored from __doc__
        """ setDefaultUp(self, a0: bool) """
        pass

    def setNativeMenuBar(self, nativeMenuBar): # real signature unknown; restored from __doc__
        """ setNativeMenuBar(self, nativeMenuBar: bool) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, a0): # real signature unknown; restored from __doc__
        """ timerEvent(self, a0: QTimerEvent) """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
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

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


