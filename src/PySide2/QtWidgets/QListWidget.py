# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QListView import QListView

class QListWidget(QListView):
    """ QListWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def addItem(self, item): # real signature unknown; restored from __doc__
        """
        addItem(self, item: PySide2.QtWidgets.QListWidgetItem) -> None
        addItem(self, label: str) -> None
        """
        pass

    def addItems(self, labels, p_str=None): # real signature unknown; restored from __doc__
        """ addItems(self, labels: typing.Sequence[str]) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def closePersistentEditor(self, index): # real signature unknown; restored from __doc__
        """
        closePersistentEditor(self, index: PySide2.QtCore.QModelIndex) -> None
        closePersistentEditor(self, item: PySide2.QtWidgets.QListWidgetItem) -> None
        """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> PySide2.QtWidgets.QListWidgetItem """
        pass

    def currentItemChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ currentRow(self) -> int """
        return 0

    def currentRowChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None """
        pass

    def dropMimeData(self, index, data, action): # real signature unknown; restored from __doc__
        """ dropMimeData(self, index: int, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction) -> bool """
        return False

    def editItem(self, item): # real signature unknown; restored from __doc__
        """ editItem(self, item: PySide2.QtWidgets.QListWidgetItem) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def findItems(self, text, flags): # real signature unknown; restored from __doc__
        """ findItems(self, text: str, flags: PySide2.QtCore.Qt.MatchFlags) -> typing.List[PySide2.QtWidgets.QListWidgetItem] """
        pass

    def indexFromItem(self, item): # real signature unknown; restored from __doc__
        """ indexFromItem(self, item: PySide2.QtWidgets.QListWidgetItem) -> PySide2.QtCore.QModelIndex """
        pass

    def insertItem(self, row, item): # real signature unknown; restored from __doc__
        """
        insertItem(self, row: int, item: PySide2.QtWidgets.QListWidgetItem) -> None
        insertItem(self, row: int, label: str) -> None
        """
        pass

    def insertItems(self, row, labels, p_str=None): # real signature unknown; restored from __doc__
        """ insertItems(self, row: int, labels: typing.Sequence[str]) -> None """
        pass

    def isItemHidden(self, item): # real signature unknown; restored from __doc__
        """ isItemHidden(self, item: PySide2.QtWidgets.QListWidgetItem) -> bool """
        return False

    def isItemSelected(self, item): # real signature unknown; restored from __doc__
        """ isItemSelected(self, item: PySide2.QtWidgets.QListWidgetItem) -> bool """
        return False

    def isPersistentEditorOpen(self, index): # real signature unknown; restored from __doc__
        """
        isPersistentEditorOpen(self, index: PySide2.QtCore.QModelIndex) -> bool
        isPersistentEditorOpen(self, item: PySide2.QtWidgets.QListWidgetItem) -> bool
        """
        return False

    def isSortingEnabled(self): # real signature unknown; restored from __doc__
        """ isSortingEnabled(self) -> bool """
        return False

    def item(self, row): # real signature unknown; restored from __doc__
        """ item(self, row: int) -> PySide2.QtWidgets.QListWidgetItem """
        pass

    def itemActivated(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, p): # real signature unknown; restored from __doc__
        """
        itemAt(self, p: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QListWidgetItem
        itemAt(self, x: int, y: int) -> PySide2.QtWidgets.QListWidgetItem
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
        """ itemFromIndex(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QListWidgetItem """
        pass

    def itemPressed(self, *args, **kwargs): # real signature unknown
        pass

    def items(self, data): # real signature unknown; restored from __doc__
        """ items(self, data: PySide2.QtCore.QMimeData) -> typing.List[PySide2.QtWidgets.QListWidgetItem] """
        pass

    def itemSelectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def itemWidget(self, item): # real signature unknown; restored from __doc__
        """ itemWidget(self, item: PySide2.QtWidgets.QListWidgetItem) -> PySide2.QtWidgets.QWidget """
        pass

    def mimeData(self, items, PySide2_QtWidgets_QListWidgetItem=None): # real signature unknown; restored from __doc__
        """ mimeData(self, items: typing.Sequence[PySide2.QtWidgets.QListWidgetItem]) -> PySide2.QtCore.QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> typing.List[str] """
        pass

    def openPersistentEditor(self, index): # real signature unknown; restored from __doc__
        """
        openPersistentEditor(self, index: PySide2.QtCore.QModelIndex) -> None
        openPersistentEditor(self, item: PySide2.QtWidgets.QListWidgetItem) -> None
        """
        pass

    def removeItemWidget(self, item): # real signature unknown; restored from __doc__
        """ removeItemWidget(self, item: PySide2.QtWidgets.QListWidgetItem) -> None """
        pass

    def row(self, item): # real signature unknown; restored from __doc__
        """ row(self, item: PySide2.QtWidgets.QListWidgetItem) -> int """
        return 0

    def scrollToItem(self, item, hint=None): # real signature unknown; restored from __doc__
        """ scrollToItem(self, item: PySide2.QtWidgets.QListWidgetItem, hint: PySide2.QtWidgets.QAbstractItemView.ScrollHint = PySide2.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible) -> None """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> typing.List[PySide2.QtWidgets.QListWidgetItem] """
        pass

    def setCurrentItem(self, item): # real signature unknown; restored from __doc__
        """
        setCurrentItem(self, item: PySide2.QtWidgets.QListWidgetItem) -> None
        setCurrentItem(self, item: PySide2.QtWidgets.QListWidgetItem, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None
        """
        pass

    def setCurrentRow(self, row): # real signature unknown; restored from __doc__
        """
        setCurrentRow(self, row: int) -> None
        setCurrentRow(self, row: int, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None
        """
        pass

    def setItemHidden(self, item, hide): # real signature unknown; restored from __doc__
        """ setItemHidden(self, item: PySide2.QtWidgets.QListWidgetItem, hide: bool) -> None """
        pass

    def setItemSelected(self, item, select): # real signature unknown; restored from __doc__
        """ setItemSelected(self, item: PySide2.QtWidgets.QListWidgetItem, select: bool) -> None """
        pass

    def setItemWidget(self, item, widget): # real signature unknown; restored from __doc__
        """ setItemWidget(self, item: PySide2.QtWidgets.QListWidgetItem, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setSelectionModel(self, selectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: PySide2.QtCore.QItemSelectionModel) -> None """
        pass

    def setSortingEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setSortingEnabled(self, enable: bool) -> None """
        pass

    def sortItems(self, order=None): # real signature unknown; restored from __doc__
        """ sortItems(self, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions """
        pass

    def takeItem(self, row): # real signature unknown; restored from __doc__
        """ takeItem(self, row: int) -> PySide2.QtWidgets.QListWidgetItem """
        pass

    def visualItemRect(self, item): # real signature unknown; restored from __doc__
        """ visualItemRect(self, item: PySide2.QtWidgets.QListWidgetItem) -> PySide2.QtCore.QRect """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50814400>'


