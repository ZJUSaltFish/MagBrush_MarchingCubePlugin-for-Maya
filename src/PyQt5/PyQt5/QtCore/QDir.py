# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDir(__sip.simplewrapper):
    """
    QDir(a0: QDir)
    QDir(path: str = '')
    QDir(path: str, nameFilter: str, sort: QDir.SortFlags = QDir.Name|QDir.IgnoreCase, filters: QDir.Filters = QDir.AllEntries)
    """
    def absoluteFilePath(self, fileName): # real signature unknown; restored from __doc__
        """ absoluteFilePath(self, fileName: str) -> str """
        return ""

    def absolutePath(self): # real signature unknown; restored from __doc__
        """ absolutePath(self) -> str """
        return ""

    def addSearchPath(self, prefix, path): # real signature unknown; restored from __doc__
        """ addSearchPath(prefix: str, path: str) """
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
        """ current() -> QDir """
        return QDir

    def currentPath(self): # real signature unknown; restored from __doc__
        """ currentPath() -> str """
        return ""

    def dirName(self): # real signature unknown; restored from __doc__
        """ dirName(self) -> str """
        return ""

    def drives(self): # real signature unknown; restored from __doc__
        """ drives() -> List[QFileInfo] """
        return []

    def entryInfoList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        entryInfoList(self, filters: Union[QDir.Filters, QDir.Filter] = QDir.NoFilter, sort: Union[QDir.SortFlags, QDir.SortFlag] = QDir.SortFlag.NoSort) -> List[QFileInfo]
        entryInfoList(self, nameFilters: Iterable[str], filters: Union[QDir.Filters, QDir.Filter] = QDir.NoFilter, sort: Union[QDir.SortFlags, QDir.SortFlag] = QDir.SortFlag.NoSort) -> List[QFileInfo]
        """
        pass

    def entryList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        entryList(self, filters: Union[QDir.Filters, QDir.Filter] = QDir.NoFilter, sort: Union[QDir.SortFlags, QDir.SortFlag] = QDir.SortFlag.NoSort) -> List[str]
        entryList(self, nameFilters: Iterable[str], filters: Union[QDir.Filters, QDir.Filter] = QDir.NoFilter, sort: Union[QDir.SortFlags, QDir.SortFlag] = QDir.SortFlag.NoSort) -> List[str]
        """
        pass

    def exists(self, name=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exists(self) -> bool
        exists(self, name: str) -> bool
        """
        return False

    def filePath(self, fileName): # real signature unknown; restored from __doc__
        """ filePath(self, fileName: str) -> str """
        return ""

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> QDir.Filters """
        pass

    def fromNativeSeparators(self, pathName): # real signature unknown; restored from __doc__
        """ fromNativeSeparators(pathName: str) -> str """
        return ""

    def home(self): # real signature unknown; restored from __doc__
        """ home() -> QDir """
        return QDir

    def homePath(self): # real signature unknown; restored from __doc__
        """ homePath() -> str """
        return ""

    def isAbsolute(self): # real signature unknown; restored from __doc__
        """ isAbsolute(self) -> bool """
        return False

    def isAbsolutePath(self, path): # real signature unknown; restored from __doc__
        """ isAbsolutePath(path: str) -> bool """
        return False

    def isEmpty(self, filters, QDir_Filters=None, QDir_Filter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isEmpty(self, filters: Union[QDir.Filters, QDir.Filter] = QDir.AllEntries|QDir.NoDotAndDotDot) -> bool """
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

    def match(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        match(filters: Iterable[str], fileName: str) -> bool
        match(filter: str, fileName: str) -> bool
        """
        return False

    def mkdir(self, dirName): # real signature unknown; restored from __doc__
        """ mkdir(self, dirName: str) -> bool """
        return False

    def mkpath(self, dirPath): # real signature unknown; restored from __doc__
        """ mkpath(self, dirPath: str) -> bool """
        return False

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> List[str] """
        return []

    def nameFiltersFromString(self, nameFilter): # real signature unknown; restored from __doc__
        """ nameFiltersFromString(nameFilter: str) -> List[str] """
        return []

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def refresh(self): # real signature unknown; restored from __doc__
        """ refresh(self) """
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
        """ root() -> QDir """
        return QDir

    def rootPath(self): # real signature unknown; restored from __doc__
        """ rootPath() -> str """
        return ""

    def searchPaths(self, prefix): # real signature unknown; restored from __doc__
        """ searchPaths(prefix: str) -> List[str] """
        return []

    def separator(self): # real signature unknown; restored from __doc__
        """ separator() -> str """
        return ""

    def setCurrent(self, path): # real signature unknown; restored from __doc__
        """ setCurrent(path: str) -> bool """
        return False

    def setFilter(self, filter, QDir_Filters=None, QDir_Filter=None): # real signature unknown; restored from __doc__
        """ setFilter(self, filter: Union[QDir.Filters, QDir.Filter]) """
        pass

    def setNameFilters(self, nameFilters, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, nameFilters: Iterable[str]) """
        pass

    def setPath(self, path): # real signature unknown; restored from __doc__
        """ setPath(self, path: str) """
        pass

    def setSearchPaths(self, prefix, searchPaths, p_str=None): # real signature unknown; restored from __doc__
        """ setSearchPaths(prefix: str, searchPaths: Iterable[str]) """
        pass

    def setSorting(self, sort, QDir_SortFlags=None, QDir_SortFlag=None): # real signature unknown; restored from __doc__
        """ setSorting(self, sort: Union[QDir.SortFlags, QDir.SortFlag]) """
        pass

    def sorting(self): # real signature unknown; restored from __doc__
        """ sorting(self) -> QDir.SortFlags """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDir) """
        pass

    def temp(self): # real signature unknown; restored from __doc__
        """ temp() -> QDir """
        return QDir

    def tempPath(self): # real signature unknown; restored from __doc__
        """ tempPath() -> str """
        return ""

    def toNativeSeparators(self, pathName): # real signature unknown; restored from __doc__
        """ toNativeSeparators(pathName: str) -> str """
        return ""

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessMask = 1008
    AllDirs = 1024
    AllEntries = 7
    CaseSensitive = 2048
    Dirs = 1
    DirsFirst = 4
    DirsLast = 32
    Drives = 4
    Executable = 64
    Files = 2
    Hidden = 256
    IgnoreCase = 16
    LocaleAware = 64
    Modified = 128
    Name = 0
    NoDot = 8192
    NoDotAndDotDot = 24576
    NoDotDot = 16384
    NoFilter = -1
    NoSort = -1
    NoSymLinks = 8
    PermissionMask = 112
    Readable = 16
    Reversed = 8
    Size = 2
    SortByMask = 3
    System = 512
    Time = 1
    Type = 128
    TypeMask = 15
    Unsorted = 3
    Writable = 32
    __hash__ = None


