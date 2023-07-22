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

class QToolBar(QWidget):
    """
    QToolBar(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QToolBar(self, title: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def actionAt(self, p): # real signature unknown; restored from __doc__
        """
        actionAt(self, p: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QAction
        actionAt(self, x: int, y: int) -> PySide2.QtWidgets.QAction
        """
        pass

    def actionEvent(self, event): # real signature unknown; restored from __doc__
        """ actionEvent(self, event: PySide2.QtGui.QActionEvent) -> None """
        pass

    def actionGeometry(self, action): # real signature unknown; restored from __doc__
        """ actionGeometry(self, action: PySide2.QtWidgets.QAction) -> PySide2.QtCore.QRect """
        pass

    def actionTriggered(self, *args, **kwargs): # real signature unknown
        pass

    def addAction(self, arg__1): # real signature unknown; restored from __doc__
        """
        addAction(self, arg__1: PySide2.QtWidgets.QAction) -> None
        addAction(self, icon: PySide2.QtGui.QIcon, text: str) -> PySide2.QtWidgets.QAction
        addAction(self, icon: PySide2.QtGui.QIcon, text: str, receiver: PySide2.QtCore.QObject, member: bytes) -> PySide2.QtWidgets.QAction
        addAction(self, text: str) -> PySide2.QtWidgets.QAction
        addAction(self, text: str, receiver: PySide2.QtCore.QObject, member: bytes) -> PySide2.QtWidgets.QAction
        """
        pass

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> PySide2.QtWidgets.QAction """
        pass

    def addWidget(self, widget): # real signature unknown; restored from __doc__
        """ addWidget(self, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtWidgets.QAction """
        pass

    def allowedAreas(self): # real signature unknown; restored from __doc__
        """ allowedAreas(self) -> PySide2.QtCore.Qt.ToolBarAreas """
        pass

    def allowedAreasChanged(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, event): # real signature unknown; restored from __doc__
        """ changeEvent(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> PySide2.QtCore.QSize """
        pass

    def iconSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionToolBar) -> None """
        pass

    def insertSeparator(self, before): # real signature unknown; restored from __doc__
        """ insertSeparator(self, before: PySide2.QtWidgets.QAction) -> PySide2.QtWidgets.QAction """
        pass

    def insertWidget(self, before, widget): # real signature unknown; restored from __doc__
        """ insertWidget(self, before: PySide2.QtWidgets.QAction, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtWidgets.QAction """
        pass

    def isAreaAllowed(self, area): # real signature unknown; restored from __doc__
        """ isAreaAllowed(self, area: PySide2.QtCore.Qt.ToolBarArea) -> bool """
        return False

    def isFloatable(self): # real signature unknown; restored from __doc__
        """ isFloatable(self) -> bool """
        return False

    def isFloating(self): # real signature unknown; restored from __doc__
        """ isFloating(self) -> bool """
        return False

    def isMovable(self): # real signature unknown; restored from __doc__
        """ isMovable(self) -> bool """
        return False

    def movableChanged(self, *args, **kwargs): # real signature unknown
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.Orientation """
        pass

    def orientationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def setAllowedAreas(self, areas): # real signature unknown; restored from __doc__
        """ setAllowedAreas(self, areas: PySide2.QtCore.Qt.ToolBarAreas) -> None """
        pass

    def setFloatable(self, floatable): # real signature unknown; restored from __doc__
        """ setFloatable(self, floatable: bool) -> None """
        pass

    def setIconSize(self, iconSize): # real signature unknown; restored from __doc__
        """ setIconSize(self, iconSize: PySide2.QtCore.QSize) -> None """
        pass

    def setMovable(self, movable): # real signature unknown; restored from __doc__
        """ setMovable(self, movable: bool) -> None """
        pass

    def setOrientation(self, orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, orientation: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def setToolButtonStyle(self, toolButtonStyle): # real signature unknown; restored from __doc__
        """ setToolButtonStyle(self, toolButtonStyle: PySide2.QtCore.Qt.ToolButtonStyle) -> None """
        pass

    def toggleViewAction(self): # real signature unknown; restored from __doc__
        """ toggleViewAction(self) -> PySide2.QtWidgets.QAction """
        pass

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ toolButtonStyle(self) -> PySide2.QtCore.Qt.ToolButtonStyle """
        pass

    def toolButtonStyleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def topLevelChanged(self, *args, **kwargs): # real signature unknown
        pass

    def visibilityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def widgetForAction(self, action): # real signature unknown; restored from __doc__
        """ widgetForAction(self, action: PySide2.QtWidgets.QAction) -> PySide2.QtWidgets.QWidget """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50830D40>'


