# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractScrollArea import QAbstractScrollArea

class QMdiArea(QAbstractScrollArea):
    """ QMdiArea(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def activateNextSubWindow(self): # real signature unknown; restored from __doc__
        """ activateNextSubWindow(self) -> None """
        pass

    def activatePreviousSubWindow(self): # real signature unknown; restored from __doc__
        """ activatePreviousSubWindow(self) -> None """
        pass

    def activationOrder(self): # real signature unknown; restored from __doc__
        """ activationOrder(self) -> PySide2.QtWidgets.QMdiArea.WindowOrder """
        pass

    def activeSubWindow(self): # real signature unknown; restored from __doc__
        """ activeSubWindow(self) -> PySide2.QtWidgets.QMdiSubWindow """
        pass

    def addSubWindow(self, widget, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addSubWindow(self, widget: PySide2.QtWidgets.QWidget, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> PySide2.QtWidgets.QMdiSubWindow """
        pass

    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> PySide2.QtGui.QBrush """
        pass

    def cascadeSubWindows(self): # real signature unknown; restored from __doc__
        """ cascadeSubWindows(self) -> None """
        pass

    def childEvent(self, childEvent): # real signature unknown; restored from __doc__
        """ childEvent(self, childEvent: PySide2.QtCore.QChildEvent) -> None """
        pass

    def closeActiveSubWindow(self): # real signature unknown; restored from __doc__
        """ closeActiveSubWindow(self) -> None """
        pass

    def closeAllSubWindows(self): # real signature unknown; restored from __doc__
        """ closeAllSubWindows(self) -> None """
        pass

    def currentSubWindow(self): # real signature unknown; restored from __doc__
        """ currentSubWindow(self) -> PySide2.QtWidgets.QMdiSubWindow """
        pass

    def documentMode(self): # real signature unknown; restored from __doc__
        """ documentMode(self) -> bool """
        return False

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def eventFilter(self, p_object, event): # real signature unknown; restored from __doc__
        """ eventFilter(self, object: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def paintEvent(self, paintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, paintEvent: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def removeSubWindow(self, widget): # real signature unknown; restored from __doc__
        """ removeSubWindow(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def resizeEvent(self, resizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, resizeEvent: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) -> None """
        pass

    def setActivationOrder(self, order): # real signature unknown; restored from __doc__
        """ setActivationOrder(self, order: PySide2.QtWidgets.QMdiArea.WindowOrder) -> None """
        pass

    def setActiveSubWindow(self, window): # real signature unknown; restored from __doc__
        """ setActiveSubWindow(self, window: PySide2.QtWidgets.QMdiSubWindow) -> None """
        pass

    def setBackground(self, background): # real signature unknown; restored from __doc__
        """ setBackground(self, background: PySide2.QtGui.QBrush) -> None """
        pass

    def setDocumentMode(self, enabled): # real signature unknown; restored from __doc__
        """ setDocumentMode(self, enabled: bool) -> None """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: PySide2.QtWidgets.QMdiArea.AreaOption, on: bool = True) -> None """
        pass

    def setTabPosition(self, position): # real signature unknown; restored from __doc__
        """ setTabPosition(self, position: PySide2.QtWidgets.QTabWidget.TabPosition) -> None """
        pass

    def setTabsClosable(self, closable): # real signature unknown; restored from __doc__
        """ setTabsClosable(self, closable: bool) -> None """
        pass

    def setTabShape(self, shape): # real signature unknown; restored from __doc__
        """ setTabShape(self, shape: PySide2.QtWidgets.QTabWidget.TabShape) -> None """
        pass

    def setTabsMovable(self, movable): # real signature unknown; restored from __doc__
        """ setTabsMovable(self, movable: bool) -> None """
        pass

    def setupViewport(self, viewport): # real signature unknown; restored from __doc__
        """ setupViewport(self, viewport: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setViewMode(self, mode): # real signature unknown; restored from __doc__
        """ setViewMode(self, mode: PySide2.QtWidgets.QMdiArea.ViewMode) -> None """
        pass

    def showEvent(self, showEvent): # real signature unknown; restored from __doc__
        """ showEvent(self, showEvent: PySide2.QtGui.QShowEvent) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def subWindowActivated(self, *args, **kwargs): # real signature unknown
        pass

    def subWindowList(self, order=None): # real signature unknown; restored from __doc__
        """ subWindowList(self, order: PySide2.QtWidgets.QMdiArea.WindowOrder = PySide2.QtWidgets.QMdiArea.WindowOrder.CreationOrder) -> typing.List[PySide2.QtWidgets.QMdiSubWindow] """
        pass

    def tabPosition(self): # real signature unknown; restored from __doc__
        """ tabPosition(self) -> PySide2.QtWidgets.QTabWidget.TabPosition """
        pass

    def tabsClosable(self): # real signature unknown; restored from __doc__
        """ tabsClosable(self) -> bool """
        return False

    def tabShape(self): # real signature unknown; restored from __doc__
        """ tabShape(self) -> PySide2.QtWidgets.QTabWidget.TabShape """
        pass

    def tabsMovable(self): # real signature unknown; restored from __doc__
        """ tabsMovable(self) -> bool """
        return False

    def testOption(self, opton): # real signature unknown; restored from __doc__
        """ testOption(self, opton: PySide2.QtWidgets.QMdiArea.AreaOption) -> bool """
        return False

    def tileSubWindows(self): # real signature unknown; restored from __doc__
        """ tileSubWindows(self) -> None """
        pass

    def timerEvent(self, timerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, timerEvent: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> PySide2.QtWidgets.QMdiArea.ViewMode """
        pass

    def viewportEvent(self, event): # real signature unknown; restored from __doc__
        """ viewportEvent(self, event: PySide2.QtCore.QEvent) -> bool """
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

    ActivationHistoryOrder = PySide2.QtWidgets.QMdiArea.WindowOrder.ActivationHistoryOrder
    AreaOption = None # (!) real value is "<class 'PySide2.QtWidgets.QMdiArea.AreaOption'>"
    AreaOptions = None # (!) real value is "<class 'PySide2.QtWidgets.QMdiArea.AreaOptions'>"
    CreationOrder = PySide2.QtWidgets.QMdiArea.WindowOrder.CreationOrder
    DontMaximizeSubWindowOnActivation = PySide2.QtWidgets.QMdiArea.AreaOption.DontMaximizeSubWindowOnActivation
    StackingOrder = PySide2.QtWidgets.QMdiArea.WindowOrder.StackingOrder
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50815000>'
    SubWindowView = PySide2.QtWidgets.QMdiArea.ViewMode.SubWindowView
    TabbedView = PySide2.QtWidgets.QMdiArea.ViewMode.TabbedView
    ViewMode = None # (!) real value is "<class 'PySide2.QtWidgets.QMdiArea.ViewMode'>"
    WindowOrder = None # (!) real value is "<class 'PySide2.QtWidgets.QMdiArea.WindowOrder'>"


