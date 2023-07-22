# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QTableView import QTableView

class QTableWidget(QTableView):
    """
    QTableWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QTableWidget(self, rows: int, columns: int, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def cellActivated(self, *args, **kwargs): # real signature unknown
        pass

    def cellChanged(self, *args, **kwargs): # real signature unknown
        pass

    def cellClicked(self, *args, **kwargs): # real signature unknown
        pass

    def cellDoubleClicked(self, *args, **kwargs): # real signature unknown
        pass

    def cellEntered(self, *args, **kwargs): # real signature unknown
        pass

    def cellPressed(self, *args, **kwargs): # real signature unknown
        pass

    def cellWidget(self, row, column): # real signature unknown; restored from __doc__
        """ cellWidget(self, row: int, column: int) -> PySide2.QtWidgets.QWidget """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clearContents(self): # real signature unknown; restored from __doc__
        """ clearContents(self) -> None """
        pass

    def closePersistentEditor(self, index): # real signature unknown; restored from __doc__
        """
        closePersistentEditor(self, index: PySide2.QtCore.QModelIndex) -> None
        closePersistentEditor(self, item: PySide2.QtWidgets.QTableWidgetItem) -> None
        """
        pass

    def column(self, item): # real signature unknown; restored from __doc__
        """ column(self, item: PySide2.QtWidgets.QTableWidgetItem) -> int """
        return 0

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def currentCellChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ currentColumn(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def currentItemChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ currentRow(self) -> int """
        return 0

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None """
        pass

    def dropMimeData(self, row, column, data, action): # real signature unknown; restored from __doc__
        """ dropMimeData(self, row: int, column: int, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction) -> bool """
        return False

    def editItem(self, item): # real signature unknown; restored from __doc__
        """ editItem(self, item: PySide2.QtWidgets.QTableWidgetItem) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def findItems(self, text, flags): # real signature unknown; restored from __doc__
        """ findItems(self, text: str, flags: PySide2.QtCore.Qt.MatchFlags) -> typing.List[PySide2.QtWidgets.QTableWidgetItem] """
        pass

    def horizontalHeaderItem(self, column): # real signature unknown; restored from __doc__
        """ horizontalHeaderItem(self, column: int) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def indexFromItem(self, item): # real signature unknown; restored from __doc__
        """ indexFromItem(self, item: PySide2.QtWidgets.QTableWidgetItem) -> PySide2.QtCore.QModelIndex """
        pass

    def insertColumn(self, column): # real signature unknown; restored from __doc__
        """ insertColumn(self, column: int) -> None """
        pass

    def insertRow(self, row): # real signature unknown; restored from __doc__
        """ insertRow(self, row: int) -> None """
        pass

    def isItemSelected(self, item): # real signature unknown; restored from __doc__
        """ isItemSelected(self, item: PySide2.QtWidgets.QTableWidgetItem) -> bool """
        return False

    def isPersistentEditorOpen(self, index): # real signature unknown; restored from __doc__
        """
        isPersistentEditorOpen(self, index: PySide2.QtCore.QModelIndex) -> bool
        isPersistentEditorOpen(self, item: PySide2.QtWidgets.QTableWidgetItem) -> bool
        """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

    def item(self, row, column): # real signature unknown; restored from __doc__
        """ item(self, row: int, column: int) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def itemActivated(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, p): # real signature unknown; restored from __doc__
        """
        itemAt(self, p: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QTableWidgetItem
        itemAt(self, x: int, y: int) -> PySide2.QtWidgets.QTableWidgetItem
        """
        pass

    def itemChanged(self, *args, **kwargs): # real signature unknown
        pass

    def itemClicked(self, *args, **kwargs): # real signature unknown
        pass

    def itemDoubleClicked(self, *args, **kwargs): # real signature unknown
        pass

    def itemEntered(self, *args, **kwargs): # real signature unknown
        pass

    def itemFromIndex(self, index): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def itemPressed(self, *args, **kwargs): # real signature unknown
        pass

    def itemPrototype(self): # real signature unknown; restored from __doc__
        """ itemPrototype(self) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def items(self, data): # real signature unknown; restored from __doc__
        """ items(self, data: PySide2.QtCore.QMimeData) -> typing.List[PySide2.QtWidgets.QTableWidgetItem] """
        pass

    def itemSelectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mimeData(self, items, PySide2_QtWidgets_QTableWidgetItem=None): # real signature unknown; restored from __doc__
        """ mimeData(self, items: typing.Sequence[PySide2.QtWidgets.QTableWidgetItem]) -> PySide2.QtCore.QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> typing.List[str] """
        pass

    def openPersistentEditor(self, index): # real signature unknown; restored from __doc__
        """
        openPersistentEditor(self, index: PySide2.QtCore.QModelIndex) -> None
        openPersistentEditor(self, item: PySide2.QtWidgets.QTableWidgetItem) -> None
        """
        pass

    def removeCellWidget(self, row, column): # real signature unknown; restored from __doc__
        """ removeCellWidget(self, row: int, column: int) -> None """
        pass

    def removeColumn(self, column): # real signature unknown; restored from __doc__
        """ removeColumn(self, column: int) -> None """
        pass

    def removeRow(self, row): # real signature unknown; restored from __doc__
        """ removeRow(self, row: int) -> None """
        pass

    def row(self, item): # real signature unknown; restored from __doc__
        """ row(self, item: PySide2.QtWidgets.QTableWidgetItem) -> int """
        return 0

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def scrollToItem(self, item, hint=None): # real signature unknown; restored from __doc__
        """ scrollToItem(self, item: PySide2.QtWidgets.QTableWidgetItem, hint: PySide2.QtWidgets.QAbstractItemView.ScrollHint = PySide2.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible) -> None """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> typing.List[PySide2.QtWidgets.QTableWidgetItem] """
        pass

    def selectedRanges(self): # real signature unknown; restored from __doc__
        """ selectedRanges(self) -> typing.List[PySide2.QtWidgets.QTableWidgetSelectionRange] """
        pass

    def setCellWidget(self, row, column, widget): # real signature unknown; restored from __doc__
        """ setCellWidget(self, row: int, column: int, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setColumnCount(self, columns): # real signature unknown; restored from __doc__
        """ setColumnCount(self, columns: int) -> None """
        pass

    def setCurrentCell(self, row, column): # real signature unknown; restored from __doc__
        """
        setCurrentCell(self, row: int, column: int) -> None
        setCurrentCell(self, row: int, column: int, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None
        """
        pass

    def setCurrentItem(self, item): # real signature unknown; restored from __doc__
        """
        setCurrentItem(self, item: PySide2.QtWidgets.QTableWidgetItem) -> None
        setCurrentItem(self, item: PySide2.QtWidgets.QTableWidgetItem, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None
        """
        pass

    def setHorizontalHeaderItem(self, column, item): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderItem(self, column: int, item: PySide2.QtWidgets.QTableWidgetItem) -> None """
        pass

    def setHorizontalHeaderLabels(self, labels, p_str=None): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderLabels(self, labels: typing.Sequence[str]) -> None """
        pass

    def setItem(self, row, column, item): # real signature unknown; restored from __doc__
        """ setItem(self, row: int, column: int, item: PySide2.QtWidgets.QTableWidgetItem) -> None """
        pass

    def setItemPrototype(self, item): # real signature unknown; restored from __doc__
        """ setItemPrototype(self, item: PySide2.QtWidgets.QTableWidgetItem) -> None """
        pass

    def setItemSelected(self, item, select): # real signature unknown; restored from __doc__
        """ setItemSelected(self, item: PySide2.QtWidgets.QTableWidgetItem, select: bool) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setRangeSelected(self, range, select): # real signature unknown; restored from __doc__
        """ setRangeSelected(self, range: PySide2.QtWidgets.QTableWidgetSelectionRange, select: bool) -> None """
        pass

    def setRowCount(self, rows): # real signature unknown; restored from __doc__
        """ setRowCount(self, rows: int) -> None """
        pass

    def setSortingEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, enable: bool) -> None """
        pass

    def setVerticalHeaderItem(self, row, item): # real signature unknown; restored from __doc__
        """ setVerticalHeaderItem(self, row: int, item: PySide2.QtWidgets.QTableWidgetItem) -> None """
        pass

    def setVerticalHeaderLabels(self, labels, p_str=None): # real signature unknown; restored from __doc__
        """ setVerticalHeaderLabels(self, labels: typing.Sequence[str]) -> None """
        pass

    def sortItems(self, column, order=None): # real signature unknown; restored from __doc__
        """ sortItems(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions """
        pass

    def takeHorizontalHeaderItem(self, column): # real signature unknown; restored from __doc__
        """ takeHorizontalHeaderItem(self, column: int) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def takeItem(self, row, column): # real signature unknown; restored from __doc__
        """ takeItem(self, row: int, column: int) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def takeVerticalHeaderItem(self, row): # real signature unknown; restored from __doc__
        """ takeVerticalHeaderItem(self, row: int) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def verticalHeaderItem(self, row): # real signature unknown; restored from __doc__
        """ verticalHeaderItem(self, row: int) -> PySide2.QtWidgets.QTableWidgetItem """
        pass

    def visualColumn(self, logicalColumn): # real signature unknown; restored from __doc__
        """ visualColumn(self, logicalColumn: int) -> int """
        return 0

    def visualItemRect(self, item): # real signature unknown; restored from __doc__
        """ visualItemRect(self, item: PySide2.QtWidgets.QTableWidgetItem) -> PySide2.QtCore.QRect """
        pass

    def visualRow(self, logicalRow): # real signature unknown; restored from __doc__
        """ visualRow(self, logicalRow: int) -> int """
        return 0

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50802000>'


