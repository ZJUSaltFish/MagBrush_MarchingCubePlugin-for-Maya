# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QFileDevice import QFileDevice

class QFile(QFileDevice):
    """
    QFile()
    QFile(name: str)
    QFile(parent: QObject)
    QFile(name: str, parent: QObject)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        copy(self, newName: str) -> bool
        copy(fileName: str, newName: str) -> bool
        """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def decodeName(self, localFileName, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        decodeName(localFileName: Union[QByteArray, bytes, bytearray]) -> str
        decodeName(localFileName: str) -> str
        """
        return ""

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeName(self, fileName): # real signature unknown; restored from __doc__
        """ encodeName(fileName: str) -> QByteArray """
        return QByteArray

    def exists(self, fileName=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exists(self) -> bool
        exists(fileName: str) -> bool
        """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        link(self, newName: str) -> bool
        link(oldname: str, newName: str) -> bool
        """
        return False

    def moveToTrash(self, fileName=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        moveToTrash(self) -> bool
        moveToTrash(fileName: str) -> Tuple[bool, str]
        """
        return False

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self, flags: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool
        open(self, fd: int, ioFlags: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag], handleFlags: Union[QFileDevice.FileHandleFlags, QFileDevice.FileHandleFlag] = QFileDevice.FileHandleFlag.DontCloseHandle) -> bool
        """
        return False

    def permissions(self, filename=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        permissions(self) -> QFileDevice.Permissions
        permissions(filename: str) -> QFileDevice.Permissions
        """
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, fileName=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(self) -> bool
        remove(fileName: str) -> bool
        """
        return False

    def rename(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        rename(self, newName: str) -> bool
        rename(oldName: str, newName: str) -> bool
        """
        return False

    def resize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resize(self, sz: int) -> bool
        resize(filename: str, sz: int) -> bool
        """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, name): # real signature unknown; restored from __doc__
        """ setFileName(self, name: str) """
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPermissions(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPermissions(self, permissionSpec: Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool
        setPermissions(filename: str, permissionSpec: Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool
        """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def symLinkTarget(self, fileName=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        symLinkTarget(self) -> str
        symLinkTarget(fileName: str) -> str
        """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


