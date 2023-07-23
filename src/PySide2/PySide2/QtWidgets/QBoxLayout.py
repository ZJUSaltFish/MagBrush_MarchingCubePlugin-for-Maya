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

class QBoxLayout(QLayout):
    """ QBoxLayout(self, arg__1: PySide2.QtWidgets.QBoxLayout.Direction, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def addItem(self, arg__1): # real signature unknown; restored from __doc__
        """ addItem(self, arg__1: PySide2.QtWidgets.QLayoutItem) -> None """
        pass

    def addLayout(self, layout, stretch=0): # real signature unknown; restored from __doc__
        """ addLayout(self, layout: PySide2.QtWidgets.QLayout, stretch: int = 0) -> None """
        pass

    def addSpacerItem(self, spacerItem): # real signature unknown; restored from __doc__
        """ addSpacerItem(self, spacerItem: PySide2.QtWidgets.QSpacerItem) -> None """
        pass

    def addSpacing(self, size): # real signature unknown; restored from __doc__
        """ addSpacing(self, size: int) -> None """
        pass

    def addStretch(self, stretch=0): # real signature unknown; restored from __doc__
        """ addStretch(self, stretch: int = 0) -> None """
        pass

    def addStrut(self, arg__1): # real signature unknown; restored from __doc__
        """ addStrut(self, arg__1: int) -> None """
        pass

    def addWidget(self, arg__1, stretch=0, alignment=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addWidget(self, arg__1: PySide2.QtWidgets.QWidget, stretch: int = 0, alignment: PySide2.QtCore.Qt.Alignment = Default(Qt.Alignment)) -> None
        addWidget(self, w: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> PySide2.QtWidgets.QBoxLayout.Direction """
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> PySide2.QtCore.Qt.Orientations """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ heightForWidth(self, arg__1: int) -> int """
        return 0

    def insertItem(self, index, arg__2): # real signature unknown; restored from __doc__
        """ insertItem(self, index: int, arg__2: PySide2.QtWidgets.QLayoutItem) -> None """
        pass

    def insertLayout(self, index, layout, stretch=0): # real signature unknown; restored from __doc__
        """ insertLayout(self, index: int, layout: PySide2.QtWidgets.QLayout, stretch: int = 0) -> None """
        pass

    def insertSpacerItem(self, index, spacerItem): # real signature unknown; restored from __doc__
        """ insertSpacerItem(self, index: int, spacerItem: PySide2.QtWidgets.QSpacerItem) -> None """
        pass

    def insertSpacing(self, index, size): # real signature unknown; restored from __doc__
        """ insertSpacing(self, index: int, size: int) -> None """
        pass

    def insertStretch(self, index, stretch=0): # real signature unknown; restored from __doc__
        """ insertStretch(self, index: int, stretch: int = 0) -> None """
        pass

    def insertWidget(self, index, widget, stretch=0, alignment=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertWidget(self, index: int, widget: PySide2.QtWidgets.QWidget, stretch: int = 0, alignment: PySide2.QtCore.Qt.Alignment = Default(Qt.Alignment)) -> None """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

    def itemAt(self, arg__1): # real signature unknown; restored from __doc__
        """ itemAt(self, arg__1: int) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> PySide2.QtCore.QSize """
        pass

    def minimumHeightForWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ minimumHeightForWidth(self, arg__1: int) -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> PySide2.QtCore.QSize """
        pass

    def setDirection(self, arg__1): # real signature unknown; restored from __doc__
        """ setDirection(self, arg__1: PySide2.QtWidgets.QBoxLayout.Direction) -> None """
        pass

    def setGeometry(self, arg__1): # real signature unknown; restored from __doc__
        """ setGeometry(self, arg__1: PySide2.QtCore.QRect) -> None """
        pass

    def setSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setSpacing(self, spacing: int) -> None """
        pass

    def setStretch(self, index, stretch): # real signature unknown; restored from __doc__
        """ setStretch(self, index: int, stretch: int) -> None """
        pass

    def setStretchFactor(self, l, stretch): # real signature unknown; restored from __doc__
        """
        setStretchFactor(self, l: PySide2.QtWidgets.QLayout, stretch: int) -> bool
        setStretchFactor(self, w: PySide2.QtWidgets.QWidget, stretch: int) -> bool
        """
        return False

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def stretch(self, index): # real signature unknown; restored from __doc__
        """ stretch(self, index: int) -> int """
        return 0

    def takeAt(self, arg__1): # real signature unknown; restored from __doc__
        """ takeAt(self, arg__1: int) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, arg__1, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    BottomToTop = PySide2.QtWidgets.QBoxLayout.Direction.BottomToTop
    Direction = None # (!) real value is "<class 'PySide2.QtWidgets.QBoxLayout.Direction'>"
    Down = PySide2.QtWidgets.QBoxLayout.Direction.Down
    LeftToRight = PySide2.QtWidgets.QBoxLayout.Direction.LeftToRight
    RightToLeft = PySide2.QtWidgets.QBoxLayout.Direction.RightToLeft
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50796280>'
    TopToBottom = PySide2.QtWidgets.QBoxLayout.Direction.TopToBottom
    Up = PySide2.QtWidgets.QBoxLayout.Direction.Up


