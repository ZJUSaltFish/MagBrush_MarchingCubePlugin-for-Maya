# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QLayoutItem import QLayoutItem

class QLayout(__PySide2_QtCore.QObject, QLayoutItem):
    """
    QLayout(self) -> None
    QLayout(self, parent: PySide2.QtWidgets.QWidget) -> None
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def addChildLayout(self, l): # real signature unknown; restored from __doc__
        """ addChildLayout(self, l: PySide2.QtWidgets.QLayout) -> None """
        pass

    def addChildWidget(self, w): # real signature unknown; restored from __doc__
        """ addChildWidget(self, w: PySide2.QtWidgets.QWidget) -> None """
        pass

    def addItem(self, arg__1): # real signature unknown; restored from __doc__
        """ addItem(self, arg__1: PySide2.QtWidgets.QLayoutItem) -> None """
        pass

    def addWidget(self, w): # real signature unknown; restored from __doc__
        """ addWidget(self, w: PySide2.QtWidgets.QWidget) -> None """
        pass

    def adoptLayout(self, layout): # real signature unknown; restored from __doc__
        """ adoptLayout(self, layout: PySide2.QtWidgets.QLayout) -> bool """
        return False

    def alignmentRect(self, arg__1): # real signature unknown; restored from __doc__
        """ alignmentRect(self, arg__1: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect """
        pass

    def childEvent(self, e): # real signature unknown; restored from __doc__
        """ childEvent(self, e: PySide2.QtCore.QChildEvent) -> None """
        pass

    def closestAcceptableSize(self, w, s): # real signature unknown; restored from __doc__
        """ closestAcceptableSize(w: PySide2.QtWidgets.QWidget, s: PySide2.QtCore.QSize) -> PySide2.QtCore.QSize """
        pass

    def contentsMargins(self): # real signature unknown; restored from __doc__
        """ contentsMargins(self) -> PySide2.QtCore.QMargins """
        pass

    def contentsRect(self): # real signature unknown; restored from __doc__
        """ contentsRect(self) -> PySide2.QtCore.QRect """
        pass

    def controlTypes(self): # real signature unknown; restored from __doc__
        """ controlTypes(self) -> PySide2.QtWidgets.QSizePolicy.ControlTypes """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> PySide2.QtCore.Qt.Orientations """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> PySide2.QtCore.QRect """
        pass

    def getContentsMargins(self): # real signature unknown; restored from __doc__
        """ getContentsMargins(self) -> typing.Tuple[int, int, int, int] """
        pass

    def indexOf(self, arg__1): # real signature unknown; restored from __doc__
        """
        indexOf(self, arg__1: PySide2.QtWidgets.QLayoutItem) -> int
        indexOf(self, arg__1: PySide2.QtWidgets.QWidget) -> int
        """
        return 0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def itemAt(self, index): # real signature unknown; restored from __doc__
        """ itemAt(self, index: int) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def layout(self): # real signature unknown; restored from __doc__
        """ layout(self) -> PySide2.QtWidgets.QLayout """
        pass

    def margin(self): # real signature unknown; restored from __doc__
        """ margin(self) -> int """
        return 0

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> PySide2.QtCore.QSize """
        pass

    def menuBar(self): # real signature unknown; restored from __doc__
        """ menuBar(self) -> PySide2.QtWidgets.QWidget """
        pass

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> PySide2.QtCore.QSize """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def removeItem(self, arg__1): # real signature unknown; restored from __doc__
        """ removeItem(self, arg__1: PySide2.QtWidgets.QLayoutItem) -> None """
        pass

    def removeWidget(self, w): # real signature unknown; restored from __doc__
        """ removeWidget(self, w: PySide2.QtWidgets.QWidget) -> None """
        pass

    def replaceWidget(self, from_, to, options=None): # real signature unknown; restored from __doc__
        """ replaceWidget(self, from_: PySide2.QtWidgets.QWidget, to: PySide2.QtWidgets.QWidget, options: PySide2.QtCore.Qt.FindChildOptions = PySide2.QtCore.Qt.FindChildOption.FindChildrenRecursively) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def setAlignment(self, arg__1): # real signature unknown; restored from __doc__
        """
        setAlignment(self, arg__1: PySide2.QtCore.Qt.Alignment) -> None
        setAlignment(self, l: PySide2.QtWidgets.QLayout, alignment: PySide2.QtCore.Qt.Alignment) -> bool
        setAlignment(self, w: PySide2.QtWidgets.QWidget, alignment: PySide2.QtCore.Qt.Alignment) -> bool
        """
        pass

    def setContentsMargins(self, left, top, right, bottom): # real signature unknown; restored from __doc__
        """
        setContentsMargins(self, left: int, top: int, right: int, bottom: int) -> None
        setContentsMargins(self, margins: PySide2.QtCore.QMargins) -> None
        """
        pass

    def setEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setEnabled(self, arg__1: bool) -> None """
        pass

    def setGeometry(self, arg__1): # real signature unknown; restored from __doc__
        """ setGeometry(self, arg__1: PySide2.QtCore.QRect) -> None """
        pass

    def setMargin(self, arg__1): # real signature unknown; restored from __doc__
        """ setMargin(self, arg__1: int) -> None """
        pass

    def setMenuBar(self, w): # real signature unknown; restored from __doc__
        """ setMenuBar(self, w: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setSizeConstraint(self, arg__1): # real signature unknown; restored from __doc__
        """ setSizeConstraint(self, arg__1: PySide2.QtWidgets.QLayout.SizeConstraint) -> None """
        pass

    def setSpacing(self, arg__1): # real signature unknown; restored from __doc__
        """ setSpacing(self, arg__1: int) -> None """
        pass

    def sizeConstraint(self): # real signature unknown; restored from __doc__
        """ sizeConstraint(self) -> PySide2.QtWidgets.QLayout.SizeConstraint """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, index): # real signature unknown; restored from __doc__
        """ takeAt(self, index: int) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def totalHeightForWidth(self, w): # real signature unknown; restored from __doc__
        """ totalHeightForWidth(self, w: int) -> int """
        return 0

    def totalMaximumSize(self): # real signature unknown; restored from __doc__
        """ totalMaximumSize(self) -> PySide2.QtCore.QSize """
        pass

    def totalMinimumSize(self): # real signature unknown; restored from __doc__
        """ totalMinimumSize(self) -> PySide2.QtCore.QSize """
        pass

    def totalSizeHint(self): # real signature unknown; restored from __doc__
        """ totalSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) -> None """
        pass

    def widgetEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ widgetEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
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

    SetDefaultConstraint = PySide2.QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
    SetFixedSize = PySide2.QtWidgets.QLayout.SizeConstraint.SetFixedSize
    SetMaximumSize = PySide2.QtWidgets.QLayout.SizeConstraint.SetMaximumSize
    SetMinAndMaxSize = PySide2.QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize
    SetMinimumSize = PySide2.QtWidgets.QLayout.SizeConstraint.SetMinimumSize
    SetNoConstraint = PySide2.QtWidgets.QLayout.SizeConstraint.SetNoConstraint
    SizeConstraint = None # (!) real value is "<class 'PySide2.QtWidgets.QLayout.SizeConstraint'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50794BC0>'


