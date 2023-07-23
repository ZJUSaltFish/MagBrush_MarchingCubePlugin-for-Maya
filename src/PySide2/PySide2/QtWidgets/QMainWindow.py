# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QWidget import QWidget

class QMainWindow(QWidget):
    """ QMainWindow(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def addDockWidget(self, area, dockwidget): # real signature unknown; restored from __doc__
        """
        addDockWidget(self, area: PySide2.QtCore.Qt.DockWidgetArea, dockwidget: PySide2.QtWidgets.QDockWidget) -> None
        addDockWidget(self, area: PySide2.QtCore.Qt.DockWidgetArea, dockwidget: PySide2.QtWidgets.QDockWidget, orientation: PySide2.QtCore.Qt.Orientation) -> None
        """
        pass

    def addToolBar(self, area, toolbar): # real signature unknown; restored from __doc__
        """
        addToolBar(self, area: PySide2.QtCore.Qt.ToolBarArea, toolbar: PySide2.QtWidgets.QToolBar) -> None
        addToolBar(self, title: str) -> PySide2.QtWidgets.QToolBar
        addToolBar(self, toolbar: PySide2.QtWidgets.QToolBar) -> None
        """
        pass

    def addToolBarBreak(self, area=None): # real signature unknown; restored from __doc__
        """ addToolBarBreak(self, area: PySide2.QtCore.Qt.ToolBarArea = PySide2.QtCore.Qt.ToolBarArea.TopToolBarArea) -> None """
        pass

    def centralWidget(self): # real signature unknown; restored from __doc__
        """ centralWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def contextMenuEvent(self, event): # real signature unknown; restored from __doc__
        """ contextMenuEvent(self, event: PySide2.QtGui.QContextMenuEvent) -> None """
        pass

    def corner(self, corner): # real signature unknown; restored from __doc__
        """ corner(self, corner: PySide2.QtCore.Qt.Corner) -> PySide2.QtCore.Qt.DockWidgetArea """
        pass

    def createPopupMenu(self): # real signature unknown; restored from __doc__
        """ createPopupMenu(self) -> PySide2.QtWidgets.QMenu """
        pass

    def dockOptions(self): # real signature unknown; restored from __doc__
        """ dockOptions(self) -> PySide2.QtWidgets.QMainWindow.DockOptions """
        pass

    def dockWidgetArea(self, dockwidget): # real signature unknown; restored from __doc__
        """ dockWidgetArea(self, dockwidget: PySide2.QtWidgets.QDockWidget) -> PySide2.QtCore.Qt.DockWidgetArea """
        pass

    def documentMode(self): # real signature unknown; restored from __doc__
        """ documentMode(self) -> bool """
        return False

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> PySide2.QtCore.QSize """
        pass

    def iconSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def insertToolBar(self, before, toolbar): # real signature unknown; restored from __doc__
        """ insertToolBar(self, before: PySide2.QtWidgets.QToolBar, toolbar: PySide2.QtWidgets.QToolBar) -> None """
        pass

    def insertToolBarBreak(self, before): # real signature unknown; restored from __doc__
        """ insertToolBarBreak(self, before: PySide2.QtWidgets.QToolBar) -> None """
        pass

    def isAnimated(self): # real signature unknown; restored from __doc__
        """ isAnimated(self) -> bool """
        return False

    def isDockNestingEnabled(self): # real signature unknown; restored from __doc__
        """ isDockNestingEnabled(self) -> bool """
        return False

    def isSeparator(self, pos): # real signature unknown; restored from __doc__
        """ isSeparator(self, pos: PySide2.QtCore.QPoint) -> bool """
        return False

    def menuBar(self): # real signature unknown; restored from __doc__
        """ menuBar(self) -> PySide2.QtWidgets.QMenuBar """
        pass

    def menuWidget(self): # real signature unknown; restored from __doc__
        """ menuWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def removeDockWidget(self, dockwidget): # real signature unknown; restored from __doc__
        """ removeDockWidget(self, dockwidget: PySide2.QtWidgets.QDockWidget) -> None """
        pass

    def removeToolBar(self, toolbar): # real signature unknown; restored from __doc__
        """ removeToolBar(self, toolbar: PySide2.QtWidgets.QToolBar) -> None """
        pass

    def removeToolBarBreak(self, before): # real signature unknown; restored from __doc__
        """ removeToolBarBreak(self, before: PySide2.QtWidgets.QToolBar) -> None """
        pass

    def resizeDocks(self, docks, PySide2_QtWidgets_QDockWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ resizeDocks(self, docks: typing.Sequence[PySide2.QtWidgets.QDockWidget], sizes: typing.Sequence[int], orientation: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def restoreDockWidget(self, dockwidget): # real signature unknown; restored from __doc__
        """ restoreDockWidget(self, dockwidget: PySide2.QtWidgets.QDockWidget) -> bool """
        return False

    def restoreState(self, state, version=0): # real signature unknown; restored from __doc__
        """ restoreState(self, state: PySide2.QtCore.QByteArray, version: int = 0) -> bool """
        return False

    def saveState(self, version=0): # real signature unknown; restored from __doc__
        """ saveState(self, version: int = 0) -> PySide2.QtCore.QByteArray """
        pass

    def setAnimated(self, enabled): # real signature unknown; restored from __doc__
        """ setAnimated(self, enabled: bool) -> None """
        pass

    def setCentralWidget(self, widget): # real signature unknown; restored from __doc__
        """ setCentralWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setCorner(self, corner, area): # real signature unknown; restored from __doc__
        """ setCorner(self, corner: PySide2.QtCore.Qt.Corner, area: PySide2.QtCore.Qt.DockWidgetArea) -> None """
        pass

    def setDockNestingEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setDockNestingEnabled(self, enabled: bool) -> None """
        pass

    def setDockOptions(self, options): # real signature unknown; restored from __doc__
        """ setDockOptions(self, options: PySide2.QtWidgets.QMainWindow.DockOptions) -> None """
        pass

    def setDocumentMode(self, enabled): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, enabled: bool) -> None """
        pass

    def setIconSize(self, iconSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, iconSize: PySide2.QtCore.QSize) -> None """
        pass

    def setMenuBar(self, menubar): # real signature unknown; restored from __doc__
        """ setMenuBar(self, menubar: PySide2.QtWidgets.QMenuBar) -> None """
        pass

    def setMenuWidget(self, menubar): # real signature unknown; restored from __doc__
        """ setMenuWidget(self, menubar: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setStatusBar(self, statusbar): # real signature unknown; restored from __doc__
        """ setStatusBar(self, statusbar: PySide2.QtWidgets.QStatusBar) -> None """
        pass

    def setTabPosition(self, areas, tabPosition): # real signature unknown; restored from __doc__
        """ setTabPosition(self, areas: PySide2.QtCore.Qt.DockWidgetAreas, tabPosition: PySide2.QtWidgets.QTabWidget.TabPosition) -> None """
        pass

    def setTabShape(self, tabShape): # real signature unknown; restored from __doc__
        """ setTabShape(self, tabShape: PySide2.QtWidgets.QTabWidget.TabShape) -> None """
        pass

    def setToolButtonStyle(self, toolButtonStyle): # real signature unknown; restored from __doc__
        """ setToolButtonStyle(self, toolButtonStyle: PySide2.QtCore.Qt.ToolButtonStyle) -> None """
        pass

    def setUnifiedTitleAndToolBarOnMac(self, set): # real signature unknown; restored from __doc__
        """ setUnifiedTitleAndToolBarOnMac(self, set: bool) -> None """
        pass

    def splitDockWidget(self, after, dockwidget, orientation): # real signature unknown; restored from __doc__
        """ splitDockWidget(self, after: PySide2.QtWidgets.QDockWidget, dockwidget: PySide2.QtWidgets.QDockWidget, orientation: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def statusBar(self): # real signature unknown; restored from __doc__
        """ statusBar(self) -> PySide2.QtWidgets.QStatusBar """
        pass

    def tabifiedDockWidgetActivated(self, *args, **kwargs): # real signature unknown
        pass

    def tabifiedDockWidgets(self, dockwidget): # real signature unknown; restored from __doc__
        """ tabifiedDockWidgets(self, dockwidget: PySide2.QtWidgets.QDockWidget) -> typing.List[PySide2.QtWidgets.QDockWidget] """
        pass

    def tabifyDockWidget(self, first, second): # real signature unknown; restored from __doc__
        """ tabifyDockWidget(self, first: PySide2.QtWidgets.QDockWidget, second: PySide2.QtWidgets.QDockWidget) -> None """
        pass

    def tabPosition(self, area): # real signature unknown; restored from __doc__
        """ tabPosition(self, area: PySide2.QtCore.Qt.DockWidgetArea) -> PySide2.QtWidgets.QTabWidget.TabPosition """
        pass

    def tabShape(self): # real signature unknown; restored from __doc__
        """ tabShape(self) -> PySide2.QtWidgets.QTabWidget.TabShape """
        pass

    def takeCentralWidget(self): # real signature unknown; restored from __doc__
        """ takeCentralWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def toolBarArea(self, toolbar): # real signature unknown; restored from __doc__
        """ toolBarArea(self, toolbar: PySide2.QtWidgets.QToolBar) -> PySide2.QtCore.Qt.ToolBarArea """
        pass

    def toolBarBreak(self, toolbar): # real signature unknown; restored from __doc__
        """ toolBarBreak(self, toolbar: PySide2.QtWidgets.QToolBar) -> bool """
        return False

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ toolButtonStyle(self) -> PySide2.QtCore.Qt.ToolButtonStyle """
        pass

    def toolButtonStyleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def unifiedTitleAndToolBarOnMac(self): # real signature unknown; restored from __doc__
        """ unifiedTitleAndToolBarOnMac(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AllowNestedDocks = PySide2.QtWidgets.QMainWindow.DockOption.AllowNestedDocks
    AllowTabbedDocks = PySide2.QtWidgets.QMainWindow.DockOption.AllowTabbedDocks
    AnimatedDocks = PySide2.QtWidgets.QMainWindow.DockOption.AnimatedDocks
    DockOption = None # (!) real value is "<class 'PySide2.QtWidgets.QMainWindow.DockOption'>"
    DockOptions = None # (!) real value is "<class 'PySide2.QtWidgets.QMainWindow.DockOptions'>"
    ForceTabbedDocks = PySide2.QtWidgets.QMainWindow.DockOption.ForceTabbedDocks
    GroupedDragging = PySide2.QtWidgets.QMainWindow.DockOption.GroupedDragging
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50833A00>'
    VerticalTabs = PySide2.QtWidgets.QMainWindow.DockOption.VerticalTabs


