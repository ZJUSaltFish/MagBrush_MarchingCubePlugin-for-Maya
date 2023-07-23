# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractItemView import QAbstractItemView

class QTableView(QAbstractItemView):
    """ QTableView(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def clearSpans(self): # real signature unknown; restored from __doc__
        """ clearSpans(self) -> None """
        pass

    def columnAt(self, x): # real signature unknown; restored from __doc__
        """ columnAt(self, x: int) -> int """
        return 0

    def columnCountChanged(self, oldCount, newCount): # real signature unknown; restored from __doc__
        """ columnCountChanged(self, oldCount: int, newCount: int) -> None """
        pass

    def columnMoved(self, column, oldIndex, newIndex): # real signature unknown; restored from __doc__
        """ columnMoved(self, column: int, oldIndex: int, newIndex: int) -> None """
        pass

    def columnResized(self, column, oldWidth, newWidth): # real signature unknown; restored from __doc__
        """ columnResized(self, column: int, oldWidth: int, newWidth: int) -> None """
        pass

    def columnSpan(self, row, column): # real signature unknown; restored from __doc__
        """ columnSpan(self, row: int, column: int) -> int """
        return 0

    def columnViewportPosition(self, column): # real signature unknown; restored from __doc__
        """ columnViewportPosition(self, column: int) -> int """
        return 0

    def columnWidth(self, column): # real signature unknown; restored from __doc__
        """ columnWidth(self, column: int) -> int """
        return 0

    def currentChanged(self, current, previous): # real signature unknown; restored from __doc__
        """ currentChanged(self, current: PySide2.QtCore.QModelIndex, previous: PySide2.QtCore.QModelIndex) -> None """
        pass

    def doItemsLayout(self): # real signature unknown; restored from __doc__
        """ doItemsLayout(self) -> None """
        pass

    def gridStyle(self): # real signature unknown; restored from __doc__
        """ gridStyle(self) -> PySide2.QtCore.Qt.PenStyle """
        pass

    def hideColumn(self, column): # real signature unknown; restored from __doc__
        """ hideColumn(self, column: int) -> None """
        pass

    def hideRow(self, row): # real signature unknown; restored from __doc__
        """ hideRow(self, row: int) -> None """
        pass

    def horizontalHeader(self): # real signature unknown; restored from __doc__
        """ horizontalHeader(self) -> PySide2.QtWidgets.QHeaderView """
        pass

    def horizontalOffset(self): # real signature unknown; restored from __doc__
        """ horizontalOffset(self) -> int """
        return 0

    def horizontalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ horizontalScrollbarAction(self, action: int) -> None """
        pass

    def indexAt(self, p): # real signature unknown; restored from __doc__
        """ indexAt(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QModelIndex """
        pass

    def isColumnHidden(self, column): # real signature unknown; restored from __doc__
        """ isColumnHidden(self, column: int) -> bool """
        return False

    def isCornerButtonEnabled(self): # real signature unknown; restored from __doc__
        """ isCornerButtonEnabled(self) -> bool """
        return False

    def isIndexHidden(self, index): # real signature unknown; restored from __doc__
        """ isIndexHidden(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def isRowHidden(self, row): # real signature unknown; restored from __doc__
        """ isRowHidden(self, row: int) -> bool """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

    def moveCursor(self, cursorAction, modifiers): # real signature unknown; restored from __doc__
        """ moveCursor(self, cursorAction: PySide2.QtWidgets.QAbstractItemView.CursorAction, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> PySide2.QtCore.QModelIndex """
        pass

    def paintEvent(self, e): # real signature unknown; restored from __doc__
        """ paintEvent(self, e: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def resizeColumnsToContents(self): # real signature unknown; restored from __doc__
        """ resizeColumnsToContents(self) -> None """
        pass

    def resizeColumnToContents(self, column): # real signature unknown; restored from __doc__
        """ resizeColumnToContents(self, column: int) -> None """
        pass

    def resizeRowsToContents(self): # real signature unknown; restored from __doc__
        """ resizeRowsToContents(self) -> None """
        pass

    def resizeRowToContents(self, row): # real signature unknown; restored from __doc__
        """ resizeRowToContents(self, row: int) -> None """
        pass

    def rowAt(self, y): # real signature unknown; restored from __doc__
        """ rowAt(self, y: int) -> int """
        return 0

    def rowCountChanged(self, oldCount, newCount): # real signature unknown; restored from __doc__
        """ rowCountChanged(self, oldCount: int, newCount: int) -> None """
        pass

    def rowHeight(self, row): # real signature unknown; restored from __doc__
        """ rowHeight(self, row: int) -> int """
        return 0

    def rowMoved(self, row, oldIndex, newIndex): # real signature unknown; restored from __doc__
        """ rowMoved(self, row: int, oldIndex: int, newIndex: int) -> None """
        pass

    def rowResized(self, row, oldHeight, newHeight): # real signature unknown; restored from __doc__
        """ rowResized(self, row: int, oldHeight: int, newHeight: int) -> None """
        pass

    def rowSpan(self, row, column): # real signature unknown; restored from __doc__
        """ rowSpan(self, row: int, column: int) -> int """
        return 0

    def rowViewportPosition(self, row): # real signature unknown; restored from __doc__
        """ rowViewportPosition(self, row: int) -> int """
        return 0

    def scrollContentsBy(self, dx, dy): # real signature unknown; restored from __doc__
        """ scrollContentsBy(self, dx: int, dy: int) -> None """
        pass

    def scrollTo(self, index, hint=None): # real signature unknown; restored from __doc__
        """ scrollTo(self, index: PySide2.QtCore.QModelIndex, hint: PySide2.QtWidgets.QAbstractItemView.ScrollHint = PySide2.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible) -> None """
        pass

    def selectColumn(self, column): # real signature unknown; restored from __doc__
        """ selectColumn(self, column: int) -> None """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> typing.List[int] """
        pass

    def selectionChanged(self, selected, deselected): # real signature unknown; restored from __doc__
        """ selectionChanged(self, selected: PySide2.QtCore.QItemSelection, deselected: PySide2.QtCore.QItemSelection) -> None """
        pass

    def selectRow(self, row): # real signature unknown; restored from __doc__
        """ selectRow(self, row: int) -> None """
        pass

    def setColumnHidden(self, column, hide): # real signature unknown; restored from __doc__
        """ setColumnHidden(self, column: int, hide: bool) -> None """
        pass

    def setColumnWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnWidth(self, column: int, width: int) -> None """
        pass

    def setCornerButtonEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setCornerButtonEnabled(self, enable: bool) -> None """
        pass

    def setGridStyle(self, style): # real signature unknown; restored from __doc__
        """ setGridStyle(self, style: PySide2.QtCore.Qt.PenStyle) -> None """
        pass

    def setHorizontalHeader(self, header): # real signature unknown; restored from __doc__
        """ setHorizontalHeader(self, header: PySide2.QtWidgets.QHeaderView) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setRootIndex(self, index): # real signature unknown; restored from __doc__
        """ setRootIndex(self, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setRowHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowHeight(self, row: int, height: int) -> None """
        pass

    def setRowHidden(self, row, hide): # real signature unknown; restored from __doc__
        """ setRowHidden(self, row: int, hide: bool) -> None """
        pass

    def setSelection(self, rect, command): # real signature unknown; restored from __doc__
        """ setSelection(self, rect: PySide2.QtCore.QRect, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None """
        pass

    def setSelectionModel(self, selectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: PySide2.QtCore.QItemSelectionModel) -> None """
        pass

    def setShowGrid(self, show): # real signature unknown; restored from __doc__
        """ setShowGrid(self, show: bool) -> None """
        pass

    def setSortingEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, enable: bool) -> None """
        pass

    def setSpan(self, row, column, rowSpan, columnSpan): # real signature unknown; restored from __doc__
        """ setSpan(self, row: int, column: int, rowSpan: int, columnSpan: int) -> None """
        pass

    def setVerticalHeader(self, header): # real signature unknown; restored from __doc__
        """ setVerticalHeader(self, header: PySide2.QtWidgets.QHeaderView) -> None """
        pass

    def setWordWrap(self, on): # real signature unknown; restored from __doc__
        """ setWordWrap(self, on: bool) -> None """
        pass

    def showColumn(self, column): # real signature unknown; restored from __doc__
        """ showColumn(self, column: int) -> None """
        pass

    def showGrid(self): # real signature unknown; restored from __doc__
        """ showGrid(self) -> bool """
        return False

    def showRow(self, row): # real signature unknown; restored from __doc__
        """ showRow(self, row: int) -> None """
        pass

    def sizeHintForColumn(self, column): # real signature unknown; restored from __doc__
        """ sizeHintForColumn(self, column: int) -> int """
        return 0

    def sizeHintForRow(self, row): # real signature unknown; restored from __doc__
        """ sizeHintForRow(self, row: int) -> int """
        return 0

    def sortByColumn(self, column): # real signature unknown; restored from __doc__
        """
        sortByColumn(self, column: int) -> None
        sortByColumn(self, column: int, order: PySide2.QtCore.Qt.SortOrder) -> None
        """
        pass

    def timerEvent(self, event): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def updateGeometries(self): # real signature unknown; restored from __doc__
        """ updateGeometries(self) -> None """
        pass

    def verticalHeader(self): # real signature unknown; restored from __doc__
        """ verticalHeader(self) -> PySide2.QtWidgets.QHeaderView """
        pass

    def verticalOffset(self): # real signature unknown; restored from __doc__
        """ verticalOffset(self) -> int """
        return 0

    def verticalScrollbarAction(self, action): # real signature unknown; restored from __doc__
        """ verticalScrollbarAction(self, action: int) -> None """
        pass

    def viewOptions(self): # real signature unknown; restored from __doc__
        """ viewOptions(self) -> PySide2.QtWidgets.QStyleOptionViewItem """
        pass

    def viewportSizeHint(self): # real signature unknown; restored from __doc__
        """ viewportSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def visualRect(self, index): # real signature unknown; restored from __doc__
        """ visualRect(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QRect """
        pass

    def visualRegionForSelection(self, selection): # real signature unknown; restored from __doc__
        """ visualRegionForSelection(self, selection: PySide2.QtCore.QItemSelection) -> PySide2.QtGui.QRegion """
        pass

    def wordWrap(self): # real signature unknown; restored from __doc__
        """ wordWrap(self) -> bool """
        return False

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F508017C0>'


