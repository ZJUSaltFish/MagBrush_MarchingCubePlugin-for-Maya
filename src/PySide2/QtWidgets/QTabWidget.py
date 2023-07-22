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

class QTabWidget(QWidget):
    """ QTabWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def addTab(self, widget, arg__2): # real signature unknown; restored from __doc__
        """
        addTab(self, widget: PySide2.QtWidgets.QWidget, arg__2: str) -> int
        addTab(self, widget: PySide2.QtWidgets.QWidget, icon: PySide2.QtGui.QIcon, label: str) -> int
        """
        return 0

    def changeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ changeEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def cornerWidget(self, corner=None): # real signature unknown; restored from __doc__
        """ cornerWidget(self, corner: PySide2.QtCore.Qt.Corner = PySide2.QtCore.Qt.Corner.TopRightCorner) -> PySide2.QtWidgets.QWidget """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ currentWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def documentMode(self): # real signature unknown; restored from __doc__
        """ documentMode(self) -> bool """
        return False

    def elideMode(self): # real signature unknown; restored from __doc__
        """ elideMode(self) -> PySide2.QtCore.Qt.TextElideMode """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, width): # real signature unknown; restored from __doc__
        """ heightForWidth(self, width: int) -> int """
        return 0

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> PySide2.QtCore.QSize """
        pass

    def indexOf(self, widget): # real signature unknown; restored from __doc__
        """ indexOf(self, widget: PySide2.QtWidgets.QWidget) -> int """
        return 0

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionTabWidgetFrame) -> None """
        pass

    def insertTab(self, index, widget, arg__3): # real signature unknown; restored from __doc__
        """
        insertTab(self, index: int, widget: PySide2.QtWidgets.QWidget, arg__3: str) -> int
        insertTab(self, index: int, widget: PySide2.QtWidgets.QWidget, icon: PySide2.QtGui.QIcon, label: str) -> int
        """
        return 0

    def isMovable(self): # real signature unknown; restored from __doc__
        """ isMovable(self) -> bool """
        return False

    def isTabEnabled(self, index): # real signature unknown; restored from __doc__
        """ isTabEnabled(self, index: int) -> bool """
        return False

    def isTabVisible(self, index): # real signature unknown; restored from __doc__
        """ isTabVisible(self, index: int) -> bool """
        return False

    def keyPressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def removeTab(self, index): # real signature unknown; restored from __doc__
        """ removeTab(self, index: int) -> None """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def setCornerWidget(self, w, corner=None): # real signature unknown; restored from __doc__
        """ setCornerWidget(self, w: PySide2.QtWidgets.QWidget, corner: PySide2.QtCore.Qt.Corner = PySide2.QtCore.Qt.Corner.TopRightCorner) -> None """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) -> None """
        pass

    def setCurrentWidget(self, widget): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setDocumentMode(self, set): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, set: bool) -> None """
        pass

    def setElideMode(self, mode): # real signature unknown; restored from __doc__
        """ setElideMode(self, mode: PySide2.QtCore.Qt.TextElideMode) -> None """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setMovable(self, movable): # real signature unknown; restored from __doc__
        """ setMovable(self, movable: bool) -> None """
        pass

    def setTabBar(self, arg__1): # real signature unknown; restored from __doc__
        """ setTabBar(self, arg__1: PySide2.QtWidgets.QTabBar) -> None """
        pass

    def setTabBarAutoHide(self, enabled): # real signature unknown; restored from __doc__
        """ setTabBarAutoHide(self, enabled: bool) -> None """
        pass

    def setTabEnabled(self, index, enabled): # real signature unknown; restored from __doc__
        """ setTabEnabled(self, index: int, enabled: bool) -> None """
        pass

    def setTabIcon(self, index, icon): # real signature unknown; restored from __doc__
        """ setTabIcon(self, index: int, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setTabPosition(self, position): # real signature unknown; restored from __doc__
        """ setTabPosition(self, position: PySide2.QtWidgets.QTabWidget.TabPosition) -> None """
        pass

    def setTabsClosable(self, closeable): # real signature unknown; restored from __doc__
        """ setTabsClosable(self, closeable: bool) -> None """
        pass

    def setTabShape(self, s): # real signature unknown; restored from __doc__
        """ setTabShape(self, s: PySide2.QtWidgets.QTabWidget.TabShape) -> None """
        pass

    def setTabText(self, index, text): # real signature unknown; restored from __doc__
        """ setTabText(self, index: int, text: str) -> None """
        pass

    def setTabToolTip(self, index, tip): # real signature unknown; restored from __doc__
        """ setTabToolTip(self, index: int, tip: str) -> None """
        pass

    def setTabVisible(self, index, visible): # real signature unknown; restored from __doc__
        """ setTabVisible(self, index: int, visible: bool) -> None """
        pass

    def setTabWhatsThis(self, index, text): # real signature unknown; restored from __doc__
        """ setTabWhatsThis(self, index: int, text: str) -> None """
        pass

    def setUsesScrollButtons(self, useButtons): # real signature unknown; restored from __doc__
        """ setUsesScrollButtons(self, useButtons: bool) -> None """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def tabBar(self): # real signature unknown; restored from __doc__
        """ tabBar(self) -> PySide2.QtWidgets.QTabBar """
        pass

    def tabBarAutoHide(self): # real signature unknown; restored from __doc__
        """ tabBarAutoHide(self) -> bool """
        return False

    def tabBarClicked(self, *args, **kwargs): # real signature unknown
        pass

    def tabBarDoubleClicked(self, *args, **kwargs): # real signature unknown
        pass

    def tabCloseRequested(self, *args, **kwargs): # real signature unknown
        pass

    def tabIcon(self, index): # real signature unknown; restored from __doc__
        """ tabIcon(self, index: int) -> PySide2.QtGui.QIcon """
        pass

    def tabInserted(self, index): # real signature unknown; restored from __doc__
        """ tabInserted(self, index: int) -> None """
        pass

    def tabPosition(self): # real signature unknown; restored from __doc__
        """ tabPosition(self) -> PySide2.QtWidgets.QTabWidget.TabPosition """
        pass

    def tabRemoved(self, index): # real signature unknown; restored from __doc__
        """ tabRemoved(self, index: int) -> None """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ tabsClosable(self) -> bool """
        return False

    def tabShape(self): # real signature unknown; restored from __doc__
        """ tabShape(self) -> PySide2.QtWidgets.QTabWidget.TabShape """
        pass

    def tabText(self, index): # real signature unknown; restored from __doc__
        """ tabText(self, index: int) -> str """
        return ""

    def tabToolTip(self, index): # real signature unknown; restored from __doc__
        """ tabToolTip(self, index: int) -> str """
        return ""

    def tabWhatsThis(self, index): # real signature unknown; restored from __doc__
        """ tabWhatsThis(self, index: int) -> str """
        return ""

    def usesScrollButtons(self): # real signature unknown; restored from __doc__
        """ usesScrollButtons(self) -> bool """
        return False

    def widget(self, index): # real signature unknown; restored from __doc__
        """ widget(self, index: int) -> PySide2.QtWidgets.QWidget """
        pass

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

    East = PySide2.QtWidgets.QTabWidget.TabPosition.East
    North = PySide2.QtWidgets.QTabWidget.TabPosition.North
    Rounded = PySide2.QtWidgets.QTabWidget.TabShape.Rounded
    South = PySide2.QtWidgets.QTabWidget.TabPosition.South
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507A7340>'
    TabPosition = None # (!) real value is "<class 'PySide2.QtWidgets.QTabWidget.TabPosition'>"
    TabShape = None # (!) real value is "<class 'PySide2.QtWidgets.QTabWidget.TabShape'>"
    Triangular = PySide2.QtWidgets.QTabWidget.TabShape.Triangular
    West = PySide2.QtWidgets.QTabWidget.TabPosition.West


