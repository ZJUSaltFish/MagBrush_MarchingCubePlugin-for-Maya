# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QFileSystemModel(__PySide2_QtCore.QAbstractItemModel):
    """ QFileSystemModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def canFetchMore(self, parent): # real signature unknown; restored from __doc__
        """ canFetchMore(self, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def data(self, index, role=None): # real signature unknown; restored from __doc__
        """ data(self, index: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def directoryLoaded(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, data, action, row, column, parent): # real signature unknown; restored from __doc__
        """ dropMimeData(self, data: PySide2.QtCore.QMimeData, action: PySide2.QtCore.Qt.DropAction, row: int, column: int, parent: PySide2.QtCore.QModelIndex) -> bool """
        return False

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def fetchMore(self, parent): # real signature unknown; restored from __doc__
        """ fetchMore(self, parent: PySide2.QtCore.QModelIndex) -> None """
        pass

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

    def fileRenamed(self, *args, **kwargs): # real signature unknown
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> PySide2.QtCore.QDir.Filters """
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

    def lastModified(self, index): # real signature unknown; restored from __doc__
        """ lastModified(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QDateTime """
        pass

    def mimeData(self, indexes, p_int=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: typing.List[int]) -> PySide2.QtCore.QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> typing.List[str] """
        pass

    def mkdir(self, parent, name): # real signature unknown; restored from __doc__
        """ mkdir(self, parent: PySide2.QtCore.QModelIndex, name: str) -> PySide2.QtCore.QModelIndex """
        pass

    def myComputer(self, role=None): # real signature unknown; restored from __doc__
        """ myComputer(self, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def nameFilterDisables(self): # real signature unknown; restored from __doc__
        """ nameFilterDisables(self) -> bool """
        return False

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> typing.List[str] """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> PySide2.QtWidgets.QFileSystemModel.Options """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """
        parent(self) -> PySide2.QtCore.QObject
        parent(self, child: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex
        """
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

    def rootDirectory(self): # real signature unknown; restored from __doc__
        """ rootDirectory(self) -> PySide2.QtCore.QDir """
        pass

    def rootPath(self): # real signature unknown; restored from __doc__
        """ rootPath(self) -> str """
        return ""

    def rootPathChanged(self, *args, **kwargs): # real signature unknown
        pass

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

    def setNameFilterDisables(self, enable): # real signature unknown; restored from __doc__
        """ setNameFilterDisables(self, enable: bool) -> None """
        pass

    def setNameFilters(self, filters, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, filters: typing.Sequence[str]) -> None """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: PySide2.QtWidgets.QFileSystemModel.Option, on: bool = True) -> None """
        pass

    def setOptions(self, options): # real signature unknown; restored from __doc__
        """ setOptions(self, options: PySide2.QtWidgets.QFileSystemModel.Options) -> None """
        pass

    def setReadOnly(self, enable): # real signature unknown; restored from __doc__
        """ setReadOnly(self, enable: bool) -> None """
        pass

    def setResolveSymlinks(self, enable): # real signature unknown; restored from __doc__
        """ setResolveSymlinks(self, enable: bool) -> None """
        pass

    def setRootPath(self, path): # real signature unknown; restored from __doc__
        """ setRootPath(self, path: str) -> PySide2.QtCore.QModelIndex """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def size(self, index): # real signature unknown; restored from __doc__
        """ size(self, index: PySide2.QtCore.QModelIndex) -> int """
        return 0

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = PySide2.QtCore.Qt.SortOrder.AscendingOrder) -> None """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions """
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: PySide2.QtWidgets.QFileSystemModel.Option) -> bool """
        return False

    def timerEvent(self, event): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def type(self, index): # real signature unknown; restored from __doc__
        """ type(self, index: PySide2.QtCore.QModelIndex) -> str """
        return ""

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

    DontResolveSymlinks = PySide2.QtWidgets.QFileSystemModel.Option.DontResolveSymlinks
    DontUseCustomDirectoryIcons = PySide2.QtWidgets.QFileSystemModel.Option.DontUseCustomDirectoryIcons
    DontWatchForChanges = PySide2.QtWidgets.QFileSystemModel.Option.DontWatchForChanges
    FileIconRole = PySide2.QtWidgets.QFileSystemModel.Roles.FileIconRole
    FileNameRole = PySide2.QtWidgets.QFileSystemModel.Roles.FileNameRole
    FilePathRole = PySide2.QtWidgets.QFileSystemModel.Roles.FilePathRole
    FilePermissions = PySide2.QtWidgets.QFileSystemModel.Roles.FilePermissions
    Option = None # (!) real value is "<class 'PySide2.QtWidgets.QFileSystemModel.Option'>"
    Options = None # (!) real value is "<class 'PySide2.QtWidgets.QFileSystemModel.Options'>"
    Roles = None # (!) real value is "<class 'PySide2.QtWidgets.QFileSystemModel.Roles'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50889340>'


