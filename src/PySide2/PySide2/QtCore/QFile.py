# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QFileDevice import QFileDevice

class QFile(QFileDevice):
    """
    QFile(self) -> None
    QFile(self, name: str) -> None
    QFile(self, name: str, parent: PySide2.QtCore.QObject) -> None
    QFile(self, parent: PySide2.QtCore.QObject) -> None
    """
    def copy(self, fileName, newName): # real signature unknown; restored from __doc__
        """
        copy(fileName: str, newName: str) -> bool
        copy(self, newName: str) -> bool
        """
        return False

    def decodeName(self, localFileName): # real signature unknown; restored from __doc__
        """
        decodeName(localFileName: PySide2.QtCore.QByteArray) -> str
        decodeName(localFileName: bytes) -> str
        """
        return ""

    def encodeName(self, fileName): # real signature unknown; restored from __doc__
        """ encodeName(fileName: str) -> PySide2.QtCore.QByteArray """
        pass

    def exists(self, fileName): # real signature unknown; restored from __doc__
        """
        exists(fileName: str) -> bool
        exists(self) -> bool
        """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def link(self, oldname, newName): # real signature unknown; restored from __doc__
        """
        link(oldname: str, newName: str) -> bool
        link(self, newName: str) -> bool
        """
        return False

    def moveToTrash(self, fileName): # real signature unknown; restored from __doc__
        """
        moveToTrash(fileName: str) -> typing.Tuple[bool, str]
        moveToTrash(self) -> bool
        """
        pass

    def open(self, fd, ioFlags, handleFlags=None): # real signature unknown; restored from __doc__
        """
        open(self, fd: int, ioFlags: PySide2.QtCore.QIODevice.OpenMode, handleFlags: PySide2.QtCore.QFileDevice.FileHandleFlags = PySide2.QtCore.QFileDevice.FileHandleFlag.DontCloseHandle) -> bool
        open(self, flags: PySide2.QtCore.QIODevice.OpenMode) -> bool
        """
        return False

    def permissions(self, filename): # real signature unknown; restored from __doc__
        """
        permissions(filename: str) -> PySide2.QtCore.QFileDevice.Permissions
        permissions(self) -> PySide2.QtCore.QFileDevice.Permissions
        """
        pass

    def readLink(self, fileName): # real signature unknown; restored from __doc__
        """
        readLink(fileName: str) -> str
        readLink(self) -> str
        """
        return ""

    def remove(self, fileName): # real signature unknown; restored from __doc__
        """
        remove(fileName: str) -> bool
        remove(self) -> bool
        """
        return False

    def rename(self, oldName, newName): # real signature unknown; restored from __doc__
        """
        rename(oldName: str, newName: str) -> bool
        rename(self, newName: str) -> bool
        """
        return False

    def resize(self, filename, sz): # real signature unknown; restored from __doc__
        """
        resize(filename: str, sz: int) -> bool
        resize(self, sz: int) -> bool
        """
        return False

    def setFileName(self, name): # real signature unknown; restored from __doc__
        """ setFileName(self, name: str) -> None """
        pass

    def setPermissions(self, filename, permissionSpec): # real signature unknown; restored from __doc__
        """
        setPermissions(filename: str, permissionSpec: PySide2.QtCore.QFileDevice.Permissions) -> bool
        setPermissions(self, permissionSpec: PySide2.QtCore.QFileDevice.Permissions) -> bool
        """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def symLinkTarget(self, fileName): # real signature unknown; restored from __doc__
        """
        symLinkTarget(fileName: str) -> str
        symLinkTarget(self) -> str
        """
        return ""

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DFC240>'


