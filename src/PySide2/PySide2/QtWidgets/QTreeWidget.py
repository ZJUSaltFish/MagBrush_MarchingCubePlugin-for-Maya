# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QTreeView import QTreeView

class QTreeWidget(QTreeView):
    """ QTreeWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def addTopLevelItem(self, item): # real signature unknown; restored from __doc__
        """ addTopLevelItem(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> None """
        pass

    def addTopLevelItems(self, items, PySide2_QtWidgets_QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ addTopLevelItems(self, items: typing.Sequence[PySide2.QtWidgets.QTreeWidgetItem]) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def closePersistentEditor(self, index): # real signature unknown; restored from __doc__
        """
        closePersistentEditor(self, index: PySide2.QtCore.QModelIndex) -> None
        closePersistentEditor(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int = 0) -> None
        """
        pass

    def collapseItem(self, item): # real signature unknown; restored from __doc__
        """ collapseItem(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> None """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ currentColumn(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def currentItemChanged(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, event): # real signature unknown; restored from __doc__
        """ dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None """
        pass

    def dropMimeData(self, parent, index, data, action): # real signature unknown; restored from __doc__
        """ dropMimeData(self, parent: PySide2.QtWidgets.QTreeWidgetItem, index: int, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction) -> bool """
        return False

    def editItem(self, item, column=0): # real signature unknown; restored from __doc__
        """ editItem(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int = 0) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def expandItem(self, item): # real signature unknown; restored from __doc__
        """ expandItem(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> None """
        pass

    def findItems(self, text, flags, column=0): # real signature unknown; restored from __doc__
        """ findItems(self, text: str, flags: PySide2.QtCore.Qt.MatchFlags, column: int = 0) -> typing.List[PySide2.QtWidgets.QTreeWidgetItem] """
        pass

    def headerItem(self): # real signature unknown; restored from __doc__
        """ headerItem(self) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def indexFromItem(self, item, column=0): # real signature unknown; restored from __doc__
        """ indexFromItem(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int = 0) -> PySide2.QtCore.QModelIndex """
        pass

    def indexOfTopLevelItem(self, item): # real signature unknown; restored from __doc__
        """ indexOfTopLevelItem(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> int """
        return 0

    def insertTopLevelItem(self, index, item): # real signature unknown; restored from __doc__
        """ insertTopLevelItem(self, index: int, item: PySide2.QtWidgets.QTreeWidgetItem) -> None """
        pass

    def insertTopLevelItems(self, index, items, PySide2_QtWidgets_QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ insertTopLevelItems(self, index: int, items: typing.Sequence[PySide2.QtWidgets.QTreeWidgetItem]) -> None """
        pass

    def invisibleRootItem(self): # real signature unknown; restored from __doc__
        """ invisibleRootItem(self) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def isFirstItemColumnSpanned(self, item): # real signature unknown; restored from __doc__
        """ isFirstItemColumnSpanned(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> bool """
        return False

    def isItemExpanded(self, item): # real signature unknown; restored from __doc__
        """ isItemExpanded(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> bool """
        return False

    def isItemHidden(self, item): # real signature unknown; restored from __doc__
        """ isItemHidden(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> bool """
        return False

    def isItemSelected(self, item): # real signature unknown; restored from __doc__
        """ isItemSelected(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> bool """
        return False

    def isPersistentEditorOpen(self, index): # real signature unknown; restored from __doc__
        """
        isPersistentEditorOpen(self, index: PySide2.QtCore.QModelIndex) -> bool
        isPersistentEditorOpen(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int = 0) -> bool
        """
        return False

    def itemAbove(self, item): # real signature unknown; restored from __doc__
        """ itemAbove(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def itemActivated(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, p): # real signature unknown; restored from __doc__
        """
        itemAt(self, p: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QTreeWidgetItem
        itemAt(self, x: int, y: int) -> PySide2.QtWidgets.QTreeWidgetItem
        """
        pass

    def itemBelow(self, item): # real signature unknown; restored from __doc__
        """ itemBelow(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def itemChanged(self, *args, **kwargs): # real signature unknown
        pass

    def itemClicked(self, *args, **kwargs): # real signature unknown
        pass

    def itemCollapsed(self, *args, **kwargs): # real signature unknown
        pass

    def itemDoubleClicked(self, *args, **kwargs): # real signature unknown
        pass

    def itemEntered(self, *args, **kwargs): # real signature unknown
        pass

    def itemExpanded(self, *args, **kwargs): # real signature unknown
        pass

    def itemFromIndex(self, index): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def itemPressed(self, *args, **kwargs): # real signature unknown
        pass

    def items(self, data): # real signature unknown; restored from __doc__
        """ items(self, data: PySide2.QtCore.QMimeData) -> typing.List[PySide2.QtWidgets.QTreeWidgetItem] """
        pass

    def itemSelectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def itemWidget(self, item, column): # real signature unknown; restored from __doc__
        """ itemWidget(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int) -> PySide2.QtWidgets.QWidget """
        pass

    def mimeData(self, items, PySide2_QtWidgets_QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ mimeData(self, items: typing.Sequence[PySide2.QtWidgets.QTreeWidgetItem]) -> PySide2.QtCore.QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> typing.List[str] """
        pass

    def openPersistentEditor(self, index): # real signature unknown; restored from __doc__
        """
        openPersistentEditor(self, index: PySide2.QtCore.QModelIndex) -> None
        openPersistentEditor(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int = 0) -> None
        """
        pass

    def removeItemWidget(self, item, column): # real signature unknown; restored from __doc__
        """ removeItemWidget(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int) -> None """
        pass

    def scrollToItem(self, item, hint=None): # real signature unknown; restored from __doc__
        """ scrollToItem(self, item: PySide2.QtWidgets.QTreeWidgetItem, hint: PySide2.QtWidgets.QAbstractItemView.ScrollHint = PySide2.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible) -> None """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> typing.List[PySide2.QtWidgets.QTreeWidgetItem] """
        pass

    def setColumnCount(self, columns): # real signature unknown; restored from __doc__
        """ setColumnCount(self, columns: int) -> None """
        pass

    def setCurrentItem(self, item): # real signature unknown; restored from __doc__
        """
        setCurrentItem(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> None
        setCurrentItem(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int) -> None
        setCurrentItem(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None
        """
        pass

    def setFirstItemColumnSpanned(self, item, span): # real signature unknown; restored from __doc__
        """ setFirstItemColumnSpanned(self, item: PySide2.QtWidgets.QTreeWidgetItem, span: bool) -> None """
        pass

    def setHeaderItem(self, item): # real signature unknown; restored from __doc__
        """ setHeaderItem(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> None """
        pass

    def setHeaderLabel(self, label): # real signature unknown; restored from __doc__
        """ setHeaderLabel(self, label: str) -> None """
        pass

    def setHeaderLabels(self, labels, p_str=None): # real signature unknown; restored from __doc__
        """ setHeaderLabels(self, labels: typing.Sequence[str]) -> None """
        pass

    def setItemExpanded(self, item, expand): # real signature unknown; restored from __doc__
        """ setItemExpanded(self, item: PySide2.QtWidgets.QTreeWidgetItem, expand: bool) -> None """
        pass

    def setItemHidden(self, item, hide): # real signature unknown; restored from __doc__
        """ setItemHidden(self, item: PySide2.QtWidgets.QTreeWidgetItem, hide: bool) -> None """
        pass

    def setItemSelected(self, item, select): # real signature unknown; restored from __doc__
        """ setItemSelected(self, item: PySide2.QtWidgets.QTreeWidgetItem, select: bool) -> None """
        pass

    def setItemWidget(self, item, column, widget): # real signature unknown; restored from __doc__
        """ setItemWidget(self, item: PySide2.QtWidgets.QTreeWidgetItem, column: int, widget: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def setSelectionModel(self, selectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, selectionModel: PySide2.QtCore.QItemSelectionModel) -> None """
        pass

    def sortColumn(self): # real signature unknown; restored from __doc__
        """ sortColumn(self) -> int """
        return 0

    def sortItems(self, column, order): # real signature unknown; restored from __doc__
        """ sortItems(self, column: int, order: PySide2.QtCore.Qt.SortOrder) -> None """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions """
        pass

    def takeTopLevelItem(self, index): # real signature unknown; restored from __doc__
        """ takeTopLevelItem(self, index: int) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def topLevelItem(self, index): # real signature unknown; restored from __doc__
        """ topLevelItem(self, index: int) -> PySide2.QtWidgets.QTreeWidgetItem """
        pass

    def topLevelItemCount(self): # real signature unknown; restored from __doc__
        """ topLevelItemCount(self) -> int """
        return 0

    def visualItemRect(self, item): # real signature unknown; restored from __doc__
        """ visualItemRect(self, item: PySide2.QtWidgets.QTreeWidgetItem) -> PySide2.QtCore.QRect """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50802F00>'


