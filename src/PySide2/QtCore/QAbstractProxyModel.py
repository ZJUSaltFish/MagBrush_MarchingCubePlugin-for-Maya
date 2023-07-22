# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractItemModel import QAbstractItemModel

class QAbstractProxyModel(QAbstractItemModel):
    """ QAbstractProxyModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def buddy(self, index): # real signature unknown; restored from __doc__
        """ buddy(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def canDropMimeData(self, data, action, row, column, parent): # real signature unknown; restored from __doc__
        """ canDropMimeData(self, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction, row: int, column: int, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def canFetchMore(self, parent): # real signature unknown; restored from __doc__
        """ canFetchMore(self, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def data(self, proxyIndex, role=None): # real signature unknown; restored from __doc__
        """ data(self, proxyIndex: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def dropMimeData(self, data, action, row, column, parent): # real signature unknown; restored from __doc__
        """ dropMimeData(self, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction, row: int, column: int, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def fetchMore(self, parent): # real signature unknown; restored from __doc__
        """ fetchMore(self, parent: PySide2.QtCore.QModelIndex) -> None """
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

    def itemData(self, index): # real signature unknown; restored from __doc__
        """ itemData(self, index: PySide2.QtCore.QModelIndex) -> typing.Dict[int, typing.Any] """
        pass

    def mapFromSource(self, sourceIndex): # real signature unknown; restored from __doc__
        """ mapFromSource(self, sourceIndex: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def mapSelectionFromSource(self, selection): # real signature unknown; restored from __doc__
        """ mapSelectionFromSource(self, selection: PySide2.QtCore.QItemSelection) -> PySide2.QtCore.QItemSelection """
        pass

    def mapSelectionToSource(self, selection): # real signature unknown; restored from __doc__
        """ mapSelectionToSource(self, selection: PySide2.QtCore.QItemSelection) -> PySide2.QtCore.QItemSelection """
        pass

    def mapToSource(self, proxyIndex): # real signature unknown; restored from __doc__
        """ mapToSource(self, proxyIndex: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def mimeData(self, indexes, p_int=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: typing.List[int]) -> PySide2.QtCore.QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> typing.List[str] """
        pass

    def resetInternalData(self): # real signature unknown; restored from __doc__
        """ resetInternalData(self) -> None """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) -> None """
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setHeaderData(self, section, orientation, value, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setItemData(self, index, roles, p_int=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: PySide2.QtCore.QModelIndex, roles: typing.Dict[int, typing.Any]) -> bool """
        return False

    def setSourceModel(self, sourceModel): # real signature unknown; restored from __doc__
        """ setSourceModel(self, sourceModel: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def sourceModel(self): # real signature unknown; restored from __doc__
        """ sourceModel(self) -> PySide2.QtCore.QAbstractItemModel """
        pass

    def sourceModelChanged(self, *args, **kwargs): # real signature unknown
        pass

    def span(self, index): # real signature unknown; restored from __doc__
        """ span(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def supportedDragActions(self): # real signature unknown; restored from __doc__
        """ supportedDragActions(self) -> PySide2.QtCore.Qt.DropActions """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E4F380>'


