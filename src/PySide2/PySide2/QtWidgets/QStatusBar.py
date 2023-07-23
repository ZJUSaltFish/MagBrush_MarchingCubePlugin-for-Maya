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

class QStatusBar(QWidget):
    """ QStatusBar(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def addPermanentWidget(self, widget, stretch=0): # real signature unknown; restored from __doc__
        """ addPermanentWidget(self, widget: PySide2.QtWidgets.QWidget, stretch: int = 0) -> None """
        pass

    def addWidget(self, widget, stretch=0): # real signature unknown; restored from __doc__
        """ addWidget(self, widget: PySide2.QtWidgets.QWidget, stretch: int = 0) -> None """
        pass

    def clearMessage(self): # real signature unknown; restored from __doc__
        """ clearMessage(self) -> None """
        pass

    def currentMessage(self): # real signature unknown; restored from __doc__
        """ currentMessage(self) -> str """
        return ""

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def hideOrShow(self): # real signature unknown; restored from __doc__
        """ hideOrShow(self) -> None """
        pass

    def insertPermanentWidget(self, index, widget, stretch=0): # real signature unknown; restored from __doc__
        """ insertPermanentWidget(self, index: int, widget: PySide2.QtWidgets.QWidget, stretch: int = 0) -> int """
        return 0

    def insertWidget(self, index, widget, stretch=0): # real signature unknown; restored from __doc__
        """ insertWidget(self, index: int, widget: PySide2.QtWidgets.QWidget, stretch: int = 0) -> int """
        return 0

    def isSizeGripEnabled(self): # real signature unknown; restored from __doc__
        """ isSizeGripEnabled(self) -> bool """
        return False

    def messageChanged(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def reformat(self): # real signature unknown; restored from __doc__
        """ reformat(self) -> None """
        pass

    def removeWidget(self, widget): # real signature unknown; restored from __doc__
        """ removeWidget(self, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def setSizeGripEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setSizeGripEnabled(self, arg__1: bool) -> None """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def showMessage(self, text, timeout=0): # real signature unknown; restored from __doc__
        """ showMessage(self, text: str, timeout: int = 0) -> None """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507A5700>'


