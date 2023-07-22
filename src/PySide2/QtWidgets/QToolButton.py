# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractButton import QAbstractButton

class QToolButton(QAbstractButton):
    """ QToolButton(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def actionEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ actionEvent(self, arg__1: PySide2.QtGui.QActionEvent) -> None """
        pass

    def arrowType(self): # real signature unknown; restored from __doc__
        """ arrowType(self) -> PySide2.QtCore.Qt.ArrowType """
        pass

    def autoRaise(self): # real signature unknown; restored from __doc__
        """ autoRaise(self) -> bool """
        return False

    def changeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ changeEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> PySide2.QtWidgets.QAction """
        pass

    def enterEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ enterEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def hitButton(self, pos): # real signature unknown; restored from __doc__
        """ hitButton(self, pos: PySide2.QtCore.QPoint) -> bool """
        return False

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionToolButton) -> None """
        pass

    def leaveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ leaveEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def menu(self): # real signature unknown; restored from __doc__
        """ menu(self) -> PySide2.QtWidgets.QMenu """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def mousePressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def nextCheckState(self): # real signature unknown; restored from __doc__
        """ nextCheckState(self) -> None """
        pass

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def popupMode(self): # real signature unknown; restored from __doc__
        """ popupMode(self) -> PySide2.QtWidgets.QToolButton.ToolButtonPopupMode """
        pass

    def setArrowType(self, type): # real signature unknown; restored from __doc__
        """ setArrowType(self, type: PySide2.QtCore.Qt.ArrowType) -> None """
        pass

    def setAutoRaise(self, enable): # real signature unknown; restored from __doc__
        """ setAutoRaise(self, enable: bool) -> None """
        pass

    def setDefaultAction(self, arg__1): # real signature unknown; restored from __doc__
        """ setDefaultAction(self, arg__1: PySide2.QtWidgets.QAction) -> None """
        pass

    def setMenu(self, menu): # real signature unknown; restored from __doc__
        """ setMenu(self, menu: PySide2.QtWidgets.QMenu) -> None """
        pass

    def setPopupMode(self, mode): # real signature unknown; restored from __doc__
        """ setPopupMode(self, mode: PySide2.QtWidgets.QToolButton.ToolButtonPopupMode) -> None """
        pass

    def setToolButtonStyle(self, style): # real signature unknown; restored from __doc__
        """ setToolButtonStyle(self, style: PySide2.QtCore.Qt.ToolButtonStyle) -> None """
        pass

    def showMenu(self): # real signature unknown; restored from __doc__
        """ showMenu(self) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def timerEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def toolButtonStyle(self): # real signature unknown; restored from __doc__
        """ toolButtonStyle(self) -> PySide2.QtCore.Qt.ToolButtonStyle """
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
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

    DelayedPopup = PySide2.QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup
    InstantPopup = PySide2.QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup
    MenuButtonPopup = PySide2.QtWidgets.QToolButton.ToolButtonPopupMode.MenuButtonPopup
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50830380>'
    ToolButtonPopupMode = None # (!) real value is "<class 'PySide2.QtWidgets.QToolButton.ToolButtonPopupMode'>"


