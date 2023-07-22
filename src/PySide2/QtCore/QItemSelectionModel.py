# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QItemSelectionModel(QObject):
    """
    QItemSelectionModel(self, model: PySide2.QtCore.QAbstractItemModel, parent: PySide2.QtCore.QObject) -> None
    QItemSelectionModel(self, model: typing.Optional[PySide2.QtCore.QAbstractItemModel] = None) -> None
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clearCurrentIndex(self): # real signature unknown; restored from __doc__
        """ clearCurrentIndex(self) -> None """
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) -> None """
        pass

    def columnIntersectsSelection(self, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnIntersectsSelection(self, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentColumnChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> PySide2.QtCore.QModelIndex """
        pass

    def currentRowChanged(self, *args, **kwargs): # real signature unknown
        pass

    def emitSelectionChanged(self, newSelection, oldSelection): # real signature unknown; restored from __doc__
        """ emitSelectionChanged(self, newSelection: PySide2.QtCore.QItemSelection, oldSelection: PySide2.QtCore.QItemSelection) -> None """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def isColumnSelected(self, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isColumnSelected(self, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def isRowSelected(self, row, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isRowSelected(self, row: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def isSelected(self, index): # real signature unknown; restored from __doc__
        """ isSelected(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> PySide2.QtCore.QAbstractItemModel """
        pass

    def modelChanged(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def rowIntersectsSelection(self, row, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowIntersectsSelection(self, row: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def select(self, index, command): # real signature unknown; restored from __doc__
        """
        select(self, index: PySide2.QtCore.QModelIndex, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None
        select(self, selection: PySide2.QtCore.QItemSelection, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None
        """
        pass

    def selectedColumns(self, row=0): # real signature unknown; restored from __doc__
        """ selectedColumns(self, row: int = 0) -> typing.List[int] """
        pass

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> typing.List[int] """
        pass

    def selectedRows(self, column=0): # real signature unknown; restored from __doc__
        """ selectedRows(self, column: int = 0) -> typing.List[int] """
        pass

    def selection(self): # real signature unknown; restored from __doc__
        """ selection(self) -> PySide2.QtCore.QItemSelection """
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, index, command): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: PySide2.QtCore.QModelIndex, command: PySide2.QtCore.QItemSelectionModel.SelectionFlags) -> None """
        pass

    def setModel(self, model): # real signature unknown; restored from __doc__
        """ setModel(self, model: PySide2.QtCore.QAbstractItemModel) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, model, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Clear = PySide2.QtCore.QItemSelectionModel.SelectionFlag.Clear
    ClearAndSelect = PySide2.QtCore.QItemSelectionModel.SelectionFlag.ClearAndSelect
    Columns = PySide2.QtCore.QItemSelectionModel.SelectionFlag.Columns
    Current = PySide2.QtCore.QItemSelectionModel.SelectionFlag.Current
    Deselect = PySide2.QtCore.QItemSelectionModel.SelectionFlag.Deselect
    NoUpdate = PySide2.QtCore.QItemSelectionModel.SelectionFlag.NoUpdate
    Rows = PySide2.QtCore.QItemSelectionModel.SelectionFlag.Rows
    Select = PySide2.QtCore.QItemSelectionModel.SelectionFlag.Select
    SelectCurrent = PySide2.QtCore.QItemSelectionModel.SelectionFlag.SelectCurrent
    SelectionFlag = None # (!) real value is "<class 'PySide2.QtCore.QItemSelectionModel.SelectionFlag'>"
    SelectionFlags = None # (!) real value is "<class 'PySide2.QtCore.QItemSelectionModel.SelectionFlags'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DCE6C0>'
    Toggle = PySide2.QtCore.QItemSelectionModel.SelectionFlag.Toggle
    ToggleCurrent = PySide2.QtCore.QItemSelectionModel.SelectionFlag.ToggleCurrent


