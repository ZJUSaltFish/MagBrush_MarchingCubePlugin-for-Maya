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

class QDesktopWidget(QWidget):
    """ QDesktopWidget(self) -> None """
    def availableGeometry(self, point): # real signature unknown; restored from __doc__
        """
        availableGeometry(self, point: PySide2.QtCore.QPoint) -> PySide2.QtCore.QRect
        availableGeometry(self, screen: int = -1) -> PySide2.QtCore.QRect
        availableGeometry(self, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtCore.QRect
        """
        pass

    def isVirtualDesktop(self): # real signature unknown; restored from __doc__
        """ isVirtualDesktop(self) -> bool """
        return False

    def numScreens(self): # real signature unknown; restored from __doc__
        """ numScreens(self) -> int """
        return 0

    def primaryScreen(self): # real signature unknown; restored from __doc__
        """ primaryScreen(self) -> int """
        return 0

    def primaryScreenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def resized(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, e): # real signature unknown; restored from __doc__
        """ resizeEvent(self, e: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def screen(self): # real signature unknown; restored from __doc__
        """
        screen(self) -> PySide2.QtGui.QScreen
        screen(self, screen: int = -1) -> PySide2.QtWidgets.QWidget
        """
        pass

    def screenCount(self): # real signature unknown; restored from __doc__
        """ screenCount(self) -> int """
        return 0

    def screenCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def screenGeometry(self, point): # real signature unknown; restored from __doc__
        """
        screenGeometry(self, point: PySide2.QtCore.QPoint) -> PySide2.QtCore.QRect
        screenGeometry(self, screen: int = -1) -> PySide2.QtCore.QRect
        screenGeometry(self, widget: PySide2.QtWidgets.QWidget) -> PySide2.QtCore.QRect
        """
        pass

    def screenNumber(self, arg__1): # real signature unknown; restored from __doc__
        """
        screenNumber(self, arg__1: PySide2.QtCore.QPoint) -> int
        screenNumber(self, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> int
        """
        return 0

    def workAreaResized(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F508584C0>'


