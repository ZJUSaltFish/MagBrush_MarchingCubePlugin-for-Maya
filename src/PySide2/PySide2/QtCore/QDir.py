# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDir(__Shiboken.Object):
    """
    QDir(self, arg__1: PySide2.QtCore.QDir) -> None
    QDir(self, path: str, nameFilter: str, sort: PySide2.QtCore.QDir.SortFlags = Instance(QDir.SortFlags(QDir.Name | QDir.IgnoreCase)), filter: PySide2.QtCore.QDir.Filters = PySide2.QtCore.QDir.Filter.AllEntries) -> None
    QDir(self, path: str = '') -> None
    """
    def absoluteFilePath(self, fileName): # real signature unknown; restored from __doc__
        """ absoluteFilePath(self, fileName: str) -> str """
        return ""

    def absolutePath(self): # real signature unknown; restored from __doc__
        """ absolutePath(self) -> str """
        return ""

    def addResourceSearchPath(self, path): # real signature unknown; restored from __doc__
        """ addResourceSearchPath(path: str) -> None """
        pass

    def addSearchPath(self, prefix, path): # real signature unknown; restored from __doc__
        """ addSearchPath(prefix: str, path: str) -> None """
        pass

    def canonicalPath(self): # real signature unknown; restored from __doc__
        """ canonicalPath(self) -> str """
        return ""

    def cd(self, dirName): # real signature unknown; restored from __doc__
        """ cd(self, dirName: str) -> bool """
        return False

    def cdUp(self): # real signature unknown; restored from __doc__
        """ cdUp(self) -> bool """
        return False

    def cleanPath(self, path): # real signature unknown; restored from __doc__
        """ cleanPath(path: str) -> str """
        return ""

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def current(self): # real signature unknown; restored from __doc__
        """ current() -> PySide2.QtCore.QDir """
        pass

    def currentPath(self): # real signature unknown; restored from __doc__
        """ currentPath() -> str """
        return ""

    def dirName(self): # real signature unknown; restored from __doc__
        """ dirName(self) -> str """
        return ""

    def drives(self): # real signature unknown; restored from __doc__
        """ drives() -> typing.List[PySide2.QtCore.QFileInfo] """
        pass

    def entryInfoList(self, filters=None, sort=None): # real signature unknown; restored from __doc__
        """
        entryInfoList(self, filters: PySide2.QtCore.QDir.Filters = PySide2.QtCore.QDir.Filter.NoFilter, sort: PySide2.QtCore.QDir.SortFlags = PySide2.QtCore.QDir.SortFlag.NoSort) -> typing.List[PySide2.QtCore.QFileInfo]
        entryInfoList(self, nameFilters: typing.Sequence[str], filters: PySide2.QtCore.QDir.Filters = PySide2.QtCore.QDir.Filter.NoFilter, sort: PySide2.QtCore.QDir.SortFlags = PySide2.QtCore.QDir.SortFlag.NoSort) -> typing.List[PySide2.QtCore.QFileInfo]
        """
        pass

    def entryList(self, filters=None, sort=None): # real signature unknown; restored from __doc__
        """
        entryList(self, filters: PySide2.QtCore.QDir.Filters = PySide2.QtCore.QDir.Filter.NoFilter, sort: PySide2.QtCore.QDir.SortFlags = PySide2.QtCore.QDir.SortFlag.NoSort) -> typing.List[str]
        entryList(self, nameFilters: typing.Sequence[str], filters: PySide2.QtCore.QDir.Filters = PySide2.QtCore.QDir.Filter.NoFilter, sort: PySide2.QtCore.QDir.SortFlags = PySide2.QtCore.QDir.SortFlag.NoSort) -> typing.List[str]
        """
        pass

    def exists(self): # real signature unknown; restored from __doc__
        """
        exists(self) -> bool
        exists(self, name: str) -> bool
        """
        return False

    def filePath(self, fileName): # real signature unknown; restored from __doc__
        """ filePath(self, fileName: str) -> str """
        return ""

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> PySide2.QtCore.QDir.Filters """
        pass

    def fromNativeSeparators(self, pathName): # real signature unknown; restored from __doc__
        """ fromNativeSeparators(pathName: str) -> str """
        return ""

    def home(self): # real signature unknown; restored from __doc__
        """ home() -> PySide2.QtCore.QDir """
        pass

    def homePath(self): # real signature unknown; restored from __doc__
        """ homePath() -> str """
        return ""

    def isAbsolute(self): # real signature unknown; restored from __doc__
        """ isAbsolute(self) -> bool """
        return False

    def isAbsolutePath(self, path): # real signature unknown; restored from __doc__
        """ isAbsolutePath(path: str) -> bool """
        return False

    def isEmpty(self, filters=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isEmpty(self, filters: PySide2.QtCore.QDir.Filters = Instance(QDir.Filters(QDir.AllEntries | QDir.NoDotAndDotDot))) -> bool """
        pass

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isRelative(self): # real signature unknown; restored from __doc__
        """ isRelative(self) -> bool """
        return False

    def isRelativePath(self, path): # real signature unknown; restored from __doc__
        """ isRelativePath(path: str) -> bool """
        return False

    def isRoot(self): # real signature unknown; restored from __doc__
        """ isRoot(self) -> bool """
        return False

    def listSeparator(self): # real signature unknown; restored from __doc__
        """ listSeparator() -> str """
        return ""

    def makeAbsolute(self): # real signature unknown; restored from __doc__
        """ makeAbsolute(self) -> bool """
        return False

    def match(self, filter, fileName): # real signature unknown; restored from __doc__
        """
        match(filter: str, fileName: str) -> bool
        match(filters: typing.Sequence[str], fileName: str) -> bool
        """
        return False

    def mkdir(self, dirName): # real signature unknown; restored from __doc__
        """ mkdir(self, dirName: str) -> bool """
        return False

    def mkpath(self, dirPath): # real signature unknown; restored from __doc__
        """ mkpath(self, dirPath: str) -> bool """
        return False

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> typing.List[str] """
        pass

    def nameFiltersFromString(self, nameFilter): # real signature unknown; restored from __doc__
        """ nameFiltersFromString(nameFilter: str) -> typing.List[str] """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def refresh(self): # real signature unknown; restored from __doc__
        """ refresh(self) -> None """
        pass

    def relativeFilePath(self, fileName): # real signature unknown; restored from __doc__
        """ relativeFilePath(self, fileName: str) -> str """
        return ""

    def remove(self, fileName): # real signature unknown; restored from __doc__
        """ remove(self, fileName: str) -> bool """
        return False

    def removeRecursively(self): # real signature unknown; restored from __doc__
        """ removeRecursively(self) -> bool """
        return False

    def rename(self, oldName, newName): # real signature unknown; restored from __doc__
        """ rename(self, oldName: str, newName: str) -> bool """
        return False

    def rmdir(self, dirName): # real signature unknown; restored from __doc__
        """ rmdir(self, dirName: str) -> bool """
        return False

    def rmpath(self, dirPath): # real signature unknown; restored from __doc__
        """ rmpath(self, dirPath: str) -> bool """
        return False

    def root(self): # real signature unknown; restored from __doc__
        """ root() -> PySide2.QtCore.QDir """
        pass

    def rootPath(self): # real signature unknown; restored from __doc__
        """ rootPath() -> str """
        return ""

    def searchPaths(self, prefix): # real signature unknown; restored from __doc__
        """ searchPaths(prefix: str) -> typing.List[str] """
        pass

    def separator(self): # real signature unknown; restored from __doc__
        """ separator() -> str """
        return ""

    def setCurrent(self, path): # real signature unknown; restored from __doc__
        """ setCurrent(path: str) -> bool """
        return False

    def setFilter(self, filter): # real signature unknown; restored from __doc__
        """ setFilter(self, filter: PySide2.QtCore.QDir.Filters) -> None """
        pass

    def setNameFilters(self, nameFilters, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, nameFilters: typing.Sequence[str]) -> None """
        pass

    def setPath(self, path): # real signature unknown; restored from __doc__
        """ setPath(self, path: str) -> None """
        pass

    def setSearchPaths(self, prefix, searchPaths, p_str=None): # real signature unknown; restored from __doc__
        """ setSearchPaths(prefix: str, searchPaths: typing.Sequence[str]) -> None """
        pass

    def setSorting(self, sort): # real signature unknown; restored from __doc__
        """ setSorting(self, sort: PySide2.QtCore.QDir.SortFlags) -> None """
        pass

    def sorting(self): # real signature unknown; restored from __doc__
        """ sorting(self) -> PySide2.QtCore.QDir.SortFlags """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QDir) -> None """
        pass

    def temp(self): # real signature unknown; restored from __doc__
        """ temp() -> PySide2.QtCore.QDir """
        pass

    def tempPath(self): # real signature unknown; restored from __doc__
        """ tempPath() -> str """
        return ""

    def toNativeSeparators(self, pathName): # real signature unknown; restored from __doc__
        """ toNativeSeparators(pathName: str) -> str """
        return ""

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, arg__1): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__(self) -> object """
        return object()

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    AccessMask = PySide2.QtCore.QDir.Filter.AccessMask
    AllDirs = PySide2.QtCore.QDir.Filter.AllDirs
    AllEntries = PySide2.QtCore.QDir.Filter.AllEntries
    CaseSensitive = PySide2.QtCore.QDir.Filter.CaseSensitive
    Dirs = PySide2.QtCore.QDir.Filter.Dirs
    DirsFirst = PySide2.QtCore.QDir.SortFlag.DirsFirst
    DirsLast = PySide2.QtCore.QDir.SortFlag.DirsLast
    Drives = PySide2.QtCore.QDir.Filter.Drives
    Executable = PySide2.QtCore.QDir.Filter.Executable
    Files = PySide2.QtCore.QDir.Filter.Files
    Filter = None # (!) real value is "<class 'PySide2.QtCore.QDir.Filter'>"
    Filters = None # (!) real value is "<class 'PySide2.QtCore.QDir.Filters'>"
    Hidden = PySide2.QtCore.QDir.Filter.Hidden
    IgnoreCase = PySide2.QtCore.QDir.SortFlag.IgnoreCase
    LocaleAware = PySide2.QtCore.QDir.SortFlag.LocaleAware
    Modified = PySide2.QtCore.QDir.Filter.Modified
    Name = PySide2.QtCore.QDir.SortFlag.Name
    NoDot = PySide2.QtCore.QDir.Filter.NoDot
    NoDotAndDotDot = PySide2.QtCore.QDir.Filter.NoDotAndDotDot
    NoDotDot = PySide2.QtCore.QDir.Filter.NoDotDot
    NoFilter = PySide2.QtCore.QDir.Filter.NoFilter
    NoSort = PySide2.QtCore.QDir.SortFlag.NoSort
    NoSymLinks = PySide2.QtCore.QDir.Filter.NoSymLinks
    PermissionMask = PySide2.QtCore.QDir.Filter.PermissionMask
    Readable = PySide2.QtCore.QDir.Filter.Readable
    Reversed = PySide2.QtCore.QDir.SortFlag.Reversed
    Size = PySide2.QtCore.QDir.SortFlag.Size
    SortByMask = PySide2.QtCore.QDir.SortFlag.SortByMask
    SortFlag = None # (!) real value is "<class 'PySide2.QtCore.QDir.SortFlag'>"
    SortFlags = None # (!) real value is "<class 'PySide2.QtCore.QDir.SortFlags'>"
    System = PySide2.QtCore.QDir.Filter.System
    Time = PySide2.QtCore.QDir.SortFlag.Time
    Type = PySide2.QtCore.QDir.SortFlag.Type
    TypeMask = PySide2.QtCore.QDir.Filter.TypeMask
    Unsorted = PySide2.QtCore.QDir.SortFlag.Unsorted
    Writable = PySide2.QtCore.QDir.Filter.Writable
    __hash__ = None


