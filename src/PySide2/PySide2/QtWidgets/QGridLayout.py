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

class QGridLayout(QLayout):
    """
    QGridLayout(self) -> None
    QGridLayout(self, parent: PySide2.QtWidgets.QWidget) -> None
    """
    def addItem(self, arg__1): # real signature unknown; restored from __doc__
        """
        addItem(self, arg__1: PySide2.QtWidgets.QLayoutItem) -> None
        addItem(self, item: PySide2.QtWidgets.QLayoutItem, row: int, column: int, rowSpan: int = 1, columnSpan: int = 1, alignment: PySide2.QtCore.Qt.Alignment = Default(Qt.Alignment)) -> None
        """
        pass

    def addLayout(self, arg__1, row, column, alignment=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addLayout(self, arg__1: PySide2.QtWidgets.QLayout, row: int, column: int, alignment: PySide2.QtCore.Qt.Alignment = Default(Qt.Alignment)) -> None
        addLayout(self, arg__1: PySide2.QtWidgets.QLayout, row: int, column: int, rowSpan: int, columnSpan: int, alignment: PySide2.QtCore.Qt.Alignment = Default(Qt.Alignment)) -> None
        """
        pass

    def addWidget(self, arg__1, row, column, alignment=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addWidget(self, arg__1: PySide2.QtWidgets.QWidget, row: int, column: int, alignment: PySide2.QtCore.Qt.Alignment = Default(Qt.Alignment)) -> None
        addWidget(self, arg__1: PySide2.QtWidgets.QWidget, row: int, column: int, rowSpan: int, columnSpan: int, alignment: PySide2.QtCore.Qt.Alignment = Default(Qt.Alignment)) -> None
        addWidget(self, w: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def cellRect(self, row, column): # real signature unknown; restored from __doc__
        """ cellRect(self, row: int, column: int) -> PySide2.QtCore.QRect """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def columnMinimumWidth(self, column): # real signature unknown; restored from __doc__
        """ columnMinimumWidth(self, column: int) -> int """
        return 0

    def columnStretch(self, column): # real signature unknown; restored from __doc__
        """ columnStretch(self, column: int) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> PySide2.QtCore.Qt.Orientations """
        pass

    def getItemPosition(self, idx): # real signature unknown; restored from __doc__
        """ getItemPosition(self, idx: int) -> typing.Tuple[int, int, int, int] """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ heightForWidth(self, arg__1: int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> int """
        return 0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

    def itemAt(self, index): # real signature unknown; restored from __doc__
        """ itemAt(self, index: int) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def itemAtPosition(self, row, column): # real signature unknown; restored from __doc__
        """ itemAtPosition(self, row: int, column: int) -> PySide2.QtWidgets.QLayoutItem """
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

    def originCorner(self): # real signature unknown; restored from __doc__
        """ originCorner(self) -> PySide2.QtCore.Qt.Corner """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowMinimumHeight(self, row): # real signature unknown; restored from __doc__
        """ rowMinimumHeight(self, row: int) -> int """
        return 0

    def rowStretch(self, row): # real signature unknown; restored from __doc__
        """ rowStretch(self, row: int) -> int """
        return 0

    def setColumnMinimumWidth(self, column, minSize): # real signature unknown; restored from __doc__
        """ setColumnMinimumWidth(self, column: int, minSize: int) -> None """
        pass

    def setColumnStretch(self, column, stretch): # real signature unknown; restored from __doc__
        """ setColumnStretch(self, column: int, stretch: int) -> None """
        pass

    def setDefaultPositioning(self, n, orient): # real signature unknown; restored from __doc__
        """ setDefaultPositioning(self, n: int, orient: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def setGeometry(self, arg__1): # real signature unknown; restored from __doc__
        """ setGeometry(self, arg__1: PySide2.QtCore.QRect) -> None """
        pass

    def setHorizontalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, spacing: int) -> None """
        pass

    def setOriginCorner(self, arg__1): # real signature unknown; restored from __doc__
        """ setOriginCorner(self, arg__1: PySide2.QtCore.Qt.Corner) -> None """
        pass

    def setRowMinimumHeight(self, row, minSize): # real signature unknown; restored from __doc__
        """ setRowMinimumHeight(self, row: int, minSize: int) -> None """
        pass

    def setRowStretch(self, row, stretch): # real signature unknown; restored from __doc__
        """ setRowStretch(self, row: int, stretch: int) -> None """
        pass

    def setSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setSpacing(self, spacing: int) -> None """
        pass

    def setVerticalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, spacing: int) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, index): # real signature unknown; restored from __doc__
        """ takeAt(self, index: int) -> PySide2.QtWidgets.QLayoutItem """
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> int """
        return 0

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50795940>'


