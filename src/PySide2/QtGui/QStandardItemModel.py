# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QStandardItemModel(__PySide2_QtCore.QAbstractItemModel):
    """
    QStandardItemModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QStandardItemModel(self, rows: int, columns: int, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def appendColumn(self, items, PySide2_QtGui_QStandardItem=None): # real signature unknown; restored from __doc__
        """ appendColumn(self, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None """
        pass

    def appendRow(self, item): # real signature unknown; restored from __doc__
        """
        appendRow(self, item: PySide2.QtGui.QStandardItem) -> None
        appendRow(self, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clearItemData(self, index): # real signature unknown; restored from __doc__
        """ clearItemData(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def data(self, index, role=None): # real signature unknown; restored from __doc__
        """ data(self, index: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def dropMimeData(self, data, action, row, column, parent): # real signature unknown; restored from __doc__
        """ dropMimeData(self, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction, row: int, column: int, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def findItems(self, text, flags=None, column=0): # real signature unknown; restored from __doc__
        """ findItems(self, text: str, flags: PySide2.QtCore.Qt.MatchFlags = PySide2.QtCore.Qt.MatchFlag.MatchExactly, column: int = 0) -> typing.List[PySide2.QtGui.QStandardItem] """
        pass

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def horizontalHeaderItem(self, column): # real signature unknown; restored from __doc__
        """ horizontalHeaderItem(self, column: int) -> PySide2.QtGui.QStandardItem """
        pass

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> PySide2.QtCore.QModelIndex """
        pass

    def indexFromItem(self, item): # real signature unknown; restored from __doc__
        """ indexFromItem(self, item: PySide2.QtGui.QStandardItem) -> PySide2.QtCore.QModelIndex """
        pass

    def insertColumn(self, column, items, PySide2_QtGui_QStandardItem=None): # real signature unknown; restored from __doc__
        """
        insertColumn(self, column: int, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None
        insertColumn(self, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool
        """
        pass

    def insertColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def insertRow(self, row, item): # real signature unknown; restored from __doc__
        """
        insertRow(self, row: int, item: PySide2.QtGui.QStandardItem) -> None
        insertRow(self, row: int, items: typing.Sequence[PySide2.QtGui.QStandardItem]) -> None
        insertRow(self, row: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool
        """
        pass

    def insertRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def invisibleRootItem(self): # real signature unknown; restored from __doc__
        """ invisibleRootItem(self) -> PySide2.QtGui.QStandardItem """
        pass

    def item(self, row, column=0): # real signature unknown; restored from __doc__
        """ item(self, row: int, column: int = 0) -> PySide2.QtGui.QStandardItem """
        pass

    def itemChanged(self, *args, **kwargs): # real signature unknown
        pass

    def itemData(self, index): # real signature unknown; restored from __doc__
        """ itemData(self, index: PySide2.QtCore.QModelIndex) -> typing.Dict[int, typing.Any] """
        pass

    def itemFromIndex(self, index): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtGui.QStandardItem """
        pass

    def itemPrototype(self): # real signature unknown; restored from __doc__
        """ itemPrototype(self) -> PySide2.QtGui.QStandardItem """
        pass

    def mimeData(self, indexes, p_int=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: typing.List[int]) -> PySide2.QtCore.QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> typing.List[str] """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """
        parent(self) -> PySide2.QtCore.QObject
        parent(self, child: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex
        """
        pass

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def removeRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def setColumnCount(self, columns): # real signature unknown; restored from __doc__
        """ setColumnCount(self, columns: int) -> None """
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setHeaderData(self, section, orientation, value, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setHorizontalHeaderItem(self, column, item): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderItem(self, column: int, item: PySide2.QtGui.QStandardItem) -> None """
        pass

    def setHorizontalHeaderLabels(self, labels, p_str=None): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderLabels(self, labels: typing.Sequence[str]) -> None """
        pass

    def setItem(self, row, column, item): # real signature unknown; restored from __doc__
        """
        setItem(self, row: int, column: int, item: PySide2.QtGui.QStandardItem) -> None
        setItem(self, row: int, item: PySide2.QtGui.QStandardItem) -> None
        """
        pass

    def setItemData(self, index, roles, p_int=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: PySide2.QtCore.QModelIndex, roles: typing.Dict[int, typing.Any]) -> bool """
        return False

    def setItemPrototype(self, item): # real signature unknown; restored from __doc__
        """ setItemPrototype(self, item: PySide2.QtGui.QStandardItem) -> None """
        pass

    def setItemRoleNames(self, roleNames, p_int=None, PySide2_QtCore_QByteArray=None): # real signature unknown; restored from __doc__
        """ setItemRoleNames(self, roleNames: typing.Dict[int, PySide2.QtCore.QByteArray]) -> None """
        pass

    def setRowCount(self, rows): # real signature unknown; restored from __doc__
        """ setRowCount(self, rows: int) -> None """
        pass

    def setSortRole(self, role): # real signature unknown; restored from __doc__
        """ setSortRole(self, role: int) -> None """
        pass

    def setVerticalHeaderItem(self, row, item): # real signature unknown; restored from __doc__
        """ setVerticalHeaderItem(self, row: int, item: PySide2.QtGui.QStandardItem) -> None """
        pass

    def setVerticalHeaderLabels(self, labels, p_str=None): # real signature unknown; restored from __doc__
        """ setVerticalHeaderLabels(self, labels: typing.Sequence[str]) -> None """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def sortRole(self): # real signature unknown; restored from __doc__
        """ sortRole(self) -> int """
        return 0

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions """
        pass

    def takeColumn(self, column): # real signature unknown; restored from __doc__
        """ takeColumn(self, column: int) -> typing.List[PySide2.QtGui.QStandardItem] """
        pass

    def takeHorizontalHeaderItem(self, column): # real signature unknown; restored from __doc__
        """ takeHorizontalHeaderItem(self, column: int) -> PySide2.QtGui.QStandardItem """
        pass

    def takeItem(self, row, column=0): # real signature unknown; restored from __doc__
        """ takeItem(self, row: int, column: int = 0) -> PySide2.QtGui.QStandardItem """
        pass

    def takeRow(self, row): # real signature unknown; restored from __doc__
        """ takeRow(self, row: int) -> typing.List[PySide2.QtGui.QStandardItem] """
        pass

    def takeVerticalHeaderItem(self, row): # real signature unknown; restored from __doc__
        """ takeVerticalHeaderItem(self, row: int) -> PySide2.QtGui.QStandardItem """
        pass

    def verticalHeaderItem(self, row): # real signature unknown; restored from __doc__
        """ verticalHeaderItem(self, row: int) -> PySide2.QtGui.QStandardItem """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F008736C0>'


