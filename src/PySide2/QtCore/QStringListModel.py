# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractListModel import QAbstractListModel

class QStringListModel(QAbstractListModel):
    """
    QStringListModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QStringListModel(self, strings: typing.Sequence[str], parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def data(self, index, role=None): # real signature unknown; restored from __doc__
        """ data(self, index: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags """
        pass

    def insertRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def itemData(self, index): # real signature unknown; restored from __doc__
        """ itemData(self, index: PySide2.QtCore.QModelIndex) -> typing.Dict[int, typing.Any] """
        pass

    def moveRows(self, sourceParent, sourceRow, count, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveRows(self, sourceParent: PySide2.QtCore.QModelIndex, sourceRow: int, count: int, destinationParent: PySide2.QtCore.QModelIndex, destinationChild: int) -> bool """
        return False

    def removeRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setItemData(self, index, roles, p_int=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: PySide2.QtCore.QModelIndex, roles: typing.Dict[int, typing.Any]) -> bool """
        return False

    def setStringList(self, strings, p_str=None): # real signature unknown; restored from __doc__
        """ setStringList(self, strings: typing.Sequence[str]) -> None """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def stringList(self): # real signature unknown; restored from __doc__
        """ stringList(self) -> typing.List[str] """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E4FC00>'


