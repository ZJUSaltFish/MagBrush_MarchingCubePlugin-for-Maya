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

class QTabBar(QWidget):
    """ QTabBar(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def accessibleTabName(self, index): # real signature unknown; restored from __doc__
        """ accessibleTabName(self, index: int) -> str """
        return ""

    def addTab(self, icon, text): # real signature unknown; restored from __doc__
        """
        addTab(self, icon: PySide2.QtGui.QIcon, text: str) -> int
        addTab(self, text: str) -> int
        """
        return 0

    def autoHide(self): # real signature unknown; restored from __doc__
        """ autoHide(self) -> bool """
        return False

    def changeCurrentOnDrag(self): # real signature unknown; restored from __doc__
        """ changeCurrentOnDrag(self) -> bool """
        return False

    def changeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ changeEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def documentMode(self): # real signature unknown; restored from __doc__
        """ documentMode(self) -> bool """
        return False

    def drawBase(self): # real signature unknown; restored from __doc__
        """ drawBase(self) -> bool """
        return False

    def elideMode(self): # real signature unknown; restored from __doc__
        """ elideMode(self) -> PySide2.QtCore.Qt.TextElideMode """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def expanding(self): # real signature unknown; restored from __doc__
        """ expanding(self) -> bool """
        return False

    def hideEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ hideEvent(self, arg__1: PySide2.QtGui.QHideEvent) -> None """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> PySide2.QtCore.QSize """
        pass

    def initStyleOption(self, option, tabIndex): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionTab, tabIndex: int) -> None """
        pass

    def insertTab(self, index, icon, text): # real signature unknown; restored from __doc__
        """
        insertTab(self, index: int, icon: PySide2.QtGui.QIcon, text: str) -> int
        insertTab(self, index: int, text: str) -> int
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

    def minimumTabSizeHint(self, index): # real signature unknown; restored from __doc__
        """ minimumTabSizeHint(self, index: int) -> PySide2.QtCore.QSize """
        pass

    def mouseMoveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def moveTab(self, from_, to): # real signature unknown; restored from __doc__
        """ moveTab(self, from_: int, to: int) -> None """
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

    def selectionBehaviorOnRemove(self): # real signature unknown; restored from __doc__
        """ selectionBehaviorOnRemove(self) -> PySide2.QtWidgets.QTabBar.SelectionBehavior """
        pass

    def setAccessibleTabName(self, index, name): # real signature unknown; restored from __doc__
        """ setAccessibleTabName(self, index: int, name: str) -> None """
        pass

    def setAutoHide(self, hide): # real signature unknown; restored from __doc__
        """ setAutoHide(self, hide: bool) -> None """
        pass

    def setChangeCurrentOnDrag(self, change): # real signature unknown; restored from __doc__
        """ setChangeCurrentOnDrag(self, change: bool) -> None """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) -> None """
        pass

    def setDocumentMode(self, set): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, set: bool) -> None """
        pass

    def setDrawBase(self, drawTheBase): # real signature unknown; restored from __doc__
        """ setDrawBase(self, drawTheBase: bool) -> None """
        pass

    def setElideMode(self, mode): # real signature unknown; restored from __doc__
        """ setElideMode(self, mode: PySide2.QtCore.Qt.TextElideMode) -> None """
        pass

    def setExpanding(self, enabled): # real signature unknown; restored from __doc__
        """ setExpanding(self, enabled: bool) -> None """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setMovable(self, movable): # real signature unknown; restored from __doc__
        """ setMovable(self, movable: bool) -> None """
        pass

    def setSelectionBehaviorOnRemove(self, behavior): # real signature unknown; restored from __doc__
        """ setSelectionBehaviorOnRemove(self, behavior: PySide2.QtWidgets.QTabBar.SelectionBehavior) -> None """
        pass

    def setShape(self, shape): # real signature unknown; restored from __doc__
        """ setShape(self, shape: PySide2.QtWidgets.QTabBar.Shape) -> None """
        pass

    def setTabButton(self, index, position, widget): # real signature unknown; restored from __doc__
        """ setTabButton(self, index: int, position: PySide2.QtWidgets.QTabBar.ButtonPosition, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setTabData(self, index, data): # real signature unknown; restored from __doc__
        """ setTabData(self, index: int, data: typing.Any) -> None """
        pass

    def setTabEnabled(self, index, enabled): # real signature unknown; restored from __doc__
        """ setTabEnabled(self, index: int, enabled: bool) -> None """
        pass

    def setTabIcon(self, index, icon): # real signature unknown; restored from __doc__
        """ setTabIcon(self, index: int, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setTabsClosable(self, closable): # real signature unknown; restored from __doc__
        """ setTabsClosable(self, closable: bool) -> None """
        pass

    def setTabText(self, index, text): # real signature unknown; restored from __doc__
        """ setTabText(self, index: int, text: str) -> None """
        pass

    def setTabTextColor(self, index, color): # real signature unknown; restored from __doc__
        """ setTabTextColor(self, index: int, color: PySide2.QtGui.QColor) -> None """
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

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> PySide2.QtWidgets.QTabBar.Shape """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def tabAt(self, pos): # real signature unknown; restored from __doc__
        """ tabAt(self, pos: PySide2.QtCore.QPoint) -> int """
        return 0

    def tabBarClicked(self, *args, **kwargs): # real signature unknown
        pass

    def tabBarDoubleClicked(self, *args, **kwargs): # real signature unknown
        pass

    def tabButton(self, index, position): # real signature unknown; restored from __doc__
        """ tabButton(self, index: int, position: PySide2.QtWidgets.QTabBar.ButtonPosition) -> PySide2.QtWidgets.QWidget """
        pass

    def tabCloseRequested(self, *args, **kwargs): # real signature unknown
        pass

    def tabData(self, index): # real signature unknown; restored from __doc__
        """ tabData(self, index: int) -> typing.Any """
        pass

    def tabIcon(self, index): # real signature unknown; restored from __doc__
        """ tabIcon(self, index: int) -> PySide2.QtGui.QIcon """
        pass

    def tabInserted(self, index): # real signature unknown; restored from __doc__
        """ tabInserted(self, index: int) -> None """
        pass

    def tabLayoutChange(self): # real signature unknown; restored from __doc__
        """ tabLayoutChange(self) -> None """
        pass

    def tabMoved(self, *args, **kwargs): # real signature unknown
        pass

    def tabRect(self, index): # real signature unknown; restored from __doc__
        """ tabRect(self, index: int) -> PySide2.QtCore.QRect """
        pass

    def tabRemoved(self, index): # real signature unknown; restored from __doc__
        """ tabRemoved(self, index: int) -> None """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ tabsClosable(self) -> bool """
        return False

    def tabSizeHint(self, index): # real signature unknown; restored from __doc__
        """ tabSizeHint(self, index: int) -> PySide2.QtCore.QSize """
        pass

    def tabText(self, index): # real signature unknown; restored from __doc__
        """ tabText(self, index: int) -> str """
        return ""

    def tabTextColor(self, index): # real signature unknown; restored from __doc__
        """ tabTextColor(self, index: int) -> PySide2.QtGui.QColor """
        pass

    def tabToolTip(self, index): # real signature unknown; restored from __doc__
        """ tabToolTip(self, index: int) -> str """
        return ""

    def tabWhatsThis(self, index): # real signature unknown; restored from __doc__
        """ tabWhatsThis(self, index: int) -> str """
        return ""

    def timerEvent(self, event): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def usesScrollButtons(self): # real signature unknown; restored from __doc__
        """ usesScrollButtons(self) -> bool """
        return False

    def wheelEvent(self, event): # real signature unknown; restored from __doc__
        """ wheelEvent(self, event: PySide2.QtGui.QWheelEvent) -> None """
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

    ButtonPosition = None # (!) real value is "<class 'PySide2.QtWidgets.QTabBar.ButtonPosition'>"
    LeftSide = PySide2.QtWidgets.QTabBar.ButtonPosition.LeftSide
    RightSide = PySide2.QtWidgets.QTabBar.ButtonPosition.RightSide
    RoundedEast = PySide2.QtWidgets.QTabBar.Shape.RoundedEast
    RoundedNorth = PySide2.QtWidgets.QTabBar.Shape.RoundedNorth
    RoundedSouth = PySide2.QtWidgets.QTabBar.Shape.RoundedSouth
    RoundedWest = PySide2.QtWidgets.QTabBar.Shape.RoundedWest
    SelectionBehavior = None # (!) real value is "<class 'PySide2.QtWidgets.QTabBar.SelectionBehavior'>"
    SelectLeftTab = PySide2.QtWidgets.QTabBar.SelectionBehavior.SelectLeftTab
    SelectPreviousTab = PySide2.QtWidgets.QTabBar.SelectionBehavior.SelectPreviousTab
    SelectRightTab = PySide2.QtWidgets.QTabBar.SelectionBehavior.SelectRightTab
    Shape = None # (!) real value is "<class 'PySide2.QtWidgets.QTabBar.Shape'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507BC100>'
    TriangularEast = PySide2.QtWidgets.QTabBar.Shape.TriangularEast
    TriangularNorth = PySide2.QtWidgets.QTabBar.Shape.TriangularNorth
    TriangularSouth = PySide2.QtWidgets.QTabBar.Shape.TriangularSouth
    TriangularWest = PySide2.QtWidgets.QTabBar.Shape.TriangularWest


