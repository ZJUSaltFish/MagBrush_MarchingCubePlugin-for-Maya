# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractScrollArea import QAbstractScrollArea

class QMdiArea(QAbstractScrollArea):
    """ QMdiArea(parent: typing.Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def activateNextSubWindow(self): # real signature unknown; restored from __doc__
        """ activateNextSubWindow(self) """
        pass

    def activatePreviousSubWindow(self): # real signature unknown; restored from __doc__
        """ activatePreviousSubWindow(self) """
        pass

    def activationOrder(self): # real signature unknown; restored from __doc__
        """ activationOrder(self) -> QMdiArea.WindowOrder """
        pass

    def activeSubWindow(self): # real signature unknown; restored from __doc__
        """ activeSubWindow(self) -> QMdiSubWindow """
        return QMdiSubWindow

    def addSubWindow(self, widget, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addSubWindow(self, widget: QWidget, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> QMdiSubWindow """
        pass

    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> QBrush """
        pass

    def cascadeSubWindows(self): # real signature unknown; restored from __doc__
        """ cascadeSubWindows(self) """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, childEvent): # real signature unknown; restored from __doc__
        """ childEvent(self, childEvent: QChildEvent) """
        pass

    def closeActiveSubWindow(self): # real signature unknown; restored from __doc__
        """ closeActiveSubWindow(self) """
        pass

    def closeAllSubWindows(self): # real signature unknown; restored from __doc__
        """ closeAllSubWindows(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentSubWindow(self): # real signature unknown; restored from __doc__
        """ currentSubWindow(self) -> QMdiSubWindow """
        return QMdiSubWindow

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentMode(self): # real signature unknown; restored from __doc__
        """ documentMode(self) -> bool """
        return False

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawFrame(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: QEvent) -> bool """
        return False

    def eventFilter(self, p_object, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, object: QObject, event: QEvent) -> bool """
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

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, paintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, paintEvent: QPaintEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeSubWindow(self, widget): # real signature unknown; restored from __doc__
        """ removeSubWindow(self, widget: QWidget) """
        pass

    def resizeEvent(self, resizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, resizeEvent: QResizeEvent) """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActivationOrder(self, order): # real signature unknown; restored from __doc__
        """ setActivationOrder(self, order: QMdiArea.WindowOrder) """
        pass

    def setActiveSubWindow(self, window): # real signature unknown; restored from __doc__
        """ setActiveSubWindow(self, window: QMdiSubWindow) """
        pass

    def setBackground(self, background, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None): # real signature unknown; restored from __doc__
        """ setBackground(self, background: Union[QBrush, QColor, Qt.GlobalColor, QGradient]) """
        pass

    def setDocumentMode(self, enabled): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, enabled: bool) """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: QMdiArea.AreaOption, on: bool = True) """
        pass

    def setTabPosition(self, position): # real signature unknown; restored from __doc__
        """ setTabPosition(self, position: QTabWidget.TabPosition) """
        pass

    def setTabsClosable(self, closable): # real signature unknown; restored from __doc__
        """ setTabsClosable(self, closable: bool) """
        pass

    def setTabShape(self, shape): # real signature unknown; restored from __doc__
        """ setTabShape(self, shape: QTabWidget.TabShape) """
        pass

    def setTabsMovable(self, movable): # real signature unknown; restored from __doc__
        """ setTabsMovable(self, movable: bool) """
        pass

    def setupViewport(self, viewport): # real signature unknown; restored from __doc__
        """ setupViewport(self, viewport: QWidget) """
        pass

    def setViewMode(self, mode): # real signature unknown; restored from __doc__
        """ setViewMode(self, mode: QMdiArea.ViewMode) """
        pass

    def setViewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, showEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, showEvent: QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def subWindowActivated(self, *args, **kwargs): # real signature unknown
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

    def subWindowList(self, order=None): # real signature unknown; restored from __doc__
        """ subWindowList(self, order: QMdiArea.WindowOrder = QMdiArea.CreationOrder) -> List[QMdiSubWindow] """
        return []

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabPosition(self): # real signature unknown; restored from __doc__
        """ tabPosition(self) -> QTabWidget.TabPosition """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ tabsClosable(self) -> bool """
        return False

    def tabShape(self): # real signature unknown; restored from __doc__
        """ tabShape(self) -> QTabWidget.TabShape """
        pass

    def tabsMovable(self): # real signature unknown; restored from __doc__
        """ tabsMovable(self) -> bool """
        return False

    def testOption(self, opton): # real signature unknown; restored from __doc__
        """ testOption(self, opton: QMdiArea.AreaOption) -> bool """
        return False

    def tileSubWindows(self): # real signature unknown; restored from __doc__
        """ tileSubWindows(self) """
        pass

    def timerEvent(self, timerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, timerEvent: QTimerEvent) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> QMdiArea.ViewMode """
        pass

    def viewportEvent(self, event): # real signature unknown; restored from __doc__
        """ viewportEvent(self, event: QEvent) -> bool """
        return False

    def viewportMargins(self, *args, **kwargs): # real signature unknown
        pass

    def viewportSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    ActivationHistoryOrder = 2
    CreationOrder = 0
    DontMaximizeSubWindowOnActivation = 1
    StackingOrder = 1
    SubWindowView = 0
    TabbedView = 1


