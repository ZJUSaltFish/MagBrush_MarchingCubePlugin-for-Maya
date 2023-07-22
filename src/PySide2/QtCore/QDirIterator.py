# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDirIterator(__Shiboken.Object):
    """
    QDirIterator(self, dir: PySide2.QtCore.QDir, flags: PySide2.QtCore.QDirIterator.IteratorFlags = PySide2.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags) -> None
    QDirIterator(self, path: str, filter: PySide2.QtCore.QDir.Filters, flags: PySide2.QtCore.QDirIterator.IteratorFlags = PySide2.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags) -> None
    QDirIterator(self, path: str, flags: PySide2.QtCore.QDirIterator.IteratorFlags = PySide2.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags) -> None
    QDirIterator(self, path: str, nameFilters: typing.Sequence[str], filters: PySide2.QtCore.QDir.Filters = PySide2.QtCore.QDir.Filter.NoFilter, flags: PySide2.QtCore.QDirIterator.IteratorFlags = PySide2.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags) -> None
    """
    def fileInfo(self): # real signature unknown; restored from __doc__
        """ fileInfo(self) -> PySide2.QtCore.QFileInfo """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def hasNext(self): # real signature unknown; restored from __doc__
        """ hasNext(self) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> str """
        return ""

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def __init__(self, dir, flags=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    FollowSymlinks = PySide2.QtCore.QDirIterator.IteratorFlag.FollowSymlinks
    IteratorFlag = None # (!) real value is "<class 'PySide2.QtCore.QDirIterator.IteratorFlag'>"
    IteratorFlags = None # (!) real value is "<class 'PySide2.QtCore.QDirIterator.IteratorFlags'>"
    NoIteratorFlags = PySide2.QtCore.QDirIterator.IteratorFlag.NoIteratorFlags
    Subdirectories = PySide2.QtCore.QDirIterator.IteratorFlag.Subdirectories


