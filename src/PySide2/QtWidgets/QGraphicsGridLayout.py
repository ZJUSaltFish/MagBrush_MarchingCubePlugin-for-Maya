# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QGraphicsLayout import QGraphicsLayout

class QGraphicsGridLayout(QGraphicsLayout):
    """ QGraphicsGridLayout(self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsLayoutItem] = None) -> None """
    def addItem(self, item, row, column, alignment=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addItem(self, item: PySide2.QtWidgets.QGraphicsLayoutItem, row: int, column: int, alignment: PySide2.QtCore.Qt.Alignment = Default(Qt.Alignment)) -> None
        addItem(self, item: PySide2.QtWidgets.QGraphicsLayoutItem, row: int, column: int, rowSpan: int, columnSpan: int, alignment: PySide2.QtCore.Qt.Alignment = Default(Qt.Alignment)) -> None
        """
        pass

    def alignment(self, item): # real signature unknown; restored from __doc__
        """ alignment(self, item: PySide2.QtWidgets.QGraphicsLayoutItem) -> PySide2.QtCore.Qt.Alignment """
        pass

    def columnAlignment(self, column): # real signature unknown; restored from __doc__
        """ columnAlignment(self, column: int) -> PySide2.QtCore.Qt.Alignment """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def columnMaximumWidth(self, column): # real signature unknown; restored from __doc__
        """ columnMaximumWidth(self, column: int) -> float """
        return 0.0

    def columnMinimumWidth(self, column): # real signature unknown; restored from __doc__
        """ columnMinimumWidth(self, column: int) -> float """
        return 0.0

    def columnPreferredWidth(self, column): # real signature unknown; restored from __doc__
        """ columnPreferredWidth(self, column: int) -> float """
        return 0.0

    def columnSpacing(self, column): # real signature unknown; restored from __doc__
        """ columnSpacing(self, column: int) -> float """
        return 0.0

    def columnStretchFactor(self, column): # real signature unknown; restored from __doc__
        """ columnStretchFactor(self, column: int) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> float """
        return 0.0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

    def itemAt(self, index): # real signature unknown; restored from __doc__
        """
        itemAt(self, index: int) -> PySide2.QtWidgets.QGraphicsLayoutItem
        itemAt(self, row: int, column: int) -> PySide2.QtWidgets.QGraphicsLayoutItem
        """
        pass

    def removeAt(self, index): # real signature unknown; restored from __doc__
        """ removeAt(self, index: int) -> None """
        pass

    def removeItem(self, item): # real signature unknown; restored from __doc__
        """ removeItem(self, item: PySide2.QtWidgets.QGraphicsLayoutItem) -> None """
        pass

    def rowAlignment(self, row): # real signature unknown; restored from __doc__
        """ rowAlignment(self, row: int) -> PySide2.QtCore.Qt.Alignment """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowMaximumHeight(self, row): # real signature unknown; restored from __doc__
        """ rowMaximumHeight(self, row: int) -> float """
        return 0.0

    def rowMinimumHeight(self, row): # real signature unknown; restored from __doc__
        """ rowMinimumHeight(self, row: int) -> float """
        return 0.0

    def rowPreferredHeight(self, row): # real signature unknown; restored from __doc__
        """ rowPreferredHeight(self, row: int) -> float """
        return 0.0

    def rowSpacing(self, row): # real signature unknown; restored from __doc__
        """ rowSpacing(self, row: int) -> float """
        return 0.0

    def rowStretchFactor(self, row): # real signature unknown; restored from __doc__
        """ rowStretchFactor(self, row: int) -> int """
        return 0

    def setAlignment(self, item, alignment): # real signature unknown; restored from __doc__
        """ setAlignment(self, item: PySide2.QtWidgets.QGraphicsLayoutItem, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setColumnAlignment(self, column, alignment): # real signature unknown; restored from __doc__
        """ setColumnAlignment(self, column: int, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setColumnFixedWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnFixedWidth(self, column: int, width: float) -> None """
        pass

    def setColumnMaximumWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnMaximumWidth(self, column: int, width: float) -> None """
        pass

    def setColumnMinimumWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnMinimumWidth(self, column: int, width: float) -> None """
        pass

    def setColumnPreferredWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnPreferredWidth(self, column: int, width: float) -> None """
        pass

    def setColumnSpacing(self, column, spacing): # real signature unknown; restored from __doc__
        """ setColumnSpacing(self, column: int, spacing: float) -> None """
        pass

    def setColumnStretchFactor(self, column, stretch): # real signature unknown; restored from __doc__
        """ setColumnStretchFactor(self, column: int, stretch: int) -> None """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def setHorizontalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, spacing: float) -> None """
        pass

    def setRowAlignment(self, row, alignment): # real signature unknown; restored from __doc__
        """ setRowAlignment(self, row: int, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setRowFixedHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowFixedHeight(self, row: int, height: float) -> None """
        pass

    def setRowMaximumHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowMaximumHeight(self, row: int, height: float) -> None """
        pass

    def setRowMinimumHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowMinimumHeight(self, row: int, height: float) -> None """
        pass

    def setRowPreferredHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowPreferredHeight(self, row: int, height: float) -> None """
        pass

    def setRowSpacing(self, row, spacing): # real signature unknown; restored from __doc__
        """ setRowSpacing(self, row: int, spacing: float) -> None """
        pass

    def setRowStretchFactor(self, row, stretch): # real signature unknown; restored from __doc__
        """ setRowStretchFactor(self, row: int, stretch: int) -> None """
        pass

    def setSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setSpacing(self, spacing: float) -> None """
        pass

    def setVerticalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, spacing: float) -> None """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: PySide2.QtCore.Qt.SizeHint, constraint: PySide2.QtCore.QSizeF = Default(QSizeF)) -> PySide2.QtCore.QSizeF """
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> float """
        return 0.0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QGraphicsLayoutItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


