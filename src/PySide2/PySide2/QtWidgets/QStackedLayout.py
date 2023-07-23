# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QLayout import QLayout

class QStackedLayout(QLayout):
    """
    QStackedLayout(self) -> None
    QStackedLayout(self, parent: PySide2.QtWidgets.QWidget) -> None
    QStackedLayout(self, parentLayout: PySide2.QtWidgets.QLayout) -> None
    """
    def addItem(self, item): # real signature unknown; restored from __doc__
        """ addItem(self, item: PySide2.QtWidgets.QLayoutItem) -> None """
        pass

    def addWidget(self, w): # real signature unknown; restored from __doc__
        """ addWidget(self, w: PySide2.QtWidgets.QWidget) -> int """
        return 0

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

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, width): # real signature unknown; restored from __doc__
        """ heightForWidth(self, width: int) -> int """
        return 0

    def insertWidget(self, index, w): # real signature unknown; restored from __doc__
        """ insertWidget(self, index: int, w: PySide2.QtWidgets.QWidget) -> int """
        return 0

    def itemAt(self, arg__1): # real signature unknown; restored from __doc__
        """ itemAt(self, arg__1: int) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> PySide2.QtCore.QSize """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) -> None """
        pass

    def setCurrentWidget(self, w): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, w: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: PySide2.QtCore.QRect) -> None """
        pass

    def setStackingMode(self, stackingMode): # real signature unknown; restored from __doc__
        """ setStackingMode(self, stackingMode: PySide2.QtWidgets.QStackedLayout.StackingMode) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def stackingMode(self): # real signature unknown; restored from __doc__
        """ stackingMode(self) -> PySide2.QtWidgets.QStackedLayout.StackingMode """
        pass

    def takeAt(self, arg__1): # real signature unknown; restored from __doc__
        """ takeAt(self, arg__1: int) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """
        widget(self) -> PySide2.QtWidgets.QWidget
        widget(self, arg__1: int) -> PySide2.QtWidgets.QWidget
        """
        pass

    def widgetRemoved(self, *args, **kwargs): # real signature unknown
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

    StackAll = PySide2.QtWidgets.QStackedLayout.StackingMode.StackAll
    StackingMode = None # (!) real value is "<class 'PySide2.QtWidgets.QStackedLayout.StackingMode'>"
    StackOne = PySide2.QtWidgets.QStackedLayout.StackingMode.StackOne
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50795E00>'


