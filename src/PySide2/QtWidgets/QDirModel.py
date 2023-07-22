# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QDirModel(__PySide2_QtCore.QAbstractItemModel):
    """
    QDirModel(self, nameFilters: typing.Sequence[str], filters: PySide2.QtCore.QDir.Filters, sort: PySide2.QtCore.QDir.SortFlags, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QDirModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def data(self, index, role=None): # real signature unknown; restored from __doc__
        """ data(self, index: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def dropMimeData(self, data, action, row, column, parent): # real signature unknown; restored from __doc__
        """ dropMimeData(self, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction, row: int, column: int, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def fileIcon(self, index): # real signature unknown; restored from __doc__
        """ fileIcon(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtGui.QIcon """
        pass

    def fileInfo(self, index): # real signature unknown; restored from __doc__
        """ fileInfo(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QFileInfo """
        pass

    def fileName(self, index): # real signature unknown; restored from __doc__
        """ fileName(self, index: PySide2.QtCore.QModelIndex) -> str """
        return ""

    def filePath(self, index): # real signature unknown; restored from __doc__
        """ filePath(self, index: PySide2.QtCore.QModelIndex) -> str """
        return ""

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> PySide2.QtCore.QDir.Filters """
        pass

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags """
        pass

    def hasChildren(self, index=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, index: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ iconProvider(self) -> PySide2.QtWidgets.QFileIconProvider """
        pass

    def index(self, path, column=0): # real signature unknown; restored from __doc__
        """
        index(self, path: str, column: int = 0) -> PySide2.QtCore.QModelIndex
        index(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> PySide2.QtCore.QModelIndex
        """
        pass

    def isDir(self, index): # real signature unknown; restored from __doc__
        """ isDir(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def lazyChildCount(self): # real signature unknown; restored from __doc__
        """ lazyChildCount(self) -> bool """
        return False

    def mimeData(self, indexes, p_int=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: typing.List[int]) -> PySide2.QtCore.QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> typing.List[str] """
        pass

    def mkdir(self, parent, name): # real signature unknown; restored from __doc__
        """ mkdir(self, parent: PySide2.QtCore.QModelIndex, name: str) -> PySide2.QtCore.QModelIndex """
        pass

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> typing.List[str] """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """
        parent(self) -> PySide2.QtCore.QObject
        parent(self, child: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex
        """
        pass

    def refresh(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ refresh(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> None """
        pass

    def remove(self, index): # real signature unknown; restored from __doc__
        """ remove(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ resolveSymlinks(self) -> bool """
        return False

    def rmdir(self, index): # real signature unknown; restored from __doc__
        """ rmdir(self, index: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setFilter(self, filters): # real signature unknown; restored from __doc__
        """ setFilter(self, filters: PySide2.QtCore.QDir.Filters) -> None """
        pass

    def setIconProvider(self, provider): # real signature unknown; restored from __doc__
        """ setIconProvider(self, provider: PySide2.QtWidgets.QFileIconProvider) -> None """
        pass

    def setLazyChildCount(self, enable): # real signature unknown; restored from __doc__
        """ setLazyChildCount(self, enable: bool) -> None """
        pass

    def setNameFilters(self, filters, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, filters: typing.Sequence[str]) -> None """
        pass

    def setReadOnly(self, enable): # real signature unknown; restored from __doc__
        """ setReadOnly(self, enable: bool) -> None """
        pass

    def setResolveSymlinks(self, enable): # real signature unknown; restored from __doc__
        """ setResolveSymlinks(self, enable: bool) -> None """
        pass

    def setSorting(self, sort): # real signature unknown; restored from __doc__
        """ setSorting(self, sort: PySide2.QtCore.QDir.SortFlags) -> None """
        pass

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def sorting(self): # real signature unknown; restored from __doc__
        """ sorting(self) -> PySide2.QtCore.QDir.SortFlags """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, nameFilters, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    FileIconRole = PySide2.QtWidgets.QDirModel.Roles.FileIconRole
    FileNameRole = PySide2.QtWidgets.QDirModel.Roles.FileNameRole
    FilePathRole = PySide2.QtWidgets.QDirModel.Roles.FilePathRole
    Roles = None # (!) real value is "<class 'PySide2.QtWidgets.QDirModel.Roles'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50889680>'


