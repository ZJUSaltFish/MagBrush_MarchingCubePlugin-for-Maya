# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractProxyModel import QAbstractProxyModel

class QSortFilterProxyModel(QAbstractProxyModel):
    """ QSortFilterProxyModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def buddy(self, index): # real signature unknown; restored from __doc__
        """ buddy(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def canFetchMore(self, parent): # real signature unknown; restored from __doc__
        """ canFetchMore(self, parent: PySide2.QtCore.QModelIndex) -> bool """
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

    def dynamicSortFilter(self): # real signature unknown; restored from __doc__
        """ dynamicSortFilter(self) -> bool """
        return False

    def dynamicSortFilterChanged(self, *args, **kwargs): # real signature unknown
        pass

    def fetchMore(self, parent): # real signature unknown; restored from __doc__
        """ fetchMore(self, parent: PySide2.QtCore.QModelIndex) -> None """
        pass

    def filterAcceptsColumn(self, source_column, source_parent): # real signature unknown; restored from __doc__
        """ filterAcceptsColumn(self, source_column: int, source_parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def filterAcceptsRow(self, source_row, source_parent): # real signature unknown; restored from __doc__
        """ filterAcceptsRow(self, source_row: int, source_parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def filterCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ filterCaseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity """
        pass

    def filterCaseSensitivityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def filterKeyColumn(self): # real signature unknown; restored from __doc__
        """ filterKeyColumn(self) -> int """
        return 0

    def filterRegExp(self): # real signature unknown; restored from __doc__
        """ filterRegExp(self) -> PySide2.QtCore.QRegExp """
        pass

    def filterRegularExpression(self): # real signature unknown; restored from __doc__
        """ filterRegularExpression(self) -> PySide2.QtCore.QRegularExpression """
        pass

    def filterRole(self): # real signature unknown; restored from __doc__
        """ filterRole(self) -> int """
        return 0

    def filterRoleChanged(self, *args, **kwargs): # real signature unknown
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

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> PySide2.QtCore.QModelIndex """
        pass

    def insertColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def insertRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) -> None """
        pass

    def invalidateFilter(self): # real signature unknown; restored from __doc__
        """ invalidateFilter(self) -> None """
        pass

    def isRecursiveFilteringEnabled(self): # real signature unknown; restored from __doc__
        """ isRecursiveFilteringEnabled(self) -> bool """
        return False

    def isSortLocaleAware(self): # real signature unknown; restored from __doc__
        """ isSortLocaleAware(self) -> bool """
        return False

    def lessThan(self, source_left, source_right): # real signature unknown; restored from __doc__
        """ lessThan(self, source_left: PySide2.QtCore.QModelIndex, source_right: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def mapFromSource(self, sourceIndex): # real signature unknown; restored from __doc__
        """ mapFromSource(self, sourceIndex: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def mapSelectionFromSource(self, sourceSelection): # real signature unknown; restored from __doc__
        """ mapSelectionFromSource(self, sourceSelection: PySide2.QtCore.QItemSelection) -> PySide2.QtCore.QItemSelection """
        pass

    def mapSelectionToSource(self, proxySelection): # real signature unknown; restored from __doc__
        """ mapSelectionToSource(self, proxySelection: PySide2.QtCore.QItemSelection) -> PySide2.QtCore.QItemSelection """
        pass

    def mapToSource(self, proxyIndex): # real signature unknown; restored from __doc__
        """ mapToSource(self, proxyIndex: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
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

    def parent(self): # real signature unknown; restored from __doc__
        """
        parent(self) -> PySide2.QtCore.QObject
        parent(self, child: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex
        """
        pass

    def recursiveFilteringEnabledChanged(self, *args, **kwargs): # real signature unknown
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

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setDynamicSortFilter(self, enable): # real signature unknown; restored from __doc__
        """ setDynamicSortFilter(self, enable: bool) -> None """
        pass

    def setFilterCaseSensitivity(self, cs): # real signature unknown; restored from __doc__
        """ setFilterCaseSensitivity(self, cs: PySide2.QtCore.Qt.CaseSensitivity) -> None """
        pass

    def setFilterFixedString(self, pattern): # real signature unknown; restored from __doc__
        """ setFilterFixedString(self, pattern: str) -> None """
        pass

    def setFilterKeyColumn(self, column): # real signature unknown; restored from __doc__
        """ setFilterKeyColumn(self, column: int) -> None """
        pass

    def setFilterRegExp(self, pattern): # real signature unknown; restored from __doc__
        """
        setFilterRegExp(self, pattern: str) -> None
        setFilterRegExp(self, regExp: PySide2.QtCore.QRegExp) -> None
        """
        pass

    def setFilterRegularExpression(self, pattern): # real signature unknown; restored from __doc__
        """
        setFilterRegularExpression(self, pattern: str) -> None
        setFilterRegularExpression(self, regularExpression: PySide2.QtCore.QRegularExpression) -> None
        """
        pass

    def setFilterRole(self, role): # real signature unknown; restored from __doc__
        """ setFilterRole(self, role: int) -> None """
        pass

    def setFilterWildcard(self, pattern): # real signature unknown; restored from __doc__
        """ setFilterWildcard(self, pattern: str) -> None """
        pass

    def setHeaderData(self, section, orientation, value, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setRecursiveFilteringEnabled(self, recursive): # real signature unknown; restored from __doc__
        """ setRecursiveFilteringEnabled(self, recursive: bool) -> None """
        pass

    def setSortCaseSensitivity(self, cs): # real signature unknown; restored from __doc__
        """ setSortCaseSensitivity(self, cs: PySide2.QtCore.Qt.CaseSensitivity) -> None """
        pass

    def setSortLocaleAware(self, on): # real signature unknown; restored from __doc__
        """ setSortLocaleAware(self, on: bool) -> None """
        pass

    def setSortRole(self, role): # real signature unknown; restored from __doc__
        """ setSortRole(self, role: int) -> None """
        pass

    def setSourceModel(self, sourceModel): # real signature unknown; restored from __doc__
        """ setSourceModel(self, sourceModel: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def sortCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ sortCaseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity """
        pass

    def sortCaseSensitivityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sortColumn(self): # real signature unknown; restored from __doc__
        """ sortColumn(self) -> int """
        return 0

    def sortLocaleAwareChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sortOrder(self): # real signature unknown; restored from __doc__
        """ sortOrder(self) -> PySide2.QtCore.Qt.SortOrder """
        pass

    def sortRole(self): # real signature unknown; restored from __doc__
        """ sortRole(self) -> int """
        return 0

    def sortRoleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def span(self, index): # real signature unknown; restored from __doc__
        """ span(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E4F840>'


