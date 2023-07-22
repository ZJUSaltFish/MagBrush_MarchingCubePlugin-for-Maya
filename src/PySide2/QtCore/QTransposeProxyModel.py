# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractProxyModel import QAbstractProxyModel

class QTransposeProxyModel(QAbstractProxyModel):
    """ QTransposeProxyModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
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

    def itemData(self, index): # real signature unknown; restored from __doc__
        """ itemData(self, index: PySide2.QtCore.QModelIndex) -> typing.Dict[int, typing.Any] """
        pass

    def mapFromSource(self, sourceIndex): # real signature unknown; restored from __doc__
        """ mapFromSource(self, sourceIndex: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def mapToSource(self, proxyIndex): # real signature unknown; restored from __doc__
        """ mapToSource(self, proxyIndex: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def moveColumns(self, sourceParent, sourceColumn, count, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveColumns(self, sourceParent: PySide2.QtCore.QModelIndex, sourceColumn: int, count: int, destinationParent: PySide2.QtCore.QModelIndex, destinationChild: int) -> bool """
        return False

    def moveRows(self, sourceParent, sourceRow, count, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveRows(self, sourceParent: PySide2.QtCore.QModelIndex, sourceRow: int, count: int, destinationParent: PySide2.QtCore.QModelIndex, destinationChild: int) -> bool """
        return False

    def parent(self): # real signature unknown; restored from __doc__
        """
        parent(self) -> PySide2.QtCore.QObject
        parent(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex
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

    def setHeaderData(self, section, orientation, value, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setItemData(self, index, roles, p_int=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: PySide2.QtCore.QModelIndex, roles: typing.Dict[int, typing.Any]) -> bool """
        return False

    def setSourceModel(self, newSourceModel): # real signature unknown; restored from __doc__
        """ setSourceModel(self, newSourceModel: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def span(self, index): # real signature unknown; restored from __doc__
        """ span(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E4F940>'


