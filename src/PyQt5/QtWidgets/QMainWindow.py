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

class QMainWindow(QWidget):
    """ QMainWindow(parent: typing.Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addDockWidget(self, area, dockwidget, orientation=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addDockWidget(self, area: Qt.DockWidgetArea, dockwidget: QDockWidget)
        addDockWidget(self, area: Qt.DockWidgetArea, dockwidget: QDockWidget, orientation: Qt.Orientation)
        """
        pass

    def addToolBar(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addToolBar(self, area: Qt.ToolBarArea, toolbar: QToolBar)
        addToolBar(self, toolbar: QToolBar)
        addToolBar(self, title: str) -> QToolBar
        """
        return QToolBar

    def addToolBarBreak(self, area=None): # real signature unknown; restored from __doc__
        """ addToolBarBreak(self, area: Qt.ToolBarArea = Qt.TopToolBarArea) """
        pass

    def centralWidget(self): # real signature unknown; restored from __doc__
        """ centralWidget(self) -> QWidget """
        return QWidget

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: QContextMenuEvent) """
        pass

    def corner(self, corner): # real signature unknown; restored from __doc__
        """ corner(self, corner: Qt.Corner) -> Qt.DockWidgetArea """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createPopupMenu(self): # real signature unknown; restored from __doc__
        """ createPopupMenu(self) -> QMenu """
        return QMenu

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dockOptions(self): # real signature unknown; restored from __doc__
        """ dockOptions(self) -> QMainWindow.DockOptions """
        pass

    def dockWidgetArea(self, dockwidget): # real signature unknown; restored from __doc__
        """ dockWidgetArea(self, dockwidget: QDockWidget) -> Qt.DockWidgetArea """
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

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: QEvent) -> bool """
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

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> QSize """
        pass

    def iconSizeChanged(self, *args, **kwargs): # real signature unknown
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

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def insertToolBar(self, before, toolbar): # real signature unknown; restored from __doc__
        """ insertToolBar(self, before: QToolBar, toolbar: QToolBar) """
        pass

    def insertToolBarBreak(self, before): # real signature unknown; restored from __doc__
        """ insertToolBarBreak(self, before: QToolBar) """
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ isAnimated(self) -> bool """
        return False

    def isDockNestingEnabled(self): # real signature unknown; restored from __doc__
        """ isDockNestingEnabled(self) -> bool """
        return False

    def isSeparator(self, pos): # real signature unknown; restored from __doc__
        """ isSeparator(self, pos: QPoint) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def menuBar(self): # real signature unknown; restored from __doc__
        """ menuBar(self) -> QMenuBar """
        return QMenuBar

    def menuWidget(self): # real signature unknown; restored from __doc__
        """ menuWidget(self) -> QWidget """
        return QWidget

    def metric(self, *args, **kwargs): # real signature unknown
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

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeDockWidget(self, dockwidget): # real signature unknown; restored from __doc__
        """ removeDockWidget(self, dockwidget: QDockWidget) """
        pass

    def removeToolBar(self, toolbar): # real signature unknown; restored from __doc__
        """ removeToolBar(self, toolbar: QToolBar) """
        pass

    def removeToolBarBreak(self, before): # real signature unknown; restored from __doc__
        """ removeToolBarBreak(self, before: QToolBar) """
        pass

    def resizeDocks(self, docks, QDockWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ resizeDocks(self, docks: Iterable[QDockWidget], sizes: Iterable[int], orientation: Qt.Orientation) """
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def restoreDockWidget(self, dockwidget): # real signature unknown; restored from __doc__
        """ restoreDockWidget(self, dockwidget: QDockWidget) -> bool """
        return False

    def restoreState(self, state, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ restoreState(self, state: Union[QByteArray, bytes, bytearray], version: int = 0) -> bool """
        pass

    def saveState(self, version=0): # real signature unknown; restored from __doc__
        """ saveState(self, version: int = 0) -> QByteArray """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAnimated(self, enabled): # real signature unknown; restored from __doc__
        """ setAnimated(self, enabled: bool) """
        pass

    def setCentralWidget(self, widget): # real signature unknown; restored from __doc__
        """ setCentralWidget(self, widget: QWidget) """
        pass

    def setCorner(self, corner, area): # real signature unknown; restored from __doc__
        """ setCorner(self, corner: Qt.Corner, area: Qt.DockWidgetArea) """
        pass

    def setDockNestingEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setDockNestingEnabled(self, enabled: bool) """
        pass

    def setDockOptions(self, options, QMainWindow_DockOptions=None, QMainWindow_DockOption=None): # real signature unknown; restored from __doc__
        """ setDockOptions(self, options: Union[QMainWindow.DockOptions, QMainWindow.DockOption]) """
        pass

    def setDocumentMode(self, enabled): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, enabled: bool) """
        pass

    def setIconSize(self, iconSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, iconSize: QSize) """
        pass

    def setMenuBar(self, menubar): # real signature unknown; restored from __doc__
        """ setMenuBar(self, menubar: QMenuBar) """
        pass

    def setMenuWidget(self, menubar): # real signature unknown; restored from __doc__
        """ setMenuWidget(self, menubar: QWidget) """
        pass

    def setStatusBar(self, statusbar): # real signature unknown; restored from __doc__
        """ setStatusBar(self, statusbar: QStatusBar) """
        pass

    def setTabPosition(self, areas, Qt_DockWidgetAreas=None, Qt_DockWidgetArea=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setTabPosition(self, areas: Union[Qt.DockWidgetAreas, Qt.DockWidgetArea], tabPosition: QTabWidget.TabPosition) """
        pass

    def setTabShape(self, tabShape): # real signature unknown; restored from __doc__
        """ setTabShape(self, tabShape: QTabWidget.TabShape) """
        pass

    def setToolButtonStyle(self, toolButtonStyle): # real signature unknown; restored from __doc__
        """ setToolButtonStyle(self, toolButtonStyle: Qt.ToolButtonStyle) """
        pass

    def setUnifiedTitleAndToolBarOnMac(self, set): # real signature unknown; restored from __doc__
        """ setUnifiedTitleAndToolBarOnMac(self, set: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def splitDockWidget(self, after, dockwidget, orientation): # real signature unknown; restored from __doc__
        """ splitDockWidget(self, after: QDockWidget, dockwidget: QDockWidget, orientation: Qt.Orientation) """
        pass

    def statusBar(self): # real signature unknown; restored from __doc__
        """ statusBar(self) -> QStatusBar """
        return QStatusBar

    def tabifiedDockWidgetActivated(self, *args, **kwargs): # real signature unknown
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

    def tabifiedDockWidgets(self, dockwidget): # real signature unknown; restored from __doc__
        """ tabifiedDockWidgets(self, dockwidget: QDockWidget) -> List[QDockWidget] """
        return []

    def tabifyDockWidget(self, first, second): # real signature unknown; restored from __doc__
        """ tabifyDockWidget(self, first: QDockWidget, second: QDockWidget) """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabPosition(self, area): # real signature unknown; restored from __doc__
        """ tabPosition(self, area: Qt.DockWidgetArea) -> QTabWidget.TabPosition """
        pass

    def tabShape(self): # real signature unknown; restored from __doc__
        """ tabShape(self) -> QTabWidget.TabShape """
        pass

    def takeCentralWidget(self): # real signature unknown; restored from __doc__
        """ takeCentralWidget(self) -> QWidget """
        return QWidget

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toolBarArea(self, toolbar): # real signature unknown; restored from __doc__
        """ toolBarArea(self, toolbar: QToolBar) -> Qt.ToolBarArea """
        pass

    def toolBarBreak(self, toolbar): # real signature unknown; restored from __doc__
        """ toolBarBreak(self, toolbar: QToolBar) -> bool """
        return False

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ toolButtonStyle(self) -> Qt.ToolButtonStyle """
        pass

    def toolButtonStyleChanged(self, *args, **kwargs): # real signature unknown
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

    def unifiedTitleAndToolBarOnMac(self): # real signature unknown; restored from __doc__
        """ unifiedTitleAndToolBarOnMac(self) -> bool """
        return False

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AllowNestedDocks = 2
    AllowTabbedDocks = 4
    AnimatedDocks = 1
    ForceTabbedDocks = 8
    GroupedDragging = 32
    VerticalTabs = 16


