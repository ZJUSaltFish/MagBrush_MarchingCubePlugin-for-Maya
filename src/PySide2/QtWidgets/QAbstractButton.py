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

class QAbstractButton(QWidget):
    """ QAbstractButton(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def animateClick(self, msec=100): # real signature unknown; restored from __doc__
        """ animateClick(self, msec: int = 100) -> None """
        pass

    def autoExclusive(self): # real signature unknown; restored from __doc__
        """ autoExclusive(self) -> bool """
        return False

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ autoRepeat(self) -> bool """
        return False

    def autoRepeatDelay(self): # real signature unknown; restored from __doc__
        """ autoRepeatDelay(self) -> int """
        return 0

    def autoRepeatInterval(self): # real signature unknown; restored from __doc__
        """ autoRepeatInterval(self) -> int """
        return 0

    def changeEvent(self, e): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: PySide2.QtCore.QEvent) -> None """
        pass

    def checkStateSet(self): # real signature unknown; restored from __doc__
        """ checkStateSet(self) -> None """
        pass

    def click(self): # real signature unknown; restored from __doc__
        """ click(self) -> None """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def focusInEvent(self, e): # real signature unknown; restored from __doc__
        """ focusInEvent(self, e: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def focusOutEvent(self, e): # real signature unknown; restored from __doc__
        """ focusOutEvent(self, e: PySide2.QtGui.QFocusEvent) -> None """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> PySide2.QtWidgets.QButtonGroup """
        pass

    def hitButton(self, pos): # real signature unknown; restored from __doc__
        """ hitButton(self, pos: PySide2.QtCore.QPoint) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def iconSize(self): # real signature unknown; restored from __doc__
        """ iconSize(self) -> PySide2.QtCore.QSize """
        pass

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ isCheckable(self) -> bool """
        return False

    def isChecked(self): # real signature unknown; restored from __doc__
        """ isChecked(self) -> bool """
        return False

    def isDown(self): # real signature unknown; restored from __doc__
        """ isDown(self) -> bool """
        return False

    def keyPressEvent(self, e): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, e: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def keyReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, e: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def mouseMoveEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mousePressEvent(self, e): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def mouseReleaseEvent(self, e): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, e: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def nextCheckState(self): # real signature unknown; restored from __doc__
        """ nextCheckState(self) -> None """
        pass

    def paintEvent(self, e): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def pressed(self, *args, **kwargs): # real signature unknown
        pass

    def released(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoExclusive(self, arg__1): # real signature unknown; restored from __doc__
        """ setAutoExclusive(self, arg__1: bool) -> None """
        pass

    def setAutoRepeat(self, arg__1): # real signature unknown; restored from __doc__
        """ setAutoRepeat(self, arg__1: bool) -> None """
        pass

    def setAutoRepeatDelay(self, arg__1): # real signature unknown; restored from __doc__
        """ setAutoRepeatDelay(self, arg__1: int) -> None """
        pass

    def setAutoRepeatInterval(self, arg__1): # real signature unknown; restored from __doc__
        """ setAutoRepeatInterval(self, arg__1: int) -> None """
        pass

    def setCheckable(self, arg__1): # real signature unknown; restored from __doc__
        """ setCheckable(self, arg__1: bool) -> None """
        pass

    def setChecked(self, arg__1): # real signature unknown; restored from __doc__
        """ setChecked(self, arg__1: bool) -> None """
        pass

    def setDown(self, arg__1): # real signature unknown; restored from __doc__
        """ setDown(self, arg__1: bool) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setIconSize(self, size): # real signature unknown; restored from __doc__
        """ setIconSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setShortcut(self, key): # real signature unknown; restored from __doc__
        """ setShortcut(self, key: PySide2.QtGui.QKeySequence) -> None """
        pass

    def setText(self, text): # real signature unknown; restored from __doc__
        """ setText(self, text: str) -> None """
        pass

    def shortcut(self): # real signature unknown; restored from __doc__
        """ shortcut(self) -> PySide2.QtGui.QKeySequence """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def timerEvent(self, e): # real signature unknown; restored from __doc__
        """ timerEvent(self, e: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def toggle(self): # real signature unknown; restored from __doc__
        """ toggle(self) -> None """
        pass

    def toggled(self, *args, **kwargs): # real signature unknown
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50817840>'


