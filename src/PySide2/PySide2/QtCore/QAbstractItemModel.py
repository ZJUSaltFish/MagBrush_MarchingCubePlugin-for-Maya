# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QAbstractItemModel(QObject):
    """ QAbstractItemModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def beginInsertColumns(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginInsertColumns(self, parent: PySide2.QtCore.QModelIndex, first: int, last: int) -> None """
        pass

    def beginInsertRows(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginInsertRows(self, parent: PySide2.QtCore.QModelIndex, first: int, last: int) -> None """
        pass

    def beginMoveColumns(self, sourceParent, sourceFirst, sourceLast, destinationParent, destinationColumn): # real signature unknown; restored from __doc__
        """ beginMoveColumns(self, sourceParent: PySide2.QtCore.QModelIndex, sourceFirst: int, sourceLast: int, destinationParent: PySide2.QtCore.QModelIndex, destinationColumn: int) -> bool """
        return False

    def beginMoveRows(self, sourceParent, sourceFirst, sourceLast, destinationParent, destinationRow): # real signature unknown; restored from __doc__
        """ beginMoveRows(self, sourceParent: PySide2.QtCore.QModelIndex, sourceFirst: int, sourceLast: int, destinationParent: PySide2.QtCore.QModelIndex, destinationRow: int) -> bool """
        return False

    def beginRemoveColumns(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginRemoveColumns(self, parent: PySide2.QtCore.QModelIndex, first: int, last: int) -> None """
        pass

    def beginRemoveRows(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginRemoveRows(self, parent: PySide2.QtCore.QModelIndex, first: int, last: int) -> None """
        pass

    def beginResetModel(self): # real signature unknown; restored from __doc__
        """ beginResetModel(self) -> None """
        pass

    def buddy(self, index): # real signature unknown; restored from __doc__
        """ buddy(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def canDropMimeData(self, data, action, row, column, parent): # real signature unknown; restored from __doc__
        """ canDropMimeData(self, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction, row: int, column: int, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def canFetchMore(self, parent): # real signature unknown; restored from __doc__
        """ canFetchMore(self, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, from_, to): # real signature unknown; restored from __doc__
        """ changePersistentIndex(self, from_: PySide2.QtCore.QModelIndex, to: PySide2.QtCore.QModelIndex) -> None """
        pass

    def changePersistentIndexList(self, from_, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ changePersistentIndexList(self, from_: typing.List[int], to: typing.List[int]) -> None """
        pass

    def checkIndex(self, index, options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ checkIndex(self, index: PySide2.QtCore.QModelIndex, options: PySide2.QtCore.QAbstractItemModel.CheckIndexOptions = Instance(PySide2.QtCore.QAbstractItemModel.CheckIndexOptions.NoOption)) -> bool """
        pass

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def columnsAboutToBeInserted(self, *args, **kwargs): # real signature unknown
        pass

    def columnsAboutToBeMoved(self, *args, **kwargs): # real signature unknown
        pass

    def columnsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def columnsInserted(self, *args, **kwargs): # real signature unknown
        pass

    def columnsMoved(self, *args, **kwargs): # real signature unknown
        pass

    def columnsRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, row, column, id=0): # real signature unknown; restored from __doc__
        """
        createIndex(self, row: int, column: int, id: int = 0) -> PySide2.QtCore.QModelIndex
        createIndex(self, row: int, column: int, ptr: object) -> PySide2.QtCore.QModelIndex
        """
        pass

    def data(self, index, role=None): # real signature unknown; restored from __doc__
        """ data(self, index: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def decodeData(self, row, column, parent, stream): # real signature unknown; restored from __doc__
        """ decodeData(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex, stream: PySide2.QtCore.QDataStream) -> bool """
        return False

    def dropMimeData(self, data, action, row, column, parent): # real signature unknown; restored from __doc__
        """ dropMimeData(self, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction, row: int, column: int, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def encodeData(self, indexes, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ encodeData(self, indexes: typing.List[int], stream: PySide2.QtCore.QDataStream) -> None """
        pass

    def endInsertColumns(self): # real signature unknown; restored from __doc__
        """ endInsertColumns(self) -> None """
        pass

    def endInsertRows(self): # real signature unknown; restored from __doc__
        """ endInsertRows(self) -> None """
        pass

    def endMoveColumns(self): # real signature unknown; restored from __doc__
        """ endMoveColumns(self) -> None """
        pass

    def endMoveRows(self): # real signature unknown; restored from __doc__
        """ endMoveRows(self) -> None """
        pass

    def endRemoveColumns(self): # real signature unknown; restored from __doc__
        """ endRemoveColumns(self) -> None """
        pass

    def endRemoveRows(self): # real signature unknown; restored from __doc__
        """ endRemoveRows(self) -> None """
        pass

    def endResetModel(self): # real signature unknown; restored from __doc__
        """ endResetModel(self) -> None """
        pass

    def fetchMore(self, parent): # real signature unknown; restored from __doc__
        """ fetchMore(self, parent: PySide2.QtCore.QModelIndex) -> None """
        pass

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def hasIndex(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasIndex(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def headerDataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> PySide2.QtCore.QModelIndex """
        pass

    def insertColumn(self, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumn(self, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def insertColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def insertRow(self, row, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRow(self, row: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def insertRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def itemData(self, index): # real signature unknown; restored from __doc__
        """ itemData(self, index: PySide2.QtCore.QModelIndex) -> typing.Dict[int, typing.Any] """
        pass

    def layoutAboutToBeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def layoutChanged(self, *args, **kwargs): # real signature unknown
        pass

    def match(self, start, role, value, hits=1, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ match(self, start: PySide2.QtCore.QModelIndex, role: int, value: typing.Any, hits: int = 1, flags: PySide2.QtCore.Qt.MatchFlags = Instance(Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap))) -> typing.List[int] """
        pass

    def mimeData(self, indexes, p_int=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: typing.List[int]) -> PySide2.QtCore.QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> typing.List[str] """
        pass

    def modelAboutToBeReset(self, *args, **kwargs): # real signature unknown
        pass

    def modelReset(self, *args, **kwargs): # real signature unknown
        pass

    def moveColumn(self, sourceParent, sourceColumn, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveColumn(self, sourceParent: PySide2.QtCore.QModelIndex, sourceColumn: int, destinationParent: PySide2.QtCore.QModelIndex, destinationChild: int) -> bool """
        return False

    def moveColumns(self, sourceParent, sourceColumn, count, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveColumns(self, sourceParent: PySide2.QtCore.QModelIndex, sourceColumn: int, count: int, destinationParent: PySide2.QtCore.QModelIndex, destinationChild: int) -> bool """
        return False

    def moveRow(self, sourceParent, sourceRow, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveRow(self, sourceParent: PySide2.QtCore.QModelIndex, sourceRow: int, destinationParent: PySide2.QtCore.QModelIndex, destinationChild: int) -> bool """
        return False

    def moveRows(self, sourceParent, sourceRow, count, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveRows(self, sourceParent: PySide2.QtCore.QModelIndex, sourceRow: int, count: int, destinationParent: PySide2.QtCore.QModelIndex, destinationChild: int) -> bool """
        return False

    def parent(self): # real signature unknown; restored from __doc__
        """
        parent(self) -> PySide2.QtCore.QObject
        parent(self, child: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex
        """
        pass

    def persistentIndexList(self): # real signature unknown; restored from __doc__
        """ persistentIndexList(self) -> typing.List[int] """
        pass

    def removeColumn(self, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumn(self, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def removeRow(self, row, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRow(self, row: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def removeRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def resetInternalData(self): # real signature unknown; restored from __doc__
        """ resetInternalData(self) -> None """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) -> None """
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ roleNames(self) -> typing.Dict[int, PySide2.QtCore.QByteArray] """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def rowsAboutToBeInserted(self, *args, **kwargs): # real signature unknown
        pass

    def rowsAboutToBeMoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, *args, **kwargs): # real signature unknown
        pass

    def rowsMoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsRemoved(self, *args, **kwargs): # real signature unknown
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

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
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

    CheckIndexOption = None # (!) real value is "<class 'PySide2.QtCore.QAbstractItemModel.CheckIndexOption'>"
    CheckIndexOptions = None # (!) real value is "<class 'PySide2.QtCore.QAbstractItemModel.CheckIndexOptions'>"
    HorizontalSortHint = PySide2.QtCore.QAbstractItemModel.LayoutChangeHint.HorizontalSortHint
    LayoutChangeHint = None # (!) real value is "<class 'PySide2.QtCore.QAbstractItemModel.LayoutChangeHint'>"
    NoLayoutChangeHint = PySide2.QtCore.QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E4F040>'
    VerticalSortHint = PySide2.QtCore.QAbstractItemModel.LayoutChangeHint.VerticalSortHint


