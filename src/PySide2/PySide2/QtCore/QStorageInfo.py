# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QStorageInfo(__Shiboken.Object):
    """
    QStorageInfo(self) -> None
    QStorageInfo(self, dir: PySide2.QtCore.QDir) -> None
    QStorageInfo(self, other: PySide2.QtCore.QStorageInfo) -> None
    QStorageInfo(self, path: str) -> None
    """
    def blockSize(self): # real signature unknown; restored from __doc__
        """ blockSize(self) -> int """
        return 0

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesFree(self): # real signature unknown; restored from __doc__
        """ bytesFree(self) -> int """
        return 0

    def bytesTotal(self): # real signature unknown; restored from __doc__
        """ bytesTotal(self) -> int """
        return 0

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QByteArray """
        pass

    def displayName(self): # real signature unknown; restored from __doc__
        """ displayName(self) -> str """
        return ""

    def fileSystemType(self): # real signature unknown; restored from __doc__
        """ fileSystemType(self) -> PySide2.QtCore.QByteArray """
        pass

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isReady(self): # real signature unknown; restored from __doc__
        """ isReady(self) -> bool """
        return False

    def isRoot(self): # real signature unknown; restored from __doc__
        """ isRoot(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def mountedVolumes(self): # real signature unknown; restored from __doc__
        """ mountedVolumes() -> typing.List[PySide2.QtCore.QStorageInfo] """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def refresh(self): # real signature unknown; restored from __doc__
        """ refresh(self) -> None """
        pass

    def root(self): # real signature unknown; restored from __doc__
        """ root() -> PySide2.QtCore.QStorageInfo """
        pass

    def rootPath(self): # real signature unknown; restored from __doc__
        """ rootPath(self) -> str """
        return ""

    def setPath(self, path): # real signature unknown; restored from __doc__
        """ setPath(self, path: str) -> None """
        pass

    def subvolume(self): # real signature unknown; restored from __doc__
        """ subvolume(self) -> PySide2.QtCore.QByteArray """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QStorageInfo) -> None """
        pass

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

    def __init__(self): # real signature unknown; restored from __doc__
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __hash__ = None


